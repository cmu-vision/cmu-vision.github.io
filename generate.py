#!/usr/bin/env python3
"""Unified site generator for Computer Vision @ CMU.

Replaces gen_people_page.py, gen_research_page.py, gen_course_page.py.
Generates: index.html, people.html, research.html, courses.html, papers.html
"""

import glob
import html
import os
import random

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------

def read_file(fpath):
    with open(fpath, 'r') as f:
        return f.read()


def write_file(fpath, content):
    with open(fpath, 'w') as f:
        f.write(content)


def get_txtfile_ids(folder):
    txtfiles = glob.glob(os.path.join(folder, '*.txt'))
    return [os.path.splitext(os.path.basename(t))[0] for t in txtfiles]


def get_txtfile_ids_skip_underscore(folder):
    """Like get_txtfile_ids but skip filenames starting with underscore."""
    ids = get_txtfile_ids(folder)
    return [i for i in ids if not i.startswith('_')]


def parse_txt(fpath):
    """Parse a key:: value text file and return (dict, key_list)."""
    elems = {}
    keys = []
    with open(fpath, 'r') as f:
        for ln in f:
            parts = ln.split('::', 1)
            if len(parts) != 2:
                continue
            key = parts[0].strip()
            val = parts[1].strip()
            elems[key] = val
            keys.append(key)
    return elems, keys


def esc(text):
    """HTML-escape a string."""
    return html.escape(text)


# ---------------------------------------------------------------------------
# People page  (people.html) — faculty only, shuffled, with interests
# ---------------------------------------------------------------------------

def person_card_html(elems):
    name = esc(elems.get('name', ''))
    url = elems.get('url', '#')
    img = elems.get('img', 'assets/incognito.jpeg')
    interests = esc(elems.get('interests', ''))

    lines = []
    lines.append('<div class="card card--person">')
    lines.append(f'  <a href="{esc(url)}">')
    lines.append(f'    <img class="card--person__photo" src="{esc(img)}" alt="{name}">')
    lines.append(f'  </a>')
    lines.append(f'  <div class="card--person__name"><a href="{esc(url)}">{name}</a></div>')
    if interests:
        lines.append(f'  <div class="card--person__interests">{interests}</div>')
    lines.append('</div>')
    return '\n'.join(lines)


def generate_people():
    template = read_file('./templates/people_base.html')
    folder = './people/faculty'
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)

    cards = []
    for pid in ids:
        elems, keys = parse_txt(os.path.join(folder, pid + '.txt'))
        if 'img' not in keys:
            elems['img'] = 'assets/incognito.jpeg'
        cards.append(person_card_html(elems))

    html_out = template.replace(
        '<!-- autogen faculty -->',
        '<!-- autogen faculty -->\n' + '\n'.join(cards)
    )
    write_file('./people.html', html_out)
    print(f'  people.html  — {len(cards)} faculty')


# ---------------------------------------------------------------------------
# Research page  (research.html) — all 37 projects, sorted by year desc
# ---------------------------------------------------------------------------

def project_card_html(elems):
    title = esc(elems.get('title', ''))
    url = elems.get('url', '#')
    img = elems.get('img', 'assets/project.jpeg')
    year = esc(elems.get('year', ''))
    topics_raw = elems.get('topics', '')
    topics_list = [t.strip() for t in topics_raw.split(',') if t.strip()]
    # data-topics attribute for JS filtering
    data_topics = ','.join(topics_list)

    tags_html = ''
    for t in topics_list:
        tags_html += f'<span class="tag">{esc(t)}</span>'

    lines = []
    lines.append(f'<div class="card card--project" data-topics="{esc(data_topics)}">')
    lines.append(f'  <a href="{esc(url)}">')
    lines.append(f'    <img class="card--project__thumb" src="{esc(img)}" alt="{title}">')
    lines.append(f'  </a>')
    lines.append(f'  <div class="card--project__body">')
    lines.append(f'    <div class="card--project__title"><a href="{esc(url)}">{title}</a></div>')
    lines.append(f'    <div class="card--project__meta">')
    lines.append(f'      <span class="card--project__year">{year}</span>')
    if tags_html:
        lines.append(f'      <div class="card--project__tags">{tags_html}</div>')
    lines.append(f'    </div>')
    lines.append(f'  </div>')
    lines.append(f'</div>')
    return '\n'.join(lines)


