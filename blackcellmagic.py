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

To keep the string literals as seen.
>>> %%black -S
>>> %%black --skip-string-normalization

:copyright: (c) 2018 by Vishwas B Sharma.
:license: MIT, see LICENSE for more details.
"""


from black import FileMode, format_str
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class


@magics_class
class FormattingMagic(Magics):
    """IPython wrapper to format cell using `https://github.com/ambv/black`."""

    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "-l", "--line_length", type=int, default=88, help="Line length"
    )
    @magic_arguments.argument(
        "-S",
        "--skip-string-normalization",
        action="store_true",
        help="No string normalization",
    )
    @cell_magic
    def black(self, line, cell):
        """Magic command to format the IPython cell."""
        args = magic_arguments.parse_argstring(self.black, line)
        line_length = args.line_length
        if args.skip_string_normalization:
            mode = FileMode.NO_STRING_NORMALIZATION
        else:
            mode = FileMode.AUTO_DETECT
        if cell:
            formated = format_str(src_contents=cell, line_length=line_length, mode=mode)
            if formated and formated[-1] == "\n":
                formated = formated[:-1]
            self.shell.set_next_input(formated, replace=True)


def load_ipython_extension(ipython):
    ipython.register_magics(FormattingMagic)
