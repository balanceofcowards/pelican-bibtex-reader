Pelican BibTeX Reader: A Plugin for Pelican
====================================================

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/pelican-bibtex-reader/build)](https://github.com/balanceofcowards/pelican-bibtex-reader/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-bibtex-reader)](https://pypi.org/project/pelican-bibtex-reader/)
![License](https://img.shields.io/pypi/l/pelican-bibtex-reader?color=blue)

A Pelican reader to process BibTeX files

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-bibtex-reader

Usage
-----

This plugin uses [python-bibtexparser](https://github.com/sciunto-org/python-bibtexparser) to parse properly formatted BibTeX files for use in
[Pelican](https://getpelican.com/). Just put a BibTeX file
with ending `.bib` anywhere in your content directory.

The content provided by this plugin consists of only a
crude HTML rendering of the key-value pairs of each
entry. However, the full bibtex database is available
as Python object in the metadata of the page (key: `bibtexdatabase`).
Using an appropriate template, nice lists of literature
can be rendered, easily. Check out [the literature list on my homepage](https://andreas.fischer-family.online/pages/publications.html)
for an example.

Metadata needed for Pelican 
(such as the title, the date, or the template to be used)
can be added at the top of the `.bib`-file, using the following syntax:

```
% Title: Some title
% Date: 01.02.2023
% ...
% Feel free to write anything else; only
% key: value
% pairs are parsed. All other comments are ignored.

@MISC{...}
```

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/balanceofcowards/pelican-bibtex-reader/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