def generate_research():
    template = read_file('./templates/research_base.html')
    folder = './projects'
    ids = get_txtfile_ids(folder)

    # Parse all projects
    projects = []
    for pid in ids:
        elems, keys = parse_txt(os.path.join(folder, pid + '.txt'))
        if 'img' not in keys:
            elems['img'] = 'assets/project.jpeg'
        projects.append(elems)

    # Sort by year descending
    projects.sort(key=lambda p: int(p.get('year', 0)), reverse=True)

    cards = [project_card_html(p) for p in projects]

    html_out = template.replace(
        '<!-- autogen projects -->',
        '<!-- autogen projects -->\n' + '\n'.join(cards)
    )
    write_file('./research.html', html_out)
    print(f'  research.html — {len(cards)} projects')


# ---------------------------------------------------------------------------
# Courses page  (courses.html) — sorted by course number ascending
# ---------------------------------------------------------------------------

def course_card_html(elems):
    number = esc(elems.get('number', ''))
    title = esc(elems.get('title', ''))
    desc = esc(elems.get('description', ''))
    url = elems.get('url', '')
    img = elems.get('img', 'courses/16385.png')

    lines = []
    lines.append('<div class="card card--course">')
    lines.append(f'  <img class="card--course__thumb" src="{esc(img)}" alt="{title}">')
    lines.append(f'  <div class="card--course__body">')
    lines.append(f'    <div class="card--course__number">{number}</div>')
    lines.append(f'    <h3 class="card--course__title">{title}</h3>')
    lines.append(f'    <p class="card--course__desc">{desc}</p>')
    if url:
        lines.append(f'    <a class="card--course__link" href="{esc(url)}">Course Website &rarr;</a>')
    lines.append(f'  </div>')
    lines.append('</div>')
    return '\n'.join(lines)


def generate_courses():
    template = read_file('./templates/courses_base.html')
    folder = './courses'
    ids = get_txtfile_ids(folder)
    ids.sort()

    cards = []
    for cid in ids:
        elems, keys = parse_txt(os.path.join(folder, cid + '.txt'))
        if 'img' not in keys:
            elems['img'] = 'courses/16385.png'
        cards.append(course_card_html(elems))

    html_out = template.replace(
        '<!-- autogen courses -->',
        '<!-- autogen courses -->\n' + '\n'.join(cards)
    )
    write_file('./courses.html', html_out)
    print(f'  courses.html  — {len(cards)} courses')


# ---------------------------------------------------------------------------
# Papers page  (papers.html) — conference sections, one .txt per paper
# ---------------------------------------------------------------------------

def paper_card_html(elems):
    title = esc(elems.get('title', ''))
    url = elems.get('url', '#')
    authors = esc(elems.get('authors', ''))
    pdf = elems.get('pdf', '')

    lines = []
    lines.append('<div class="card card--paper">')
    lines.append(f'  <div class="card--paper__body">')
    title_line = f'<a href="{esc(url)}">{title}</a>'
    if pdf:
        title_line += f' <a class="card--paper__pdf" href="{esc(pdf)}">PDF</a>'
    lines.append(f'    <div class="card--paper__title-line">{title_line}</div>')
    lines.append(f'    <div class="card--paper__authors">{authors}</div>')
    lines.append(f'  </div>')
    lines.append('</div>')
    return '\n'.join(lines)


def _conference_display_name(folder_name):
    """Turn e.g. cvpr2025 into 'CVPR 2025'."""
    if len(folder_name) >= 4 and folder_name[-4:].isdigit():
        conf = folder_name[:-4].upper()
        year = folder_name[-4:]
        return f'{conf} {year}'
    return folder_name.replace('_', ' ').title()


