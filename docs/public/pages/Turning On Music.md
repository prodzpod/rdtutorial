Music is one of the most important part in RD. it's a rhythm game after all.
![Screenshot](/rdtutorial/public/images/basics/basics_8.jpg)  
let's click the **Sound Tab** to put some sounds in.

![Screenshot](/rdtutorial/public/images/basics/basics_9.jpg)  
cool! we have a whole new tab. let's try clicking at the start of the level.

![Screenshot](/rdtutorial/public/images/basics/basics_10.jpg)  
choose "Play Song", that's what we want.

![Screenshot](/rdtutorial/public/images/basics/basics_11.jpg)  
After that, you'll get some things... but ignore those for now, and click the folder icon.  
Remember that you need an **.ogg** file. the game will technically accept other formats... but they're either huge in file size or has inconsistent timing- which is *very bad for rhythm games*.  
Here's [mp3 to ogg](https://flicflac-audio-converter.en.softonic.com/) converter if you need one.

...wait, you don't have your music at hand? that's fine! we can download it off youtube, soundcloud, spotify and all that.

[youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html) allows you to directly download to ogg and also download from multiple platforms, but in conjunction with the converter, i found [This](https://4k-video-downloader.en.softonic.com/download) pretty fast too. use what you feel like it, as long as the result is an **.ogg** file.

![Screenshot](/rdtutorial/public/images/basics/basics_12.jpg)  
Okay! we have our music. now, let's calculate the bpm... click there, and hit your space bar to the beat.

![Screenshot](/rdtutorial/public/images/basics/basics_13.jpg)  
I got 132 BPM! but unless you're super precise, this number will be wrong. let's use the **scroll bar**...

![Screenshot](/rdtutorial/public/images/basics/basics_14.jpg)  
Adjust your bpm by 1 until it sorta match up. be aware that some songs have **decimal BPM**, and... for those edge cases, scroll down.

![Screenshot](/rdtutorial/public/images/basics/basics_15.jpg)  
Now, most of the time, the sound won't perfectly match. we also need to set the **offset**! let's go back to the *rows* tab.

![Screenshot](/rdtutorial/public/images/basics/basics_16.jpg)  
Yup, a bit off. even if it doesn't look off, try playing it and see if the beats line up. you should be able to only hear 1 sound, rather than 2 consecutive sounds- if you know what I mean.

![Screenshot](/rdtutorial/public/images/basics/basics_17.jpg)  
So, how do you change the offset? go back to the *sounds* tab, and click on the *play song* event you placed down. click on the *spanner icon*.

![Screenshot](/rdtutorial/public/images/basics/basics_18.jpg)  
There! there's the offset. go back to your bar far ahead, and mess it with my 50ms or so until it fits the best.

![Screenshot](/rdtutorial/public/images/basics/basics_19.jpg)  
There! now it works.

## Still Having Trouble...?

There are some songs that are... a bit weird. weird BPM, weird offset... in that case, we need to go deeper.

![Screenshot](/rdtutorial/public/images/basics/basics_20.jpg)  
You can use a DAW or something, but we'll be using [Audacity](https://www.audacityteam.org/download/) for this tutorial. since it's free and all.

Let's zoom in to the beginning of the song. use the scroll wheel or zoom in button.

![Screenshot](/rdtutorial/public/images/basics/basics_21.jpg)  
There's the silence! drag your mouse from the beginning of the song to the end of this silence.

![Screenshot](/rdtutorial/public/images/basics/basics_22.jpg)  
press delete, then File > Export. remember to make it an **.ogg** file!

and you should be good! set the offset to 0ms, then try to figure out what the BPM is.

![Screenshot](/rdtutorial/public/images/basics/basics_23.jpg)  
<span style="color:#808080">good level btw ![RDZip: ](/rdtutorial/public/images/icon/auburn.png)<button class="rdzip" data-clipboard-text="https://cdn.discordapp.com/attachments/611380148431749151/839276814501019648/nelward_-_Ghost.rdzip">go play it</button></span>
of course, there are exceptions to this as well. when the song is performed live, there could be slight BPM drifts mid song, the song could accelerate, decellerate... yeah. In that case, ask for help on the discord server. people may be able to help you?

## We're done with the basics!

Woo! Finally. Let's go and make some charts now.