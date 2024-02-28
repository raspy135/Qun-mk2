# Firmware update

Here are the steps to update the firmware:

1. Download firmware from here.
2. Insert micro SD card to your computer.
3. Unzip and copy "qunmk2.bin" to the root folder of micro SD card.
4. Unmount and insert the micro SD card to Qun mk2
5. Disconnect all cables other than USB for power. **DO NOT USE USB BATTERY WHEN UPGRADING THE FIRMWARE. Underpowered USB battery might break flash memory**
6. Keep pressing "REC" button on the bottom base board (Located at bottom-left side of the base board, under SEQ PLAY button), and connect USB cable, or press "RST" button on base board.
7. "Firmware updater" message will be shown when the updater booted.
8. After "Updating" message, then "Done" message will be shown.
9. Reset the board.

# History
- v4.80
  
  - Bug fix: Sampler/Granular preset can be muted when loading from preset folder. (This introduced v4.78)
  
- v4.79

  - Bug fix: SHIFT + turn dial mode sub-mode change was broken.

- v4.78

  - Better bucket change behavior with Granular/sampler (Faster loading and better muting)
  - Bug fix: Incorrect wav file reading when metadata chunk appears before data chunk

- v4.77

  - Bug fix: Occasional system crashes by turning dial in Looper mode

- v4.76

  - Behavior change: Looper master volume is applied when Wav file preview in file selection (SHIFT + OK) is played. Looper master volume can be changed by PLAY+SYSTEM+Dial, or SYSTEM+PARAM+Dial(For crossfading between the sound engine)
  - Bug fix: Engine initialization issue on Granular engine.
  - New feature: Double-clicking mode button(PLAY or PARAM) + B[1-8], No or OK to change sub mode

- v4.75

  - Bug fix: Proper wav file reading in case there is extra data at the bottom

  - Bug fix: Stereo Rec was broken, when it is a new recording to the Scene

  - 8th swing is back (CFG, long press button 6). 16th and 8th swing can be combined, great for off-grid feeling.

  - Performance improvement (A lot of internal changes)

  - Behavior change: Coast action in scratch mode was removed for more precise scratching.

  - Bug fix: Scratch mode was broken

- v4.74

  - Bug fix: Performance gliches with stereo recording to the looper

- v4.73

  - Slightly better MIDI clock latency

  - Better behavior with receiving external MIDI clock

- v4.72

  - Clearing Parameter Locking supports multiple button press (B[1-8] + PARAM)

  - 9999 depth Almost unlimited undo list is added for looper. REC+PARAM to open the list. H0000_1A_0000.wav is the file for undo history. Select the first item will behave as the original undo feature. You can load any history of any track here. SHIFT + OK to preview the sound.

  - Looper fade in/out length is shortened to 1/4.

  - Bug fix: LFO width was not reflected when Extra processing is on.

  - Bug fix: Granular's repeat (RPT) and repeat timestretch (RPT_TS) mode didn't behave as expected for long time. Now it behaves more like granular.

  - Behavior change: Voice steal disabled when it looks like a drum kit. (Spread >0 and <2)

  - Preset update: DR-606, RX21 (Some gliches removed)

  - Updated cheat sheet (Typo fixed)

- v4.71

  - Now filelist(Preset, granular and import) can support up to 128 files per folder. Navigate with B7, B8 (SHIFT for Page scroll) to access more than the 48th file.

  - Bug fix: Sometimes live PL locking consume 2 slots for 1 parameter.

- v4.70

  - Bug fix: Sequencer status(On/Off) was not updated when real-time parameter lock is recorded.

  - Bug fix: Occasionally PL lock was not restored properly

  - Bug fix: Pattern chain was broken

  - Faster bucket switching 

- v4.69

  - Bug fix: VU meter shows incorrect channels

  - Bug fix: BPM information was not informed to Granular engine when preset is loaded, and BPM mode is pattern.

  - Behavior change: Finer Granular engine's starting point granularity.

  - New feature: All LEDs are on on the even steps when sequencer live recording is on.

  - New feature: Real-time Parameter Lock recording: In sequencer live recording, sound engine parameter change will be recorded as Parameter Lock.

  - New feature: Editing current step: In sequencer live recording, current step can be spedified by B7 + B8. "Edit the current step while Sequencer live recording" section in the manual for detail.

