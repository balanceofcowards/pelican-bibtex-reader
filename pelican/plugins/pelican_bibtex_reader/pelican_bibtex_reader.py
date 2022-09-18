import datetime as dt
import os

from pelican import signals
from pelican.readers import BaseReader

from . import bibtex

class BibTeXReader(BaseReader):
    enabled = True

    file_extensions = ['bib']

    # You need to have a read method, which takes a filename and returns
    # some content and the associated metadata.
    def read(self, filename):
        metadata = {'title': os.path.basename(filename)[:-4],
                    'date': str(dt.date.today())}

        with open(filename, 'rb') as raw_file:
            bibstring = bibtex.get_decoded_string_from_file(raw_file)
            metadata['bibtexdatabase'] = bibtex.get_bibitems(bibstring).entries

        metadata.update(get_keyvalue_pairs(filename))

        parsed = {}
        for key, value in metadata.items():
            parsed[key] = self.process_metadata(key, value)

        content = generate_HTML_content(metadata['bibtexdatabase'])
        return content, parsed

def get_keyvalue_pairs(filename):
    result = {}
    with open(filename) as bibfile:
        for line in bibfile:
            if line[0] != '%': break
            if not ':' in line: continue
            key, value = [e.strip() for e in line[1:].split(':', 1)]
            result[key] = value
    return result

def generate_HTML_content(bibelements):
    result = "".join(f"<li>{key_value_to_HTML(e)}</li>"
            for e in bibelements)
    return f"<ol>{result}</ol>"

def key_value_to_HTML(dictionary):
    result = "".join(f"<li><strong>{k}: </strong>{v}</li>"
                     for k, v in dictionary.items())
    return f"<ul style='list-style-type: none;'>{result}</ul>"

def add_reader(readers):
    readers.reader_classes['bib'] = BibTeXReader

def register():
    signals.readers_init.connect(add_reader)
