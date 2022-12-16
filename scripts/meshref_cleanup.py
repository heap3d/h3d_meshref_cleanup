#!/usr/bin/python
# ================================
# (C)2022 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# cleanup meshref scene file0

import lx
import modo
import modo.constants as c
import sys

sys.path.append(
    "{}\\scripts".format(lx.eval("query platformservice alias ? {kit_h3d_utilites:}"))
)
import h3d_utils as h3du
from h3d_debug import H3dDebug


def get_parents_hierarchy(item):
    if not item:
        return []
    if not item.parent:
        return []
    return [item.parent].extend(get_parents_hierarchy(item.parent))


def get_filtered_items(items, filtered_types):
    filtered_items = set()
    for item in items:
        try:
            itype = h3du.itype_int(item.type)
        except LookupError:
            continue
        if itype not in filtered_types:
            continue
        # add item which type is in filtered_types
        filtered_items.add(item)

    return filtered_items


def get_items_to_delete():
    return []


def delete_items(items):
    h3dd.print_items(items)


def main():
    # TODO add polygon part tags cleaning
    # TODO left base material in a scene
    # TODO remove everything except filtered types list
    
    # TODO create list of items to delete

    filtered_types = [
        c.MESH_TYPE,
        c.MORPHDEFORM_TYPE,
        c.GROUPLOCATOR_TYPE,
        c.LOCATOR_TYPE,
    ]
    scene_items = modo.scene.current().items()


if __name__ == "__main__":
    h3dd = H3dDebug()
    main()
