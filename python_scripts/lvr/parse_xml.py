#!/usr/bin/env python
# -*- encoding: utf8 -*-

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
    print root
    print root.tag, root.attrib
    for child_of_root in root:
        print child_of_root.tag, child_of_root.text
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))

