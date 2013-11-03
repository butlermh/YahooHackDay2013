---
layout: post
title: Mapping to a standard schema I
description: "Mapping data to a standard schema: Part one"
modified: 2013-11-02
category: articles
comments: true
author: mark
---

One common task when working with open data is [data integration](http://en.wikipedia.org/wiki/Data_integration). One problem that data integration has to address is [schema mapping](http://en.wikipedia.org/wiki/Schema_Matching) i.e. mapping to different datasets into a common schema. For example several datasets provided by `data.taipei.gov.tw` supply locational information but they use a variety of different properties to represent location, for example `latitude` has different names in different datasets:

{% highlight bash %}
 latitude   
 lat   
 GTag_latitude   
 y   
{% endhighlight %} 

There are several ways of dealing with this problem but here we would like to demonstrate how YUI's [DataSourceJSONSchema](http://yuilibrary.com/yui/docs/api/classes/DataSourceJSONSchema.html) can help with this problem. Here we use `key` and `locator` in order to map the schema.

{% highlight html %}
src.plug(Y.Plugin.DataSourceJSONSchema, {  
   schema: {  
   resultListLocator: "",  
   resultFields: [  
     {key: "name"},   
     {key: "certification_category"},   
     {key: "tel"},   
     {key: "traffic_info"},   
     {key: "display_addr"},  
     {key: "poi_addr"},  
     {key: "longitude", locator:"X"},   
     {key: "latitude", locator:"Y"}  
   ]  
   }  
 });
{% endhighlight %}  

See this [complete example](http://yahoo.clouduct.com:8000/examples/example01.html) for the [Taipei Hotel Certification dataset](http://data.taipei.gov.tw/opendata/apply/NewDataContent?oid=A7A4D96D-BC71-4AB6-BD57-824A392B01FD).
