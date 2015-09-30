---
layout: post
title:  "The Lifecycle of a Youtube Video: Phases, Content and Popularity"
date:   2014-10-03 20:03:02
tags:
 - YouTube video
 - popularity prediction
 - cross domain analysis
custom_js:
 - https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js
 - https://cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.min.js
 - /assets/js/plotSegFitResult.js 
custom_css:
 - https://cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.css
 - /assets/css/chart.css
comments: true
---
> <div class="scfont">Excerpt:</div> Use time series segmentation method to explore YouTube viewcount phases and improve prediction
> 
> <a href="{{ page.url }}"> <img class="excerptimage" src="{{ site.url }}/assets/img/complexityofviewcount.png" /> <a>

<!--more-->

by <a href="yuhonglin.github.io">Honglin Yu</a>, <a href="http://users.cecs.anu.edu.au/~xlx/">Lexing Xie</a> and <a href="http://users.cecs.anu.edu.au/~ssanner/">Scott Sanner</a>


<h3> Highlights </h3>
<ul>
    <li> Implemented an efficient time series segmentation algorithm <a href="https://github.com/yuhonglin/segfit">segfit</a> </li>
    <li> Crawled millions of YouTube viewcount history (based on <a href="https://github.com/yuhonglin/YTCrawl">YTCrawl</a>) </li>
	<li> Data used in paper can be found <a href="https://www.dropbox.com/s/4af3646w8omhago/data_released.tar.bz2?dl=0">here</a></li>
    <li> Many social insights </li>
	<li> Ground truth labelling <a href="http://cantabile.anu.edu.au/segfit/label/">website (occasionally down).</a>  </li>
</ul>

<h3> Examples of viewcount phases</h3>

<ul>
    <li> <span style="background-color: #3399FF; color: white">Blue curve</span> : daily viewcount of each video. </li>
    <li> <span style="background-color: #8B0000; color: white">Red curves</span> : phases (segments) found by <a href="https://github.com/yuhonglin/segfit">segfit</a>. </li>
</ul>

<div class="container">
	<div class="col-md-6 chartdiv" id='chart1'><a id='title1'>1</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart2'><a id='title2'>2</a><svg class="chart"></svg></div>
	<div class="clearfix visible-block"></div>
		
	<div class="col-md-6 chartdiv" id='chart3'><a id='title3'>3</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart4'><a id='title4'>4</a><svg class="chart"></svg></div>

	<div class="clearfix visible-md"></div>

	<div class="col-md-6 chartdiv" id='chart5'><a id='title5'>5</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart6'><a id='title6'>6</a><svg class="chart"></svg></div>

    <div class="clearfix visible-md"></div> 

	<div class="col-md-6 chartdiv" id='chart7'><a id='title7'>7</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart8'><a id='title8'>8</a><svg class="chart"></svg></div>

	<div class="clearfix visible-md"></div> 

	<div class="col-md-6 chartdiv" id='chart9'><a id='title9'>9</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart10'><a id='title10'>10</a><svg class="chart"></svg></div>

	<div class="clearfix visible-md"></div> 

	<div class="col-md-6 chartdiv" id='chart11'><a id='title11'>11</a><svg class="chart"></svg></div>
	<div class="col-md-6 chartdiv" id='chart12'><a id='title12'>12</a><svg class="chart"></svg></div>
</div>
