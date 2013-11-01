# Yahoo Hack Day 2013 Notes

## Sources of open data

 * http://developer.yahoo.com/yql/console/
 * http://data.taipei.gov.tw
 * http://cloud.culture.tw/frontsite/opendata
 * http://dbpedia.org/
 * http://linkedgeodata.org/
 * http://www4.wiwiss.fu-berlin.de/factbook/
 * http://www.freebase.com/
 * http://musicbrainz.org/
 * http://www4.wiwiss.fu-berlin.de/wikicompany/
 * http://www.mpi-inf.mpg.de/yago-naga/yago/
 * http://www.geonames.org/

## How to download Taipei datasets

Mirror the two open data websites to local disk

    mkdir opendata
    cd opendata
    wget -mk http://data.taipei.gov.tw
    wget -mk http://cloud.culture.tw/frontsite/opendata

Unfortunately this only gets a small subset of the data.taipei.gov.tw data because they do not use the [web architecture](http://www.w3.org/DesignIssues/), instead relying on javascript on their site ... so we need other methods to get more data ... do a Google query in order to get a list of JSON resources. First we need to set .wgetrc so we look like a real browser:

    ## Local settings (for a user to set in his $HOME/.wgetrc).
    header = Accept-Language: en-us,en;q=0.5
    header = Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    header = Connection: keep-alive
    user_agent = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36
    #robots = off
    referer=http://data.taipei.gov.tw/

Then query Google:

    wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+json&num=100&complete=0' --output-document download1.txt
    wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+json&num=100&complete=0&start=100' --output-document download2.txt
    wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+csv&num=100&complete=0' --output-document download3.txt
    cat download1.txt download2.txt download3.txt > download.txt

Then get the list of URLs

    grep '"http://data.taipei.gov.tw.*?"' download.txt -o -P | sed 's/"//g' | sort | uniq > download-clean.txt

Then crawl the URLs - these seems to throw a lot of 403 forbidden's like we are being blocked but I haven't found away around that ... but it does manage to get some extra data too ...

    wget -k -r -N -l 1 -nc --no-remove-listing -i download-clean.txt 

Once we have done this then in *cloud.culture.tw* most of the data is stored in `cloud.culture.tw/frontsite/trans` in Excel, XML and JSON format while in *data.taipei.gov.tw* it is in `data.taipei.gov.tw/opendata/apply` either in the `file` directory for CSV or in the `json` directory for JSON. 

## Analyzing datasets

Many of the datasets contain positional information. They seem to be derived from GIS shapefiles. Use grep to identify which files have positional information:

    cd data.taipei.gov.tw/opendata/apply/json
    remove any files smaller than 1KB, useless
    grep "lat" * -l
    cd data.taipei.gov.tw/opendata/apply/query
    grep "lat" * -l

This gives us datasets of:

    (01) NzRBNTc0NDUtMjMxMi00RTk1LTkxMjgtNzgzMzU5MEQzRDc3
    Stores with bring your own cutlery Privileges Taipei location data
    1.6MB

    (02) MDk0RTRDNEUtMkUzNS00Qjc2LUJEQkItRjg0MkRDMEE4NjVC
    Taipei public areas Complimentary wireless Internet hotspot location data
    1.4 MB

    (03) NjgzOTY1RjUtN0UyMy00MTM0LUFEQjEtOTlDNEZCMUVBNTE3
    Taipei leisure city park locations
    54.3 KB

    (04) NjkxREYyRUQtODAwQi00OEY0LUEwOUMtQjdGQTdBNDVENkQz
    Taipei pro Mountain Trail
    24.9 KB

    (05) QTdBNEQ5NkQtQkM3MS00QUI2LUJENTctODI0QTM5MkIwMUZE
    Taipei OK certification - hotel industry
    30.3 kb

    (06) RDU5NkRFQzktREQ0OS00OUE3LUFCRjYtQkYzN0I2NTYyN0JE
    Taipei market location
    83.2 kb

###

Next steps is to make some simple "Hello World" pages that demonstrate different datasets being displayed in YUI.

I had some problems with this .. I can't get the samples to work from the `taipei.gov.tw` server. 

Instead you need to go to datasets/samples then start a web server e.g. 

    python -m SimpleHTTPServer

then open

    http://localhost:8000/index.html

Note it takes some time for the data sets to render ...
    









