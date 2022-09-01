import datetime as dt

from pelican import signals
from pelican.readers import BaseReader

from . import bibtex

# Create a new reader class, inheriting from the pelican.reader.BaseReader
class BibTeXReader(BaseReader):
    enabled = True  # Yeah, you probably want that :-)

    # The list of file extensions you want this reader to match with.
    # If multiple readers were to use the same extension, the latest will
    # win (so the one you're defining here, most probably).
    file_extensions = ['bib']

    # You need to have a read method, which takes a filename and returns
    # some content and the associated metadata.
    def read(self, filename):
        metadata = {'title': 'Publications',
                    'template': 'publications',
                    'date': str(dt.date.today())}

        parsed = {}
        for key, value in metadata.items():
            parsed[key] = self.process_metadata(key, value)

        with open(filename, 'rb') as raw_file:
            bibstring = bibtex.get_decoded_string_from_file(raw_file)
            parsed["elements"] = bibtex.get_bibitems(bibstring).entries
        return "Some content", parsed

def add_reader(readers):
    readers.reader_classes['bib'] = BibTeXReader

# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)
