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

from dataclasses import dataclass, field
from datetime import datetime
from .painter import Painter
from .timeline import Timeline
from .task import Task
from .helper import Helper

@dataclass
class Group:
    """Roadmap Group class"""

    text: str = field(init=True, default=None)
    font: str = field(init=True, default=None)
    font_size: int = field(init=True, default=None)
    font_colour: str = field(init=True, default=None)
    fill_colour: str = field(init=True, default=None)
    text_alignment: str = field(init=True, default=None)

    box_x: int = field(init=False, default=0)
    box_y: int = field(init=False, default=0)
    box_width: int = field(init=False, default=0)
    box_height: int = field(init=False, default=0)
    tasks: list = field(init=False, default_factory=list)
    text_x: int = field(init=False, default=0)
    text_y: int = field(init=False, default=0)
    painter: Painter = None

    # def __post_init__(self):
    #     """This method is called after __init__() is called"""
    #     self.tasks = []
    #     self.text_x = 0
    #     self.text_y = 0

    def add_task(
        self,
        text: str,
        start: datetime,
        end: datetime,
        font: str = "",
        font_size: int = 0,
        font_colour: str = "",
        fill_colour: str = "",
        text_alignment: str = "centre",
        style: str = "rectangle",
    ) -> Task:
        """Add new task to group

        Args:
            text (str): Task text
            start (datetime): Task start date
            end (datetime): Task end date
            font (str, optional): Task font. Defaults to "Arial".
            font_size (int, optional): Task font size. Defaults to 12.
            font_colour (str, optional): Task font colour. Defaults to "Black". HTML colour name or hex code. Eg. #FFFFFF or LightGreen
            fill_colour (str, optional): Task fill colour. Defaults to "LightGreen". HTML colour name or hex code
            text_alignment (str, optional): Task text alignment. Defaults to "centre". Options: "left", "centre", "right"

        Return:
            Task: Task instance to be used in with statement
        """

        font = font or self.painter.task_font
        font_size = font_size or self.painter.task_font_size
        font_colour = font_colour or self.painter.task_font_colour
        fill_colour = fill_colour or self.painter.task_fill_colour
        style = style or self.painter.task_style

        task = Task(
            text=text,
            start=start,
            end=end,
            font=font,
            font_size=font_size,
            font_colour=font_colour,
            fill_colour=fill_colour,
            text_alignment=text_alignment,
            style=style,
            painter=self.painter,
        )

        self.tasks.append(task)

        return task

    def set_draw_position(self, painter: Painter, timeline: Timeline) -> None:
        """Set group draw position

        Args:
            painter (Painter): Pillow wrapper class instance
            timeline (Timeline): Timeline instance
        """

        # Calculate number of milestones in group
        milestone_count = 0
        for task in self.tasks:
            ### Fixed in v1.3.2
            if len(task.milestones) > 0:
                milestone_count += 1
            # milestone_count += len(task.milestones)
            # milestone_count += 1  ### Fixed in v1.3.1
            if len(task.milestones) == 0:
                for parallel_task in task.tasks:
                    milestone_count += len(parallel_task.milestones)
                    break  ### We only need to know whether there milestone exists in the parallel tasks

        # Calc group height
        task_count = len(self.tasks)
        self.box_height = (
            (20 * task_count)
            + (painter.additional_height_for_milestone * milestone_count)
            + (5 * task_count)
            + (2 * (task_count - 1))
        )

        self.box_width = (
            painter.width - (painter.left_margin + painter.right_margin)
        ) * painter.group_box_width_percentage

        self.box_x = painter.left_margin

        self.box_y = painter.next_y_pos + painter.additional_height_for_milestone

        self.text_x, self.text_y = painter.get_display_text_position(
            self.box_x,
            self.box_y,
            self.box_width,
            self.box_height,
            self.text,
            self.text_alignment,
            self.font,
            self.font_size,
        )

        Helper.printc(
            f"Group: [{self.text}], x: {self.box_x}, y: {self.box_y}, width: {self.box_width}, height: {self.box_height}",
            show_level="group",
        )

        painter.next_y_pos = self.box_y
        for task in self.tasks:
            task.set_draw_position(painter, self.box_x, painter.next_y_pos, timeline)
            Helper.printc(
                f"\tTask: [{task.text}], x: {task.box_x}, y: {task.box_y}, width: {task.box_width}, height: {task.box_height}",
                show_level="task",)

        painter.next_y_pos = self.box_y + self.box_height

    def draw(self, painter: Painter) -> None:
        """Draw group

        Args:
            painter (Painter): Pillow wrapper class instance
        """
        # Step 1: draw group
        painter.draw_box_with_text(
            self.box_x,
            self.box_y,
            self.box_width,
            self.box_height,
            self.fill_colour,
            self.text,
            self.text_alignment,
            self.font,
            self.font_size,
            self.font_colour,
        )

        # Step 2: draw tasks
        for tasks in self.tasks:
            tasks.draw(painter)

    def __enter__(self):
        """This method is called when the 'with' statement is used"""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """This method is called when the 'with' statement is used"""
        pass
