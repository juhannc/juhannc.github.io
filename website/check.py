#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse,unquote
import argparse
parser=argparse.ArgumentParser(description='Audit built PoC links and static content')
parser.add_argument('output',type=Path)
args=parser.parse_args()
root=args.output.resolve()
errors=[]
for file in root.rglob('*.html'):
 soup=BeautifulSoup(file.read_text(),'html.parser')
 non_code=BeautifulSoup(file.read_text(),'html.parser')
 for pre in non_code.select('pre'):pre.decompose()
 if '{{' in str(non_code) or '{%' in str(non_code):errors.append(f'Liquid remains: {file}')
 ids=[x['id'] for x in soup.select('[id]')]
 if len(ids)!=len(set(ids)):errors.append(f'Duplicate IDs: {file}')
 for a in soup.select('[href], [src]'):
  url=a.get('href',a.get('src')); parsed=urlparse(url)
  if parsed.scheme or parsed.netloc:continue
  target=(root/parsed.path.lstrip('/')) if parsed.path.startswith('/') else (file.parent/parsed.path)
  if not parsed.path:target=file
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'Broken: {file.relative_to(root)} -> {url}')
  elif parsed.fragment and target.suffix=='.html' and not BeautifulSoup(target.read_text(),'html.parser').find(id=unquote(parsed.fragment)):
   errors.append(f'Missing anchor: {file.relative_to(root)} -> {url}')
assert '{{' not in (root/'llms.txt').read_text()
for path in ['files/Johann_Christensen_Resume.pdf','Johann_Christensen_Headshot.jpg']:
 assert (root/path).read_bytes()==(Path(__file__).resolve().parents[1]/path).read_bytes()
print('Static audit:',errors or 'All HTML links, anchors, IDs, source rendering, and exact PDF/headshot copies pass')

assert not errors
