Installation instructions
=========================
We recommend installing `anaconda <https://www.continuum.io/>`_ prior to using this package.

Installing *NUSSL* is easy using pip and the Python Package Index. This will install all required dependencies alongside the
NUSSL installation. Use the following command::

        pip install librosa

or::

        sudo pip install librosa

to install system-wide.

Alternatively, you may download the source code and install with the following command::

        python setup.py install

Finally, you may download and copy the nussl folder into your working directory and directly import the modules

nussl requires: ``python 2.7``, ``numpy version >= 1.8.0``, ``scipy version >= 0.13.0``, and
``matplotlib version >= 1.3.1`` all of which are satisfied by `anaconda <https://www.continuum.io/>`_.