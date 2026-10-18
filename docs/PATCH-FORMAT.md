# Patch format (version 1)

One patch = one `.json` file. Plain text, easy to diff, easy to share. Panel values use the printed scale of the Pro-1 (0 to 10, one decimal). Switches use the words printed on the panel.

Control names come from the Behringer PRO-1 Quick Start Guide (controls 1 to 31 and the specifications page). Nothing here is read from the synth: the Pro-1 cannot send or receive programs over MIDI, so a patch is a recipe the user sets by hand.

## Example
```json
{
  "format": "catpro1-patch",
  "version": 1,
  "name": "Init",
  "author": "SpeakingColors",
  "category": "Bass",
  "tags": ["init", "example"],
  "notes": "Starting point: every knob at a neutral value.",
  "license": "CC0-1.0",
  "panel": {
    "oscA": {"freq": 5, "octave": 1, "saw": true, "pulse": false, "pw": 5, "sync": false},
    "oscB": {"freq": 5, "octave": 1, "saw": true, "tri": false, "pulse": false, "pw": 5, "loFreq": false, "kybd": true},
    "mixer": {"oscA": 7, "oscB": 0, "noise": 0},
    "filter": {"cutoff": 6, "resonance": 2, "envAmount": 3, "kybdAmount": 5},
    "filterEnv": {"attack": 0, "decay": 4, "sustain": 3, "release": 2},
    "ampEnv": {"attack": 0, "decay": 4, "sustain": 8, "release": 2},
    "glide": {"rate": 0, "auto": false},
    "lfo": {"freq": 4, "saw": false, "tri": true, "pulse": false},
    "mod": {
      "filterEnv": {"amount": 0, "route": "wheel"},
      "oscB": {"amount": 0, "route": "wheel"},
      "lfo": {"amount": 0, "route": "wheel"},
      "dest": {"oscAFreq": "off", "oscAPw": "off", "oscBFreq": "off", "oscBPw": "off", "filter": "off"}
    },
    "modes": {"poly": false, "retrig": false, "repeat": false, "drone": false, "arp": "off", "seq": "off"},
    "global": {"tune": 5, "volume": 7}
  },
  "cables": [
    {"from": "LFO OUT", "to": "CUTOFF CV"}
  ]
}
```

## Rules
- `format` must be `catpro1-patch`, `version` is `1`.
- `name` (required, max 60 chars), `author`, `category`, `tags`, `notes`, `license` are text. `license` should be CC0-1.0 or CC-BY-4.0 so others may reuse the patch.
- `octave`: 0 to 3. Other knobs: 0 to 10.
- `route` (mod sources): `wheel` or `direct`. `dest` values: `off`, `wheel` or `direct`.
- `arp`: `off`, `up`, `updown`. `seq`: `off`, `seq1`, `seq2`.
- `cables`: patch-bay connections, free text names taken from the rear panel labels (for example `LFO OUT`, `CUTOFF CV`, `OSC CV`, `MOD WH CV`, `GATE/CLK`).
- Unknown extra fields are kept and ignored, so the format can grow.

## Open items
- Exact range of the glide and LFO knobs in panel units should be checked on hardware.
- Sequencer note data (SEQ1 and SEQ2, 64 notes each) is not part of version 1.