- v4.68

  - Bug fix: Voice steal logic was incorrect.

- v4.67

  - BPM detection logic from filename was improved (When you load WAV files to the Looper)

  - In QUAD voice mode, the oldest voice will be stealed when it receives more than 4 voices.

  - New shortcut: 2nd pattern and 3rd pattern for parallel pattern run can be set by pressing SPLAY + B[1-8] (Primary pattern) + B[1-8] (2nd pattern), if you press another button while you keep pressing the primary pattern button, then it will be for the 3rd pattern. Assign the same pattern one more time to erase the assignment. (If you release the primary pattern, chain pattern shortcut will be activated.)

- v4.66

  - Critical bug fix: Synth might crash when the sample is played before BPM is changed or session is loaded.

- v4.65

  - Sample recording in Granular mode will wait for signal.

- v4.64

  - Looper recording, sequencer live recording and looper track select can be triggered via MIDI. See Sequencer / Looper Control MIDI specification section in the manual for detail.
  - Undo (REC + PARAM) works on stereo tracks as well.

- v4.63

  - Bug fix: Compressor quality was degraded.
  - Preset bug fix: Drum/Snare2 was broken. (Sd_template/preset/Drums/p_snare2.dat)

- v4.62

  - Performance improvement 
  - Sequencer's Tune preview velocity changed to 90

- v4.61

  - Bug fix: Modulation bug fix (Envelope invert was not applied to voice 3,4)
  - Copy Scene added. LPLAY + B[1-5] + Dial. (Just like Pattern copy or Bucket copy)

- v4.60

  - Disable SD card overclocking, I see some SD card doesn't take the option.

- v4.59

  - Performance improvement
  - Experimental: Battery sensing logic improvement

- v4.58

  - Bug fix: Sine wave change caused volume down for normal sine wave.
  - Preset adjustment due to the first item bug fix, recommend to update under /presets/Leads and /presets/Keys folder.

- v4.57

  - Bug fix: VCF mod cutoff was broken (Introduced by v4.56)

- v4.56

  - Performance improvement

  - Scratch mode was broken since v4.55

  - Some modulation routing bug fix

  - Now Sine wave shape takes Width modulation and it works as Wavefolding. When you set width to sine wave, it will be modified, it can be used like fixed wavetable.

    - The preset patches sd_template/preset/Guitars/P_OUTTU2.DAT, sd_template/preset/Guitars/P_OUTTUN.DAT sd_template/preset/Keys/P_EPIAN3.DAT, sd_template/preset/Keys/P_EPIAN4.DAT has been added. The patches uses the new feature.

  - Bug fix: Sometimes unrelated parameter changed when you edit parameters.

    

- v4.55

  - Looper status view is added. To switch looper status, simply press REC.
  - Bug fix: Relative 2nd/3rd pattern was broken since 4.40 (Period was not working properly)

- v4.54

  - Bug fix: Reverse Slice processing was broken.
  - "Slice" initial template is added for multiple slicing point preset. It will setup basic config for sampler and set slice spread to 1 and disable KEYSYNC (1N2N)
  - Live slicing in Granular mode has been added (Only works with "ONE" granular mode)
    1. Initialize preset with "Slice" template. (Shift + PARAM and select "Slice")
    2. Go Granular mode and load sample or record sample
    3. Set the first slicing point to the head of playing point and set length to 127(max), which is the default values.
    4. Press play button and **keep pressing the play button**. Loaded sample will play.
    5. Press B[1-8] button to slice while you keep pressing the play button. B1 will set Slice 1, B2 will set Slice 2 and so on.
    6. Length is set to 90 when the length is short. Fine tune length and starting points.

- v4.53

  - Bug fix: Realtime sequencer recording was broken (introduced at v4.52)

- v4.52

  - Input volume meter is added to granular
  - Improved wave shape indication in granular mode
  - Granular's starting positions resolution increased from 128 to 256 levels.
  - System major mode and preset Loading/Saving UI is updated. Now it's using the same interface as sample loading, preset is categorized by interument type (Like Bass, Drums, Keys..) , not banks. Banks are still available for backward compatibility. It requires to update SD card preset structure. Please download sd_template.zip, expand it on your PC, and copy files and folders under /preset.

  - Bucket name (preset name) indicated when you select the current bucket
  - (Not firmware update) : Factory presets reviewed and revised, added some new presets.

