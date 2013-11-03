---
layout: post
title: Things we could not get to work
description: "Things we could not get to work"
modified: 2013-11-02
category: articles
comments: true
author: mark
---

We also tried a number of techniques that we were not able to get to work in the time available. We would have liked to use [YQL](http://developer.yahoo.com/yql) to query the data catalogues of [data.taipei.gov.tw](http://data.taipei.gov.tw) and [data.gov.tw](http://data.gov.tw) but we did not full sets of results in either case - we did not find the reason for this, perhaps some timeout problem.

We also explored using a [utility for converting JSON to CSV](https://github.com/zeMirco/json2csv) written using [node.js](http://nodejs.org/). After some fiddling with the [node package manager](https://npmjs.org/), we discovered that it was necessary to specify all the attributes you wanted converted. This is potentially quite time consuming so in the end we decided to write a simple Python script. It was fun trying node though. 
