Title: Mozilla Dev Derby July
Date: 2012-07-29 16:30:00 -0400
Category: CSS
Tags: CSS3, Sass, Dev Derby

I've spent some time this weekend working on an entry for <a href="https://developer.mozilla.org/en-US/demos/devderby">Mozilla's Dev Derby</a>. You can find my entry <a href="https://developer.mozilla.org/en-US/demos/detail/antique-clock">hosted on the competition site</a>. This is my first entry so please, go ahead and vote for it.

I also noted today before I submitted my entry that I'm not the only one who <a href="https://developer.mozilla.org/en-US/demos/detail/counter-clock">thought to make a clock</a>. It's interesting to see our our visuals, animations, and implementations differ.

####How I Did It

I've this entry available as a <a href="https://github.com/rhysyngsun/devderby-07-2012">GitHub repo</a> so you can browse the source yourself.

I wanted this to be a relatively quick weekend project and fun to do. A requirement of the competition is for it to work across various browsers, so I started with <a href="http://sass-lang.com/">Sass</a> and <a href="http://compass-style.org/">Compass</a> to deal with generating a lot of the yuck that comes with browser specific code (particularly vendor-prefixed CSS). Sass was also very useful in generating the animations. Just compare the <a href="https://github.com/rhysyngsun/devderby-07-2012/blob/master/sass/a55 linesnimations.scss">Sass source</a> (55 lines) and the <a href="https://github.com/rhysyngsun/devderby-07-2012/blob/master/css/animations.css">generated CSS</a> (1914 lines) to get an idea of how painful and impossible this would have been to do in a weekend.

![CSS3 Roman Numerals]({filename}/images/07-2012/numerals.png)

Getting the hands of the clock was relatively straightforward. The difficult part was in positioning the Roman numerals. In order for those numerals to fit correctly in the ring around the edge, they had to be rotated individually around the center of the clock face. Additionally the overall set of numerals for a given hour had to be approximately centered on the radius line for that hour. The combination of those two pretty much ruled out positioning individual characters as a sane strategy.

Instead, I opted for grouping the numerals (wrapping in `<span>` tags) in a parent `<div>` and rotating that `<div>` around the center. I then individually tweaked the characters by rotating them around the same point in smaller increments. I also created guides to help me align the numerals on the radius lines. You can see it commented out <a href="https://github.com/rhysyngsun/devderby-07-2012/blob/master/sass/styles.scss#L39">on line 39 here</a>.

All in all it took me about 8-10 hours over the weekend to create this. Most of that time was spent playing with css tranforms.

I'll definitely putting in an entry for August as that contest is <a href="http://vsnap.com">near and dear to my heart</a>. `</shameless-plug>`
