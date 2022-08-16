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
def parse_project_info(project_id, project_folder):
    elems = {}
    keys = []
    fpath = os.path.join(project_folder, project_id  + '.txt')

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

    if 'url' not in keys:
        elems['url'] = '#'
    if 'img' not in keys:
        elems['img'] = 'assets/project.jpeg'

    return elems, keys


def get_project_html_string(id, elems, keys):
    comment_str = '<!--------------------------------------------------------------------------->'
    project_str = ''
    project_str += '\n' + comment_str + '\n'
    project_str += '<table class="projectTable" id="{}">\n'.format(id)
    project_str += '<tr>\n<td>\n'
    project_str += '<a href="{}">\n <div class="imButtonWrapper"> \n <img src="{}" />\n</div>\n</a>\n'.format(elems['url'], elems['img'])
    project_str += '</td>\n</tr>\n<tr>\n<td>\n'
    project_str += '<a href="{}">{}</a>\n'.format(elems['url'], elems['title'])
    project_str += '</td>\n</tr>\n</table>\n'

    ## Meta fields
    # add some javascript here if needed using the  id for the added element

    project_str += comment_str + '\n'
    return project_str


if __name__ == '__main__':
    page_string = read_file('./research_base.html')

    ###########################################################################
    ###########################################################################

    folder = './projects'
    project_string = ''
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)
    num_project = 0
    for id in ids:
        elems, keys = parse_project_info(id, folder)
        if 'year' not in keys:
            pass
        if int(elems['year']) < (CURRENT_YEAR - 1):
            pass
        project_string += get_project_html_string(id, elems, keys)

        num_project+= 1
        if num_project >= MAX_PROJECTS:
            break

    page_string = page_string.replace('<!-- autogen projects -->', '<!-- autogen projects -->\n' + project_string)

    ###########################################################################
    ###########################################################################

    fpath = './research.html'
    with open(fpath, 'w') as f:
        f.write(page_string)
