---
layout: post
title: Getting Data
description: "Getting Data"
modified: 2013-11-02
category: articles
comments: true
author: mark
---

Sites like [Dbpedia](http://www.dbpedia.org/) let you [download their datasets](http://wiki.dbpedia.org/Downloads39) so you can host them locally. This is great because it lets you perform experiments with the data without overloading their server. However what do you do when a site provides many datasets but no easy way to download them all?
One approach is to mirror websites locally using wget: 

{% highlight bash %}
wget -mk http://data.taipei.gov.tw  
wget -mk http://cloud.culture.tw/frontsite/opendata
{% endhighlight %}  

Here we use the m mirror option to mirror the site and the k rewrite option to modify the URLs so we can browse the site locally. However unfortunately the [data.taipei.go.tw](http://data.taipei.go.tw) site [does not give URLs for the search results](http://www.w3.org/DesignIssues/Axioms.html) meaning we only get a small subset of the available datasets. Is there any way around this? One approach is to query Google to get a list of datasets. However to do this we first need to configure wget so it looks like a real browser by creating a `.wgetrc` file: 

{% highlight bash %}
## Local settings (for a user to set in his $HOME/.wgetrc).  
header = Accept-Language: en-us,en;q=0.5  
header = Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
header = Connection: keep-alive  
user_agent = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) 
    Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36  
#robots = off  
referer=http://data.taipei.gov.tw/
{% endhighlight %}  

Now we can query Google programmatically to get a list of datasets at `data.taipei.gov.tw`: 

{% highlight bash %}
wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+json&amp;num=100&amp;complete=0' --output-document download1.txt  
wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+json&amp;num=100&amp;complete=0&amp;start=100' --output-document download2.txt  
wget 'http://www.google.com/search?q=site:data.taipei.gov.tw+csv&amp;num=100&amp;complete=0' --output-document download3.txt  
cat download1.txt download2.txt download3.txt > download.txt
{% endhighlight %}   

Next we do use some [quick and dirty regular expressions](http://www.codinghorror.com/blog/2009/11/parsing-html-the-cthulhu-way.html) in order to get a list of dataset URLs from the Google result pages we downloaded: 

{% highlight bash %}
grep '"http://data.taipei.gov.tw.*?"' download.txt -o -P | sed 's/"//g' | sort | uniq > download-clean.txt  
{% endhighlight %}

Now we can use wget to retrieve the dataset URLs: 

{% highlight bash %}
wget -k -r -N -l 1 -nc --no-remove-listing -i download-clean.txt   
{% endhighlight %}

Note we use nc no clobber to avoid downloading resources twice and set the `l` recursion parameter to 1 so we just get the linked dataset. Once we have done this then the Excel, [XML](http://en.wikipedia.org/wiki/XML) and [JSON](http://en.wikipedia.org/wiki/JSON) data from `cloud.culture.tw`  is stored in
 
    cloud.culture.tw/frontsite/trans

The data from `data.taipei.gov.tw` is stored in

    data.taipei.gov.tw/opendata/apply 

Here the file directory contains [CSV](http://en.wikipedia.org/wiki/Comma-separated_values) or [shapefile](http://en.wikipedia.org/wiki/Shapefile) data in zip format while the `json` and `query` directories contain JSON data.

