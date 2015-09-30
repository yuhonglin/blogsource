---
layout: post
title:  "Visual Meme Sequence Analysis on YouTube (Video Remix Analysis)"
date:   2012-08-30 19:10:15
tags:
 - Video shot detection
 - Frequent item set mining	 
 - openCV 
 - libavcodec
 - Smith-Waterman algorithm
comments: true
---
> <div class="scfont">Excerpt:</div> Mining visual meme sequences from large number of videos
>
> <a href="{{ page.url }}"> <img src="{{ site.url }}/assets/img/flow.png"> </a>

<!--more-->

by <a ref="yuhonglin.github.io">Honglin Yu</a> and <a ref="http://users.cecs.anu.edu.au/~xlx/">Lexing Xie</a>

<h3> Motivation </h3>
Many YouTube videos are ```remix videos``` which consist of ```shots``` copied from other videos. Former work built system trying to find out duplicate shots in large number of videos. This work aims to further take the association rules and orders of shots into consideration. The motivation of this work are,
<ul>
    <li> "Order" of shots is crucially important for video making (see <a href="http://en.wikipedia.org/wiki/Montage_%28filmmaking%29">Montage</a>, <a href="http://en.wikipedia.org/wiki/Kuleshov_Effect">Kuleshov Effect</a>) </li>
    <li> Enable viral content analysis at shot sequence level  </li>
    <li> Try to understand human video editing preference, w.r.t. different topics </li>
</ul>

<h3> System Overview </h3>
We have built the following system to find visual meme sequences.
<p><figure>
    <img src="{{ site.url }}/assets/img/flow.png">
    <figcaption>Fig.1 Working flow of the system</figcaption>
</figure></p>


<h3> Result </h3>
<a href="{{ site.url }}/assets/img/iranianelection.png">Here</a> is an example of the mining results (22.5MB). Every row is the shots for each video in chronological order.
And the black lines connect the visual memes we found. (These videos are about <a href="http://en.wikipedia.org/wiki/2009%E2%80%9310_Iranian_election_protests">2009 Iranian election protests</a>)


<h3> Software Developed </h3>
<ul>
    <li>
	<a href="https://github.com/yuhonglin/shotdetect">ShotDetect</a>: detect shots of videos
	<ul>
	    <li> It is fast, deveploped by C++ and is directly based on libavcodec and openCV etc. </li>
	    <li> It can deal with all formats of online videos (thanks to libavcodec etc.) </li>
	    <li> The performace is quite good (F1 score > 80% from a test on 400 shots) </li>
	</ul>
    </li>
    <li>
	<a href="https://github.com/yuhonglin/PySW">PySW</a>: implement Smith-Waterman Algorithms for sub-sequence matching (written in C++, wrapped in python)
    </li>
    <li>
	Various powerful parallel crawling and preprocessing programs
	<ul>
	    <li> Deployed on <a href="http://nci.org.au/"> The National Computational Infrastructure </a> </li>
	    <li> Processed > 15TB data </li>
	</ul>	
    </li>    
</ul>

<h3> Poster </h3>
Download from <a href="http://cecs.anu.edu.au/files/posters/2012/u4975468.pdf">here</a> (12.2MB).
