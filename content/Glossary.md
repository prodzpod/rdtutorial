Let's talk about the common terms used for Rhythm Doctor Levelmaking, and terms that will be used without explanation in this tutorial series. Terms you might hear in #rd-editor or #microscope in #[RDL] are also included.

Whenever you're confused about a word, refer to this page.  
use **CTRL-F** to search for a specific term you're looking for.

## Meta
**Rhythm Doctor** (**RD**)  
Game you're playing.

**Rhythm Doctor Lounge** (**RDL**)  
Official discord server for RD.

**A Dance of Fire and Ice** (**ADOFAI**)  
Another game from the same company. if people compare your level to this, it means the gameplay feels spammy.

**Level**  
Your custom... well, level. It's called "level" in this game, but people will understand you if you say "map" or "customs" as well.

**Chart**  
Can be interchangable with #[Level], but mostly refer to #[Gameplay] exclusively.

**Difficulty Curve**  
Increase or decrease in difficulty over the course of the level. refer to [[Difficulty Curve]].

**Sightread**  
Playing the level first time, without knowing the music. **Sightread Friendly** means it feels fair for first time players, and generally seen as good level design.

**Blind Friendly**  
Playing the level without seeing. #[RD] is an audio game- therefore its generally good for a level to be unambiguous even without any #[Visual] #[Cue]s.

**.rdzip**  
RDZips are the file extension your level should be in. sometimes it's used to describe levels.

**Showcase** / **Workshop**  
#[RD]'s most custom levels are not in the Steam Workshop, instead, it is stored in the **#rd-showcase** channel within #[RDL], and can be accessed outside the discord server by [Auburnsummer's Website](https://auburnsummer.github.io/rdlevels/).

## General
**BPM**  
**Beats Per Minute**. how fast a song is. tempo.

**Offset**  
Actual starting position of the song, *ms* stands for Millisecond (0.001 second).

**Sync**  
Short for syncronization. if the #[BPM] and #[Offset] you set is appropriate, the music and gameplay should be in sync.

**Otto**  
![basics/glossary_0.png]
This fella. Autoplays the #[Level]. you'll be using this in levelmaking a lot. click the icon to toggle autoplay.

**Metronome**
![basics/glossary_1.png]
Useful for testing if the #[Level] is in #[Sync]. quite literally is a metronome. click the icon to toggle.

**Frame**  
Measurement of time determined by **FPS** (Frames Per Second), #[RD] runs at 60 #[FPS].

**Bar**, **Beat** and **Crochet**s  
![basics/glossary_2.png]
*Bar* and *Beat* is a measure of time we'll be using often to describe. in the picture, one square equals one beat, and 8 bar equals one bar labeled by each number.

![basics/glossary_3.png]
Let's try and read this #[Classic] beat's position. based on the number left to the beat, we can tell it's in bar 2. and from bar 2, it's positioned 4 squares later, so it's beat 4.

Crochets indicate how many beats are in a bar. you can change how many beats are in a bar by using a **Set Crochets in a Bar** event. Bars are also sometimes referred to as **Measures**.

**Tick**, **Pulse** and **Hit**  
![basics/glossary_4.png]
a classic beat is composed of 7 Pulses, with the last one being a Hit. hits are where you're supposed to hit, and the pulses are everytime a pulse moves through the #[Row]. pulses are labeled with green strips, where hits are labeled with yellow. 

Ticks are an average distance between each pulses. in the picture, each pulses are positioned 1 beat apart, therefore it's a 1-tick #[Classic] beat.

**Swing**  
![basics/glossary_5.png]
Swings makes the interval between pulses irregular in a specific way.

For 1-tick classic beat, every 2 pulses are 2 beats apart. but if there's a 0.5 swing, the second pulse takes 0.5 beat to move to third, and first takes 1.5 beat. the overall length does not change because of the swing, but swings change the position of even-numbered pulses.

![basics/glossary_6.png]
**Sound**  
Sounds indicate every sound that is played in a level. musics, #[Clap]s, #[Beat Sound]s, #[Heart Explosion]s, #[Cue]s...

You can place and change different sounds using the sounds tab.

**Row**  
Rows are the core of gameplay. every #[Character] has a row that pulses appear. if you've played the game, you'll know what rows are.

You can place different kinds of pulses and configure #[Character]s using the rows tab.

**Event**  
Events are what makes #[VFX] and more. everything that isn't related to the #[Gameplay] or #[Sounds] go here. you will be seeing the events tab a lot.

**Room**  
There are four rooms in levels, each of which you can change the camera, size, background and foreground independantly. stacking and utilizing multiple rooms will be crucial for making good #[VFX] and pretty levels. you can place rows in different rooms using the number buttons, and you can change room size, transparency and more at the rooms tab.

**Margins** / **Rank Margins**  
![basics/glossary_7.png]
When we say "margins", we refer to the maximum misses allowed to get each ranks. you can change rank margins at the **Sound Setting** button in the #[Sounds] tab (don't ask me why it's there), but misses allowed for S+ is fixed at 0.

