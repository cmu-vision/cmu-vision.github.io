## cmu-vision-web

### Adding to the 'People' page
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
