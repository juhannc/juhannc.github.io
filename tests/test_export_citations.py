import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'export_citations.py'
spec = importlib.util.spec_from_file_location('export_citations', MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CitationExportTests(unittest.TestCase):
    def test_journal_fields_dates_and_private_metadata(self):
        entry = {'ID': 'Example2026', 'ENTRYTYPE': 'article', 'author': 'Doe, Jane',
                 'title': 'AI in Aviation', 'date': '2026-09-23', 'journaltitle': 'Journal',
                 'file': '/private/library/paper.pdf', 'groups': 'Internal', 'abstract': 'Long text'}
        result = module.export_entry(entry)
        self.assertIn('date = {2026-09-23}', result['biblatex'])
        self.assertIn('journaltitle = {Journal}', result['biblatex'])
        self.assertIn('year = {2026}', result['bibtex'])
        self.assertIn('month = sep', result['bibtex'])
        self.assertIn('journal = {Journal}', result['bibtex'])
        self.assertIn('title = {AI in Aviation},', result['bibtex'])
        self.assertIn('title = {AI in Aviation},', result['biblatex'])
        for value in result.values():
            self.assertNotIn('/private/', value)
            self.assertNotIn('Internal', value)
            self.assertNotIn('abstract =', value)

    def test_thesis_has_traditional_type_and_school(self):
        result = module.export_entry({'ID': 'Thesis2025', 'ENTRYTYPE': 'thesis',
                                      'title': 'Thesis', 'date': '2025', 'type': 'mathesis',
                                      'institution': 'University'})
        self.assertIn('@thesis{Thesis2025,', result['biblatex'])
        self.assertIn('@mastersthesis{Thesis2025,', result['bibtex'])
        self.assertIn('school = {University}', result['bibtex'])
        self.assertNotIn('institution =', result['bibtex'])

    def test_software_and_forthcoming_status_survive_conversion(self):
        result = module.export_entry({'ID': 'Software2026', 'ENTRYTYPE': 'software',
                                      'title': 'Safety Nets', 'date': '2026-12',
                                      'version': '1.0.0', 'publisher': 'Zenodo',
                                      'pubstate': 'accepted'})
        self.assertIn('@software{', result['biblatex'])
        self.assertIn('@misc{', result['bibtex'])
        self.assertIn('version 1.0.0', result['bibtex'])
        self.assertIn('Accepted; forthcoming', result['bibtex'])
        self.assertNotIn('pubstate =', result['bibtex'])

    def test_serialized_entries_round_trip(self):
        entry = {'ID': 'Unicode2026', 'ENTRYTYPE': 'inproceedings',
                 'title': 'AI {Safety}', 'author': r'K{\"{o}}ster, Frank and Christensen, Johann',
                 'date': '2026-09', 'booktitle': 'Conference'}
        result = module.export_entry(entry)
        for text in result.values():
            parsed = module.read_bibliography(text)
            self.assertIn(entry['ID'], parsed)
            self.assertEqual(parsed[entry['ID']]['author'], entry['author'])
            self.assertEqual(parsed[entry['ID']]['title'], entry['title'])
            self.assertEqual(parsed[entry['ID']].get('booktitle'), entry['booktitle'])


if __name__ == '__main__':
    unittest.main()
