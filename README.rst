blackcellmagic
==============

|pypiv| |pyv| |Licence| |Thanks|

IPython magic command to format python code in cell using `black`_.

What is the magic command?
--------------------------

.. code:: python

    %%black

Setup
-----

Using pip
~~~~~~~~~

.. code:: bash

    pip install blackcellmagic

Directly from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    git clone https://github.com/csurfer/blackcellmagic.git
    python blackcellmagic/setup.py install

Load Extension in IPython
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    %load_ext blackcellmagic

Usage
-----

.. code:: python

    # To have it formatted to black default length 88.
    %%black

    # To have it formatted to a particular line length.
    %%black -l 79
    %%black --line_length 79

Extras
------

Tobin Jones has been kind enough to develop a NPM package over blackcellmagic to format all cells at once which can be found `here`_.


Contributing
------------

Bug Reports and Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please use `issue tracker`_ for reporting bugs or feature requests.

Development
~~~~~~~~~~~

Pull requests are most welcome.

Buy the developer a cup of coffee!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you found the utility helpful you can buy me a cup of coffee using

|Donate|


.. _black: https://github.com/ambv/black

.. _issue tracker: https://github.com/csurfer/blackcellmagic/issues

.. |Donate| image:: https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted

.. |Thanks| image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/csurfer

.. |Licence| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/csurfer/blackcellmagic/master/LICENSE

.. |pypiv| image:: https://img.shields.io/pypi/v/py-heat-magic.svg
   :target: https://pypi.python.org/pypi/blackcellmagic

.. |pyv| image:: https://img.shields.io/pypi/pyversions/blackcellmagic.svg
   :target: https://pypi.python.org/pypi/blackcellmagic

.. _here: https://github.com/tobinjones/jupyterlab_formatblack
