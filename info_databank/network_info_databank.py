from pprint import pprint

counter = 0


class Item:
    def __init__(self):
        self.name = input('Input the name of the item:')
        self.category_types = input('Do you know the type example -> ABC | E | DE:')
        self.desc = input('Description:')
        self.det_desc = input('Detailed description | FF (file path):')
        if not self.category_types.isalpha():
            self.category_types = None


def count(reset=False):
    global counter
    if reset:
        counter = 0
        return counter
    counter += 1
    return counter


def is_not_category(_type):
    for c in _type:
        if c.isdigit():
            return True


def create_category(_category_types):
    global counter
    _r_handle = open('data-bank.nid', 'r')
    lines = _r_handle.readlines()
    _type = None
    character = chr(65)
    max_ = 0
    # break up the lines
    for line in lines:

        # get the data item type
        _type = line.split(':')[0]

        if is_not_category(_type):
            continue

        # then count nr of times
        if _category_types:
            for c2 in _type:
                if c2 in _category_types:
                    count()
        if counter > max_:
            max_ = counter

        for c in _type:
            # add new character as category
            if ord(character) <= ord(c):
                character = chr(ord(c) + 1)

        count(reset=True)

    # data item type
    di_type = character if _category_types is None else ''.join([_category_types for _ in range(max_ + 1)])
    _r_handle.close()
    return di_type


def add_category(_name, _category_types: str = None):
    cat_type = create_category(_category_types)
    _append_handle = open('data-bank.nid', 'a')
    _append_handle.write(cat_type + ':' + _name + ';\n')
    _append_handle.close()
    count(reset=True)


def add_item(_itm: Item):
    global counter
    _r_handle = open('data-bank.nid', 'r')
    lines = _r_handle.readlines()
    count(reset=True)
    found_categories = ''
    for line in lines:
        category_type = line.split(':')[0]
        for c in category_type:
            if c in _itm.category_types and c not in found_categories:
                count()
                found_categories += c

    _w_handle = open('data-bank.nid', 'a')
    if found_categories == '':
        # creating new category
        print("Did not find the categories, creating new..")
        found_categories = create_category(_itm.category_types)

    count(reset=True)
    for line in lines:
        item_id = line.split(':')[0]
        for c in item_id:
            if c.isdigit():
                count()
                break

    id_ = counter + 1
    item_id = found_categories + str(id_)
    _w_handle.write(item_id + ':' + f"|name->{_itm.name}, "
                                    f"|desc-> {_itm.desc}, "
                                    f"|det_desc-> {_itm.det_desc};\n")

    _w_handle.close()


def get_items(search_str: str = ""):
    _r_handle = open('data-bank.nid', 'r')
    lines = _r_handle.readlines()
    cat_type_ = ''
    items = []
    for line in lines:
        itm_id_ = line.split(':')[0]
        for c in itm_id_:
            if c.isalpha():
                cat_type_ += c
        is_item = False
        for c in itm_id_:
            if c.isdigit():
                is_item = True

        if is_item:
            name_ = line.split('|name->')[1].split(',')[0]
            desc_ = line.split('|desc->')[1].split(',')[0]
            det_desc_ = line.split('|det_desc->')[1].split(',')[0]
            if search_str in (name_ or desc_ or det_desc_):
                items.append({'id': itm_id_,
                              'type': cat_type_,
                              'name': name_,
                              'description': desc_,
                              'detailed_description': det_desc_})
    return items


def get_category_names(type_: str = '') -> list[str]:
    _r_handle = open("data-bank.nid", 'r')
    lines = _r_handle.readlines()
    name_list = []
    for line in lines:
        id_ = line.split(':')[0]
        name_ = line.split(':')[1].split(';')[0]
        if type_ in id_:
            name_list.append(name_)

    return name_list


def display(items: bool = True, search_str: str = ""):
    if items:
        ls(get_items(search_str), 'Items:')


def ls(list_: [], title: str):
    from rich.console import Console
    console = Console()
    console.clear()
    pprint('\t' + title)
    for i in list_:
        pprint(i, indent=2)


if __name__ == '__main__':
    inp = input('Run cmd (ls cmd to list commands):')
    if inp == '':
        exit(0)
    if 'add' in inp:
        if 'cat' in inp:
            name = input('Input the name of the category:')
            category_types = input('Do you know the type example -> AAA | B | FF:')
            if not category_types.isalpha():
                category_types = None
            add_category(name, category_types)
        if 'itm' in inp:
            itm = Item()
            if not itm.category_types.isalpha():
                category_types = None
            add_item(itm)
    if 'get' in inp:
        # get category name
        if 'cat' and 'name' in inp:
            category_types = input('Do you know the type example -> A | B | FF:')
            ls(get_category_names(category_types), title="Categories:")
        # get category type
    if 'ls' and 'items' in inp:
        search_str = input('Search string:')
        display(items=True, search_str=search_str)



