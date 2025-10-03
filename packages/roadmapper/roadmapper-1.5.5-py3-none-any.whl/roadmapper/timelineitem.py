# MIT License

# Copyright (c) 2022 CS Goh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import calendar
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from .painter import Painter
from .timelinemode import TimelineMode


@dataclass(kw_only=True)
class TimelineItem:
    """Roadmap TimelineItem class"""

    text: str = field(init=True, default=None)
    value: str = field(init=True, default=None)
    start: datetime = field(init=True, default=None)
    end: datetime = field(init=True, default=None)
    font: str = field(init=True, default=None)
    font_size: int = field(init=True, default=None)
    font_colour: str = field(init=True, default=None)
    fill_colour: str = field(init=True, default=None)

    box_x: int = field(init=False, default=0)
    box_y: int = field(init=False, default=0)
    box_width: int = field(init=False, default=0)
    box_height: int = field(init=False, default=0)
    text_x: int = field(init=False, default=0)
    text_y: int = field(init=False, default=0)

    def __calculate_text_draw_position(self, painter: Painter) -> tuple:
        """Calculate the text draw position based on the box position and size

        A Args:
            painter (Painter): Pillow wrapper class instance

        Returns:
            tuple(int, int): (x, y) position of the text
        """

        return painter.get_display_text_position(
            self.box_x,
            self.box_y,
            self.box_width,
            self.box_height,
            self.text,
            "centre",
            self.font,
            self.font_size,
        )

    def set_draw_position(
        self,
        painter: Painter,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """Set the draw position of the timeline item

        Args:
            painter (Painter): Pillow wrapper class instance
            x (int): x position of the box
            y (int): y position of the box
            width (int): width of the box
            height (int): height of the box
        """
        self.box_x = x
        self.box_y = y
        self.box_width = width
        self.box_height = height
        self.text_x, self.text_y = self.__calculate_text_draw_position(painter)
        painter.next_y_pos = self.box_y

        # Helper.printc(
        #     f"      [{self.text}] {self.box_x=}, {self.box_width=}",
        #     show_level="marker",
        # )

    def get_timeline_period(
        self, mode: TimelineMode, previous_start, previous_end
    ) -> tuple:
        """Get the timeline period based on the timeline mode

        Args:
            mode (TimelineMode): Timeline mode

        Returns:
            tuple(datetime, datetime): start datetime and end datetime of the timeline period
        """

        if mode == TimelineMode.WEEKLY:
            this_year = self.value[:4]
            this_week = self.value[4:]

            # --- FIX for #106 (Start) ---
            timeline_start_period = datetime.strptime(
                f"{this_year} {this_week} 1", "%G %V %u"
            )
            timeline_end_period = datetime.strptime(
                f"{this_year} {this_week} 7", "%G %V %u"
            )

            if (
                timeline_start_period == previous_start
                and timeline_end_period == previous_end
            ):
                this_week = int(this_week) + 1
                timeline_start_period = datetime.strptime(
                    f"{this_year} {this_week} 1", "%G %V %u"
                )
                timeline_end_period = datetime.strptime(
                    f"{this_year} {this_week} 7", "%G %V %u"
                )
            # --- FIX for #106 (End) ---

        if mode == TimelineMode.MONTHLY:

            this_year = int(self.value[:4])
            this_month = int(self.value[4:])
            _, month_end_day = calendar.monthrange(this_year, this_month)
            timeline_start_period = datetime(this_year, this_month, 1)
            timeline_end_period = datetime(this_year, this_month, month_end_day)

        if mode == TimelineMode.QUARTERLY:
            this_year = int(self.value[:4])
            this_quarter = int(self.value[4:])
            if this_quarter == 1:
                this_month = 1
            elif this_quarter == 2:
                this_month = 4
            elif this_quarter == 3:
                this_month = 7
            elif this_quarter == 4:
                this_month = 10

            timeline_start_period = datetime(
                this_year, 3 * ((this_month - 1) // 3) + 1, 1
            )
            timeline_end_period = datetime(
                this_year + 3 * this_quarter // 12, 3 * this_quarter % 12 + 1, 1
            ) + timedelta(days=-1)

        if mode == TimelineMode.HALF_YEARLY:
            this_year = int(self.value[:4])
            this_half = int(self.value[4:])
            if this_half == 1:
                timeline_start_period = datetime(this_year, 1, 1)
                timeline_end_period = datetime(this_year, 6, 30)
            elif this_half == 2:
                timeline_start_period = datetime(this_year, 7, 1)
                timeline_end_period = datetime(this_year, 12, 31)

        if mode == TimelineMode.YEARLY:
            timeline_start_period = datetime(int(self.value), 1, 1)
            timeline_end_period = datetime(int(self.value), 12, 31)

        return timeline_start_period, timeline_end_period

    def get_timeline_pos_percentage(
        self, mode: TimelineMode, task_or_milestone_date: datetime
    ) -> float:
        """Get the timeline position percentage based on the task or milestone date

        Args:
            mode (TimelineMode): Timeline mode
            task_or_milestone_date (datetime): Task or milestone date

        Returns:
            float: Timeline position percentage
        """
        correct_timeline = False
        pos_percentage = 0
        timeline_start_period, timeline_end_period = self.get_timeline_period(
            mode, None, None
        )

        if mode == TimelineMode.WEEKLY:
            pos_percentage = task_or_milestone_date.weekday() / 7
            milestone_period = (
                f"{task_or_milestone_date.year}{task_or_milestone_date.strftime('%W')}"
            )
            this_period = (
                f"{timeline_start_period.year}{timeline_start_period.strftime('%W')}"
            )
            if milestone_period == this_period:
                correct_timeline = True

        if mode == TimelineMode.MONTHLY:
            _, last_day = calendar.monthrange(
                timeline_start_period.year, timeline_start_period.month
            )
            pos_percentage = round(task_or_milestone_date.day / last_day, 1)
            if (
                task_or_milestone_date.year == timeline_start_period.year
                and task_or_milestone_date.month == timeline_start_period.month
            ):
                correct_timeline = True

        if mode == TimelineMode.QUARTERLY:
            this_period = self.value
            this_year = int(this_period[:4])
            int(this_period[4:])

            if this_period[-1] == "1":
                date_of_first_day_of_quarter = datetime(this_year, 1, 1)
                date_of_last_day_of_quarter = datetime(
                    this_year, 3, calendar.monthrange(this_year, 3)[1]
                )

            elif this_period[-1] == "2":
                date_of_first_day_of_quarter = datetime(this_year, 4, 1)
                date_of_last_day_of_quarter = datetime(
                    this_year, 6, calendar.monthrange(this_year, 6)[1]
                )

            elif this_period[-1] == "3":
                date_of_first_day_of_quarter = datetime(this_year, 7, 1)
                date_of_last_day_of_quarter = datetime(
                    this_year, 9, calendar.monthrange(this_year, 9)[1]
                )

            elif this_period[-1] == "4":
                date_of_first_day_of_quarter = datetime(this_year, 10, 1)
                date_of_last_day_of_quarter = datetime(
                    this_year, 12, calendar.monthrange(this_year, 12)[1]
                )

            days_in_quarter = (
                date_of_last_day_of_quarter - date_of_first_day_of_quarter
            ).days
            days_progress_in_quarter = (
                days_in_quarter
                - (date_of_last_day_of_quarter - task_or_milestone_date).days
            )
            pos_percentage = days_progress_in_quarter / days_in_quarter

            milestone_period = f"{task_or_milestone_date.year}{self.__get_quarter_from_date(task_or_milestone_date)}"
            if milestone_period == this_period:
                correct_timeline = True

        if mode == TimelineMode.HALF_YEARLY:
            this_period = self.value
            this_year = int(this_period[:4])

            if this_period[-1] == "1":
                date_of_first_day_of_halfyear = datetime(this_year, 1, 1)
                date_of_last_day_of_halfyear = datetime(
                    this_year, 6, calendar.monthrange(this_year, 6)[1]
                )

            else:
                date_of_first_day_of_halfyear = datetime(this_year, 7, 1)
                date_of_last_day_of_halfyear = datetime(
                    this_year, 12, calendar.monthrange(this_year, 12)[1]
                )
            ### calc number of days between first day of quarter and last day of quarter
            days_in_halfyear = (
                date_of_last_day_of_halfyear - date_of_first_day_of_halfyear
            ).days
            days_progress_in_halfyear = (
                days_in_halfyear
                - (date_of_last_day_of_halfyear - task_or_milestone_date).days
            )
            pos_percentage = days_progress_in_halfyear / days_in_halfyear
            milestone_period = f"{task_or_milestone_date.year}{self.__get_halfyear_from_date(task_or_milestone_date)}"
            if milestone_period == this_period:
                correct_timeline = True

        if mode == TimelineMode.YEARLY:
            this_period = self.value
            this_year = int(this_period[:4])
            date_of_first_day_of_year = datetime(this_year, 1, 1)
            date_of_last_day_of_year = datetime(
                this_year, 12, calendar.monthrange(this_year, 12)[1]
            )
            ### calc number of days between first day of quarter and last day of quarter
            days_in_year = (date_of_last_day_of_year - date_of_first_day_of_year).days
            days_progress_in_year = (
                days_in_year - (date_of_last_day_of_year - task_or_milestone_date).days
            )
            pos_percentage = days_progress_in_year / days_in_year
            milestone_period = f"{task_or_milestone_date.year}"
            if milestone_period == this_period:
                correct_timeline = True

        return (correct_timeline, pos_percentage)

    def __get_quarter_from_date(self, this_date: datetime) -> int:
        """Returns the quarter of a given date

        Args:
            date (datetime): date

        Returns:
            int: quarter
        """
        return (this_date.month - 1) // 3 + 1

    def __get_halfyear_from_date(self, this_date: datetime) -> int:
        """Returns the halfyear of a given date

        Args:
            date (datetime): date

        Returns:
            int: halfyear
        """
        return (this_date.month - 1) // 6 + 1

    def draw(self, painter: Painter) -> None:
        """Draws the timeline

        Args:
            painter (Painter): Pillow wrapper class instance
        """

        painter.draw_box_with_text(
            self.box_x,
            self.box_y,
            self.box_width,
            self.box_height,
            self.fill_colour,
            self.text,
            "centre",
            self.font,
            self.font_size,
            self.font_colour,
        )

    def draw_vertical_line(self, painter: Painter) -> None:
        """Draws the timeline

        Args:
            painter (Painter): Pillow wrapper class instance
        """
        x_pos = self.box_x - 1
        painter.draw_line(
            x_pos,
            self.box_y + self.box_height,
            x_pos,
            painter.next_y_pos + 10,
            "#e6e6e6",
            50,
            1,
            "solid",
        )
