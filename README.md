# blackcellmagic

[![pypiv](https://img.shields.io/pypi/v/blackcellmagic.svg)](https://pypi.python.org/pypi/blackcellmagic)
[![pyv](https://img.shields.io/pypi/pyversions/blackcellmagic.svg)](https://pypi.python.org/pypi/blackcellmagic)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/blackcellmagic/master/LICENSE)
[![Downloads](https://pepy.tech/badge/blackcellmagic)](https://pepy.tech/project/blackcellmagic)

IPython magic command to format python code in cell using [black](https://github.com/ambv/black).

![Demo](https://i.imgur.com/9W8NLUu.gif)

## What is the magic command?

```python
%%black
```

## Setup

### Using pip

```bash
pip install blackcellmagic
```

### Directly from the repository

```bash
git clone https://github.com/csurfer/blackcellmagic.git
python blackcellmagic/setup.py install
```

### Load Extension in IPython

```python
%load_ext blackcellmagic
```

## Usage

```python
# To have it formatted to black default length 88 with string normalization.
%%black

# To have it formatted to a particular line length.
%%black -l 79
%%black --line-length 79

# To skip string normalization.
%%black -S
%%black --skip-string-normalization
```

## Extras

Tobin Jones has been kind enough to develop a NPM package over blackcellmagic to format all cells at once which can be found [here](https://github.com/tobinjones/jupyterlab_formatblack).

## Contributing

### Bug Reports and Feature Requests

Please use [issue tracker](https://github.com/csurfer/blackcellmagic/issues) for reporting bugs or feature requests.

### Development

Pull requests are most welcome.

### Buy the developer a cup of coffee!

If you found the utility helpful you can buy me a cup of coffee using

[![Donate](https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
