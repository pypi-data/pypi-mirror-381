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
from .painter import Painter


@dataclass(kw_only=True)
class Footer:
    """Roadmap Footer class"""

    text: str = field(init=True, default=None)
    font: str = field(init=True, default=None)
    font_size: int = field(init=True, default=None)
    font_colour: str = field(init=True, default=None)
    x: int = field(init=False, default=0)
    y: int = field(init=False, default=0)

    def __calculate_draw_position(self, painter: Painter) -> tuple[int, int]:
        """Calculate footer draw position

        Args:
            painter (Painter): Pillow wrapper class instance

        Returns:
            tuple[int, int]: Footer x and y position
        """
        self.width, self.height = painter.get_text_dimension(
            self.text, self.font, self.font_size
        )
        # 20px is the marging between the last drawn item and the footer
        return (
            painter.width / 2
        ) - self.width / 2, painter.next_y_pos + self.height + 20

    def set_draw_position(self, painter: Painter) -> None:
        """Set footer draw position

        Args:
            painter (Painter): Pillow wrapper class instance
            last_y_pos (int): Last drawn item y position
        """
        self.x, self.y = self.__calculate_draw_position(painter)
        painter.next_y_pos = self.y + self.height + 35

    def draw(self, painter: Painter) -> None:
        """Draw footer

        Args:
            painter (Painter): Pillow wrapper class instance
        """

        # add 35px top margin before drawing the footer
        painter.draw_text(
            self.x, self.y + 35, self.text, self.font, self.font_size, self.font_colour
        )
