# Yahoo Hack Day 2013 Notes

## How to download datasets

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






