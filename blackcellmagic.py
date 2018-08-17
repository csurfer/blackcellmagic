"""
black
~~~~~
Module implementing IPython cell magic to format code using black, the
uncompromising python code formatter.

Usage of black:

To have it formatted to black default length 88.
>>> %%black

To have it formatted to a particular line length.
>>> %%black -l 79
>>> %%black --line_length 79

:copyright: (c) 2018 by Vishwas B Sharma.
:license: MIT, see LICENSE for more details.
"""


from black import format_str
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
import re

@magics_class
class FormattingMagic(Magics):
    """IPython wrapper to format cell using `https://github.com/ambv/black`."""

    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "-l", "--line_length", type=int, default=88, help="Line length"
    )
    @cell_magic
    def black(self, line, cell):
        """Magic command to format the IPython cell."""
        args = magic_arguments.parse_argstring(self.black, line)
        line_length = args.line_length
        if cell:
            # Comment magics
            cell = re.sub(r"^%", r"##!%", cell)
            cell = re.sub(r"\n\s*%(?=\w+)", "\n##!%", cell)
            try:
                formated = format_str(src_contents=cell, line_length=line_length)
                if formated and formated[-1] == "\n":
                    formated = formated[:-1]
            except ValueError as e:
                formated = cell
                print(e)
            finally:
                # Uncomment magics
                formated = re.sub(r"^##!%", r"%", formated)
                formated = re.sub(r"##!%(?=\w+)", "%", formated)
                # No matter success or not, something will always be put back
                self.shell.set_next_input(formated, replace=True)


def load_ipython_extension(ipython):
    ipython.register_magics(FormattingMagic)