**Legal**  
If your level follows the #[Peer Review] #[Criteria], your levels are labeled legal. this doesn't mean your level is good, but it means your levels are at least fair.

**Gimmick**  
"Special Type of Heartbeat" is considered a gimmick in this game. for example, **Skipshot** is a gimmick. you might know it by the rattle sound along with the X going down an SVT row (#[Oneshot] row).

There are a lot of gimmicks in this game, some notable ones are listed in the #[Types of Beats] section in the glossary. For now, check out [The Gimmick Case Files](https://docs.google.com/document/d/120DVpDAR2xUbwxIhmRlKUzTfzQChDOk7EgKVsq1LTAc/edit) for more detailed list.

**NotRD**  
when a level does not follow conventional RD rules, we call those levels NotRD. some examples includes:
- a:[G and Tonic](https://cdn.discordapp.com/attachments/611380148431749151/621537169890344980/Ladybug_-_G_and_Tonic.rdzip)
- a:[Nhelv](https://cdn.discordapp.com/attachments/611380148431749151/674351919359197249/Silentroom_-_Nhelv.rdzip)
- a:[Square](https://cdn.discordapp.com/attachments/611380148431749151/644361060337451048/Various_-_Square.rdzip)
- a:[Reverence](https://cdn.discordapp.com/attachments/611380148431749151/815745464418041886/Vospi_-_Reverence.rdzip)
- a:[8OROCHI](https://www.dropbox.com/s/lnbx4r0gkgq7omi?dl=1)
- a:[Windows XP Start Menu](https://cdn.discordapp.com/attachments/611380148431749151/827261751706910800/Interactive_Mode_-_Window_XP_Start_Menu.rdzip)
<c>Thanks to pastel, waterdroplet02 and bayou for suggesting me notrd levels</c>

**Gameplay** / **Visual**  
Gameplay is what goes on in the rows tab. when you should hit and all that. #[VFX] goes on top of gameplay. while not being able to see the rows adds to the difficulty, people usually refer to gameplay as just charts.

## Sounds
**Cue**  
Levels feed off of cues. there are different kinds of cues for different kinds of beats. let's go over some of them.

**Get Set Go** (**GSG**)  
These cues are used to signify the start of #[Oneshot] beats. you may have heard this if you played any level with #[Oneshot] rows. putting in get set go cues are very important, and we'll discuss how to put this cue in detail in [[Saving My Kneecaps]] page.

**Nurse Cue**  
These can be applied with a Set Counting Sound event. these are usually used to signify unusual #[Freetime]s or tutorialize some beats. 

<c>In the main game, it's also used to justify #[5-Beats], but don't??? {-x----} exists??????</c>

**Bird Cue** / **Whistle Cue**  
Also applied with Set Counting, but this one has a use.
in a fast {-x-x-x} row, Bird cues are used to signify a 4-Beat is coming. it's not necessary, but it will make your level more fair and friendly to #[Sightread]. Bird cues are labeled as "Cockatiel" in the in-game menu.

**Owl Cue**  
Same with bird cues, but for {-xx-xx} rows. These are a little more necessary than Bird cues, as 3-Beats don't give enough audio cues to prepare for a hit.

**CPU Cue**  
<c>Ah yes, Saviour of Everything /s</c>  
CPU Cues are used to tutorialize and legalize everything that isn't covered by other cues. it can be accessed with Set Row Players event in the #[Events] tab, and by setting that #[Row] to CPU.

This will be best understood with video.
insert a video about CPU Cueing

**Clap**  
Claps are the sounds you hear every hit, it can be changed with a Set Clap event in the #[Sounds] tab.

**Heart Explosion**  
When you successfully hit, after a few beats you will see and hear what's called a Heart Explosion. you can change the timing and volume in the #[Sounds] tab, and the visual shockwave intensity using #[CCM]s.

**Mistake**  
Synonymous with misses, you can also change the miss sound using the #[Sounds] tab.

**Beat Sound** / **Hit Sound**  
![basics/glossary_6.png]
Beat sounds are sounds you hear every #[Pulse], and are different for each #[Row]. (see #[Shakaritis])  
You can change the initial beat sounds by clicking on the #[Character]s in the #[Rows] tab, and change on the fly with Set Beat Sound event in the #[Sounds] tab.

## Types of Beats
![basics/glossary_7.png]
**Classic** Beat / **Oneshot** Beat  
Classics are your everyday beats. hit at the 7th beat thing. Oneshots are what the main game calls "SVT Beats". the ones that needs get set go and stuff.

**X Rows**  
![basics/glossary_8.png]
also known as **Offbeat** or "Heart skipping a beat" (in the main game), it silences a pulse. don't silence the first pulse though! (See #[Bad X Rows])

**Freetime**  
![basics/glossary_9.png]
Using freetimes, you can control each pulse, make pulses go backwards, and do basically everything. keep in mind what you're doing is probably illegal and will have to be #[CPU Cue]d.

**Stacked** Beats  
Beats that overlap a lot are called "Stacked" beats. Stacked classics are usually bad (see #[Shakaritis]) but Stacked oneshots are considered good (as long as the hits line up).

<c>and now watch me steal descriptions from the case files</c>
**Skipshot**  
Do not defibrillate (skip) the next oneshot’s hit.
A red X will slide across the line with a “rattle” audio cue.
In story mode, it counts as a miss when you hit a skipshot.

**Squareshot**  
A oneshot which only occurs once. Does not require a “stop” cue.
Commonly used with irregular oneshots, or for far-spaced oneshots.

**Freezeshot**  
Delays the oneshot according to the spacing of the audio cues.

**Insom Beat**  
Watch the unaltered pattern, and then repeat it while it glitches out.
“Keep counting to seven, no matter what!”

**Syncopation**  
Hit the beat on the 6.5th instead of the 7th.
The ‘beatskip’ does not have to be on the final beat.
<iframe src="https://www.youtube.com/embed/QZ9bG3zkbc8" 
    width="560" 
    height="315"
    frameborder="0" 
    allowfullscreen>
</iframe>
<c>Thank you maddy/saladplainzone ur the best</c>

**8-Beat**  
Hit the beat on the 8th instead of the 7th. The beat starts on the second beat, moves left, and then continues as usual.
<c>remind me to make detailed description of these sometimes later</c>

## Common Mistakes <c>and related things</c>
**Peer Review**  
Peer Review is a thing that happens within #[RDL], done mostly by the moderators. This is where your levels will be judged #[Legal] or not. if your level is legal, your level on [Auburnsummer](https://auburnsummer.github.io/rdlevels/)'s will have a green checkmark, and will be visible to everyone. (Otherwise, you must check "Show Unapproved Levels" to view your level.)

**Criteria**  
This usually refers to the rules you'll have to keep in order to make your level #[Legal].
![criteria](https://cdn.discordapp.com/attachments/515678914316861451/854591623793999883/unknown.png)

**Metadata**  
![basics/glossary_10.png]
Metadata refers to the song name, artist name, and author name, as well as tags, description and stuff you put in the "Export" tab of "Sound Setting".

Having the right metadata is important, check out the [Metadata guideline](https://docs.google.com/document/d/15v2MDEYqn424-xGXfEsrNCkUVx_tDGWM6Vf8QXVgp58/edit?usp=sharing) for detail.

**Backlog**  
Sometimes on #[RDL], people play through a bunch of levels and give feedback for everything. aside from asking for feedback in general, this can be a good way to see what's wrong with your levels.  
<c>see im intentionally leaving out your name so people don't look at you as "the backlog person" because your much more than that and you should know and be not pressured A-</c>

**Uncued** / **Miscued**  
When there's no cue where there should be, it's uncued. when the cue is there but done in a wrong way, it's miscued.

**Bad X Rows**  
There are illegal kinds of X Rows.
- {x-----} X on the first beat
- {-xxxxx} 5 x's
- {-xxxx-}
- {-xxx-x} and {-x-xxx}, while #[Legal], is still frowned upon
- more than 3 Xs with swings (according to @okami)

**Shakaritis**  
If multiple rows share a beatsound, or if there's many #[Stacked] classics, it can be hard to differenciate which sounds are coming from which row. Considering RD is a #[Blind Friendly] game, this is considered not good.

**Heck Swing**  
if you set your #[Swing] value to maximum (twice the #[Tick] value), the #[Row] will act like a {-x-x-x} row but without the xs. this is illegal.

**Psuedos**  
When your #[Hit]s are very close but not in the same #[Beat], you get something that you have to hit twice. this is called a psuedo.

**RHClones** / **Clones**  
When you're recreating something from another game instead of making your own, it's called a Clone. this is generally frowned upon, and sometimes even illegal.

## VFX
VFX is shorthand for Visual Effects, it's what the name suggests- effects that are #[Visual]. aside from #[X Dancing], VFX happen in the #[Events] and #[Rooms] tab.

**Character**s  
Characters are what's to the left of rows, it's what the term suggests. 

**Custom Character**s (**CC**s)  
It's characters that aren't given to you, use the folder button next to the character dropdown to select a character.

**JSON Generator** / **jsongen**
[A tool](http://deadlysprinklez.github.io/rdtools/jsongenerator) that autogenerates the .json file needed for #[Custom Character]s.

**VFX Preset**s / **preset**s  

themes
rooms
magic room
camera
hall of mirror (hom) / HoMvert
true camera
windowdance
event filter
classybeat
box of shapes
resolution
easing

## RDCode
Conditionals
call custom method (ccm)s
comment commands
surgery
tags
play styles
bar / prebar
sort offset
variables