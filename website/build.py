#!/usr/bin/env python3
"""Build the production website from curated profile and bibliographic sources."""
from pathlib import Path
import argparse
import json
import hashlib
import re
import shutil
import sys
from html import escape
from xml.sax.saxutils import escape as xml_escape

import markdown
import yaml
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
from pylatexenc.latex2text import LatexNodes2Text

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
from export_citations import read_bibliography


def frontmatter(path):
    _, front, body = path.read_text().split('---', 2)
    return yaml.safe_load(front), body


def build(out):
    out.mkdir(parents=True, exist_ok=True)
    env = Environment(loader=FileSystemLoader(HERE / 'templates'), autoescape=select_autoescape())
    domain = (ROOT / 'CNAME').read_text().strip()
    site_url = 'https://' + domain
    config = yaml.safe_load((ROOT / '_config.yml').read_text())
    citations = json.loads((ROOT / '_data/citations.json').read_text())
    labels = {'manuscripts': 'Journal Article', 'conferences': 'Conference Paper',
              'academic': 'Academic Thesis', 'preprints': 'Preprint', 'supervised': 'Supervised Thesis'}
    publications = []
    for path in (ROOT / '_publications').rglob('*.md'):
        p, body = frontmatter(path)
        if p.get('category') not in labels:
            continue
        p.update(url=p['permalink'].rstrip('/') + '/', year=str(p['date'])[:4],
                 date=str(p['date']), label=labels[p['category']],
                 abstract=Markup(markdown.markdown(body)), citations=citations[p['bibkey']])
        entry = next(iter(read_bibliography(p['citations']['biblatex']).values()))
        p['authors'] = ', '.join(LatexNodes2Text().latex_to_text(' '.join(reversed(name.split(', ', 1))))
                                for name in entry.get('author', '').split(' and '))
        p['citation_html'] = Markup(p.get('citation', ''))
        publications.append(p)
    publications.sort(key=lambda p: p['date'], reverse=True)
    by_key = {p['bibkey']: p for p in publications}
    services = yaml.safe_load((ROOT / '_data/service.yml').read_text())
    academic_service = yaml.safe_load((ROOT / '_data/academic_service.yml').read_text())
    for award in academic_service['recognition']:
        award['publication'] = by_key[award['bibkey']]
    _, cv = frontmatter(ROOT / '_pages/cv.md')
    cv = re.sub(r"{{\s*'([^']+)'\s*\| relative_url\s*}}", r'\1', cv)
    soup = BeautifulSoup(cv, 'html.parser')
    # Career/education/skills/teaching remain curated in cv.md. Dynamic panels
    # are rendered directly from canonical publication/service data in Jinja.
    cv_panels = []
    for panel in soup.select('[data-resume-panel]'):
        key = panel['data-resume-panel']
        if key in ('selected-publications', 'service'):
            panel.clear()
        cv_panels.append(dict(id=key, html=Markup(str(panel))))
    base = dict(publications=publications, supervised=[p for p in publications if p['category'] == 'supervised'],
                services=services, academic_service=academic_service,
                nav=[('Overview', '/'), ('Publications', '/publications/'), ('CV', '/cv/'), ('Service', '/service/')],
                selected=[by_key[k] for k in ['Christensen2026', 'Christensen2026a', 'Christensen2025']],
                cv_selected=[by_key[k] for k in ['Christensen2026', 'Christensen2025', 'Berro2025', 'Christensen2024']],
                cv_panels=cv_panels, site_url=site_url,
                asset_versions={p.name: hashlib.sha256(p.read_bytes()).hexdigest()[:12] for p in (HERE / "assets").iterdir() if p.is_file()},
                profile_description='Johann Christensen — AI expert and researcher at DLR. Safe AI for aviation, robotics, and autonomous systems.')
    paths = []

    def render(template, path, title, active, **kwargs):
        target = out / path.lstrip('/')
        if not target.suffix:
            target = target / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(env.get_template(template).render(**base, title=title, active=active, path=path, **kwargs))
        paths.append(path)

    render('home.html', '/', 'Safe AI for Aviation', 'Overview')
    render('publications.html', '/publications/', 'Publications', 'Publications')
    render('cv.html', '/cv/', 'Curriculum Vitae', 'CV')
    render('service.html', '/service/', 'Academic Service', 'Service')
    for p in publications:
        render('publication.html', p['url'], p['title'], 'Publications', p=p)
    render('sitemap.html', '/sitemap/', 'Sitemap', '')
    render('404.html', '/404.html', 'Page Not Found', '')
    shutil.copytree(HERE / 'assets', out / 'assets', dirs_exist_ok=True)
    shutil.copytree(ROOT / 'images', out / 'images', dirs_exist_ok=True)
    resources = {'Johann_Christensen_Headshot.jpg', 'files/Johann_Christensen_Resume.pdf'}
    for publication in publications:
        for field in ('handouturl', 'posterurl', 'slidesurl', 'paperurl'):
            url = publication.get(field) or ''
            if url.startswith('/files/'):
                resources.add(url.lstrip('/'))
    for f in resources:
        target = out / f
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / f, target)
    _, llms = frontmatter(ROOT / 'llms.txt')
    research_lines = '\n'.join(f'- [{p["title"]}]({site_url}{p["url"]}): {p["venue"]}, {p["year"]}. '
                               f'{p.get("publication_status", "")} {p["excerpt"]}'
                               for p in [by_key[k] for k in ['Christensen2026', 'Christensen2026a', 'Christensen2025', 'Berro2025']])
    llms = re.sub(r'{% assign selected_keys.*?{% endfor %}', lambda m: research_lines, llms, flags=re.S)
    llms = re.sub(r"{{\s*'([^']+)'\s*\| absolute_url\s*}}", lambda m: site_url + m[1], llms)
    llms = re.sub(r'{{\s*site.author.(\w+)\s*}}', lambda m: str(config['author'].get(m[1], '')), llms)
    (out / 'llms.txt').write_text(llms.lstrip() + f'\n- [Academic Service]({site_url}/service/): Reviewing, recognition, and thesis supervision.\n')
    (out / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        ''.join(f'<url><loc>{xml_escape(site_url + p)}</loc></url>' for p in paths if p != '/404.html') + '</urlset>')
    (out / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n')
    (out / 'CNAME').write_text(domain + '\n')
    (out / '.nojekyll').touch()
    for alias, canonical in {'/about/': '/', '/about.html': '/', '/resume/': '/cv/', '/cv-json/': '/cv/', '/resume-json/': '/cv/'}.items():
        target = out / alias.lstrip('/')
        if not target.suffix:
            target = target / 'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Page Moved</title>'
                          f'<link rel="canonical" href="{site_url}{canonical}"><meta http-equiv="refresh" content="0;url={canonical}">'
                          f'</head><body><a href="{canonical}">Continue to {escape(canonical)}</a></body></html>')
    print(f'Built {len(publications)} publication pages, {len(services)} reviewing activities and {len(paths)} total pages in {out}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    build(args.output.resolve())
