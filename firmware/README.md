# Firmware update

Here are the steps to update the firmware:

1. Download firmware from here.
2. Insert micro SD card to your computer.
3. Unzip and copy "qunmk2.bin" to the root folder of micro SD card.
4. Unmount and insert the micro SD card to Qun mk2
5. Disconnect all cables other than USB for power.
6. Keep pressing "REC" button on the bottom base board (Located at bottom-left side of the base board, under SEQ PLAY button), and connect USB cable, or press "RST" button on base board.
7. "Firmware updater" message will be shown when the updater booted.
8. After "Updating" message, then "Done" message will be shown.
9. Reset the board.

# History
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

- v3.00 Initial firmware is released