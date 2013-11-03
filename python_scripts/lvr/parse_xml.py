#!/usr/bin/env python
# -*- encoding: utf8 -*-
# coding=UTF-8

import sys
import optparse
import xml.etree.cElementTree as ET


__author__ = 'fcamel'


def main(args):
    '''\
    %prog [options]
    '''
    tree = ET.ElementTree(file='H_lvr_land_A.XML')
    root = tree.getroot()
    #print root
    result_list = []
    #print root.tag, root.attrib
    for child_of_root in root:
        #print child_of_root.tag, child_of_root.text
        tmp_dict = {}
        for child_of_child in child_of_root:
            #print child_of_child
            if child_of_child.tag is None:
                continue
            tag = str(child_of_child.tag.encode('utf-8'))
            if child_of_child.text is None:
                continue
            text = str(child_of_child.text.encode('utf-8'))
            tmp_dict[tag] = text
        result_list.append(tmp_dict)
    result = {}
    result["items"] = return_list
    result_2 = json.dumps(result, ensure_ascii=False)
    print result_2.encode('utf-8')
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))

