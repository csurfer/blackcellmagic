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
            try:
                from black import FileMode
                mode = FileMode(line_length=line_length)
                formatted = format_str(src_contents=cell, mode=mode)
            except TypeError:
                formatted = format_str(src_contents=cell, line_length=line_length)
            if formatted and formatted[-1] == "\n":
                    formatted = formatted[:-1]
            self.shell.set_next_input(formatted, replace=True)


def load_ipython_extension(ipython):
    ipython.register_magics(FormattingMagic)
