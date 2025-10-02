cuesplit
========

Python script that splits CD audio and add metadata tags using the information
extracted from CUE sheet.

Based on ffmpeg and libcue. Currently supports flac, mp3 and wav as output formats.

Requirements
------------

- ffmpeg binary (in $PATH)
- `pylibcue <https://pypi.org/project/pylibcue/>`_

Install
-------

.. code-block:: bash

	pip install cuesplit

Usage
-----

.. code-block:: bash

	cuesplit -h
	cuesplit -i input.cue -o ./output/ -f mp3 -j 4

License
-------

cuesplit is licensed under the GNU General Public License v2.0.
