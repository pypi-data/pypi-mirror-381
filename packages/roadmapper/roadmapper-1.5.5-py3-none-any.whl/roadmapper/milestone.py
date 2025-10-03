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
from typing import Union

from .alignment import Alignment, AlignmentDirection, OffsetType
from .painter import Painter


@dataclass(kw_only=True)
class Milestone:
    """Roadmap Milestone class"""

    text: str = field(init=True, default=None)
    date: datetime = field(init=True, default=None)
    font: str = field(init=True, default=None)
    font_size: int = field(init=True, default=None)
    font_colour: str = field(init=True, default=None)
    fill_colour: str = field(init=True, default=None)
    text_alignment: Union[str, Alignment] = field(init=True, default=None)

    diamond_x: int = field(init=False, default=0)
    diamond_y: int = field(init=False, default=0)
    diamond_width: int = field(init=False, default=0)
    diamond_height: int = field(init=False, default=0)
    text_x: int = field(init=False, default=0)
    text_y: int = field(init=False, default=0)

    def draw(self, painter: Painter) -> None:
        """Draw milestone

        Args:
            painter (Painter): Pillow wrapper class instance
        """
        if (self.diamond_x != 0) and (self.diamond_y != 0):
            painter.draw_diamond(
                self.diamond_x,
                self.diamond_y,
                self.diamond_width,
                self.diamond_height,
                self.fill_colour,
            )

        alignment = Alignment.from_value(
            alignment=self.text_alignment,
            default_offset_type=OffsetType.PERCENT,
            default_offset=0.5,
        )

        self.apply_offset(alignment=alignment, painter=painter)

        if (self.text_x != 0) and (self.text_y != 0):
            painter.draw_text(
                self.text_x,
                self.text_y,
                self.text,
                self.font,
                self.font_size,
                self.font_colour,
            )

    def apply_offset(self, alignment: Alignment, painter: Painter) -> None:
        direction, offset_type, offset = alignment.as_tuple()
        if direction is None or direction == AlignmentDirection.CENTER:
            return  # Center does not require an offset

        if offset_type == OffsetType.PERCENT:
            text_width, _ = painter.get_text_dimension(
                            text=self.text, font=self.font, font_size=self.font_size
                        )
            offset = alignment.percent_of(text_width)

        if direction == AlignmentDirection.RIGHT and offset:
            self.text_x += offset
        elif direction == AlignmentDirection.LEFT and offset:
            self.text_x -= offset
