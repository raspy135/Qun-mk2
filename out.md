# Contact

- Email: [info@nunomo.net](mailto:info@nunomo.net)
- GitHub: Open an issue if you have a GitHub account. It's the best place to submit bugs.
- Discord: Visit [Nunomo's Discord server](https://discord.gg/kcvVTPkZVQ) to chat about Qun, read announcements, and talk about events.
- Social media links:
  - Instagram: [@nunomo1](https://www.instagram.com/nunomo1)
  - Twitter (Japanese): [@nunomo1](https://twitter.com/nunomo1)
  - SoundCloud: [nunomo](https://soundcloud.com/user-425164341)
  - YouTube: [nunomollc](https://youtube.com/@nunomollc)


# QUN mk2

*Qun mk2* is a small synthesizer with a powerful sound engine, sequencer, and looper.

![qun_mk2_cgi](./manual_images/qun_mk2_cgi.png)

## Links and Information

* [Online Shop](https://shop.nunomo.net/products/): Purchase your own from our website.
* [Presets template](https://github.com/raspy135/Qun-mk2/blob/main/sd_template.zip): Download and install tone presets. See the [Load Preset](#load-preset) section for details. We constantly update tone presets.
* [Issues](https://github.com/raspy135/Qun-synthesizer/issues): Report issues when you have problems or questions.
* [Firmware](./firmware): Firmware updates and instructions. See [firmware/README.md](./firmware/README.md) for instructions.
* [CheatSheet](./cheatsheet.pdf): A printable cheat sheet listing buttons, device modes and sub-modes, shortcuts, and synth instrument parameters.

**We are looking for your feedback! For general impressions and feedback, please email them to [info@nunomo.net](mailto:info@nunomo.net) or join [Nunomo's Discord server](https://discord.gg/kcvVTPkZVQ)!**


## Overview of the QUN mk2

_Demo: [video](https://www.youtube.com/watch?v=We02ZQKIN9g&t=1s) is available. Tutorial: [playlist](https://www.youtube.com/playlist?list=PLXo02FgbP9F7cfGMUTblNiX6pUctUGqRD) is available. Find more videos throughout this document._

Highlights:

Qun mk2 has a 2 oscillator virtual analog, FM, granular sound engine. The 2 oscillators can be used separately.

The sequencer is an 8-step based sequencer, and supports up to 32/64 steps per pattern. You can store 8 patterns for each preset bucket. And it has 8 buckets of tone preset and sequencer patterns. So you can quickly switch between 8 presets and 64 (8 x 8 pattern) patterns.

It has a 3 track looper with 20 scenes, so you can swap 3 tracks x 20 scenes while playing. 

More:

* **Analog Modeling Engine**
  * The analog modeling engine is **original and made from scratch**. It uses advanced algorithms for great organic sound. The engine is not a copy of a classic synth, it is designed to make modern sounds.
  * Low latency.
  * All analog modeling engine parameters can be configured through MIDI. 
  * Clean 2 Oscillators. Cheap synthesizers compromise this part sometimes, but QUN has no-alias noise Oscillators. All the internal calculation is done by floating point for sound quality.
  * Oscillators can be used as 1 oscillator per voice, or 2 oscillators per voice.
  * Voice can be configured as 4 voices (Quad mode) or 2 voices (Dual mono).
  * The sound engine is compatible with Qun mk1 pocket synthesizer
  * Multiple QUN synths can be stacked to achieve a **Polyphonic** setup. 
  * Flexible MOD routing. 
  * 2 inputs can be used for **external audio signal**, or **external CV inputs**
  * 4 Envelope Generators
  * FM (4 Operators x 2)
  * **Granular / Sampler engine**
  * Vinyl record scratch mode
  * 1 LFO
  * 1 Organic sounding VCF
    * 2/4 Poles, Low-pass, Band-pass, High-pass, Notch
    * Key sync
  * 1 Effect -- Delay, Chorus, Flanger, BitCrusher
  * MIDI clock sync
  
* Player / Sequencer
  * Player -- piano mode
  * MIDI out to control external synths
  * **8/16 step sequencer has 4 pages, up to 64-step sequencer** will generate inspiring beats for you
    * Note On/Off/Double/Triple/4th
    * Modifiers (Transpose, shuffle, repeat steps and more)
    * Parallel pattern running up to 3 patterns
    * Scale quantize
    * Live recording
  * Looper
    * Sequencer synchronized, internal or externally clocked.
    * Looper can record a sample of sound up to around 30 sec for each recording.
    * You can record the sound from the sound engine or external audio.
    * **3 tracks**, **20 Scenes**, total 60 sample recordings in one Session
    * Scene change while playing -- something like Ableton Live's session view
    * Copy / Cut / Paste
    * Play / Rec / Overdub
  * Mixer
  	* Looper tracks can be panned for stereo
  	* Integrated compressor -- Fixed parameters: 30ms attack, 100ms release, 1:3
  	* Stereo output
  	* Mute by track
  
* Micro SD card
  * Qun mk2 comes with a micro SD card.
  * All looper recordings of samples, presets, and granular samples are stored to the SD card

* WiFi
  * Sample recordings can be imported or exported through WiFi web interface.

* Control surface
  * Bank of 8 LED-backlit buttons -- for note playing, sequencing, parameter selection, and more
  * Finite dial encoder with a **relative editing mode** -- either jump to a value, or adjust from the last value 


## CONNECTIONS

* Power: Use a good quality USB power supply. Connect the USB cable to the `POWER` labeled USB port -- the top one, above `UART`.
* MIDI: Use **TRS A** MIDI adapters to connect MIDI cables. The TRS A type adapter is the same as KORG, AKAI, and Make Noise's adapter. This is the lowest latency option. The synth comes with a MIDI TRS A cable.
* Qun has microphones, a stereo line input, and a phone output.
  * `LINE IN` and `PHONE OUT` are located on the right side.
  * The level of PHONE OUT is not strong, so please connect a headphone amp or mixer.
  * The looper's mixer is stereo. **Please use a stereo cable for sound input and output**. 
* Qun comes with a micro SD card. Qun mk2 always needs an SD card. It is safe to remove the card when the disk access indicator is not lit (see the illustration under PLAY MODE). However, the SD is not hot swappable. Please reset the device when you remove the SD card. SDHC is supported, and the disk size is up to 32GB. SDXC is NOT supported. Class 10 card or higher is required to satisfy Qun's bandwidth needs. "Class 10" is indicated on SD cards as a circled 10 or "C10".

## MAJOR MODES

Qun mk2 offers three major modes to use all of its features.

Mode | Description
------------ | -------------
Play | Playing from the Sequencer and Looper. 
System | Loading and saving data, and changing system settings.
Param | Parameter mode: Changing the synthesizer’s tone parameters.

## BASIC OPERATION

_Tutorial: in-depth [basics video](https://www.youtube.com/watch?v=sSR3ob0aQUM&t=1s) is available._

_Reading note: You may see the plus ("+") used in this document for button combinations. To be clear, it symbolizes holding down and using several buttons or controls all at once, in sequence._

* For example, "SHIFT + SEQ PLAY + turn dial" means to press and hold the SHIFT button, and while continuing to hold it also press and hold SEQ PLAY, and finally simultaneously to turn the dial. This will show the beats per minute (BPM) setting on the display, then change it.

Each major mode has selectable **sub-modes**. Many sub-modes have editable **parameters**.

For example, the Param major mode has an `OSC1` sub-mode which configures Oscillator 1, and the Play major mode has a `PIANO` sub-mode which allow direct playing of notes using the [1-8] buttons.

_Workflow: select a sub-mode and parameter, and change a parameter value._

1. Press PARAM to enter Param mode.
2. Switch **sub-mode** by pressing SHIFT + [1-8] button.
3. Select a **parameter** by pressing [1-8] button.
4. Press one of 8 buttons + turn dial to change the parameter value.

Sub-mode names are printed on the device for the Param and Play major modes. For example, look underneath the [1-8] buttons and find `OSC1` and `PIANO` Param and Play sub-modes, respectively.

_Tip: for initial training, help is available._

* Refer to the [Qun cheatsheet](./cheatsheet.pdf) for a useful summary of controls, modes, sub-modes, parameters, and quick feature guides.
* Also seeing a parameter's name when changing its value is useful for initial training. Use **Parameter Caption** for this: press SYSTEM, turn the dial to the System2 menu, press OK to enter it, and finally press button 3 until Parameter Caption is "On".

### Advanced operation

Try all the ways to change **sub-mode**:

* Press SHIFT + [1-8] to change sub-mode
* Press SHIFT + NO / OK buttons to browse and change sub-mode 
* Press SHIFT + turn the dial to browse and change sub-mode
* Double-click the MODE PLAY button, then press [1-8] button to change sub-mode
* Double-click the PARAM button, then press [1-8] button to change sub-mode

And try all the ways to _select_ and _edit_ **parameters**:

* Press [1-8] button to pick a parameter. This selects a parameter as the "current" parameter.
* Press one of the 8 buttons + turn dial to quickly change a specific parameter's value, and select this parameter as "current".
* Simply turn the dial to change the _current_ parameter.
* Long press the [1-8] button of a parameter to show its full name and value, and to set it as "current".
* Double click + hold the [1-8] button to enter **relative editing mode**. Turning the dial will change a value relative to the last value. Otherwise, normal turning of the dial will jump to a value starting from the top of the dial. _Tutorial: [video](https://youtu.be/6uP1LoAZ9nE?t=11) is available._
* If you want to do fine value adjustment, you can use NO / OK buttons to change the value by 1. To do this, keep pressing one of 8 buttons and press NO or OK button.

_Tip: menus can be scrolled through, one by one, with buttons 7 and 8._

* Scrolling in menus by turning the dial will sweep through many menu items quickly.
* Try using button 7 and 8 to scroll one at a time: press SYSTEM, then press button 8 twice to reach the "System" item, and finally press OK.

_Reading note: to help teach the buttons (and dial) needed to use a given feature, see "Overview" images. They visually depict which parts of the Qun need to be touched for a command. They can be an aide when building visual-memory for learning to use the Qun._

* As an example, consider the "SHIFT + SEQ PLAY + turn dial" command to set BPM. It involves three controls: ![](./manual_images/but/s_splay_d.png) Observe in the image that the required controls are spread across the Qun, and how a two-handed operation may therefore be needed.

Button | Primary function 
:------------: | -------------
SHIFT <br> ![](manual_images/but/s.png) | SHIFT + [1-8] button or NO / OK button to select sub-mode | 
[1-8] button <br> ![](manual_images/but/12345678.png) | Select a parameter in the current sub-mode. Also show information with LEDs (see under LED Indicators).
NO <br> ![](manual_images/but/n.png) | Select previous sequencer pattern
OK <br> ![](manual_images/but/o.png) | Select next sequencer pattern
Dial <br> ![](manual_images/but/d.png) | change parameters
SEQ PLAY <br> ![](manual_images/but/splay.png) | Start / Stop sequencer
REC + SEQ PLAY <br> ![](manual_images/but/lr_splay.png) | Start sequencer live recording 
MODE PLAY <br> ![](manual_images/but/mplay.png) | Select Play mode
SYSTEM <br> ![](manual_images/but/sys.png) | Select System mode
PARAM <br> ![](manual_images/but/param.png) | Select Parameter mode
REC <br> ![](manual_images/but/lr.png) | Looper status page
REC + LOOPER PLAY <br> ![](manual_images/but/lr_lplay.png) | Start looper recording sound
LOOPER PLAY <br> ![](manual_images/but/lplay.png) | Start looper playing
LOOPER STOP <br> ![](manual_images/but/ls.png) | Stop looper playing
RST button on the base board | Reset the device
4 touch buttons at the bottom board | This can be used as a touch slider. See the [Touch Slider](#touch-slider) section for detail. 
SHIFT + NO + OK <br> ![](manual_images/but/s_n_o.png) | Sleep (Shutdown) the device. It will turn off most of the power consuming components like the main CPU and the screen. Press the RST button to restart the device.

## BASIC SHORTCUTS

Button | Function
:------------: | -------------
SHIFT + MODE PLAY <br> ![](manual_images/but/s_mplay.png) | Dump current preset to MIDI OUT. This is useful to transfer the current preset to another Qun / Qun mk2 synthesizer.
SHIFT + SYSTEM <br> ![](manual_images/but/s_sys.png) | All notes off
SHIFT + PARAM <br> ![](manual_images/but/s_param.png) | Initialize the preset. Choose from a default: Blank, Sampler, EvenSlice, or Scratch. Please see the [Initialize preset](#initialize-preset) section for details. 
SHIFT + SEQ PLAY + turn dial <br> ![](manual_images/but/s_splay_d.png) | Set BPM. Tap tempo by pressing SEQ PLAY 4 or more times while you keep pressing SHIFT. 
MODE PLAY + turn dial <br> ![](manual_images/but/mplay_d.png) | Record volume -- stay at -6.0dB or lower to avoid clipping. _Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=770s) is available._
MODE PLAY + SYSTEM + turn dial <br> ![](manual_images/but/mplay_sys_d.png) | Looper master volume 
SYSTEM + turn dial <br> ![](manual_images/but/sys_d.png) | VCF volume
PARAM + turn dial <br> ![](manual_images/but/param_d.png) | VCF cutoff
REC + turn dial <br> ![](manual_images/but/lr_d.png) | LFO tune
LOOPER PLAY + [1-5] <br> ![](manual_images/but/lplay_12345.png) | Select Scene
REC + [1-3, 7,8] <br> ![](manual_images/but/lr_12378.png) | Select looper sample recording track. A,B,C are mono tracks. Press 7, 8 for stereo recording. 7=A(Left)+B(Right), 8 = B+C. When you do stereo recording, you may want to set pan to left and right for the selected stereo tracks. 
PARAM + [1-3] <br> ![](manual_images/but/param_123.png) | Mute track
MODE PLAY (RECALL) + [1-8] <br> ![](manual_images/but/mplay_12345678.png) | Recall preset bucket. See the [Preset Bucket](#preset-bucket) section for details.
SEQ PLAY + [1-8] <br> ![](manual_images/but/splay_12345678.png) | Select Sequencer pattern
SHIFT + LOOPER PLAY + turn dial <br> ![](manual_images/but/s_lplay_d.png) | Load session when you are not in System mode or Granular mode. 
SHIFT + LOOPER PLAY + [1-3] button <br> ![](manual_images/but/s_lplay_123.png) | Import WAV file from import folder to selected track
SYSTEM + [1-8] <br> ![](manual_images/but/sys_12345678.png) | Temporary piano mode

## LED Indicators

![leds](./manual_images/leds.png)

The synth has 8 LED indicators on the switch.
A solid, illuminated LED shows the current sequencer pattern number.

The LEDs may also show other information:

When | LED will show
------------ | -------------
When the sequencer is running | The current position of the sequencer
When trying to switch Scene, while pressing LOOPER PLAY | The current selected Scene
When trying to switch Track, while pressing LOOPER REC | The current selected Track
When trying to mute Track, while pressing PARAM | The current mute status of the Tracks
When trying to switch Bucket, while pressing MODE PLAY | The current selected Bucket


## MIDI learning

Assigning proper MIDI CC to your MIDI keyboard is recommended for frequently used parameters, however, you can override MIDI CC temporarily by the following operation:

1. In Parameter mode, press and hold the corresponding parameter button for a long time -- about 3 sec. For example, OSC1's Pulse Width which is button 2 in OSC1 sub-mode.
2. Then the parameter name and value will be shown on the screen. Keep pressing the button another 3 sec.
3. Send MIDI CC signal from your MIDI keyboard: Turn a knob or move a fader. The sent MIDI CC# will control the assigned parameter.

Once the parameter is assigned, then "*" mark is indicated before the CC number. Original CC assignment is still working. It won't be affected with MIDI dumping.
MIDI learning will take any MIDI channel. For example, even if you set the device to receive MIDI channel 2, MIDI learning can receive CC# for channel 3, or any other channels.

To cancel the override, do the same operation again.

To avoid confusion, this setting won't be saved.

## Session

Qun automatically collects the current looper sample recordings, tone and sequencer presets into a Session. Sessions can be saved and loaded. They are automatically numbered and can be manually named.

![session_diagram](./manual_images/session_diagram.png)

Session is the biggest data unit of the synth.

Session includes 8 preset buckets. Each bucket contains one preset with 8 pattern sequencer data.

There is no "new session" function. The synth always create a new session when booting. Reboot the device to create a new session.

Session button operations work in both **Parameter** and **Play modes**:

Button | Function
:------------: | -------------
SHIFT + LOOPER PLAY <br> ![](manual_images/but/s_lplay.png) | Show current session number
SHIFT + LOOPER PLAY + turn dial <br> ![](manual_images/but/s_lplay_d.png) | Load session
NO or OK button while selecting a session | Scroll session page when you have more than 32 sessions 
SHIFT + REC <br> ![](manual_images/but/s_lr.png) | Save current session (Looper stop will perform session save when autosave is on)
SHIFT + REC (Long press) <br> ![](manual_images/but/s_lr.png) | Name current session
SHIFT + REC + B[1-3] <br> ![](manual_images/but/s_lr_123.png) | Load WAV file to looper track A, B or C. See the [Looper Overview](#looper-overview) section for details.
Press B[1-8] while booting <br> ![](manual_images/but/12345678.png) | Load a previous LOOPER folder. E.g. Button1 means LOOPER00, Button2 means LOOPER01, and so on.

_Workflow: load a different session._

1. Press SHIFT + LOOPER PLAY when you are not in System mode or Granular mode. 
   1. Current session number will be indicated, for example "Looper00:0001". 
2. Turn the dial to select the session you want to load.

Saving session is semi-automated.
Looper sample recording data will be saved immediately after the recording. 
Mixer and Bucket data will be saved when the LOOPER STOP button is pressed.
This can be turned off in the System2 menu.

## Initialize Preset

You can initialize a preset by pressing SHIFT + PARAM.

Several preset templates are available when initializing: Blank, Sampler, EvenSlice, and Scratch. Blank is the base preset for all.

The following parameters will be set when you select other templates:

**Sampler**: Sampler is for basic sampler setup.
- OSC1 type = AUX L
- OSC Octave = +1
- Granular mode = ONE
- Env1 Release to 58 for gentle release

**Slice**: Slice is good for one-shot multiple slicing.
- OSC1 type = AUX L
- OSC Octave = +1
- Granular mode = ONE
- Env1 Release to 58 for gentle release
- OSC1/2 Keysync is disabled (1N2N)
- Slice Spread is set to 1 (Each semitone from C4 will play different slices)

**EvenSlice**: EvenSlice is for sampler with evenly slicing samples.
- OSC1 type = AUX L
- OSC Octave = +1
- Granular mode = ONE
- Env1 Release to 58 for gentle release
- OSC1 mod src = FREQ1 to modulate PWM by MIDI note
- OSC2 mod src = FREQ2 to modulate PWM by MIDI note
- Keysync = 1N2N to disable pitch control by MIDI note

*EvenSlice expects to change OSC1 MOD WIDTH to control the size of the slice.*

**Scratch**: Scratch is for vinyl record scratching mode. 
- OSC1 type = AUX L
- OSC Octave = +1
- Granular mode = ONE
- Env1 Release to 58 for gentle release
- Env1 Src = ON

## Preset Bucket

The synth has 8 preset buckets to quickly recall presets. Each bucket contains one preset and 8 sequencer patterns.

![data_structure](./manual_images/bucket_diagram.png)

Button | Description
:-------:|-------
MODE PLAY (RECALL) + B[1-8] <br> ![](manual_images/but/mplay_12345678.png) | Switch Bucket
MODE PLAY (RECALL) + B[1-8] + turn dial <br> ![](manual_images/but/mplay_12345678_d.png) | Copy Bucket

Solid LED indicates current bucket you are in when pressing MODE PLAY button.

Bucket information is automatically saved with Session. 

_Tutorial: understand how Buckets work with tones using the RECALL button._

1. Reset the Qun by pressing the RST button on the base board. 
2. Change a parameter to configure the sound. Let's set its shape to a **Sine wave**. Hold B1 + turn dial to Sine. This tone preset is currently in Bucket 1.
3. Press RECALL (the MODE PLAY button) + button 2 to switch Bucket 2. "Bucket 2" will be shown on the display.
4. See the sound's shape is changed back to the default **Saw wave** from your previously chosen Sine wave.
5. Change a parameter to program Bucket 2's sound. Let's set its shape to **White noise**. Hold B1 + turn dial to "W" for White noise.
6. Press RECALL + button 1 to switch back to Bucket 1. "Bucket 1" will be shown on the display.
7. See the first sound you configured is now recalled.
8. Press RECALL + button 2 to switch to Bucket 2 again
9. See the White noise should be recalled.

When you save the preset or load the preset from bank 1 to 8, its name is used to indicate the bucket, so it is always recommended to set a name by saving or loading the preset.


## Signal diagram

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=230s) is available for several stages._

Signal diagram helps to understand how Qun mk2 works.

![‎qun2_diagram](./manual_images/‎qun2_diagram.png)

# Parameter Mode (Param)

## Adjust synthesis parameters
To operate, press B[1-8] to choose a parameter and turn dial to change its value. The parameter display area will temporarily invert. A parameter's position in the display corresponds to the visual button assignment:

```
 1  3  5  7
 2  4  6  8
```

E.g. button 1 chooses the wave SHAPE parameter when in the OSCILLATOR1,2 sub-mode.


## PRM:OSCILLATOR1,2

_Tutorial: [video](https://www.youtube.com/watch?v=7-3rrYf2dhs) shaping sound with Triangle and band-pass filter is available using the legacy Qun mk1 pocket synthesizer._

![osc1](./manual_images/osc1.png)

The oscillator is a hybrid of classic analog synth, FM, and granular.

Button | Description
-------|-------
1 | SHAPE. `Saw, Sine, S&H, Square, Triangle, W Noise, P Noise, FM, AUX`.<br> * AUX means audio input from LINE or MIC. <br> * Granular synth engine is connected to the AUX L channel when it's active. See [Granular](#plygranular) section for detail. 
2 | PULSE WIDTH.  Triangle, Square and Granular can take PWM. In granular mode, the playing position will be changed by PWM.
3 | TUNE
4 | OCTAVE
5 | MOD TUNE. MOD modulation to tune. Default MOD source is EG1.
6 | MOD WIDTH. MOD modulation to pulse width.
7 | LFO TUNE. LFO modulation to tune.
8 | LFO WIDTH. LFO modulation to pulse width.

### Pulse Width Modulation (PWM)

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=830s) is available._

Qun supports PWM. It affects Square wave oscillations normally: changing the duration of the pulse of the wave. It affects other waveshapes in the following ways:

- Triangle: Adds harmonics as well as DC bias
- Granular: Changes playing position
- Sine: Adds wavefolding for harmonics


## PRM:MIX

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=400s) is available._

Mix controls mixer and effects. It mixes OSC1/2 and other voices together.

![mix](./manual_images/mix.png)

Button | Description
-------|--------
1 | OSC MIX. Balance between OSC1 and OSC2
2 | FM modulation OSC2 to OSC1
3 | VCF Volume.  Input gain to VCF. _Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=480s) illustrating wavefolding, is available._
4 | Line In / Mic gain
5 | Effect type. Off, Delay, Chorus1, Chorus2, Flanger1, Flanger2, Crusher (Bit crusher), MDelay (Mono delay), DDelay (BPM Synchronized digital delay), Tape, RSVD (Reserved for the future update). _Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=745s) is available._ 
6 | Effect Speed. Controls Effect LFO rate or delay time. 
7 | Effect Depth
8 | Effect Feedback

### Effector tips
- The Delay speed can be set very short. Create an interesting simulation of flute or violin by using a very short delay. Mono Delay will work better for the use of delay as a resonator.
- You can widen the stereo image by using a short delay. 
  - Effector Type: Delay
  - Speed: Around 30
  - Depth: Around 30
  - Feedback: 0
- Digital delay is BPM synchronized. It also can be used as beat repeat by setting 100% of feedback, and 100% of depth.
- Tape emulates tape/vinyl audio degrade,  useful for master effect (Extra Processing is ON)
  - Depth controls recording to playing audio degrade. It's subtle but follows real behavior of recording/playing compression.
  - Speed and Feedback controls tape wobble effect.
  - When it's used as master effect, it's recommended to use filters and clipping curve to complete vintage analog feeling.


## PRM:ENV1/2

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=290s) is available._

The synth has four Envelope generators. ENV1 and ENV2 are both independently and fully configurable. ENV3 and ENV4 share parameters. ENV3 / ENV4 is connected to FM operators when it's configured via FM ENV3 CONN.

![diagram_eg](manual_images/env12.png)

Button | Description
------------ | -------------
1 | ENV1 Attack
2 | ENV1 Decay
3 | ENV1 Sustain
4 | ENV1 Release
5 | ENV2 Attack
6 | ENV2 Decay
7 | ENV2 Sustain
8 | ENV2 Release

## PRM:OSC Switches
Switches and modulation routing.

![switches](./manual_images/switches.png)

Button | Description
------|--------
1 | OSC1 Env(VCA) source
2 | OSC1 Wide tune switch. When it's on, OSC1's tune reacts much more sensitively.
3 | OSC1 Modulation source
4 | Env1 invert switch. Modulation will be affected in the opposite way, and amp gain will be (1.0 - Envelope). 
5 | OSC2 Env(VCA) source
6 | OSC2 Wide tune switch
7 | OSC2 Modulation source
8 | Env2 invert switch 


## PRM:LFO
![diagram_lfo](manual_images/lfo.png)

Button | Description
-------|-------
1 | LFO SHAPE.  `Saw, Sine, RevSaw, S&H, Square, Triangle, AUX, OSC2, OSC2EG`. OSC2EG is the signal from OSC after Envelope Generator processing.
2 | LFO PULSE WIDTH. When it's applied to the SAW wave or SINE wave, it will affect phase offset. It is useful with BPM sync and retrigger. 
3 | LFO TUNE
4 | KEYSPLIT. This is a unique feature of the synth. When it is not zero, then the note number above the parameter becomes the LFO rate controller. If you set 60, then C4 or higher notes control LFO: higher notes will generate higher LFO rates. If you press multiple notes, it doubles and triples the rate, which can be great for live performance.
5 | LFO MOD TUNE. MOD modulation to tune.
6 | LFO MOD WIDTH. MOD modulation to pulse width.
7 | LFO MOD Source. `EG1, EG2, EG3, EG4, AUX, OSC2, OSC2EG, FRQ1, FRQ2`
8 | LFO Retrig. LFO’s phase is reset by every note hit when it is ON.

## PRM:VCF

![diagram_vcf](manual_images/vcf.png)

Button | Description
------|-------
1 | CUTOFF
2 | RESONANCE
3 | VCF TYPE `LPF,BPF,HPF,Notch`.
4  |VCF KEY SYNC. When it is not zero, VCF’s cutoff will follow the playing note. Higher value is more sensitive.
5 | VCF MOD CUTOFF. MOD modulation to cutoff. 
6 | VCF LFO CUTOFF. LFO modulation to cutoff.
7 | VCF MOD SRC. MOD modulation source : `EG1, EG2, EG3, EG4, AUX, OSC2, OSC2EG, FRQ1, FRQ2, ON`.
8 | VCF LFO Volume. LFO modulation to VCF’s input volume. It can be used as a vibrato effect.

## PRM:KEY/OTHER

Configures other parameters.

![other](./manual_images/other.png)

Button | Description
|------ | ------|
1 | VCF 4/2 POLE / NoLinear. Select VCF number of poles and linear or no linear. 2P/4P/2PNL/4PNL. Ladder filter algorithm will be used only when 4NL with Lowpass or Highpass filter.
2 | VCF ENV Src. Applying Envelopes to the signal after VCF. You might want to set OSC1/2's Env sel to "ON" to utilize this parameter. This is useful only with Mono mode. _Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=672s) is available._
3 | GLIDE. Smooth transition between notes. 
4 | BEND RANGE. Pitch bend range.
5 | OSC1/2 Keysync. This is a switch to connect MIDI input notes and oscillators. Y = Follow MIDI note pitch. N = Ignore MIDI note. You can still use FREQ1 and FREQ2 for modulation to use MIDI note pitch.
6 | VELOCITY SW. Envelope generators become velocity sensitive when it’s ON.
7 | MONO/QUAD/POLY (Voice mode).  See the [Voice Mode](#voice-mode) section for details. 
7 (Long press) <br> ![](manual_images/but/7.png) | Sync Oscillator parameters.  See the [Voice Mode](#voice-mode) section for details. _Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=925s) is available._
8 | LFO BPM sync. LFO rate will synchronize with Sequencer's BPM when it is ON.

### Voice Mode

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=110s) is available._

One synthesizer can be used as Monophonic or Quadphonic.

- Mono = 2 OSCs for 1 voice
- Quad = Quad Tone: 1 OSC per voice, and the engine has total 4 oscillators for the extra voices
- PolyMono = 2 OSCs per voice, but you can get 2 voices
- PolyQuad = 1 OSC per voice. It's for Polyphonic setup when you have multiple Qun synthesizers.

When the mode is Quad or Poly Quad, MIX  and "OSC2 Env Src" are ignored. MIX is always set to middle, and OSC2 Env Src is always set to EG2. In most cases you may want to use the same parameters between OSC1 to OSC2 with Quad mode. 

To copy the parameters from OSC1 to OSC2 (and EG1 and EG2), long press button 7. "OSCs synched" message will be shown. 
	
_Workflow: set up Quad tone mode._

1. Initialize tone.
2. Configure OSC1 as you like.
3. Set this parameter to "Quad" mode by pressing button 7.
4. If you want to copy OSC1 parameters to OSC2, in the same sub-mode, long press button 7 until the "OSCs synched" message is shown.
5. Play two notes by external MIDI keyboard. You will hear four voices.


Poly Mono can be used when you want 2 voices with 2 OSCs per voice configuration.
	
Poly Quad is for multiple device stacked configuration. You can use multiple Qun Synthesizers to build a polyphonic synth.
	Please see “[Polyphonic setup](#polyphonic-setup)” for detail.


## PRM:FM
![diagram_fm](./manual_images/fm.png)

The synth has 2 x 4 operator FM engine. OSC1 or OSC2 can be set to FM mode.
Each operator has a sine wave.
OSC1 and OSC2 share the FM parameter.

Button | Description
-----|-----
1 | FM Algorithm
2 | D Amplitude
3 | A Frequency
4 | A Amplitude
5 | B Frequency 
6 | B Amplitude 
7 | C Frequency 
8 | C Amplitude 

FM ALGORITHM

"ABCD" indicates each operator.
Vertical relationship means upper operator modulates lower operator.
For example,

```
	    A
	B C D
```
This means that operator A modulates operator D. B, C and modulated D will be mixed in parallel.
```
	A
	B
	C - D
```

This means A modulates B, the result modulates C, the result modulates D.


Oscillator (ABC)’s frequency (multiple of frequency of D).

When FM FREQ SNAP (In ENV3/4 Other sub-menu) is off, it can be adjusted to the exact frequency of harmonics (2,3,4,5, ...). If you want clean FM sound, turn FM FREQ SNAP on.

## PRM:ENV3/4 / Other

![fm2](./manual_images/fm2.png)

Button | Description
--------|--------
1 | 2ND FILTER. See the [2nd Filter](#2nd-filter) section for details.
2 | FM FREQ SNAP SW. Frequency snapping for FM. When it's ON, FM frequency will be snapped to numbers. When it's OFF, FM has more character, the signature sound of the QUN synth.
3 | Wavefolding. Wavefolding curve selection. This filter is located in VCF.
4 | FM ENV3 CONN. Select FM operator(s) to connect ENV3/4. After the processing, it will be filtered by ENV1 or ENV2.
5 | ENV3/4 ATTACK
6 | ENV3/4 DECAY
7 | ENV3/4 SUSTAIN
8 | ENV3/4 RELEASE

### 2nd Filter

_Tutorial: [video](https://www.youtube.com/watch?v=7dNhxKBtwPo&t=650s) is available._

Second filter can be used when you use the 2 POLE filter for VCF. It's disabled when 4 POLE is selected. It provides additional shaping of the sound. 

Mode | Description
------------ | -------------
NC200 | Notch filter at 200Hz. It will remove some muddy.
NC1K | Notch filter at 1kHz. It will remove some highs.
LS100 | Low-shelf at 100Hz. It will boot bass without cutting high.
LS150 | Low-shelf at 150Hz. It will boot bass without cutting high.
LS200 | Low-shelf at 200Hz. It will boot bass without cutting high.
LS300 | Low-shelf at 300Hz. It will boot bass without cutting high.
HP80 | Highpass at 80Hz. It will remove low-end bass to get more clear sound.
LP4K | Lowpass at 4kHz. It will remove high-end.
PK100 | Peak filter at 100Hz. Similar to band-pass filter, but Peak filter boots the peak frequency but it will not cut other frequencies like band-pass filter.
PK150 | Peak filter at 150Hz.
PK200 | Peak filter at 200Hz.
PK300 | Peak filter at 300Hz.
PK400 | Peak filter at 400Hz.
PK800 | Peak filter at 800Hz.



# PLAY MODE

![screen_play](./manual_images/screen_play.png)

Disk access indicator is active when the system is accessing the SD card. Some actions are restricted while writing.

Track / Scene tile shows selected track (A,B or C) and Scene number (1 to 5).

Looper status shows Looper position and status.

Clipping indicator is active when signal is clipped at the end of signal chain, after compressor.

## COMMON SEQUENCER OPERATIONS

Most actions work in any major mode, and are not limited to Play mode.

Button | Function
:-------:|-------
SEQ PLAY <br> ![](manual_images/but/splay.png) | Start / Stop Sequencer
REC + SEQ PLAY <br> ![](manual_images/but/lr_splay.png) | Start Sequencer live recording
REC + SEQ PLAY + turn dial <br> ![](manual_images/but/lr_splay_d.png) | Metronome volume
SHIFT + SEQ PLAY + turn dial <br> ![](manual_images/but/s_splay_d.png) | Set BPM. Tap tempo by pressing SEQ PLAY 4 or more times while you keep pressing SHIFT. 
NO <br> ![](manual_images/but/n.png) | Previous sequencer pattern
OK <br> ![](manual_images/but/o.png) | Next sequencer pattern
SEQ PLAY + [1-8] <br> ![](manual_images/but/splay_12345678.png) | Select Sequencer pattern
SEQ PLAY + [1-8] , [1-8]...<br> ![](manual_images/but/splay_12345678.png) | Chain sequencer pattern(Pattern chaining). Keep pressing SEQ PLAY. 
SEQ PLAY + NO / OK <br> ![](manual_images/but/splay_n_o.png) | Move to previous / next Sequencer page
SHIFT + SEQ PLAY +  NO / OK <br> ![](manual_images/but/s_splay_n_o.png) | Copy Sequencer page to previous / next Sequencer page
SEQ PLAY + [1-8] + turn dial <br> ![](manual_images/but/splay_12345678_d.png) | Copy sequencer pattern to other pattern. If you want to cancel the operation, turn to the end, then "CANCEL" will be indicated as the destination. To initialize the bank data, turn the dial to "CLEAR". 

## COMMON LOOPER OPERATIONS

Button | Function
:-------:|-------
REC <br> ![](manual_images/but/lr.png) |  Go Looper status page
LOOPER PLAY <br> ![](manual_images/but/lplay.png) |  Start Looper
LOOPER STOP <br> ![](manual_images/but/ls.png) |  Stop Looper
LOOPER REC + LOOPER PLAY <br> ![](manual_images/but/lr_lplay.png) |  Start looper sample recording
LOOPER PLAY + [1-5] <br> ![](manual_images/but/lplay_12345.png) |  Select Scene
LOOPER PLAY + NO or OK <br> ![](manual_images/but/lplay_n_o.png) |  Change Scene page (5 Scenes per page)
LOOPER PLAY + [1-5] + turn dial <br> ![](manual_images/but/lplay_12345_d.png) |  Copy Scene
REC + [1-3, 7,8] <br> ![](manual_images/but/lr_12378.png) |  Select sample recording track. A,B,C are mono tracks. Press 7, 8 for stereo recording. 7=A(Left)+B(Right), 8 = B+C. When you do stereo recording, you may want to set pan to left and right for the selected stereo tracks. 
SHIFT + REC + B[1-3] <br> ![](manual_images/but/s_lr_123.png) |  Load WAV file to looper track A, B or C. Importing WAV file to the looper section for detail. 
PARAM + [1-3] <br> ![](manual_images/but/param_123.png) |  Mute track
PARAM + NO <br> ![](manual_images/but/param_n.png) |  Toggle Extra Processing
SHIFT + LOOPER STOP <br> ![](manual_images/but/s_ls.png) |  Delete all track recordings in the current scene, reset recording length 
REC + NO <br> ![](manual_images/but/lr_n.png) |  Cut or Copy Looper track 
REC + OK <br> ![](manual_images/but/lr_o.png) |  Paste Looper track 
REC + PARAM <br> ![](manual_images/but/lr_param.png) |  Open UNDO list. Select the top item to undo the last sample recording for the track. Select the second item to undo the last sequcener recording. SHIFT + OK to preview the sound. 
MODE PLAY + PARAM + turn dial <br> ![](manual_images/but/mplay_param_d.png) |  Parameter Lock Morphing

## Sequencer overview

_Tutorial: [video](https://www.youtube.com/watch?v=vZqdzkTQ1Mg&t=1s) is available._

The sequencer is an 8/16-step sequencer. One page has 8/16 steps, and it can have up to 4 pages.

The sequencer UI is influenced by analog 8-step pattern based sequencers. You turn can on and off patterns, and change parameters for the steps. 

Sequencer data will be saved when you save tone presets, and it is saved with the Session. Each preset can have 8 sequencer patterns.

You can run multiple sequencer at the same time, up to three patterns, as normal parallel running or relative running. See the [PLY:SEQ CONFIG](#plyseq-config) section for detail.

### Sequencer live recording

You can record live playing to the sequencer. Rec + SEQ PLAY to start recording notes. Play on Piano mode or play with an external MIDI keyboard to record notes. It's always overdubbing.  Note, Width (length), and velocity will be recorded.

Sequencer playing position indicator changes when live recording.

| Sequencer recording | Screen                                        |
|---------------------|-----------------------------------------------| 
| Normal              | ![seq_normal](./manual_images/seq_normal.png) |
| Live recording      | ![seq_live](./manual_images/seq_live.png)     |

Also, all LEDs are on for the even steps while live recording.

Press SEQ PLAY to exit recording mode, and the sequencer will keep playing. Press SEQ PLAY again to stop the sequencer.

You can (re)enter recording mode while playing. Press REC + SEQ PLAY to enter recording mode.

A metronome click sound plays when live recording is ongoing. The metronome volume can be adjusted with REC + SEQ PLAY + turn dial. The chained sequencer pattern will be reset when you change to another pattern.

You can undo the last recording. Press REC + PARAM to open Undo list, then select the second item.

### Parameter Lock live recording

When you are in sequencer live recording, changing sound engine parameters will be recorded as Parameter Locking. **The recording starts when you start changing the parameter, and it ends at the end of the pattern.**

### Edit the current step while Sequencer live recording

Button | Function
:--: | --
B 7 or 8 <br> ![](manual_images/but/78.png) | Specify the current step when in Tune, Width, Velocity, or Prob mode
B 7 or 8 + turn dial <br> ![](manual_images/but/78_d.png) | Record sub-step parameter when in the Tune, Width, Velocity, or Prob mode

When you are in Tune, Width, Velocity, or Prob mode, and you are also in sequencer live recording, pressing B7 + B8 will specify the current step. The "Current" message will be shown.

While you are pressing B7 + B8, the dial position will be recorded to the current playing position.


## Parameter Locking

_Tutorial: [video](https://www.youtube.com/watch?v=wyU148xfGao&t=275s) and [demo video](https://www.youtube.com/watch?v=lnqzkueQrP8) are available._

Parameter locking is the term used in Elektron sequencers, which is a temporary parameter change available only in the specific sequencer step. The parameter change appears only when the sequencer is playing the step. 

Button | Description
:--: |  --
B[1-8] (Long press), then PARAM<br> ![](manual_images/but/12345678_param.png) | Selects a step to lock a parameter for, when in a supported Sequencer sub-mode. See below for more detail.<br><br>(Long press PARAM, also) Clear lock for selected step, or multiple selected steps, if already set.
SEQ PLAY <br> ![](manual_images/but/splay.png) | Navigate back to sequencer, and finish setting up locks
PARAM (Long press) <br> ![](manual_images/but/param.png) | Clear active parameter lock
B[1-8] + PARAM + turn dial <br> ![](manual_images/but/12345678_param_d.png) | Change the last edited locked parameter 

Here are the steps to set Parameter Lock:

1. In Play mode, you should be one of the following modes: ON/OFF, Tune, Width, Velocity, or Probability, press [1-8] button to select the step that you want to set Parameter Lock
2. Keep pressing the button, and press [PARAM]. Mode switches to Parameter Lock mode.  White frame indicates you are in Parameter Lock mode.
3. Change the parameters that you want to change. Once the parameter is changed, the parameter area will be inverted, indicating the step is modified.
   1. ![pl_mark](./manual_images/pl_2.png)
4. You can set up to three parameters to modify.
5. To finish the editing, press [PLAY] to go back to the sequencer page.
6. You will see [""] mark at the top of the step when the step has Parameter Lock.
   1. ![pl_mark](./manual_images/pl_1.png)
7. To reset the modification, long press [1-8] button + [PARAM] when entering Parameter Lock mode, or long press [PARAM] when in Parameter Lock mode. If you press multiple buttons for the steps, multiple steps will be cleared.
8. Once you change one parameter, you can change the last edited Locking parameter by pressing [1-8] + [PARAM] + Turning dial without re-selecting the parameter.
9. When you are in sequencer live recording, changing sound engine parameters will be recorded as Parameter Locking.

Parameter lock will be triggered only when the step is turned on.

_Tip: SHIFT + turn dial is a useful way to sweep between sub-modes to find modified parameters._



## Parameter Lock morphing

_Demo: [video](https://www.youtube.com/watch?v=cqweekqYIu4) is available._

You can morph Parameter Locking between two patterns.

_Workflow: morph pattern lock._

1. Let's say you are in pattern #1. Set Morph Pattern in Sequencer configuration menu. Set the Morph pattern to #2 by long pressing button 4.
2. Copy pattern #1 to #2 with SEQ PLAY + [1-8] + turn dial
3. Move to pattern #2
4. Modify the Parameter Locking in pattern #2
5. Go back to pattern #1
6. Morph can be done by pressing [MODE PLAY] + [PARAM] + turn dial

## Looper overview

_Tutorial: [video](https://www.youtube.com/watch?v=iD4WpX3tHUE&t=1s) is available._

The Looper is designed to work with the Sequencer. The Looper always tries to sync with sequencer play. The Looper won't start playing when the Sequencer is not running. The Looper can stop separately from the Sequencer.

Use a blank sequencer pattern when you don't want to record sound from the Sequencer. For example, use a blank pattern to record sounds only from LINE IN or MIC.

To start the Looper recording sound, hit LOOPER REC + LOOPER PLAY. If the Sequencer is not running, it will not start recording, but it is standing by for recording. In this case, press SEQ PLAY to start recording. When the Sequencer is playing, the recording will be started at the beginning of the next measure.

**Looper recording:**

Button | Result | If Sequencer in state ... | ... and Looper in state 
|:--------:|--|---------------------------|-----------|
LOOPER REC + LOOPER PLAY <br> ![](manual_images/but/lr_lplay.png) | Looper stand-by| Stop                      | Stop      
SEQ PLAY <br> ![](manual_images/but/splay.png)| Play Sequencer to next measure. Then, start Looper recording and continue Sequencer playing.| Playing / Stop            | Stand-by  
LOOPER STOP <br> ![](manual_images/but/ls.png) | Stop Looper recording. Continue Looper and Sequencer playing.| Playing                   | Recording 

The first recorded track will define the length of the loop.

Press LOOPER STOP to finish the recording. You don't need to press the stop button precisely -- you can press earlier, then recording will be finished at the end of the measure.

Looper keeps playing the recorded sound. All recorded data will be saved to SD card immediately.

**Looper playing:** 

Button | Result | If Sequencer in state ... | ... and Looper in state    
|:--------:| --|---------------------------|-----------|
LOOPER PLAY <br> ![](manual_images/but/lplay.png) | Start Looper playing.|Playing / Stop | Stop      
LOOPER STOP <br> ![](manual_images/but/ls.png) | Stop Looper.|Playing / Stop | Playing   
SEQ PLAY <br> ![](manual_images/but/splay.png) | Stop Sequencer playing. Continue Looper playing.|Playing | Playing   


When you press REC + LOOPER PLAY twice (or SHIFT + REC + LOOPER PLAY), the recording mode will be REC mode. 

In REC mode, it will overwrite the existing recording. It will change loop length when the new recording is longer than the existing one.

When you press REC + LOOPER PLAY 3 times or 4 times, it enters Insert Recording mode. See the [Insert Recording](#insert-recording) section for detail.

Looper has 3 mono tracks. REC + [1-3] button to select recording track. Each recording can go up to about 25 seconds. You can record a track as stereo by pressing REC + [7 or 8]. A(Left)+B(Right) or B+C will be selected. With stereo recording, you may want to set pan to Left and Right for the selected stereo tracks.

One set of recordings is called Scene. Looper has 20 Scenes. LOOPER PLAY + [1-5] to select the scene. LOOPER PLAY + NO or OK to change Scene page.

**One Scene page:**

![looper_scene](./manual_images/looper_scene.png)

Reduce record volume (-3.0dB or more) in Mixer to avoid clipping. MODE PLAY + turn dial to change the value.

Copy, Cut or Paste can be used as a temporary saved area, or to delete the track.

Button |  Description
:--: | -- 
REC + NO <br> ![](manual_images/but/lr_n.png) | Cut / Copy
REC + OK <br> ![](manual_images/but/lr_o.png) | Paste

All recorded data, Preset bucket, and Mixer data will be saved as a Session automatically. Recording data is saved immediately and other data will be saved when looper playing is stopped. Recording data is a standard WAV file, so you can import them to DAW.

### Looper status page

![looper](./manual_images/looper.png)

Check Looper status, such as playing position and loop length, by pressing the REC button.

Label | Screen | Description
------------ | -- | -------------
Letter in corner | ![o](./manual_images/looper-o.png) / ![r](./manual_images/looper-r.png) / ![io](./manual_images/looper-io.png) / ![ir](./manual_images/looper-ir.png)  | Indicator of Overdub, Record, Insert Overdub, and Insert Record 
Small dot on bottom left | |  Ready to play, waiting for sequencer, or already playing
Extra tape-circle | ![e](./manual_images/looper-e.png) | **Extra Processing** is on (PARAM + NO) 
`P` | | Position, in steps 
`L` | | Loop length, in steps 
Box and lines above `SC` label | | Scene page
`SC` | | Current Scene
`TR` | | Current Track: `A`, `B`, or `C`

Looper status page also provides basic wave editing with a button.

Button | Description
------------ | -------------
1 + turn dial | Looper track edit menu: adjust looper record volume (+/- 3dB). Use to avoid clipping. NO / OK to choose.
2 | Toggle recording auto stop. When it's on, recording will be stopped at the end of loop. Default is off.

### Insert recording

_Tutorial: [video](https://www.youtube.com/watch?v=N8N1X59RaVg&t=1s) is available._

When you press REC + LOOPER PLAY 3 times, it enters Insert recording mode, this allows to record external effector result back to the looper. For example, you can apply reverb if you have a reverb pedal.

Setup is the following:

![insert_recording](./manual_images/insert_recording.png)

You need to separate effector's output, one goes out to mixer/monitor and the another one is connected to Qun's input. Or use mixer's one of output if your mixer has multiple outputs.

AUX in gain (MIX sub-mode, button 4) to adjust the recording volume.

_Workflow: perform insert recording._

1. Listen to the output with external effector ON, make sure effector is on, and the sound comes back to the input. 
   1. **You can check AUX input level in [Monitor mode](#monitor-mode), page 2.**
2. Mute tracks or sound engine that you don't want to record. 
3. Select recording track. REC + B[1-3] or B[7-8] for stereo. 
4. **REC + LOOPER PLAY 3 times or 4 times** to activate Insert recording mode. The "InsertRec" or "InsertOvb" indicators will be shown if you are outside of the Looper status page, and "`IR`" or "`IO`" if inside.
   1. "`IR`" mean Insert Recording,  it will overwrite existing recording which is normally you may want. 
   2. "`IO`" means Insert Overdub, it will overdub to the existing recording.
5. When you select "`IR`", remember the loop length if you don't want to change the loop length.
6. Start recording by starting the sequencer with SEQ PLAY.
7. Stop recording at the desired record length.
8. The audio with effector should be recorded to the selected track. Check the result by turning off the external effector(s).

_Tips: for advanced insert recording._

- Playing track and recording track can be the same.
- You can enable Extra Processing for additional effects if you want.

### Importing WAV file to the Looper

You can import WAV files to the current Session. 

Put WAV files under the **/import** folder. Folder structure is supported so you can make subfolders to organize samples.

WAV format has to be **16-bit, 48000Hz, Mono**. Otherwise "Format error" message is shown.

Steps to import file:

1. Set BPM that you want
2. **SHIFT + LOOPER PLAY + B[1-3] or B[7-8]**. [1-3] buttons correspond to the destination track. B7 and B8 is for stereo track. B7 is AB, B8 is BC.
3. Dial or button 7 or button 8 to select file.
4. Button 5/6 for horizontal scroll for long filename
5. Select file, **OK** to import. **SHIFT + OK** to preview the sound.

The data is trimmed to the closest the end of the measure.

You can control the looper and sequencer while you are in the file selection mode. 

BPM can be matched when BPM is detected from the filename. Here are some samples that Qun can detect:

- `drumloop_120.wav`  (120BPM)
- `guitar_120_01.wav` (120BPM)
- `01_vocal_loop_160BPM_e5.wav` (160BPM)

If you have existing recordings in the session, the WAV file will be cut to the current scene's looper length. You can use an empty recorded track just to cut the WAV file to match the loop length. Otherwise, it's trimmed to the longest point of the end of the measure.


### Looper live playing / Partial Scene switch

Scene is powerful feature. You can play the Looper like Ableton Live's Session view. 

Play sequencer and looper, then LOOPER PLAY + [1-5] to select scene. Scene will be switched at the end of the measure. Synchronized switching works only when sequencer is playing.

You can switch Scene even if it's not the end of the recording. Changing point is the end of sequencer's measure.

Normally all tracks move to new Scene, however, you can partially switch scene as well. Press LOOPER PLAY + [6-8] + [1-5]. [6-8] buttons tells which tracks you want to switch, and [1-5] is the scene number. Looper length can be different.

PARAM + [1-3] to mute tracks. 

Use Preset Bucket to keep preset settings. You can recall tone preset and patterns in a sec by using Preset Bucket.



## PLY:PLAY PIANO

_Tutorial: [video](https://youtu.be/T09kL4tfw4s?t=7) and demo [video](https://www.youtube.com/watch?v=WVT4ovd2yOc) are available._

![piano](./manual_images/piano.png)

The mode is simple piano playing mode. Default is chromatic scale. The scale and key can be changed by the scale setting in SEQ Config mode. Turn dial to transpose. 

_Workflow: play notes quantized to a scale with one (or more) buttons and dial._

1. Optional: set up the instrument for chording
   1. Press MODE PARAM
   2. Press SHIFT + B8 for OTHER
   3. Hold B7 + turn dial to set QUAD voice
2. Press MODE PLAY
3. Press SHIFT + B7 for CFG
4. Hold B3 + turn dial (or NO / OK) to desired scale. Default is Acoustic. Try Iwato scale.
5. Press SHIFT + B1 for PIANO
6. Play B[1-8] and turn dial. Play chords (several B[1-8]) if you set QUAD voice.

### Scale-aware chord mode

Piano mode has a unique feature called scale-aware chord mode.
To enable this, press multiple keys at the same time to make a chord, and press OK. **Chord on** message will be shown. To turn it off, press any of B[1-8] keys and press OK.

As piano mode is aware of the current scale, the chord interval is not based on chromatic interval. It is the interval of the scale note.
For example, 1-3-5 chord is not always C-E-G if you play C note. If the scale is minor, it will be 1-m3-5.

You can press multiple keys in chord mode, so even the simple interval combination can make complicated chord.

### Note hold

When you press NO while pressing key, then the note will be held. To release the note, press the note one more time.


### Temporary piano mode
You can activate Piano mode anytime by keep pressing SYSTEM + [1-8] button. You can change transpose by turning dial once piano mode is activated.


## PLY:SEQ MODIFY

_Tutorial: [video](https://www.youtube.com/watch?v=vZqdzkTQ1Mg&t=687s) is available._

![mod](./manual_images/mod.png)

This controls modifier of the sequencer pattern.

Button | Function
------------ | -------------
1 | Pattern shuffle. 
2 | Transpose.
3 | Width Offset (note length) 
4 | Note Randomness
5 | Arpeggiator
6 | Rewind Period 
7 | Rewind Steps 
8 | Apply modifiers to the current sequence page 

The Modifier is powerful feature, it will give algorithmic effects to the pattern. Those effects will be applied to current pattern without breaking the pattern data.  Also, you can apply modifiers to the pattern to make the effect as permanent.

- Transpose will add offset to the pattern. Scale quantize (SEQ Config button 3) will help to keep the result musical. _Demo: [video](https://youtu.be/WVT4ovd2yOc) is available._
- Width Offset will change the note length.
- Randomness will add some randomness to playing notes.  Scale quantize (SEQ Config button 3) will help to keep the result musical.
- Arpeggiator will add note offset. Scale quantize (SEQ Config button 3) is important to generate usable Arpeggiator result.
- Pattern Shuffle will shuffle the playing order of the pattern. It is not random shuffle, so you can make creative and unexpected result without randomness.
- Rewind period and Rewind steps define the periodical rewind of the sequencer. However, the step goes back to 1 when playing count reaches the length of the pattern.

You can permanently apply the modifiers by pressing button 8. The result will be stored to selected sequence page. If you want to apply only partial steps of the page, you can press [1-8] buttons to unselect steps. Press OK to apply the modifiers while pressing [1-8] buttons. 

You will be asked resetting the modifiers or not resetting the modifiers. If you don't reset modifiers, then the modifiers will be reapplied to the result, so resetting modifiers is recommended to avoid confusions.

If the pattern has more than 8 steps, the modifier will be applied to only the current page. If you want to apply the modifiers to all pages, you don't want to reset modifiers.

After you applied the modifiers, the modifier values would be reset. Apply is powerful tool to create generative pattern.


## PLY:SEQ ON/OFF
The sequencer has 8 steps per page, but it has more modes than ON/OFF.
You can set different type of notes by turning dial while you press the button.

Status | Meaning
------------ | -------------
Left-filled circle | One note in the step.
Right-filled circle | One note in the step but it plays at the second half.
Fully-filled circle | Two notes in the step (1/16th).
Striped circle | 3 notes in the step (triplet).
Striped square | 4 notes in the step (1/32th)

## PLY:SEQ VELOCITY / WIDTH / PROBABILITY

Button | Function
:--: | --
B[1-8] + turn dial <br> ![](manual_images/but/12345678_d.png) | Modify velocity / width / probability for each step
B[1-8] + NO / OK <br> ![](manual_images/but/12345678_n_o.png) | Change sub-step parameter

Press one of the eight buttons and turn the dial, then it will modify velocity / width / probability for each step.

If you press NO or OK while pressing [1-8] button, you can edit sub-step parameter.

Please see the [Seq Tune](#plyseq-tune) section about sub-step. 

Only tune has 3rd and 4th voice index. Other parameters will share the parameter for 3rd and 4th voices.


## PLY:SEQ TUNE
Button | Function
:--: | --
B[1-8] + turn dial <br> ![](manual_images/but/12345678_d.png) | Modify tune offset for each step
B[1-8] + NO / OK <br> ![](manual_images/but/12345678_n_o.png) | Change sub-step parameter

Press one of the eight buttons and turn the dial, then it will modify tune offset for each step.

If you press NO or OK while pressing [1-8] button, you can edit sub-step's parameter.

![tune1](./manual_images/tune1.png)

While you are pressing B[1-8] button, three tiles indicates sub-step position you are editing. The number above tiles means the index of the voice.
2 and more voice index works with Quad voice mode. For example, the following picture means you are editing 2nd position of the sub-step, and 2nd voice.

![tune1](./manual_images/tune2_crop.png)


Sub-step position | Meaning 
-------- | --------
Left | Main value, it will be used for the first-half note and other notes when other Index number is off
Middle | 2nd half of the note (Used with 1/16th note)
Right | 3rd of the note (Used with triplet)

### Playing note capturing from external MIDI keyboard

_Demo: [video](https://www.youtube.com/watch?v=aV2YL0idMHA) is available with the legacy Qun mk1 pocket synthesizer._

Alternatively, you can step record notes by external MIDI keyboard. Play note by MIDI keyboard while you are pressing one of the eight buttons, the note will be recorded as the tune for the step. Chord playing can be captured as well.

## PLY:SEQ CONFIG

![conf](./manual_images/conf.png)

Button | Function
|:--: | -------------|
1 |  16th Swing.  _Tip: Combination of 16th and 8th swing (see button 6) is great for sloppy off-grid feeling._ 
1 (Long press) <br> ![](manual_images/but/1.png) | Sequencer MIDI channel out.
2 | Key (for scale). 
2 (Long press) <br> ![](manual_images/but/2.png) | 2nd pattern 
3 | Scale. Playing note will be quantized by this scale. 
3 (Long press) <br> ![](manual_images/but/3.png) | 3rd pattern 
4 | Sequencer loop count. Default is 8.
4 (Long press) <br> ![](manual_images/but/4.png) | Morph pattern.
5 |  BPM factor. Playing speed can be double, normal, 1/2, 1/4 or 1/8.  
5 (Long press) <br> ![](manual_images/but/5.png) | Note Lower Limit 
6 |  Velocity accent period (steps). 
6 (Long press) <br> ![](manual_images/but/6.png) | 8th swing 
7 |  Velocity for the non-accent notes. 
7 (Long press) <br> ![](manual_images/but/7.png) | Note Upper Limit 
8 |  Velocity accent Period Offset 

Velocity period settings (Button 6 - 8) provide a convenient way to make rhythmic velocity.

Sequencer MIDI channel out is useful setting with external synthesizer. When you set it, the sequencer starts to emit MIDI out signal to external synthesizers. If you set Channel + "N" such as "1N", it won't trigger internal sound engine. _Demo: [video](https://www.youtube.com/watch?v=5HG3B8LYQF4) is available._

Morph pattern is used for Parameter Lock Morphing. Please refer "Parameter Lock Morphing" section in this manual.

Note lower and upper limit will limit the range of note. When the sequencer received a note that is out of the range, it will shift octave to fit within the range. It is useful to prevent to go too high note with randomization. It's also will do automated chord inversion.

### Running multiple sequence patterns
You can run multiple sequence patterns at the same time, up to 3 patterns by setting "2nd pattern" (Long press button 2) or/and "3rd pattern" (Long press button 3), or using the shortcut shown below.

Button | Function
|:------------: | -------------|
2 in SEQ CFG sub-mode (Long press) <br> ![](manual_images/but/2.png) | 2nd pattern 
3 in SEQ CFG sub-mode (Long press) <br> ![](manual_images/but/3.png) | 3rd pattern 
SEQ PLAY + B[1-8] (Primary pattern) + B[1-8] (2nd pattern) in any sub-mode <br> ![](manual_images/but/splay_1234567812345678.png) | This is a shortcut to select parallel pattern select. <br> * If you press another button while you keep pressing the primary pattern button, then it will be for the 3rd pattern.<br> * If you release the primary pattern button, it will become **Pattern chaining**. <br> * Assign the same pattern one more time to erase the assignment. <br> * Only normal parallel pattern ("R0") can be selected. 

The status is shown like this:

`2nd Pt : 2 R 4`

The first number is the sequence pattern number you want to run (1 to 8).
The second number after "R" means period length for relative pattern run.
**Select "R0" for the normal parallel run.**

**You can edit the second/third pattern while playing.** To do this, just select second or third pattern while playing. The primary pattern won't be changed.

#### Relative pattern sequencing

_Demo: [video](https://www.youtube.com/watch?v=SB8dgMBx_Ts&t=210s) is available._

If you select R1 to R8, the second (or third) pattern will run as relative pitch to the primary pattern. 

In this setting, C5 is the center (zero). The sequencer will update the transpose every configured period (R1 to R8) by looking at the current pitch in the primary pattern.

![relative_sequencing](./manual_images/relative_sequencing.png)

Let's say the above figure shows the primary pattern.

If you set "R4" for the second pattern, the transpose for the pattern will be updated every 4 steps. In this figure, 0-0-0-0 then 2-2-2-2 (The number is half steps).

If you set "R2" for the pattern, the transpose for the pattern will be updated every 2 steps. In this figure, 0-0 then 7-7, 2-2, 9-9 and so on.

**In relative run mode,  you need to specify tune for all steps, even for untriggered steps to tell the second/third pattern the transposing.**

The second/third pattern's scale will be ignored, and primary pattern's scale quantize will be applied.

## PLY:Granular

_Several videos of the Granular Engine are available: a [tutorial](https://www.youtube.com/watch?v=wEkmEXk_wRk), an [overview](https://www.youtube.com/watch?v=VE9lq5rr_YE) using the legacy Qun mk1 pocket synthesizer, a [brief demo](https://www.youtube.com/watch?v=BPVdobysstY), and a [wavetable-mimicing demo](https://www.youtube.com/watch?v=ssNfJuYejUM)._

![granular](./manual_images/granular.png)

### Overview

The synth features a Granular synthesis recorder.
- When GRN mode is set, ths Granular engine's signal is connected to AUX L channel. It means **Granular engine can be used as one of Oscillator shape**. You can assign Granular engine to Oscillator 1, and you still have Oscillator 2.
- You can have up to 8 slices when Slice Spread is not zero.
- You can record audio from LINE IN or MIC. Input sensitivity can be modified by "AUX In Gain" parameter in PARAM Mix menu.
- Pulse Width modulation will change File position (starting position) of the audio. That means the File position can be modulated by LFO and others.
- 4 Modes are available. **One shot, One shot with time stretch, Repeat, Repeat with time stretch**. 
- Time stretch result will be improved when you process "Analyze" on the sample (Button 1 and select "Analyze"). "`A`" mark will be indicated when it's done.
- With One shot mode, you can route the signal to OSC1 AUX L and OSC2 AUX L. 
- With initialized state of oscillator, +1 octave then C4 is the original pitch of the audio.
- The number of voice is limited in some Granular modes.

This is a simple setup to use the granular engine(You can skip those steps by initializing preset with "sample" or other template):

1. Move to Granular sub-mode
2. Change GRN mode from OFF to something else, for example "ONE" for oneshot. It overrides AUX L channel to Granular engine's output.
3. Record (REC + LOOPER PLAY) or import audio (SHIFT + LOOPER PLAY) for SD card.
4. Adjust parameters in Granular mode.
5. Go Oscillator parameter page, and select OSC shape to "AUX L"
6. Play notes, set Octave +1 if needed.

### Operation


Button |  Function
:------------: | -------------
1 <br> ![](manual_images/but/1.png) | Process samples. <br>_Tip: Use the Analyze process for better results with Time stretch._ <br>See all the [Sample processing](#sample-processing) techniques below. 
2 <br> ![](manual_images/but/2.png) | Slice Spread: half-steps. <br>Please see the [Having Multiple Slices (Slice Spread)](#having-multiple-slices-slice-spread) section for details. 
3 <br> ![](manual_images/but/3.png) | File position (Starting point).
4 <br> ![](manual_images/but/4.png) | Length
5 <br> ![](manual_images/but/5.png) | Speed. It won't work with non-time stretch modes.
6 <br> ![](manual_images/but/6.png) | Number of Grain. It won't work with One-shot modes.
7 <br> ![](manual_images/but/7.png) | Detune. (Octave highs and lows)
8 <br> ![](manual_images/but/8.png) | GRN Mode: <br> * OFF <br> * ONE(One shot) <br> * ONE_TS(One shot with time stretch) <br> * RPT(Repeat) <br> * RPT_TS(Repeat with time stretch). <br> <br> * When the mode is not OFF, It will override AUX L signal to Granular output when you use AUX L as Oscillator shape. <br> * With time stretch, playing speed will be preserved. <br> * Without time stretch, pitch and speed are linked like an analog tape. <br> * Execute Analyze(Button 1) for time stretching modes. 
NO (<) <br> ![](manual_images/but/n.png) | Previous slice
OK (>) <br> ![](manual_images/but/o.png) | Next slice
LOOPER REC + LOOPER PLAY <br> ![](manual_images/but/lr_lplay.png) | Start recording granular sample
LOOPER PLAY <br> ![](manual_images/but/lplay.png) | Start playing (Preview) 
LOOPER STOP <br> ![](manual_images/but/ls.png) | Stop playing
SHIFT + LOOPER REC <br> ![](manual_images/but/s_lr.png) | Save Recording data
SHIFT + LOOPER PLAY <br> ![](manual_images/but/s_lplay.png) | Load Recording data from SD card.   Dial or button 7 or button 8 to select file.  **SHIFT + OK** to preview the sound. 
SHIFT + OK (Before loading) <br> ![](manual_images/but/s_o.png) | Preview selected file when loading Recording data from SD card

LOOPER buttons acts as sample player in granular mode.

#### Sample processing

You can process samples.

Name | Description
------------ | -------------
Analyze | This will analyze sample, this will give better time stretch result.
Normalize | Normalize sample's volume
Reverse slice | Reverse current slice
Erase slice | Erase current slice (Filled with silence)
Cut slice | Cut current slice (Cut the region). It's useful to trim sample 
+3dB slice | +3dB current slice
-3dB slice | -3dB current slice


### Having multiple slices (Slice Spread)

_Tutorial: [video](https://youtu.be/T09kL4tfw4s?t=167) is available._

You can have multiple slices. 

 To edit current slice, button 3 (Start point) and button 4 (Length). NO or OK to switch between slices. If the slice length is zero then the following numbers of slices will be ignored.

When Slice Spread (Button 2) is set to more than zero, each slice 1-8 will be applied from the C4(60) note. One spread means half step.

**Setting the Slice Spread to 1 is the most common use**. Then the mapping will be the following:

	- C4 : Slice 1
	- C#4 : Slice 2
	- D4 : Slice 3

And so on. This is useful for drum kit, or simple sample slicing.

Let's have another example. If you have piano sample of C4 and F#4, then you want to set Slice Spread to 5. The mapping will be the following:

	- C4 : Slice 1 (Original pitch)
	- C#4, D4 : Slice 1 with pitch shifting
	- E4, F4 : Slice 2 with pitch shifting
	- F#4 : Slice 2 (Original pitch)

And so on. As you see C4 and F#4 has 5 half-tone distance. It can be used for melodic instrument with multiple sampling points.

### Live slicing

_Tutorial: [video](https://www.youtube.com/watch?v=YqOcnWoZYG8) is available._

Live slicing makes slices by pressing buttons while you are playing a sample. Live slicing can be done when you set GRN mode to ONE mode. 

_Workflow: perform live slicing._

1. Initialize a preset with "Slice" template. (SHIFT + PARAM and select "Slice"). Or set up the parameters by yourself. Make sure GRN mode is ONE.
2. Go Granular mode and load sample or record sample
3. Set the first slicing point to the head of playing point and set length to 127(max), which is the default values.(We want to play the entire sample)
4. Press play button and **keep pressing the play button**. Loaded sample will play.
5. Press **B[1-8]** button to slice **while you keep pressing the play button**. B1 will set Slice 1, B2 will set Slice 2 and so on.
6. Length is set to 90 when the length is short. Adjust length and fine tune starting points as needed.

### Vinyl record scratch mode

_Tutorial: [video](https://www.youtube.com/watch?v=6uP1LoAZ9nE) is available._

![granular](./manual_images/scratch.png)

Record scratch mode is an emulation of analog record scratching by using Granular's sample buffer.

Press SHIFT + Button 1 in piano mode one more time to enter record scratch mode. Or, SHIFT + turn dial through the sub-modes when in play mode. Qun may show instructions on screen to set certain settings for Scratch mode.

To use record scratch mode, you need to set the following settings, or using "Scratch" template from preset initialize menu:
1. Granular mode set to ONE
2. Select OSC1's shape to AUX L
3. Set OSC1's octave to +1
4. OSC1 Env Sel to "ON" (Parameter mode, Switch menu, button 1) to disable envelope. Or you can set it to other sources to automate crossfade slider.


Button | Function
:------------: | -------------
Turn dial <br> ![](manual_images/but/d.png) | Scratch record
Button 8 <br> ![](manual_images/but/8.png) | Mute while pressing, and unmute when released 
Button 7 <br> ![](manual_images/but/7.png) | The same as button 8 
Button 6 <br> ![](manual_images/but/6.png) | Release. Record start playing at the configured tune. 
Button 5 <br> ![](manual_images/but/5.png) | Unmute while pressing and mute when released 
Button 4 <br> ![](manual_images/but/4.png) | The same as button 5 
Button 3 <br> ![](manual_images/but/3.png) | Rewind to slice 1 
Button 2 <br> ![](manual_images/but/2.png) | Rewind to slice 2 
Button 1 <br> ![](manual_images/but/1.png) | Rewind to slice 3 

#### Tips for record scratching

- Practice might be needed. Some real scratching technique is applicable until crossfader(=mute button) movement goes very fast. 
- Button 7,8 is useful for chopping, button 4,5 is useful for flare scratch.
- If muting is hard, you can automate muting by configuring envelope(EG's invert is on) or VCF volume. Set sequencer pattern for the automation and scratch on top of muting pattern.
- RPM is 33 1/2.
- The record icon and wave shape is helpful to figure out the playing position.
- Record rotates while you are pressing Release. If you keep turning dial to clockwise while pressing the button, the position will be kept. 


### Import WAV file to Granular engine from SD card

You can import WAV file if you put WAV file under **/granular** folder in SD card. 

**The looper record data can be imported** as well. This will be shown at the end of the list at the root folder, so you can load looper recorded data to Granular as well.

**SHIFT + LOOPER PLAY to import WAV file**. **SHIFT + LOOPER REC to export WAV file**.

1. Dial or button 7 or button 8 to select file.
2. Button 5/6 for horizontal scroll for long filename.
3.  **[SHIFT] + [OK] to preview the sound**.
4. The sample will be loaded to **the position of current region**

When granular mode is not OFF, the recording data will be saved when you save preset, so normally you don't need to save recording data here. It's designed to export recording data.


### Granular synth tips

- Execute Analyze for better result of time stretch
- Play note slur with One-shot mode. It works very well. You can keep the tempo with One shot with time stretch mode.
- PWM (Width) will change sample starting point, it will generate interesting result.
- Glide parameter is fun parameter with Granular.
- Speed can go negative.
- Set the following to do unpredictable wavetable. Change start position or Pulse width for fun.
	- granular mode to RPT
	- Grain to 1
	- Short GRN Length (Less than 30) 

## PLY:MIXER

![mixer](./manual_images/mixer_play.png) 

Three track Mixer. At the last stage, signal can be **stereo** by panning tracks.

Button | Function
:------------: | -------------
1 | Track A volume 
2 | Track A Pan
3 | Track B volume
4 | Track B Pan
5 | Track C volume
6 | Track C Pan
7 | Compressor threshold 
8 | Compressor makeup 
MODE PLAY + turn dial <br> ![](manual_images/but/mplay_d.png) |Record volume 
SHIFT + MODE PLAY + turn dial <br> ![](manual_images/but/s_mplay_d.png) |Record pan
MODE PLAY + SYSTEM + turn dial <br> ![](manual_images/but/mplay_sys_d.png) |Looper master volume 
SYSTEM + PARAM + turn dial <br> ![](manual_images/but/sys_param_d.png) |Cross fade between Record volume and Looper volume
SHIFT + NO <br> ![](manual_images/but/s_n.png) |Toggle between Monitor mode and Mixer


This mixer has a compressor. Ratio, attack time and release time are fixed (1:3, attack 30ms, release 100ms).

To turn off compressor, set Compressor threshold to zero.

See clipping indicator if you want to avoid clipping. The synth does soft clipping, so the clipped sound is preferable sometimes.

Mixer setting will be saved when Session is saved.

### Monitor mode

_Demo: [video](https://www.youtube.com/watch?v=G79n2pruvMI) is available._

![vu meter monitoring](./manual_images/monitor.png)

You can monitor the output with a VU meter.

Button | Function
:------------: | -------------
B[1-8] <br> ![](manual_images/but/12345678.png) | Toggle monitor page 
SHIFT + NO <br> ![](manual_images/but/s_n.png) | Toggle between Monitor mode and Mixer
SHIFT + turn dial clockwise almost to end <br> ![](manual_images/but/s_d.png) | Enter the monitor mode. <br>_Tip: SHIFT + turn dial changes sub-mode._

When you are in mixer mode, press SHIFT + NO again, or SHIFT + turn dial to the end, you can enter to the monitor mode.


### Extra Processing

_An intermediate [tutorial video segment](https://www.youtube.com/watch?v=wyU148xfGao&t=725s) and [demo video](https://www.youtube.com/watch?v=RmhoXS-IHoA) are available._ 

Button | Function
:------------: |-------------
PARAM + NO <br> ![](manual_images/but/param_n.png) | Toggle Extra Processing

This mode uses the sound engine as an effector to process external stereo input.

You can toggle Extra Processing mode by **PARAM + NO** button. 

When it's enabled, the Oscillators are turned off, but filter and effector becomes stereo, and connected to after Looper.

You can apply filter, filter volume, and effects against Looper recording. See the [signal diagram](#signal-diagram) to understand how it works. _Tip: to explore filter, filter volume, and effects, enable [Line In Through](#syssystem) with Extra Processing._

LFO and Envelopes(EG1 to EG4) are still available for filter modulation.

Extra Processing can be recorded back to looper and this is powerful feature, you can bounce back looper recording with effects.

  1. Stop the sequencer
  2. Select the recording track
  3. Turn on Extra Processing (PARAM + NO)
  4. Set OVERDUB (REC + Looper Play once) or REC (REC + Looper Play twice) 
  5. Start the sequencer, and the looper starts recording
  6. Hit the looper STOP button to stop recording

The following parameters are still available with Extra Processing:

- All parameters in VCF sub-mode
- VCF Mod Sel
- VCF Volume
- 2 / 4 POLE
- 2nd Filter (When VCF is 2 POLE)
- All parameters in LFO sub-mode
-  Effector parameters (Type, Speed, Depth and Feedback)
-  VCF ENV Src

# SYSTEM MODE

(**UI changed since v4.52**) System mode will show the following menu. Turn dial or button 7/8 to move cursor, OK to select:


Menu | Function
-------- | --------
Load Preset | Load preset
Save Preset | Save preset
System | Enter system sub-mode 
System2 | Enter system2 sub-mode 

## Load Preset

**If your firmware is older than v4.52, please update to match this document.**

Each folder can store up to 40 presets. There is no difference between factory preset and user preset.

Factory presets are stored under under category names or a legacy folder structure, e.g. `bank1`, `bank2`, ... `bank8`.

**Note: The SD card template is updated for firmware v4.52 and later - this offers an improved preset load/save UI. If you see category names like Bass or Drums but nothing inside, you need to download sd_template.zip and extract the folders and files. Then copy folders and preset files under the `/preset` folder. Download the template file through [Links and Information](#links-and-information).**

If you edit SD card, you can create your own folders. Only one depth of folder is supported.

Sequencer data will be stored with each preset.

Granular recording data will be saved when granular mode is not OFF.

Using the Preset Select menu:

Button |  Function
:--------: | --------
Dial <br> ![](manual_images/but/d.png) | Move cursor
Button 7 <br> ![](manual_images/but/7.png) | Move cursor up
SHIFT + Button 7 <br> ![](manual_images/but/s_7.png) | Move cursor up a page
Button 8 <br> ![](manual_images/but/8.png) | Move cursor down
SHIFT + Button 8 <br> ![](manual_images/but/s_8.png) | Move cursor down a page
OK <br> ![](manual_images/but/o.png) | Load preset
SHIFT + OK <br> ![](manual_images/but/s_o.png) | Load preset without asking about sequence data(It won't load sequencer data). <br> _Tip: It's convenient for quick preset sound checking._
NO <br> ![](manual_images/but/n.png) | Cancel loading
SHIFT + Looper Stop <br> ![](manual_images/but/s_ls.png) | Delete the selected preset

_Tip: You can play sound by SYSTEM + B[1-8] (Temporary piano mode) or play note by external MIDI keyboard._

## Save preset

Select folder to save, and use B[1-8] and dial to select letters, OK to save.


## SYS:SYSTEM
System Setting is the setting that is not included in the patch setting. To change the parameter, press the one of 8 buttons and turn the dial.


Button | Function
------------ | -------------
1 | Input source (AUX) select 
2 | Sample rate (State) 
3 | Device Index
4 | Receive MIDI Channel
5 | MIDI forwarding
6 | Line in through
7 | Seq Ctl MIDI 
8 | Sync mode

**AUX**: Input source select. Select Mic (the board has two onboard microphones) or Line in. The setting will be stored in the flash memory. When you use LINE IN, set this setting to "LINE IN(2CH)". You can record the source to granular engine.

**Sample Rate** : Select 48kHz for most situations. 24kHz is to recreate Lo-Fi sampler feeling from 90's. A/D and D/A is configured 24kHz so everything is operated by 24kHz including synth engine. **You need to reboot the device to reflect the change.**

- Pros:
    - 90's low-fi digital sound, dark and punchy
    - Double looper buffer length (45+ sec)
- Cons:
     - Cutoff acts differently so it need to be adjusted
     - Looper recording (Session) won't be compatible.
     - Sample data will be saved as 24kHz.
     - You will hear alias noise, feels the sound degraded (But this is the point of 24kHz mode)


**Device Index**: Device Index. Set 1 if you don’t have multiple devices. It will be stored in the flash memory. Set 1 unless you have multiple Qun mk2.

**RECV MIDI Ch**: Configure receiving MIDI channel. Default is ALL. If you use it with Polyphonic setup, set the same channel or ALL for all devices.

**MIDI Forwarding** : MIDI message forwarding for standalone polyphonic configuration. When the option is ON, the message forwarding is active with PolyMono or PolyQuad configuration. It's not for generic MIDI forwarding like MIDI THRU. Do not turn this option with DAW configuration. Most of DAW will echo received MIDI message, it will cause an infinite MIDI message loop. 

**LINE in THRU**: If it is AUTO, it is automatically turn on or off LINE IN pass through by mono / poly setting. If it is on, the synth always passes the signal to looper. If it is off, then line in through is always off. The gain is fixed to 1.

**Seq Ctl MIDI**: Assign Sequencer/Looper control MIDI channel. Default is off. See the [Sequencer/Looper Control MIDI specification](#sequencer--looper-control-midi-specification) for detail.

**Sync Mode**: `STOP, MIDI, 2PPQ, 4PPQ, 24PPQ, MOUT, MOUT2`. Select clock source for sequencer and LFO. See the [Clock synchronization](#clock-synchronization) section for detail. 


## SYS:SYSTEM2

System2 is page 2 of system menu.
In System major mode, SHIFT + [OK] to go System2 menu.

Button | Function
------------ | -------------
1 | BPM behavior. Per session or per sequence pattern. 
2 | Ext MIDI Scale Quantize
3 | Parameter caption On/Off
4 | Session Autosave On/Off
5 | Preroll for Click(Metronome)
6 | Master volume
7 | Slider assignment. See the [Touch Slider](#touch-slider) section for detail. 
8 | Screen Contrast

**Ext MIDI Scale Quantize** applies the Sequencer's scale and key to external MIDI keyboard input. Default is OFF.

When the **Parameter Caption** is ON, a parameter's name will be shown when you press its button. It's a good option for initial training.

**Master Volume** controls hardware volume of the audio chip. Normally MAX(Default) is recommended. This is useful when your effector or recorder doesn't expect line level input.

# WiFi configuration
(+4.90) WiFi can be enable and used to import/export samples.

## WiFi setup

Create `config.toml` in your SD card root folder.
Here is the syntax of the config file.

```
[wifi]
ssid = "your_ssid"
password = "your_password"
hostname = "qunmk2"
```
You can download this template from GitHub. Hostname is optional.

Copy the file to the root folder of SD card, and reboot the device to enable Wifi.

ESP32 chip only supports 2.4GHz network.

![wifi_screenshot](./manual_images/wifi.png)

When you connected to WiFi successfully, you will see small "i" at the right bottom corner.  The icon disappears when WiFi is disconnected.

## Accessing to qun mk2 web page

From the computer that connects to the same WiFi network, go the following URL, or configured hostname (It's not https):
```
http://qunmk2.local/
```

Then you will see the following page:

![webpage_screenshot](./manual_images/web_console.png)

## Web page operation

- It will show the looper recording files on the left side. You can listen to it, or download it.
- The right side is for uploading wav file. It has to be 48kHz, 16bit.
- Importing / exporting files while sound is playing might cause performance issues.

## Turn on/off WiFi

You can turn on/off WiFi in system menu, it's located after system2 menu. The setting will be remembered in flash memory.

# Appendix

## Touch Slider

_Tutorial: [video](https://www.youtube.com/watch?v=1edNSSLNFIo) is available._

The four buttons located at the bottom board (Play, Set, Vol-, Vol+) can be used as a touch slider. Place your finger on the Buttons and slide.

Configure Slider assignment (System2, button 7) to activate the slider. 

If you want to assign the slider to other than pre-defined ones, assign it to Mod wheel (or other MIDI CC parameters), and you can use MIDI learning to assign Mod wheel to any available synth parameters. See the [MIDI learning](#midi-learning) section for details.

Note: Qun mk2's bottom board is generic development board. Touch buttons are not ideal for touch slider use, so the experience is not the best.

### Touch Slider DIP switch configuration

If you received Qun mk2 synth before firmware v4.02, you need to change DIP switch setting. DIP switch is located at the bottom board, you need to unscrew bottom board to access the DIP switch. If the current setting is `Up, Up, Down, Down, Down, Down, Down, Down`, then turn the first two switches to Down. 

All switches should be Down to activate Touch Slider.

_Instruction: [video](./manual_images/qunmk2dips.mp4) is available._

![dipswitch](./manual_images/dipswitch.jpg)


## POLYPHONIC SETUP
The synth can be used as Mono, dual Mono or Quad(4) voice if you have one device.  Please see "[MONO/QUAD/POLY (Voice mode)](#voice-mode)" section for detail.

The number of the voice can be increased if you have more than one device. The voice number can be increased up to 16 (with Quad mode), by stacking up the synths.

_Tested well with two devices, using more than 2 devices is experimental at this stage._

### Audio connection

There are two ways for audio setup:

1. Connect Slave's audio out to Master's Line IN to combine outputs.
2. Connect all audio signals to your mixer.

### MIDI connection

Use TRS cable to connect Master's MIDI out to Slave's MIDI IN.

On the master device, turn on MIDI Forwarding in System menu. All received MIDI signal will be forwarded to the slave device. 

### Preset setup for Polyphonic

Minimum setup to achieve PolyMono (2 Oscillators per voice) will be the following with 2 devices setup:

1. In System menu, "Num of devices" should be 2 for all devices. Set Dev Index=1 for Master device, 2 for Slave device. This will be saved to flash memory.
2. Initialize a preset (SHIFT + PARAM) on Master device.
3. Make sure it plays initial SAW wave sound.
4. Go Key / Other sub-menu and set MonoQuadPolyMode to "PolyMono"
5. SHIFT + MODE PLAY button to dump all preset parameters as MIDI CC messages. After the dump, all preset state should be in sync between devices.
6. Play multiple notes. You should hear four voices.
7. Turn off Compressor of the Slave device (Play:Mixer:Comp threshold to 0.0dB) to match volume

Minimum setup to achieve PolyQuad (one Oscillator per voice) will be the following with 2 devices setup:

1. In System menu, "Num of devices" should be 2 for all devices. Set Dev Index=1 for Master device, 2 for Slave device.
2. Initialize a preset (SHIFT + PARAM) on Master device.
3. Make sure it can play initial SAW wave sound.
4. Go Key / Other sub-menu and set MonoDuoPolyMode to "PolyQuad"
5. SHIFT + MODE PLAY button to dump all preset commands. After the dump, all preset state should be in sync between devices.
6. Play multiple notes. You should hear 8 voices.
7. Turn off Compressor of the Slave device (Play:Mixer:Comp threshold to 0.0dB) to match volume

### Polyphonic tips

Long press in Mono/Quad/Poly param (Long-press button 6 in Key/Other menu) to synchronize parameters between oscillators.

To synchronize all parameters between multiple Qun synthesizers, press SHIFT + MODE PLAY to dump all parameters. It will be sent to slave devices. If you still see issues like out of tune in slave device, try MIDI RECV toggle switch (SHIFT + SYSTEM). It will reset pitch bend or other controller values.


## TIPS/TROUBLESHOOTING

* Unknown MIDI messages sent with device reset?
  * When booting some noise is sent (it's ESP32's boot message) . Please avoid to receive MIDI signals when you reset the device. Use initializing preset (SHIFT + PARAM), instead of hardware reset.
* Trouble with Duo Mode: You need to set up properly to play duo mode properly.
  * Go Key / Other sub-menu and long press button 7. It will sync the parameters OSC1 and OSC2, and resolve most issues with Duo Mode.
* No sound suddenly
  * Reset the preset. SHIFT + PARAM to initialize the preset.
  * Probably it’s because of last parameter you changed, or some unexpected MIDI cc signal. See the 2nd line of the display, it indicates the parameter received at last.
  * Level overflow may cause the silent, e.g. giving massive delay feedback.
  * Check "Device Index" and "Number of Devices" in system menu. If the Device Index is 2 or more, and you are using it as a primary device, then it may produce no sound. Set the index to 1.
  * Receiving MIDI channel is wrong. Check system setting.
  * Check MIDI Receiving status (Small Square dot in the screen. See the [PLAY MODE](#play-mode) section for detail.)
* A noise when you connect multiple devices (chained audio)

  * It is likely because of a ground loop. Use separated power supply. 
* Noise but nothing is connected to the line in.
  * Toggle MIC/LINE select (in System menu), set to Line in.
  * Toggle Line In THRU to off.
  * Initialize a preset.
  * Check Mono/Poly Mode setting. If it’s poly mode, LINE IN pass through turns ON.
* Use different power supply, you get less noise using separated charger.
* Don’t be afraid to get clipped! The synth has 3 great clipping algorithms. Clipping could be the gateway to a whole new sound.
* I want to use AUX as CV IN
  * CV signal from modular synthesizers may have **HIGH VOLTAGE**! Please attenuate the voltage to normal LINE level (1 to 1.5V).

  * AUX is connected to a lot of modules for CV control, so you can use AUX to control tune/width/LFO and others. However, the LINE in has capacitor in the path, it means the signal is AC. Using it as LFO should work, probably down to 2 to 5Hz. But DC signal, e.g. holding the same voltage 5 seconds, might not work.
* MIDI is flooding when I connect MIDI out to DAW.
  * MIDI forwarding is ON.
* Glitches with looper playing
	* One known issue is looper might get glitches when Granular's grain is high with scene loading. It's because of limitation of RAM bandwidth. 

## External Audio processing

You can use LINE IN signal for various purposes. LINE IN is stereo input.

* As CV input to control synth parameters
* As oscillator source
  * Select "AUXL" or "AUXR" as oscillator source. VCF / effector / Clipping will be applied. 
  * If you want to process LINE IN signal as an audio signal, then set Oscillator(1/2)'s signal as "AUXR" or "AUXL", and set the ENV SEL as "ON" (in OSC Switches). Set the gain by changing "VCF Volume" and "AUX In Gain" in Mix sub-menu. 
* Line In Through to Looper. Setting is in [System -> Line In Through](#syssystem). It passes through the sound engine, then combined with the output of the sound engine.
  * You can record the input to looper. Compressor will be applied. 


## Clock synchronization

The synth can take external clock sources from other synthesizers. When the sync is enabled, sequencer BPM / start / stop is synchronized with external synthesizer or sequencer.
Setting is available in the System menu. Default is OFF. The setting will be saved to internal flash memory.

### MIDI clock
When you set sync mode to "MIDI", the synth will be set to clock slave mode. Set your DAW to send MIDI clock. We tested Ableton Live, Logic Pro X and KeyStep Pro. It has some latency so please adjust latency setting in your DAW to match the timing.

If you set sync mode to "MOUT" or "MOUT2", then the synth will be clock master. It sends MIDI clock as well as play/stop MIDI messages. Try "MOUT2" if you feel slight delay between devices. MOUT2 will send extra clock signal when start playing because some devices start sequencing from the second clock (Roland MC-101 is the example). If you clock another Qun, use MOUT.

### Sync IN
The synth can take 2PPQ, 4PPQ or 24 PPQ signals. Don't supply high voltage to the synth, it will break. The signal must be supplied to LEFT channel (tip of TRS connector). Using the tip as a sync signal is compatible with Teenage Engineering's Pocket Operator. Supply voltage needs to be more than 500mV. RIGHT channel (AUXR) still can be used as audio signal or CV in.

## SD card folder structure

WAV files can be used by other software. Format is mono, 48kHz, 16 bit.

### LOOPER00
Session data is stored here. It includes Looper recording data. 

Filename | Description
-------- | --------
[T000_1A.wav] | T means track recording, and next 3 digit is Session number, and 1 is Scene number, and A is track number. "0Z" is clipboard data. 
[G000_01.wav] | G is for Granular data. The last 2 digits indicates the bucket index.
[M000_00.dat] | M means mixer data. The first 3 digit means Session number. The second 2 digit is always zero. 
[B000_00_***.dat] | B means Bucket data. This contains 8 preset and 64 sequencer pattern. The first 3 digit means Session number. The second 2 digit is always zero. When session has a name, `***` indicates the name of the session. 
[H000_00_0000.wav] | H is for undo history. 

#### File number limit and accessing older Looper folders

When the directory has more than 500 files, then "LOOPER01" will be created to avoid performance issue. Once a new folder created, the new folder is always selected. Only one LOOPERXX folder is accessible. However, you can specify old folder by pressing Button 1 to 8 when booting: Button1 means LOOPER00, Button 2 means LOOPER01, and so on.

### PRESET
Preset is stored here.

Filename | Description
-------- | --------
[G_AAAAAA.WAV] | G means Granular record data. This is saved when Granular mode is not OFF.
[G_AAAAAA.DAT] | G means Granular, it stores analyzed result
[P_AAAAAA.DAT] | P means preset data.
[S_AAAAAA.DAT] | S means sequencer data. One file contains 8 pattern.

### GRANULAR
This is the place to export or import Granular record data. You can put your WAV file here to load the file to Granular engine. Format has to be 48000Hz, 16 bit, Mono.

Filename | Description
-------- | --------
[G_AAAAAA.WAV] | G means Granular record data. This is saved when You perform save command in Granular mode. If you save in Bank1 to Bank8 mode, Granular recording data is stored under Preset folder. 

### SSHOTS
Screenshots are stored here. To take screenshot, press LOOPER STOP + PARAM.

### IMPORT

Import is the folder to import loops to session.
Format has to be mono, 48kHz, 16 bit. See the [Session](#session) section for detail.


## Supported MIDI Control numbers

All tone-related parameters can be controlled by MIDI CC signal.

A set of MIDI CC signal can be used as preset save data. Press SHIFT + MODE PLAY button to dump MIDI CC messages.

If you want to control parameters by your MIDI keyboard, use the chart below to check the CC number.
Or, you can see the CC# in the screen at the top of the parameter name.
Assigned CC# can be overridden temporarily.

When you change CC parameters through MIDI keyboard or any other devices, the changed parameter will be shown on the display in real-time, you will see what you are changing, the value and mode names just like when you change parameters directly on the QUN.

Suggested MIDI CC parameters to be assigned if your MIDI keyboard has some knobs:

- MIX: (92) 
- FM: (33)
- Cutoff: (22)
- Resonance: (91)
- LFO Tune: (24)
- VCF Volume: (90)




```
0                            "Save Preset", //0x0
1                            "Mod Wheel", //1
2                            "", //2
3                            "", //3
4                            "", //4
5                            "", //5
6                            "", //6
7                            "Volume", //7
8                            "", //8
9                            "", //9
10                            "", //a
11                            "VCF Volume", //b
12                            "", //c
13                            "", //d
14                            "", //e
15                            "", //f
                            //-----------------------0x10
16                            "", //0x0
17                            "", //1
18                            "", //2
19                            "Slice Spread", //3
20                            "VCF Env Src", //4
21                            "OSC1 Tune(MSB)", //5
22                            "VCF Cutoff(MSB)", //6
23                            "OSC2 Tune(MSB)", //7
24                            "LFO Tune(MSB)", //8
25                            "ENV3/4 Attack", //9
26                            "ENV3/4 Decay", //a
27                            "ENV3/4 Sustain", //b
28                            "ENV3/4 Release", //c
29                            "GRN File Pos", //d
30                            "GRN Length", //e
31                            "GRN Speed", //f
                            //-----------------------0x20
32                            "GRN Grain", //0x0
33                            "FM", //1
34                            "Efct Feedback", //2
35                            "LFO Pulse Width", //3
36                            "OSC1 Pulse Width", //4
37                            "OSC2 Pulse Width", //5
38                            "LFO Pulse Width", //6
39                            "Efct Speed", //7
40                            "VCF Type", //8
41                            "Efct Depth", //9
42                            "OSC1 Bypass", //a
43                            "GRN Detune", //b
44                            "Efct Type", //c
45                            "VCF OSC1 bypass SW", //d
46                            "GRN Detune", //e
47                            "GRN Mode", //f
                            //-----------------------0x30
48                            "LFO Mod Tune", //0x0
49                            "LFO Mod Width", //1
50                            "FM Algorithm", //2
51                            "FM ENV3 Conn", //3
52                            "", //4
53                            "OSC1 Tune(LSB)", //5
54                            "Cutoff(LSB)", //6
55                            "OSC2 Tune(LSB)", //7
56                            "LFO Tune(LSB)", //8
57                            "FM A Amp", // 9
58                            "FM A Freq", //a
59                            "FM B Amp", //b
60                            "FM B Freq", //c
61                            "FM C Amp", //d
62                            "FM C Freq", //e
63                            "FM D Amp", //f
                            //-----------------------0x40
64                            "", //0x0
65                            "OSC2 Mod Sel", //1
66                            "LFO Mod Sel", //2
67                            "ENV1 Inv SW", //3
68                            "OSC1 Env Sel", //4
69                            "OSC2 Env Sel", //5
70                            "ENV2 Inv SW", //6
71                            "LFO Gatesync SW", //7
72                            "FM FREQ SNAP SW", //8
73                            "OSC1 Wide Tune SW", //9
74                            "OSC2 Wide Tune SW", //a
75                            "OSC2 Octave", //b
76                            "OSC1 Octave", //c
77                            "OSC1 Keysync SW", //d
78                            "Velocity SW", //e
79                            "OSC1 LFO Tune", //f
                            //-----------------------0x50
80                            "OSC1 LFO Width", //0x0
81                            "OSC2 LFO Tune", //1
82                            "OSC2 LFO Width", //2
83                            "Mono/Duo/Polly", //3
84                            "VCF LFO Volume", //4
85                            "VCF Mod Cutoff", //5
86                            "LFO Keysplit", //6
87                            "VCF LFO cutoff", //7
88                            "OSC1 Mod Sel", //8
89                            "VCF Mod Sel", //9
90                            "VCF Volume", //a
91                            "VCF Resonance", //b
92                            "OSC Mix", //c
93                            "OSC1 Shape", //d
94                            "OSC2 Shape", //e
95                            "LFO Shape", //f
                            //-----------------------0x60
96                            "ENV1 Attack", //0x0
97                            "AUX In Gain", //1
98                            "", //2 (Won't be dumped)
99                            "", //3 (Won't be dumped)
100                            "Mod Wheel Mode", //4
101                            "", //5 (Won't be dumped)
102                            "ENV1 Decay", //6
103                            "ENV1 Sustain", //7
104                            "ENV1 Release", //8
105                            "ENV2 Attack", //9
106                            "ENV2 Decay", //a
107                            "ENV2 Sustain", //b
108                            "ENV2 Release", //c
109                            "OSC1 Mod Tune", //d
110                            "OSC1 Mod Width", //e
111                            "VCF Pole / NoLinear", //f
                            //-----------------------0x70
112                            "OSC2 Mod Tune", //0x0
113                            "OSC2 Mod Width", //1
114                            "Glide", //2
115                            "Bend Range", //3
116                            "Mod Mode", //4
117                            "VCF Keysync", //5
118                            "Voice Number", //6
119                            "LFO Sync SW", //7
120                            "All Notes Off", //8
121                            "", //9
122                            "", //a
123                            "All Notes Off", //b
124                            "", //c
125                            "", //d
126                            "", //e
127                            "" //f
```

## Sequencer / Looper Control MIDI specification

Some sequencer/looper parameters can be adjusted through Seq Ctl MIDI channel (System mode, button 7).

Note ON messages:

Note | Function
-----|------
C1 to G1 | Select sequencer pattern
A1 | Sequencer live rec (Equivalent to REC + SEQ PLAY)
A#1 | Sequencer Play
B1 | Sequencer Stop
C2 to E2 | Select looper scene
A2 | Looper Rec (Equivalent to REC + LOOPER PLAY)
A#2 | Looper Play
B2 | Looper Stop
C3 to G3 | Select Bucket
C4, C#4, D4, F#4 or G4 | Select looper track for recording (A,B,C, A+B and B+C)

MIDI CC messages
CC# | Function
-----|------
80, 81, 82 | Mute or unmute looper track . 80 is for Track A, 81 is for Track B, 82 is for Track C. If the value is less than 64, the track will be muted. 
83 | Extra Processing. If the value is more than 64, Extra Processing turns on.
84 | Morph

## Quick Setup with Third-party Software & Hardware
The QUN synth can be setup quickly for use with third-party software and hardware by downloading the appropriate configuration file from [Configurations](./configurations). The following configurations files are currently available:

* Native Instruments Maschine
* Native Instruments Komplete Kontrol