def generate_papers():
    template = read_file('./templates/papers_base.html')
    papers_dir = './papers'
    if not os.path.isdir(papers_dir):
        html_out = template.replace(
            '<!-- autogen papers -->',
            '<!-- autogen papers -->\n      <p class="papers-empty">No papers yet. Coming soon.</p>'
        )
        write_file('./papers.html', html_out)
        print(f'  papers.html  — 0 papers (empty)')
        return

    subfolders = [d for d in os.listdir(papers_dir)
                  if os.path.isdir(os.path.join(papers_dir, d)) and not d.startswith('.')]
    # Sort: year descending, then folder ascending (so CVPR 2026 before ICLR 2026)
    def _papers_sort_key(s):
        year = int(s[-4:]) if len(s) >= 4 and s[-4:].isdigit() else 0
        return (-year, s)
    subfolders.sort(key=_papers_sort_key)

    # Build filter bar buttons and sections
    filter_buttons = ['<div class="filter-bar papers-filter-bar">']
    filter_buttons.append('  <button class="filter-btn active" data-conference="all">All</button>')
    sections_html = []
    total_papers = 0
    for folder_name in subfolders:
        folder = os.path.join(papers_dir, folder_name)
        ids = get_txtfile_ids_skip_underscore(folder)
        if not ids:
            continue
        display_name = _conference_display_name(folder_name)
        filter_buttons.append(f'  <button class="filter-btn" data-conference="{esc(folder_name)}">{esc(display_name)}</button>')
        papers = []
        for pid in ids:
            fpath = os.path.join(folder, pid + '.txt')
            elems, keys = parse_txt(fpath)
            papers.append(elems)
        random.shuffle(papers)
        cards = [paper_card_html(p) for p in papers]
        count_text = f'({len(papers)} paper{"s" if len(papers) != 1 else ""})'
        section = (
            f'<div class="papers-section" data-conference="{esc(folder_name)}">\n'
            f'  <h2 class="papers-section__title">{esc(display_name)} <span class="papers-section__count">{count_text}</span></h2>\n'
            f'  <div class="grid--papers">\n'
            + '\n'.join(cards) + '\n'
            f'  </div>\n</div>'
        )
        sections_html.append(section)
        total_papers += len(papers)

    if not sections_html:
        content = '      <p class="papers-empty">No papers yet. Coming soon.</p>'
    else:
        filter_buttons.append('</div>')
        content = '\n'.join(filter_buttons) + '\n\n' + '\n'.join(sections_html)

    html_out = template.replace('<!-- autogen papers -->', '<!-- autogen papers -->\n' + content)
    write_file('./papers.html', html_out)
    print(f'  papers.html  — {total_papers} papers in {len(sections_html)} conference(s)')


# ---------------------------------------------------------------------------
# Index / Overview page  (index.html) — 6 featured projects (most recent)
# ---------------------------------------------------------------------------

def generate_index():
    template = read_file('./templates/index_base.html')
    folder = './projects'
    ids = get_txtfile_ids(folder)

    projects = []
    for pid in ids:
        elems, keys = parse_txt(os.path.join(folder, pid + '.txt'))
        if 'img' not in keys:
            elems['img'] = 'assets/project.jpeg'
        projects.append(elems)

    # Sort by year descending
    projects.sort(key=lambda p: int(p.get('year', 0)), reverse=True)

    # Pick 6 featured projects that cover diverse topics.
    # Walk the recency-sorted list; skip a project if its primary topic
    # (first listed) has already been used, unless we need to fill slots.
    target = 6
    topic_order = [
        '3D Vision', 'Generative Models', 'Computational Imaging',
        'Robotics', 'Recognition & Detection', 'Scene Understanding',
    ]
    used_topics = set()
    featured = []

    # Pass 1: one project per primary topic (most recent for that topic)
    for topic in topic_order:
        if len(featured) >= target:
            break
        for p in projects:
            if p in featured:
                continue
            p_topics = [t.strip() for t in p.get('topics', '').split(',') if t.strip()]
            if topic in p_topics:
                featured.append(p)
                used_topics.update(p_topics)
                break

    # Pass 2: fill remaining slots with most-recent unused projects
    for p in projects:
        if len(featured) >= target:
            break
        if p not in featured:
            featured.append(p)

    cards = [project_card_html(p) for p in featured]

    html_out = template.replace(
        '<!-- autogen featured -->',
        '<!-- autogen featured -->\n' + '\n'.join(cards)
    )
    write_file('./index.html', html_out)
    print(f'  index.html    — {len(featured)} featured projects')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print('Generating site...')
    generate_index()
    generate_people()
    generate_research()
    generate_courses()
    generate_papers()
    print('Done!')
