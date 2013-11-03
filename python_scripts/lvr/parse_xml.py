#!/usr/bin/env python
# -*- encoding: utf8 -*-
# coding=UTF-8

import json
import sys
import optparse
import xml.etree.cElementTree as ET



from os import listdir
from os.path import isfile, join

__author__ = 'fcamel'

def main(args):
    '''\
    %prog [options]
    '''
    result_list = []
    mypath="/Users/chandler/workspace/YahooHackDay2013/python_scripts/lvr"
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    for filename in onlyfiles:
        if "A_lvr_land_A.XML" not in filename: continue
        #print filename
        result_list.append(get_data_from_file(filename))
    #print result_list
    result = {}
    result["items"] = result_list
    result_2 = json.dumps(result, ensure_ascii=False)
    print result_2
    return 0


def get_data_from_file(filename):
    result_list = []
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    #print root
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
    return result_list


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))

