
.. NOTES FOR CREATING A RELEASE:
..
..   * bump the version number in scrubadub/__init__.py
..   * update docs/changelog.rst
..   * git push
..   * create a release https://github.com/LeapBeyond/scrubadub/releases
..      * This should trigger a github action to upload to pypi
..      * ReadTheDocs.io should see any changes and also rebuild the docs


***************
scrubadub_spacy
***************

``scrubadub`` removes personally identifiable information from text.
``scrubadub_spacy`` is an extension that uses spaCy NLP models to remove personal information from text.

This package contains two extra detectors:

* ``scrubadub_spacy.detectors.SpacyEnityDetector`` - A detector that uses the spacy NER model to find locations, names, dates and other entities.
* ``scrubadub_spacy.detectors.SpacyNameDetector`` - A detector that uses the spacy NER model and context words to find names in text.

For more information on how to use this package see the
`scrubadub spacy documentation <https://scrubadub.readthedocs.io/en/develop/names.html#spacy>`_
and the `scrubadub repository <https://github.com/LeapBeyond/scrubadub>`_.


.. image:: https://img.shields.io/github/workflow/status/LeapBeyond/scrubadub_spacy/Python%20package/main
   :target: https://github.com/LeapBeyond/scrubadub_spacy/actions?query=workflow%3A%22Python+package%22+branch%3Amain
   :alt:  Build Status
.. image:: https://img.shields.io/pypi/v/scrubadub_spacy.svg
   :target: https://pypi.org/project/scrubadub_spacy/
   :alt:  Version
.. image:: https://img.shields.io/pypi/dm/scrubadub_spacy.svg
   :target: https://pypi.org/project/scrubadub_spacy/
   :alt:  Downloads
.. image:: https://coveralls.io/repos/github/LeapBeyond/scrubadub_spacy/badge.svg?branch=master
   :target: https://coveralls.io/r/LeapBeyond/scrubadub_spacy
   :alt:  Test Coverage
.. image:: https://readthedocs.org/projects/scrubadub/badge/?version=latest
   :target: https://readthedocs.org/projects/scrubadub/?badge=latest
   :alt:  Documentation Status


New maintainers
---------------

`LeapBeyond <http://leapbeyond.ai/>`_ are excited to be supporting scrubadub with ongoing maintenance and development.
Thanks to all of the contributors who made this package a success, but especially `@deanmalmgren <https://github.com/deanmalmgren>`_, `IDEO <https://www.ideo.com/>`_ and `Datascope <https://datascopeanalytics.com/>`_.
