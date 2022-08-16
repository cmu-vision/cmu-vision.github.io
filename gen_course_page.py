import os
import glob
import random

MAX_PROJECTS = 24
CURRENT_YEAR = 2022

def read_file(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    return content

def get_txtfile_ids(folder):
    txtfiles = glob.glob('{}/*.txt'.format(folder))
    ids = [os.path.basename(txtfile)[:-4] for txtfile in txtfiles]
    return ids

# <img class="paper static" title="paper" src="src.png" />
def parse_course_info(course_id, course_folder):
    elems = {}
    keys = []
    fpath = os.path.join(course_folder, course_id  + '.txt')

    with open(fpath, 'r') as f:
        for ln in f.readlines():
            ln_items = ln.split('::')
            if len(ln_items) != 2:
                continue
            key, val = ln_items[0], ln_items[1]
            key = key.rstrip().lstrip()
            val = val.rstrip().lstrip()
            elems[key] = val
            keys.append(key)

    if 'img' not in keys:
        elems['img'] = 'courses/16385.jpeg'

    return elems, keys


def get_course_html_string(id, elems, keys):
    comment_str = '<!--------------------------------------------------------------------------->'
    course_str = ''
    course_str += '\n' + comment_str + '\n'
    course_str += '<table class="course" id={}>\n'.format(id)
    course_str += '<tr>\n<td>\n'
    course_str += '<div class="cropTeaser" style="background-image: url(\'{}\');">\n</div>\n'.format(elems['img'])
    course_str += '</td>\n<td class="courseDescription">\n'
    course_str += '<h2 class="courseTitle"> {} : {} </h2> \n {} \n'.format(elems['number'], elems['title'], elems['description'])
    if 'url' in keys:
        course_str += '<p class="offeringList"><a href="{}">Course Website</a></p>\n'.format(elems['url'])
    course_str += '</td>\n</tr>\n</table>\n'

    ## Meta fields
    # add some javascript here if needed using the  id for the added element

    course_str += comment_str + '\n'
    return course_str


if __name__ == '__main__':
    page_string = read_file('./courses_base.html')

    ###########################################################################
    ###########################################################################

    folder = './courses'
    courses_string = ''
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)
    for id in ids:
        elems, keys = parse_course_info(id, folder)
        courses_string += get_course_html_string(id, elems, keys)

    page_string = page_string.replace('<!-- autogen courses -->', '<!-- autogen courses -->\n' + courses_string)

    ###########################################################################
    ###########################################################################

    fpath = './courses.html'
    with open(fpath, 'w') as f:
        f.write(page_string)
