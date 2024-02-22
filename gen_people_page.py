import os
import glob
import random

CURRENT_YEAR = 2024

def read_file(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    return content

def get_txtfile_ids(folder):
    txtfiles = glob.glob('{}/*.txt'.format(folder))
    ids = [os.path.basename(txtfile)[:-4] for txtfile in txtfiles]
    return ids

# <img class="paper static" title="paper" src="src.png" />
def parse_person_info(person_id, person_folder):
    elems = {}
    keys = []
    fpath = os.path.join(person_folder, person_id + '.txt')

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
        elems['img'] = 'assets/incognito.jpeg'

    return elems, keys


def get_person_html_string(id, elems, keys):
    comment_str = '<!--------------------------------------------------------------------------->'
    person_str = ''
    person_str += '\n' + comment_str + '\n'
    person_str += '<table class="personTable" id="{}">\n'.format(id)
    person_str += '<tr>\n<td>\n'
    person_str += '<a href="{}">\n <div class="imButtonWrapper"> \n <img alt="{}" src="{}" />\n</div>\n</a>\n'.format(elems['url'], elems['name'], elems['img'])
    person_str += '</td>\n</tr>\n<tr>\n<td>\n'
    person_str += '<a href="{}">{}</a>\n'.format(elems['url'], elems['name'])
    person_str += '</td>\n</tr>\n</table>\n'

    ## Meta fields
    # add some javascript here if needed using the  id for the added element

    person_str += comment_str + '\n'
    return person_str


if __name__ == '__main__':
    page_string = read_file('./people_base.html')

    ###########################################################################
    ###########################################################################

    folder = './people/faculty'
    people_string = ''
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)
    for id in ids:
        elems, keys = parse_person_info(id, folder)
        people_string += get_person_html_string(id, elems, keys)
    page_string = page_string.replace('<!-- autogen faculty -->', '<!-- autogen faculty -->\n' + people_string)

    ###########################################################################
    ###########################################################################

    folder = './people/postdocs'
    people_string = ''
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)
    for id in ids:
        elems, keys = parse_person_info(id, folder)
        if 'year' not in keys:
            continue
        if (int(elems['year']) < (CURRENT_YEAR - 2)):
            continue
        people_string += get_person_html_string(id, elems, keys)
    page_string = page_string.replace('<!-- autogen postdocs -->', '<!-- autogen postdocs -->\n' + people_string)

    ###########################################################################
    ###########################################################################

    folder = './people/students'
    people_string = ''
    ids = get_txtfile_ids(folder)
    random.shuffle(ids)
    for id in ids:
        elems, keys = parse_person_info(id, folder)
        if 'year' not in keys:
            continue
        if 'program' not in keys:
            continue
        if 'MS' not in elems['program'] and 'PhD' not in elems['program']:
            continue
        if 'MS' in elems['program'] and (int(elems['year']) < (CURRENT_YEAR - 2)):
            continue
        if 'PhD' in elems['program'] and (int(elems['year']) < (CURRENT_YEAR - 7)):
            continue

        people_string += get_person_html_string(id, elems, keys)
    page_string = page_string.replace('<!-- autogen students -->', '<!-- autogen students -->\n' + people_string)

    ###########################################################################
    ###########################################################################

    fpath = './index.html'
    with open(fpath, 'w') as f:
        f.write(page_string)
