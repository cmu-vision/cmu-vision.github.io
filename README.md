## cmu-vision-web

## Adding People
Each person can be added by creating a pull request that adds a text file `andrew_id.txt` in the `people/{faculty/student/postocs}` folder. The text file should have the following format:

```
name:: Full Name
img:: link_to_image
url:: link_to_personal_webpage
program:: PhD or MS (required for students)
year:: year_started_at_CMU (required for students, postdocs, and visitors)
```

**Please make sure the image linked is less than 50 KB.** 

The image url can be an external link, or you can add an image to the appropriate subfolder in `people/{faculty/student/postdocs}/andrew_id.jpeg` in the same pull request. For example, Shubham's image is saved in `people/faculty/stulsian.jpeg` and the txt file link is `img:: people/faculty/stulsian.jpeg`.



## Adding a Research Project
Each project can be added by creating a pull request that adds a text file `project_id.txt` in the `projects/` folder (see [examples](projects/)). The text file should have the following format:

```
title:: Project or Publication Title
img:: link_to_image_or_gif
url:: link_to_project_webpage_or_pdf
year:: year_published (required so we can automatically show recent projects)
```

The image should ideally be an external link (so we don't host a large github repo) but you may also add an image to the projects folder and link to it if no external link is available. You you can also link to a GIF file, but not a video (e.g. MP4). The image will be resized to a 2:1 aspect ratio, so please choose an appropriate project teaser.



## Adding a Course
Each course can be added by creating a pull request that adds a text file `coursenum.txt` in the `courses/` folder (see [examples](courses/)). The text file should have the following format:

```
number: official_course_number (or multiple numbers for cross-listed ones)
title:: Course Title
description:: Short descption about the course. Please DO NOT use a line-break, or the description will only show until the first \n .
(optional) img:: link_to_image (if no url, entirely skip this line. Do not even add 'img:: ' to the text)
(optional) url:: link_to_course_webpage (if no url, entirely skip this line. Do not add 'url:: ' to the text)
```

The image should ideally be an external link (so we don't host a large github repo) but you may also add an image to the course folder and link to it if no external link is available. The image will be resized to a 1:1 aspect ratio, so please choose an appropriate project teaser.
