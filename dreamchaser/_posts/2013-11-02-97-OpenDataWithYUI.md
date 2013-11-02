---
layout: post
title: Displaying open data
description: "Displaying open data"
modified: 2013-11-02
category: articles
comments: true
author: mark
---

It is really helpful to be able to explore open data to find out what you can use it for. YUI has an extensive library of Javascript controls that can be used for tasks like this. YUI uses [DataSource](http://yuilibrary.com/yui/docs/datasource/) to retrieve data. It comes in four flavors: 

* [DataSource.Local](http://yuilibrary.com/yui/docs/datasource/datasource-local.html) 
* [DataSource.Get](http://yuilibrary.com/yui/docs/datasource/datasource-get.html)
* [DataSource.IO](http://yuilibrary.com/yui/docs/datasource/datasource-io.html)
* [DataSource.Function](http://yuilibrary.com/yui/docs/datasource/datasource-function.html).

Here we are interested in `DataSource.Get` and `DataSource.IO` as they let you work with remote resources. One difficulty with retrieving open data sets is browsers prohibit requesting data from a server in a different domain, due to same origin policy. `DataSource.Get` overcomes this by using [JSONP (JSON with padding)](http://en.wikipedia.org/wiki/JSONP) which wraps the JSON request so it looks like a Javascript script. However this means that the end point needs to support JSONP, unlike `DataSource.IO` which [will work with standard JSON endpoints](http://yuilibrary.com/yui/docs/datasource/datasource-io.html).

So what do we do if we need to [query an open data endpoint that does not support JSONP](http://stackoverflow.com/questions/2131740/online-jsonp-converter-wrapper)? One approach is to use a service like [Json2JsonP](http://json2jsonp.com/) that can wrap standard JSON endpoints and turn them into JSONP ones. There are some security risks with this - the service could potentially perform [Javascript injection](http://deadliestwebattacks.com/2013/01/22/know-your-javascript-injections/) - but for now we will trust this one.

Here is a webpage that allows you to browse the dataset listing [restaurants in Taipei that give discounts if you bring your own cutlery](http://data.taipei.gov.tw/opendata/apply/NewDataContent;jsessionid=C1BACB4D704764015BFC9B5EF899B2D0?oid=74A57445-2312-4E95-9128-7833590D3D77). You can see [the example running here](http://yahoo.clouduct.com:8000/examples/example01.html) although there is a short delay while the data is retrieved.

{% highlight html %}
<!DOCTYPE html>  
<meta http-equiv="content-type" content="text/html; charset=utf-8">  
<title>臺北市自備餐具享優惠</title>  
<body class="yui3-skin-sam">  
<h1>臺北市自備餐具享優惠</h1>  
<div id="datatable"></div>  
<script src="http://yui.yahooapis.com/3.13.0/build/yui/yui-min.js"></script>  
<script>  
YUI().use('datatable', 'datasource-get', 'datasource-io', 'datasource-jsonschema', 'datatable-paginator', function (Y) {  
 var src = new Y.DataSource.Get({  
   source: 'http://json2jsonp.com/'  
 });  
 src.plug(Y.Plugin.DataSourceJSONSchema, {  
   schema: {  
   resultListLocator: ""  
   }  
 });  
 var table = new Y.DataTable({ columns: [  
     "name",   
     "district",   
     "operationCategory",   
     "operationType",   
     "telephone",   
     "openingHours",   
     "address",   
     "discountPeriod",   
     "discountCategory",   
     "discountCondition",   
     "discountContent",   
     "longitude",   
     "latitude"  
 ],  
 rowsPerPage: 10,  
 paginatorLocation: ['header', 'footer']   
 });  
 table.plug(Y.Plugin.DataTableDataSource, { datasource: src });  
 table.render('#datatable');  
 table.datasource.load({request: 
'?url=http://data.taipei.gov.tw/opendata/apply/json/NzRBNTc0NDUtMjMxMi00RTk1LTkxMjgtNzgzMzU5MEQzRDc3'});  
});  
</script>  
</body> 
{% endhighlight %}
