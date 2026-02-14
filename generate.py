#!/usr/bin/env python3
"""Unified site generator for Computer Vision @ CMU.

Replaces gen_people_page.py, gen_research_page.py, gen_course_page.py.
Generates: index.html, people.html, research.html, courses.html
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
    print('Done!')
