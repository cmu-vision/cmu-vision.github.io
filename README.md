## cmu-vision-web

Website for the Computer Vision group at Carnegie Mellon University.

### Site Structure

```
templates/          HTML base templates (index, people, research, courses)
people/             Faculty, student, and postdoc data files
  faculty/          One .txt file per faculty member
  students/         One .txt file per student
  postdocs/         One .txt file per postdoc
projects/           One .txt file per research project
courses/            One .txt file per course (+ optional thumbnail images)
assets/             Logo, icons, and default images
css/style.css       Site stylesheet
js/                 JavaScript (topic filtering, responsive nav)
sponsorship.html    Static sponsorship page (not auto-generated)
generate.py         Generates index.html, people.html, research.html, courses.html
```

### Generating the Site

After adding or editing any data files, regenerate the HTML pages:

```bash
python generate.py
```

This reads the templates in `templates/` and data files in `people/`, `projects/`, and `courses/`, then writes `index.html`, `people.html`, `research.html`, and `courses.html`.

### Adding People

Create a pull request that adds a text file `andrew_id.txt` in `people/{faculty,students,postdocs}/`:

```
name:: Full Name
img:: link_to_image
url:: link_to_personal_webpage
interests:: Research interests (faculty only)
program:: PhD or MS (students only)
year:: year_started_at_CMU (students, postdocs, and visitors)
```

**Please make sure the image linked is less than 50 KB.**

The image URL can be an external link, or you can add an image to the appropriate subfolder (e.g. `people/faculty/stulsian.jpeg`) and reference it as `img:: people/faculty/stulsian.jpeg`.

### Adding a Research Project

Create a pull request that adds a text file in `projects/` named `YEAR_ProjectName.txt`:

```
title:: Project or Publication Title
url:: link_to_project_webpage_or_pdf
img:: link_to_image_or_gif
year:: year_published
topics:: comma, separated, topics
```

Available topics: `3D Vision`, `Generative Models`, `Computational Imaging`, `Robotics`, `Recognition & Detection`, `Scene Understanding`.

The image should ideally be an external link (to keep the repo small). GIFs are supported but not videos. The image is displayed at a 2:1 aspect ratio, so choose an appropriate teaser.

### Adding a Course

Create a pull request that adds a text file `coursenum.txt` in `courses/`:

```
number:: official_course_number
title:: Course Title
description:: Short description (single line, no line breaks)
img:: link_to_image (optional — omit this line entirely if not available)
url:: link_to_course_webpage (optional — omit this line entirely if not available)
```

The course image is displayed at a 1:1 aspect ratio.
