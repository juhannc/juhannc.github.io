#!/usr/bin/env python3
"""Export public BibLaTeX and traditional BibTeX citations for the site collection.

Usage: python scripts/export_citations.py /path/to/literature.bib
Requires the optional packages in scripts/requirements-citations.txt.
"""
import argparse
import json
from pathlib import Path
import re

import bibtexparser
import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FIELDS = (
    'author', 'editor', 'title', 'date', 'journaltitle', 'booktitle', 'institution',
    'type', 'volume', 'number', 'pages', 'eid', 'series', 'publisher', 'location',
    'doi', 'url', 'isbn', 'issn', 'eprint', 'eprinttype', 'eprintclass', 'version',
    'pubstate', 'eventtitle', 'eventdate', 'venue', 'pagetotal',
)
TRADITIONAL_FIELDS = (
    'author', 'editor', 'title', 'booktitle', 'volume', 'number', 'pages', 'series', 'publisher',
    'doi', 'url', 'isbn', 'issn',
)
MONTHS = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')


def read_bibliography(text):
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    parser.homogenize_fields = False
    entries = bibtexparser.loads(text, parser=parser).entries
    return {entry['ID']: entry for entry in entries}


def serialize(entry_type, key, fields):
    if not re.fullmatch(r'[A-Za-z0-9_:.-]+', key):
        raise ValueError(f'Unsupported citation key: {key!r}')
    lines = [f'@{entry_type}{{{key},']
    for name, value in fields.items():
        if not value:
            continue
        # Protect title capitalization, including AI, ACAS, and ODD.
        if name == 'title':
            value = '{' + value + '}'
        if name == 'month' and value in MONTHS:
            lines.append(f'  {name} = {value},')
        else:
            lines.append(f'  {name} = {{{value}}},')
    return '\n'.join(lines + ['}']) + '\n'


def export_entry(entry):
    key, original_type = entry['ID'], entry['ENTRYTYPE'].lower()
    biblatex = {field: entry[field] for field in PUBLIC_FIELDS if entry.get(field)}
    bibtex = {field: entry[field] for field in TRADITIONAL_FIELDS if entry.get(field)}
    entry_type = original_type
    notes = []
    if entry.get('journaltitle'):
        bibtex['journal'] = entry['journaltitle']
    if entry.get('location'):
        bibtex['address'] = entry['location']
    if entry.get('date'):
        match = re.match(r'^(\d{4})(?:-(\d{2}))?', entry['date'])
        if not match:
            raise ValueError(f'Unsupported publication date for {key}')
        bibtex['year'] = match[1]
        if match[2]:
            bibtex['month'] = MONTHS[int(match[2]) - 1]
    if original_type == 'thesis':
        entry_type = 'mastersthesis' if entry.get('type') == 'mathesis' else 'phdthesis'
        bibtex['school'] = entry.get('institution', '')
    elif original_type == 'report':
        entry_type = 'techreport'
        bibtex['institution'] = entry.get('institution', '')
    elif original_type == 'software':
        entry_type = 'misc'
        notes.append('Software' + (', version ' + entry['version'] if entry.get('version') else ''))
        bibtex['howpublished'] = entry.get('publisher', '')
    elif original_type == 'online':
        entry_type = 'misc'
    elif original_type not in {'article', 'inproceedings', 'incollection', 'book', 'inbook', 'proceedings', 'misc'}:
        raise ValueError(f'Unsupported entry type for {key}: {original_type}')
    if entry.get('eprint'):
        notes.append((entry.get('eprinttype', 'Preprint') + ':' + entry['eprint']))
    if entry.get('pubstate'):
        notes.append({'accepted': 'Accepted; forthcoming', 'forthcoming': 'Forthcoming'}
                     .get(entry['pubstate'], entry['pubstate']))
    if notes:
        bibtex['note'] = '. '.join(notes)
    return {'biblatex': serialize(original_type, key, biblatex),
            'bibtex': serialize(entry_type, key, bibtex)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bibliography', type=Path)
    args = parser.parse_args()
    bibliography = read_bibliography(args.bibliography.read_text())
    citations = {}
    for path in sorted((ROOT / '_publications').rglob('*.md')):
        metadata = yaml.safe_load(path.read_text().split('---', 2)[1])
        key = metadata.get('bibkey')
        if not key or key not in bibliography:
            raise ValueError(f'{path.relative_to(ROOT)} needs a bibkey present in the source bibliography')
        if key in citations:
            raise ValueError(f'Duplicate publication key: {key}')
        citations[key] = export_entry(bibliography[key])
    (ROOT / '_data' / 'citations.json').write_text(
        json.dumps(citations, indent=2, ensure_ascii=False) + '\n')
    print(f'Exported BibLaTeX and BibTeX citations for {len(citations)} publications.')


if __name__ == '__main__':
    main()
