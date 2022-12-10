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
- v3.88
	
	- Now Granular sample data will be saved when the session is saved as G000_00.wav in session folder. You don't need to save the preset to save the granular sample anymore.
	- Bug fix: Granular engine clipping logic was not correct.
	
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