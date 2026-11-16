"""Production migration regressions exercised against a fresh static build."""
import subprocess,sys,tempfile,unittest
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
class SiteBuildTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.temp=tempfile.TemporaryDirectory();cls.out=Path(cls.temp.name)
  builder=ROOT/('website' if (ROOT/'website').exists() else 'redesign')/'build.py'
  subprocess.run([sys.executable,str(builder),'--output',str(cls.out)],check=True,capture_output=True)
 @classmethod
 def tearDownClass(cls):cls.temp.cleanup()
 def soup(self,path):return BeautifulSoup((self.out/path).read_text(),'html.parser')
 def test_cv_selected_publications_are_cards_and_preserve_status(self):
  panel=self.soup('cv/index.html').select_one('[data-resume-panel="selected-publications"]')
  self.assertEqual(len(panel.select('.paper-card')),4)
  self.assertIn('Accepted',panel.get_text())
 def test_reviewing_and_supervision(self):
  cv=self.soup('cv/index.html')
  self.assertIsNotNone(cv.find('a',string='Reviewing & Service'))
  for name in ['Jiahua Wei','Friedrich Werner','Mina Randolf','ICTAI','Session Chair','Best of Session Paper Award']:
   self.assertIn(name,cv.get_text())
 def test_migration_metadata_and_domain(self):
  home=self.soup('index.html')
  self.assertEqual((self.out/'CNAME').read_text().strip(),'www.chrstnsn.de')
  self.assertTrue((self.out/'.nojekyll').exists())
  self.assertEqual(home.select_one('link[rel="canonical"]')['href'],'https://www.chrstnsn.de/')
  self.assertEqual(len(home.select('.organization-logo')),3)
 def test_conference_handouts_belong_to_matching_publications(self):
  for slug in ['2024-09-29-Towards-Certifiable-AI-in-Aviation','2024-10-28-Advancing-the-AI-Based-Realization-of-ACASX','2026-09-13-On-the-Applicability-of-Safety-Nets-A-Safety-By-Design-Solution-for-Certifying-Neural-Networks']:
   page=self.soup(f'publication/{slug}/index.html')
   a=page.find('a',string=lambda x:x and 'Talk Handout' in x)
   self.assertIsNotNone(a)
   self.assertTrue((self.out/a['href'].lstrip('/')).read_bytes().startswith(b'%PDF-'))
if __name__=='__main__':unittest.main()
