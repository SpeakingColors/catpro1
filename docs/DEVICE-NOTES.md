# Pro-1: device notes

Sources: Behringer PRO-1 Quick Start Guide (our project files) and the third-party "Behringer Pro-1 Ctrlr panel" documentation v2.3 (2021-11-28, ). The second source is not from Behringer; treat its claims as community knowledge.

## The key limit

Per the Ctrlr panel documentation, the Pro-1 does **not** support:

- loading or saving programs over MIDI, or
- changing program parameters with MIDI CC or NRPN.

It does accept **global settings** through SysEx, and these cannot be read back (write only). The three global settings the panel manages are:

- Note priority
- Pitch bend range (panel default 0x0C, i.e. 12 semitones)
- MIDI clock output (on or off)

So a "controller" plugin that moves the Pro-1's knobs is not possible. Cat Pro-1 is therefore planned as a **patch book**: record the knob positions of a patch (manually or via the on-screen panel), store them with notes, name, category and cable routing, and show them back as a recall sheet. It can also send the global settings and play notes and clock.

## Confirmed from the Quick Start Guide

- Class-compliant USB MIDI device, 5-pin MIDI IN and MIDI OUT/THRU on DIN.
- MIDI channel is chosen with four DIP switches (item 74).
- Eurorack format, 16-voice poly chain, 9 patch cables in the modulation matrix, arpeggiator (up, up/down, off), two sequences.

## SysEx facts seen in the third-party panel docs

- Behringer manufacturer ID 00 20 32, Pro-1 model bytes 00 01 08. A global settings message was shown as `F0 00 20 32 00 01 08 11 ...` (the panel monitor examples).
- The 600-byte "sound data" format in that document is the panel's own storage layout ("nothing official or unofficial from Behringer"), and is not transferred by MIDI.

## Open items

1. Exact global-settings SysEx byte layout (needs the full example messages or a capture).
2. Whether the Pro-1 sends anything useful on its own (panel edits are not transmitted according to the panel docs; verify on hardware).