- v4.51

  - Bug fix: Looper overdub didn't work at the first of recording of the track, when you keep recording to the second loop.

  - Tap tempo is added. To do tap tempo, SHIFT + SEQ PLAY, and tap SEQ PLAY 4 or more time while you are pressing SHIFT.

- v4.50

  - 24kHz mode is added. (System, button2, reboot is needed to reflect the change). This brings the following:
    - Benefit:
      - 90's low-fi digital sound
      - Double looper buffer length (45+ sec)
    - Compatibility issues:
      - Cutoff acts differently so it need to be adjusted
      - Looper recording (Session) won't be compatible.
      - You might feel the sound degraded
  - Bug fix: LFO's S&H oscillator won't reset the value when retriggered
  - Bug fix: Scratch initial template was broken
  - Accordion patch in bank7 (accord) was updated. Overwrite P_ACCORD.DAT in sd_template/preset/bank7 or use sd_template.zip to update all of patches.
  - Bug fix: MIDI note stack issue (probably it's solved)

- v4.43
  - In Tune sub-mode, preview the sound when you press B1-8 buttons, or when you selecting sub-steps.

  - Sequencer page won't be reset when you start playing

  - Sequencer sub-step selection is held when you press the same button

  - Better graphic to indicate the current sub-step you are editing.

- v4.42
  - Performance improvement
  - Sample will be loaded to the selected trim beginning position when you load WAV file to granular. It is useful to build drum kit (or collection of one-shot samples) from one-shot WAV files.
  - Erase slice, Cut slice, +3dB slice, -3dB slice are added in granular's processing menu (button1). Reverse is replaced to reverse slice. Trim to head was replaced to Cut slice.
  - Preset can be loaded without exiting menu by pressing SHIFT + OK. You can check the sound by pressing SYSTEM + B1-8 (temp piano mode) or external MIDI keyboard.

- v4.41
  - Now granular's PWM(which affects to starting position) will be quantized by 64th note.
  - "Scratch" initial template is added.
  - File selection improvements:
    - Button 7/8 to scroll (from v4.40), Shift + B7/8 for page scroll
    - Button 5/6 for horizontal scroll to see long filename
    - Folder icon for better visual.
    - Shift + NO to go back root folder

- v4.40(Beta)
  - Bug fix: Sequencer play/stop was broken when it's triggered by Seq MIDI channel.
  - Bug fix: Occasional MIDI note stack (Not 100% validated)
  - Bug fix: Extra process recording clipping fix
  - When you are playing multiple sequence patterns (second or/and third pattern), you can edit second / third pattern while running sequencer. To do this, just select the second or third pattern. In this case primary pattern won't change. If you select unrelated pattern, the primary pattern will be changed as normal operation.
  - You can use button 7 or 8 to scroll cursor when you are in file selection modes such as preset loading or sample loading.
  - Initialize preset has three templates (Blank, sampler, evenslice)
  - Overclocking SD card for the better performance (It might introduce instability?)
  - Deleting highpass filter from Delay(stereo) to reduce load

- v4.38
  - Bug fix: Double click detection

  - 

- v4.37
  - "Seq Ctl MIDI" (System, button 7) is added, it enables to control Sequencer and Looper via MIDI. See "Sequencer / Looper Control MIDI specification" for detail in the manual.
    - Pattern change
    - Bucket change
    - Scene change
    - Seq play/stop
    - Looper play/stop
    - Extra Processing on/off
    - Mute looper track
    - Morph
  - In PARAM mode and with relative mode, the parameter will be unassigned when button is released to reposition the dial.
  - Bank 6 becomes the default system sub mode after boot.
  - Better double click detection

- v4.36
  - Bug Fix: BPM is preserved when preset was loaded

- v4.35
  - Sequencer chain pattern limit is increased up to 32

  - Bug fix: Realtime recording width recorded wrong when BPM factor is not 1

- v4.34
  - Slightly better clipping handling

  - Bug fix: BPM changed to 92 when pattern is cleared

  - Improved scale quantize algorithm, more chance to get full scale only with white keys.

- v4.33
  - Snappier envelope response when attack or release is zero. Set attack/release to 1 or 2 to get the behavior of previous versions.

  - (It's not firmware update) sd_template.zip has been updated

- v4.32
  - Slight performance improvement

- v4.31(Beta)
  - Bug fix : Occasional no-sound issue with Oneshot granular.

- v4.30(Beta)
  - Bug fix: SHIFT + Dial submenu switch was broken.

  - Bug fix: Looper files are not listed in Granular's loading page.

- v4.29(Beta)
  - Better file browsing UI with folders. Now the last visited folder is remembered, and NO button goes parent folder instead of canceling the operation. If you are at the root folder it will cancel the operation.

  - Wav file preview now becomes real preview without loading. Press SHIFT + OK to preview wav file.

  - BPM matching option when wav file imported to looper (SHIFT + LOOPER STOP + B[1-3]). BPM is detected from the filename.

  - Copy bucket can be done by MODE PLAY(RECALL) + B[1-8] + Turn Dial

  - Bug fix: Width modulation (starting point) issues with oneshot granular mode

  - Sequencer width (note length) adjustment range is widened to 105.

- v4.28
  - Performance improvement

  - Bug fix: Occasional no-sound with Granular

- v4.25
  - Bug fix: Sync problem with MIDI and clock. Now it has much better tracking with tempo change and alignment.

  - Some performance improvement

- v4.22
  - Bug fix: Sequencer sometimes pauses when BPM is changed by changing bucket.
  - Alignment improvement with clock synchronization

- v4.21
  - BPM behavior (Per session or per pattern) can be changed in System2, button 1.

- v4.19
  - Metronome volume can be adjusted by REC+SEQ PLAY + Turn dial
  - You can chain pattern by pressing SEQ PLAY + B[1-8], then press B[1-8] while keep pressing SEQ PLAY. Up to 16 patterns can be chained.
  - Performance improvement

- v4.17

  - Some performance improvement

  - Bug fix: Sometimes patch loading stuck with looper play

- v4.15

  - Bug fix : 4NL filter will oscillate when it sets to non-supported type of filters
  - Bug fix: Messages to MIDI channel 1 was always picked up. 

- v4.14

  - You can turn off internal sound engine to set "1N" to "16N" in  Seq MIDI channel (Long press button1 in Seq config menu) 
  - Note Lower limit (Long press button 5 in Seq config) and Note upper limit(Long press button 7 in Seq config) is added. It will limit note range. When the note is out of range, the note will be shifted octave lower or highter to fit the range. It's useful with random modifier, transpose. It will be affected like automated chord inversion.

- v4.13

  - Some priority adjustment for stability
  - Removed 8th swing due for stability

- v4.12

  - Little tuning on scratch engine
  - Behavior change : Now 4NL filter mode uses Stilson code from https://github.com/ddiakopoulos/MoogLadders. It has smoother resonance response.
    Only Low-pass and high-pass filter works. High-pass filter is done by substructing so the result won't be perfect.
  - Behavior change : Granular's Repeat(RPT) mode will use multiple slicing point when the length is more than zero.
  - 8th swing is back, it's at long press button 5 in Seq config.

- v4.11 (Beta)

  - Record scratch mode is added. Press SHIFT + Button 1 one more time in piano mode to enter Record scratch mode. See manual for detail.
  - Behavior change: Envelope invert behavior will be affected to amp src. 
  - Envelope generators (EG1 to EG4) is available in Extra processing mode.
  - Bug fix: Multiple slicing parameter values might have wrong value at initialization.
  - Granular can read stereo track(It will be downmix to mono)
  - Other bug fixes, performance improvements
  - Relative adjustment mode is added. To enable relative mode, double click the corresponding parameter and turn dial in Param mode, or Play modifier, mixer, seq config or granular.

- v4.09

  - Some performance optimizations

  - Record pan is added (SHIFT + PLAY + Turn Dial), you can pan synth engine's output.

  - Monitor mode is added. It's a bit hidden, press SHIFT + No one more time in mixer mode then enter to monitor mode, or SHIFT + turn dial and turn dial to the end in play mode.

- v4.07

  - Bug fix: Extra processed data loopback recording was not great when the signal was clipped.

  - Bug fix: Unwanted pop when LFO's shape Sine or Saw and tune moves suddenly

- v4.06

  - Bug fix: UI bug fix introduced in v4.04 (UI goes old style after saving)

  - Looper was not rewind properly when sequencer is clocked by other sources.

- v4.04 (Beta)

  - Sleep is added. SHIFT + NO + OK to sleep. To restart device, press RST button on the bottom board.
  - Bug fix: Autosave was unintendly performed sometimes even when autosave is off. The bug was introduced at v4.00. 
  - Now you can name session by long pressing SHIFT + REC.
  - Tiny "R" or "O" is indicated at the top left of the screen when you are recording(Record or Overdub) in some modes like Parameter modes or Play Modifier.

- v4.03 (Beta)

  - Filter type 2PNL and 4PNL has more taste and juice.(Subtle change)
  - Bug fix: Behavior with flooded MIDI traffic
  - Bug fix: MIDI NOTE OFF was not working
  - When the voice mode is set to QUAD, OSC2 always used EG2 as Evelope source. But now you can set other sources. It still uses EG2/EG4 when you set it to EG1/EG3.

- v4.02 (Beta)

  - Added touch slider. It needs DIP switch setting change. See Touch Slider section, and Touch Slider DIP switch configuration for detail.

- v4.01 (Beta)

  - Bug fix: Subtle behavior degrade fix

- v4.00 (Beta)

  - Multiple slicing points up to 8 are now supported with Slice Spread
  - Slice Spread (Button2 in granular mode) is added to granular engine, now you can easily slice samples. Please check granular section of the manual for detail.
  - Saving data and Bucket data was updated to support slice spread. Newer version of the firmware can read previous data but older version will not be able to read the data made by v4.00 and later.
  - Number of voice with Oneshot mode increased to 4 with Quad mode (most of cases)
  - Bug fix: Piano mode scale quantize with transpose was wrong.
  - Bug fix: Bug fixes related to granular
  - Some of drum kits were rebuild to use multiple slicing points. It's available in bank6, under sd_template folder, or download sd_template.zip.
  - New Piano mode GUI

- v3.96

  - Bug fix: Detune behavior


  - Number of voice with Oneshot mode increased to 3 with Quad mode.

  - Bug fix: Performance degrade introduced at v3.94

- v3.94

  - Small behavior fix, performance improvements
  - "Trim to head" is added into granular's edit menu
  - Bug fix: The operation explained in Parameter Lock #8 was broken.
    *--Once you changed one parameter, you can change the last edited Locking parameter by pressing [1-8] + [PARAM] + Turning dial without re-selecting the parameter.--*

- v3.93

  - Bug fix: Pop noise with Granular introduced v3.91, including some small improvements.
  - Hide hidden files (The files start with ".") 
  - In granular preview with One shot, the sound play won't be repeated.

- v3.92

  - Small improvement of Time stretching algorithm

  - File index indicator is back (Only for the first line).

  - Bug fix: Sample loading with offset

- v3.91

  - Granular processes (Analyze, Normalize, Reverse) are added (Button1 in Granular mode). Analyze gives much better result with Time stretch (One_TS and Rpt_ts). 

- v3.90

  - Bug fix: Granular engine's playing position at the center of PWM was slightly shifted

- v3.89

  - The number of file in one folder limit extended to 48
  - Now Granular sample data will be saved when the session is saved as G000_00.wav in session folder. You don't need to save the preset to save the granular sample anymore.
  - Bug fix: Granular engine clipping logic was not correct.

- v3.88

  - (Deleted)

- v3.87

  - Bug fix: Clock sync through line in was broken.

- v3.86

  - Bug fix: Preset loading position was shifted when GRN File pos is not zero. 

- v3.85

  - Behavior change: OSC1 Bypass deleted. VCF ENV src is added instead.

- v3.84

  - Bug fix: Real time recording isue with LFO Keysplit
  - Bug fix: Parameter lock is disabled for sub patterns
  - Behavior change: 16th swing becomes default.

- v3.82

  - Bug fix: Relative parallel pattern run calculation
  - Bug fix: With specific conditions, bucket change won't resume LFO properly
  - Mode button won't switch major mode when the button was pressed longer than about 0.5 seconds, to prevent unwanted Major mode change
  - Bug fix: All note off doesn't work sometimes
  - Button response improvement

- v3.80

  - REC mode is supported for the looper. Unlike Overdub, REC will overwrite existing recording, and it also overwrite loop record length if the new recording is longer than the existing recording. To enable REC mode, press REC+Looper Play twice.
  - The sound processed by Extra processing can be recorded back to looper. This can be used as effector, volume adjustment and mixdown.
  - Send and Return was removed to avoid confusion.

- v3.79

  - Even smoother and faster response for VCF Volume, Cutoff and Oscillator Tune (Ocatave, tune and pitch wheel) response

- v3.78

  - MIDI, SD, clipping indicator is always shown regardless the looper status
  - In Play Modify, Config and Mixer mode, sequencer indicator moved to bottom and it has more space.
  - Smoother MIDI CC response for Cutoff and VCF Volume.

- v3.77

  - Master volume is added in system2 menu. It's hardware volume. Normally Max(Default) is recommended. It's useful when your effector or recorder doesn't expect line level input.
  - Change default Rec Volume to -6dB to avoid unintended clipping.

- v3.75

  - Performance improvement

  - When you load sample for granular from SD, the file will be loaded at the beginning of the loop set by File Pos, not the beginning of the buffer.

  - Bug fix: Sequence and Granular wav file were not deleted when preset was deleted.

  - New feature: You can set preroll for Click(Metronome). The setting is avaiable under system2 menu.

  - System: LINE IN THRU parameter has three setting. AUTO(Default), Off and On.

- v3.74

  - New effect: BPM synchronized Digital Delay. It can be used as beat repeat by setting feedback and depth to 100%. Useful with Parameter Locking.

  - Bug fix: Precise value adjustment didn't work in Parameter Locking mode.

  - New shortcut: The last edited Parameter locking parameter can be modified just by pressing [1-8] + PARAM + Turn dial

  - New Feature: Morphing Parameter Locking between two patterns.

- v3.73

  - Slight UI improvement

  - Piano mode can be activated anytime temporary, by keep pressing SYSTEM + 1-8 button. 

  - You can delete preset by pressing SHIFT + STOP (delete) while selecting preset

  - Bug fix / sound engine behavior change : Effect depth was doubled.

- v3.71

  - Some parameter's transition speed is increased for Parameter Lock

- v3.70

  - Performance improvement

  - Bug fix: MDelay was not enabled with Extra processing

  - You can set "OFF" to voice index 0 in Seq tune mode. The note won't be triggered with this setting.

  - New feature: Parameter lock

- v3.65

  - Granular import supports folder structure
  - Small UI improvements
  - You can import sample without exiting file list mode by pressing SHIFT + OK.

- v3.63

  - Bug fix: Looper sample import was broken.
  - Glanular accepts wider PWM range.

- v3.62

  - Metronome sound is now much easier to hear.

  - Bug fix: LFO BPM sync was broken.

  - LFO's BPM sync behaves better, now the phase will be reset when the sequencer rewinds.

  - In LFO mode, PWM can be applied to SAW, REVERSED SAW and SINE wave. It will affect as phase offset.

- v3.61

  - Bug fix : Fix an issue with stereo recording

- v3.60 (Beta)

  - Stereo recording is now supported.  When selecting track, button 7 = Track A(Left)+B(Right), button 8 = Track B+C. You may want to set pan to left and right for the selected stereo tracks.

  - Looper will start and stop with sequencer when external MIDI sequencer is started or stopped in MIDI clock slave mode.

- v3.56

  - Looper volume is added : MODE PLAY + SYSTEM + turn dial

  - Cross fade between Rec Volume and Looper Volume : SYSTEM + PARAM + turn dial

  - Behavior change: Buttons has to be pressed to change parameter in Play mode 

  - Bug fix: Sometime autosave is executed even when autosave setting is off.

- v3.54

  - Bug fix: Some UI issues

- v3.53

  - Bug fix: Delay has an issue with long delay time.

  - Session Autosave can be turned off in System2 menu. SHIFT + Rec to execute manual saving.

- v3.52

  - Small behavior improvement when you long press a button to show the full parameter name.

- V3.51(Beta)

  - Parameter caption mode is added in System2 menu. It's a good option for training.

- v3.50 (Beta)

  - Introducing new UI for the parameter mode
  - Some parameter button assignment changed due to UI change in Parameter mode.
  - Screen contrast adjustment in system2 menu
  - Sequence live recording is added. Rec + Seq play to record. Play with external MIDI keyboard or internal piano mode. See manual for detail.

- v3.46

  - Change compressor's default threshold to 0.0dB (OFF) to avoid clipping.
  - Now you can load looper record data to granular. The recording will be listed at the end of the file list.
  - Slight sound improvement on Sine and FM.

- v3.45

  - UI improvement: Session save can be performaed by S+REC. Pressing Looper stop will save Sesssion as well, but this is a bit easier to guess. "Ses saved" message is added when you press Looper stop.

- v3.44

  - Bug fix: Swing behavior with BPM factor
  - Bug fix: MIDI clock out with parallel pattern play
  - Bug fix: Sending MIDI signal from external keyboard when it SEQ MIDI channel is set.

- v3.42
  - Granular engine's grain cross fade period set shorter when the length is less than 30. It's good when using granular engine as (kind of) wavetable. Set the following value to do unpredictable wavetable:
    - granular mode to RPT
    - Grain to 1
    - Very short GRN Length (Less than 30) 
  - Bug fix: Performance issue with heavy load

- v3.41

  - BPM factor supports 0.125 and 0.25.
  - Ext MIDI scale quantize is added. Setting is available in System2 mode.
  - Bug fix: Note indication in Tune mode
  - New feature: Parallel sequencer pattern running. See "Running multiple sequence patterns" section in the manual for detail.

- v3.34

  - Bug fix : Sequencer page copy can perform by Shift + Seq Play + (YES or NO). Previous method is still working but not recommended.

- v3.33

  - Performance improvement
  - Bug fix: Sequencer behavior with chord
  - Bug fix: Line in channel balance and matching level with polyphonic setup
  - Add an ability to select old LOOPER folder (https://github.com/raspy135/Qun-mk2#looper00) 

- v3.32		
  - Bug fix: Looper playback was mixed between channels, the bug introduced by recent firmware.

- v3.31 (deleted)

- v3.30
  - Effector output is now stereo. Preset was updated to get the benefit of stereo effector, so please download and install preset as well. To download preset, download ../sd_template.zip and expand it, copy them to sd card.
  - MDelay(Mono delay) is added to keep backward compatibility, and use it as a resonator.

- v3.27

  - Number of the recording will be indicated when you are selecting session

- v3.26

  (Deleted)

- v3.25

  - Performance improvement 

- v3.24
  - Added a dialog to confirm initializing tone 

- v3.23
  - Performance improvement

- v3.22
  - Rewind period and Rewind steps modifier are added.
  - When applying the modifier, you can choose resetting or not resetting the modifiers

- v3.21
  - Bug fix: Granular's out of tune issue
  - Now Sequencer tune supports up to 4 voices
  - In Play:Tune, chord play from external MIDI keyboard can be captured
  - Bug fix: Granular's automatic sample loading when bucket is switched (System tries to find a sample when bucket is named,

- v3.20
  - Bug fix: System crush when long sample is imported
  - Better WAV file compatibility (WAV file with JUNK chunk supported) 

- v3.19
  - (Bad firmware, deteled)	 

- v3.18
  - Bug fix: Some modulation sources (OSC2, OSC2EG) were not working properly

- v3.17
  - Performance improvement
  - Longer time to activate long press
  - Softer clipping at the end of the signal

- v3.16
  - Bug fix: Loading scene issue with mixed length of recordings

- v3.15
  - Bug fix: FM (Mix, button 2, FM between Osc1 and Osc2) was not working properly	
  - Bug fix: Note off was sent to MIDI OUT even if the ext sequencer midi channel is off

- v3.14
  - Startup screen added

- v3.13
  - Bug fix:  OSC1 bypass was not working properly
  - Performance improvement

- v3.12
  - Improved processing time when deleting all tracks in the scene,
  - A bug fix with probability for second note
  - Improved clipping noise

- v3.11: Deleted

- v3.10 : Number of voice was doubled, now it supports up to 4 voices. Bit crusher effect added.

- ### v3.00 Initial firmware is released