import re
import bibtexparser

class BibTeXDecodingError(ValueError):
    pass

def get_bibitems(bibstring):
    parser = bibtexparser.bparser.BibTexParser(
        ignore_nonstandard_types=False,
        common_strings=True,
        customization=customize_bibtex)
    try:
        result = parser.parse(bibstring)
    except bibtexparser.bibdatabase.UndefinedString as e:
        raise BibTeXDecodingError('Error while parsing: {}. '.format(e)
                         + 'Try finding and replacing that string in your '
                         + 'bibtex file.')
    return result

def customize_bibtex(record):
    record = bibtexparser.customization.convert_to_unicode(record)
    record = bibtexparser.customization.author(record)
    record = bibtexparser.customization.keyword(record)
    if 'keywords' in record:
        record['keywords'] = record['keywords'].replace(';', ',')
    record = bibtexparser.customization.doi(record)
    record = bibtexparser.customization.page_double_hyphen(record)
    if "pages" in record:
        record["pages"] = record["pages"].replace('--', '\u2013')
    return record


def get_decoded_string_from_file(bibfile):
    bytestream = bibfile.read()
    tried_encodings = []
    proposed_encoding = re.search(b"[Ee]ncoding: (\\S+)", bytestream)
    if proposed_encoding:
        encoding = proposed_encoding.group(1).decode("utf-8")
        try:
            result = bytestream.decode(encoding)
            return result
        except:
            tried_encodings.append(encoding)
    try:
        result = bytestream.decode("utf-8-sig") # Handle BOM transparently
        return result
    except:
        tried_encodings.append("utf-8")
    try:
        result = bytestream.decode("latin1")
        return result
    except:
        tried_encodings.append("latin1")
        raise BibTeXDecodingError("Unknown file encoding. "
                                  + "Could not decode properly.", tried_encodings)

