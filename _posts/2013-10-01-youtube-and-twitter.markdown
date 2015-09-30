---
layout: post
title:  "Predict YouTube Video Popularity with Twitter's Feed"
date:   2013-10-01 20:03:02
tags:
 - YouTube video
 - popularity prediction
 - cross domain analysis
comments: true
---
> <div class="scfont">Excerpt:</div> We predict viewcount *jumps* and *early* viewcounts of YouTube videos, which are mission impossible for former methods (without external information).
> <a href="{{ page.url }}"> <img class="excerptimage" src="{{ site.url }}/assets/img/twitter2youtube_lx.png" /> </a>

<!--more-->

by <a ref="yuhonglin.github.io">Honglin Yu</a>, <a ref="http://users.cecs.anu.edu.au/~xlx/">Lexing Xie</a> and <a href="http://users.cecs.anu.edu.au/~ssanner/">Scott Sanner</a>

<h3> Motivation </h3>
<ul>
    <li> Online social networks are far not isolated islands. Understanding their interaction has both commercial and research values.</li>
    <li> With the help of external information, we can better predict YouTube video popularity. </li>
    <li> Treating viewcount changes as a measure, we can understand what kinds of tweeting patterns truely indicate the popularity of things mentioned in tweets.</li>
</ul>

<figure class="centeredImage">
    <img src="{{ site.url }}/assets/img/twitter2youtube.png">
    <figcaption>Fig.1 Example of five tweets mentioning one YouTube video and the two questions we try to answer.</figcaption>
</figure>


<h3> Problem Setup </h3>
We proposed two prediction problems which are mission impossible without external information:
<ul>
    <li> Predict videos' viewcount right after uploading (<div class="scfont"> Early </div>) </li>
    <li> Predict whether videos' viewcount suddenly increase (<div class="scfont"> Jump </div>) </li>
</ul>

<h3> Result Highlights (<a href="http://cantabile.anu.edu.au/yt/demo/">Demo</a>) </h3>

Here are two examples of showing clear correlation between tweets pulses and viewcount increases. For more details about our results (i.e. performances of each features), please look at our <a href="{{ site.url }}/assets/posters/mm14_poster.pdf">poster</a> or <a href="http://users.cecs.anu.edu.au/~xlx/papers/acmmm14.pdf">paper</a>.

<div class="centeredimage">
        <img class="horizon-align-2" src="{{ site.url }}/assets/img/yt_example_jump.png" />
        <img class="horizon-align-2" src="{{ site.url }}/assets/img/yt_example_early.png" />
	<figcaption>Fig.2 Left: A video having less than 9000 views in its first 3 months, and then gaining 1.2 million views within 15 days. Right: A video with a few dozen Twitter mentions and nearly 200,000 views in its first 15 days.</figcaption>
</div>


<h3> Twitter Features Highlights </h3>
<ul>
    <li> User graph features: degree, pagerank and hub/authority scores computed from a Twitter user graph of  41.7 million nodes and 1.47 billion edges. </li>
    <li> User behavior features: the frequencies of their usage and engagement of hashtag, retweeting etc. extracted from 476 million tweets. </li>
</ul>

<p><figure class="centeredImage">
    <img src="{{ site.url }}/assets/img/flow_yt.png" id="flow-yt">
    <figcaption>Fig.3 Working flow of the system.</figcaption>
</figure></p>

<h3> Software Highlights </h3>
<ul>
    <li> <a href="https://github.com/yuhonglin/YTCrawl">YTcrawl</a> : a powerful YouTube viewcount history crawler. </li>
    <li> Programs (in C++) to efficiently compute centrality scores (mainstream tools like NetworkX or iGraph do not work due to the huge size of the graph). </li>
    <li> Various programs/scripts to efficiently do feature engineering. </li>
</ul>

<h3> Conclusions </h3>
<ul>
    <li> Our work confirms that Twitter information can be effectively used to predict video popularity on YouTube. </li>
    <li> Twitter user features associated with tweeting activities are more informative than graph features. Having a diverse range of users and associated tweeting activities is
more informative than the total or average volume of activity of these users.</li>
</ul>

<h3> Posters </h3>
For more details, please see the <a href="{{ site.url }}/assets/posters/mm14_poster.pdf">poster</a>.
