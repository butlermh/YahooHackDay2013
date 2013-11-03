#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
from optparse import OptionParser


def convert_tw97_to_wgs(x, y):
    out = {'status':False}
    lat = None
    lon = None
    result = os.popen('echo '+str(x)+' '+str(y)+' | proj -I +proj=tmerc +ellps=GRS80 +lon_0=121 +x_0=250000 +k=0.9999 -f "%.8f"').read().strip() # lat, lng 格式, 不必再轉換
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

def check_lat_lng(lat, lng):
    if float(lat) > float(lng):
        return lng, lat
    return lat, lng
def main():
    return_list = []
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)

    parser.add_option("-f", "--file", dest="filename",
                      help="read data from FILENAME")
    parser.add_option("-o", "--longitude",
                      dest="longitude")
    parser.add_option("-a", "--latitude",
                      dest="latitude")
    parser.add_option("-t", "--type",
                      dest="data_type")
    parser.add_option("-l", "--label",
                      dest="data_label")
    parser.add_option("-c", "--convert", action="store_true",
                      default=False, dest="convert")
    (options, args) = parser.parse_args()
    """
    if options.filename:
        print "reading %s..." % options.filename

    print options.latitude
    print options.longitude
    print options.data_type
    """
    with open( options.filename ,"r") as myfile:
        data = myfile.read()
    data_dict = json.loads(data)
    #print len(data_dict)
    #print data_dict
    filter_same_latlng = {}
    for my_dict in data_dict:
        tmp_dict = {}
        for k in my_dict:
            if(k==options.latitude):
               continue
            if(k==options.longitude):
               continue
            if(k=="id"):
               continue
            tmp_dict[k] = my_dict[k]

        if options.convert:
            new_latlng_dict = convert_tw97_to_wgs(my_dict[options.latitude], my_dict[options.longitude])
            lat, log = str(new_latlng_dict['lat']) , str(new_latlng_dict['lng'])
            #print new_latlng_dict
            #print new_latlng
        else:
            lat, log = my_dict[options.latitude] , my_dict[options.longitude]
        lat, log = check_lat_lng(lat, log)
        new_latlng = lat + "," + log
        tmp_dict["latlng"] = new_latlng
        tmp_dict["type"] = options.data_type
        #tmp_dict["label"] = options.data_label
        #print tmp_dict
        if new_latlng in filter_same_latlng:
            pass
        else:
            filter_same_latlng[new_latlng] = 1
            return_list.append(tmp_dict)
    result = {}
    result["items"] = return_list
    result_2 = json.dumps(result, ensure_ascii=False)
    print result_2.encode('utf-8')

if __name__ == "__main__":
    main()
