#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from utils import convert_tw97_to_wgs
from optparse import OptionParser

__author__ = 'Chandler Huang <previa@gmail.com>'

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

    with open( options.filename ,"r") as myfile:
        data = myfile.read()
    data_dict = json.loads(data)
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
        else:
            lat, log = my_dict[options.latitude] , my_dict[options.longitude]
        lat, log = check_lat_lng(lat, log)
        new_latlng = lat + "," + log
        tmp_dict["latlng"] = new_latlng
        tmp_dict["type"] = options.data_type
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
