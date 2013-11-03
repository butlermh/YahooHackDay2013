#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import optparse
import os
import re

__author__ = 'Chandler Huang <previa@gmail.com>'

def convert_tw97_to_wgs(x, y):
    out = {'status':False}
    lat = None
    lon = None
    result = os.popen('echo '+str(x)+' '+str(y)+' | proj -I +proj=tmerc +ellps=GRS80 +lon_0=121 +x_0=250000 +k=0.9999 -f "%.8f"').read().strip()
    process = re.compile( '([0-9]+\.[0-9]+)', re.DOTALL )
    for item in process.findall(result):
        if lon == None:
            lon = float(item)
        elif lat == None:
            lat = float(item)
        else:
            break

    if lat == None or lon == None:
        return out
    out['lat'] = lat
    out['lng'] = lon
    out['status'] = True
    return out

def main(args):
    '''\
    %prog [options]
    '''
    return 0


if __name__ == '__main__':
    parser = optparse.OptionParser(usage=main.__doc__)
    options, args = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))

