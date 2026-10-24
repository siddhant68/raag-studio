# Musical vocabulary

The current app exposes 38 style presets and 56 named instruments. These are prompt/plan choices; their presence in the performance is a listening question.

## Styles

| Style | Family | Voice | Tempo range | Meter | Form |
| --- | --- | --- | --- | --- | --- |
| Hindi acoustic ballad (`hindi_acoustic_ballad`) | hindi_song | sung | 68–84 | 4/4 | pop_song |
| Bollywood romantic (`bollywood_romantic`) | hindi_song | sung | 64–88 | 4/4 | mukhda_antara |
| Bollywood dance number (`bollywood_dance`) | hindi_song | sung | 112–132 | 4/4 | dance_song |
| Retro filmi (`bollywood_retro`) | hindi_song | sung | 84–110 | 4/4 | mukhda_antara |
| Sufi rock (`sufi_rock`) | hindi_song | sung | 80–110 | 4/4 | pop_song |
| Qawwali (`qawwali`) | hindi_song | sung | 84–120 | 4/4 | qawwali |
| Ghazal (`ghazal`) | hindi_song | sung | 60–80 | 4/4 | ghazal |
| Bhajan (`bhajan`) | hindi_song | sung | 70–100 | 4/4 | folk_song |
| Punjabi bhangra pop (`punjabi_bhangra`) | hindi_song | sung | 120–140 | 4/4 | dance_song |
| Hindi indie acoustic (`hindi_indie_acoustic`) | hindi_song | sung | 72–100 | 4/4 | pop_song |
| Hindi rock (`hindi_rock`) | hindi_song | sung | 100–140 | 4/4 | pop_song |
| Hindi pop R&B (`hindi_pop_rnb`) | hindi_song | sung | 70–100 | 4/4 | pop_song |
| Hindi lo-fi (`hindi_lofi`) | hindi_song | sung | 70–90 | 4/4 | pop_song |
| Desi hip-hop (`hindi_hiphop`) | hindi_song | sung | 80–100 | 4/4 | rap_song |
| Rajasthani folk (`rajasthani_folk`) | hindi_song | sung | 90–120 | 4/4 | folk_song |
| Hindustani semi-classical (`semi_classical`) | hindi_song | sung | 60–80 | 4/4 | ghazal |
| Raag: bansuri at dawn (`raag_bansuri`) | indian_instrumental | instrumental | 66–90 | 4/4 | raag |
| Raag: sitar evening (`raag_sitar`) | indian_instrumental | instrumental | 64–92 | 4/4 | raag |
| Indian fusion (`indian_fusion`) | indian_instrumental | instrumental | 84–112 | 4/4 | instrumental_song |
| Indian epic cinematic (`indian_cinematic`) | indian_instrumental | wordless | 80–110 | 4/4 | cinematic |
| Meditation (`meditation`) | indian_instrumental | instrumental | 60–72 | 4/4 | ambient |
| Warm cinematic ensemble (`warm_cinematic_acoustic`) | instrumental | wordless | 76–100 | 4/4 | wordless_song |
| Pop ballad (`pop_ballad`) | english_song | sung | 64–84 | 4/4 | pop_song |
| Acoustic singer-songwriter (`acoustic_pop`) | english_song | sung | 76–108 | 4/4 | pop_song |
| Dance pop (`dance_pop`) | english_song | sung | 112–128 | 4/4 | dance_song |
| Indie folk (`indie_folk`) | english_song | sung | 80–116 | 4/4 | folk_song |
| Country pop (`country_pop`) | english_song | sung | 84–120 | 4/4 | pop_song |
| Rock anthem (`rock_anthem`) | english_song | sung | 100–140 | 4/4 | pop_song |
| Alternative rock (`alt_rock`) | english_song | sung | 96–132 | 4/4 | pop_song |
| R&B / neo-soul (`rnb_soul`) | english_song | sung | 68–96 | 4/4 | pop_song |
| Hip-hop / trap (`hiphop_trap`) | english_song | sung | 70–100 | 4/4 | rap_song |
| EDM / progressive house (`edm_house`) | electronic | sung | 120–130 | 4/4 | edm |
| Synthwave (`synthwave`) | electronic | instrumental | 84–118 | 4/4 | instrumental_song |
| Lo-fi beat (`lofi_hiphop`) | electronic | instrumental | 70–90 | 4/4 | loop_beat |
| Jazz lounge (`jazz_lounge`) | english_song | sung | 70–120 | 4/4 | jazz |
| Cinematic orchestral (`cinematic_orchestral`) | instrumental | instrumental | 64–100 | 4/4 | cinematic |
| Ambient (`ambient`) | instrumental | instrumental | 60–76 | 4/4 | ambient |
| Solo piano (`piano_neoclassical`) | instrumental | instrumental | 60–90 | 4/4 | instrumental_song |

## Instruments

| Instrument | ID | Family | Typical job |
| --- | --- | --- | --- |
| Bansuri | `bansuri` | melodic | answer |
| Tabla | `tabla` | rhythm | rhythm |
| Tanpura | `tanpura` | drone | drone |
| Santoor | `santoor` | melodic | texture |
| Sitar | `sitar` | melodic | texture |
| Ghatam | `ghatam` | rhythm | rhythm |
| Violin | `violin` | melodic | answer |
| Cello | `cello` | melodic | harmony |
| Strings | `strings` | harmony | harmony |
| Piano | `piano` | harmony | harmony |
| Acoustic guitar | `acoustic_guitar` | harmony | harmony |
| Bass | `bass` | bass | harmony |
| Light percussion | `light_percussion` | rhythm | rhythm |
| Choir | `choir` | voices | harmony |
| Harmonium | `harmonium` | harmony | drone |
| Sarangi | `sarangi` | melodic | answer |
| Shehnai | `shehnai` | melodic | answer |
| Sarod | `sarod` | melodic | texture |
| Veena | `veena` | melodic | texture |
| Dholak | `dholak` | rhythm | rhythm |
| Dhol | `dhol` | rhythm | rhythm |
| Mridangam | `mridangam` | rhythm | rhythm |
| Tumbi | `tumbi` | melodic | answer |
| Manjira | `manjira` | rhythm | rhythm |
| Ektara | `ektara` | melodic | drone |
| Handclaps | `handclaps` | rhythm | rhythm |
| Nylon guitar | `nylon_guitar` | harmony | harmony |
| Electric guitar | `electric_guitar` | melodic | harmony |
| Upright bass | `upright_bass` | bass | harmony |
| Drum kit | `drum_kit` | rhythm | rhythm |
| Brushed drums | `brushed_drums` | rhythm | rhythm |
| Cajon | `cajon` | rhythm | rhythm |
| Harp | `harp` | harmony | texture |
| Concert flute | `concert_flute` | melodic | answer |
| Clarinet | `clarinet` | melodic | answer |
| Saxophone | `saxophone` | melodic | answer |
| Trumpet | `trumpet` | melodic | answer |
| Brass section | `brass` | harmony | harmony |
| Organ | `organ` | harmony | harmony |
| Electric piano | `rhodes` | harmony | harmony |
| Ukulele | `ukulele` | harmony | harmony |
| Mandolin | `mandolin` | melodic | answer |
| Accordion | `accordion` | melodic | answer |
| Harmonica | `harmonica` | melodic | answer |
| Bells | `bells` | texture | texture |
| Synth pad | `synth_pad` | texture | texture |
| Synth lead | `synth_lead` | melodic | answer |
| Synth bass | `synth_bass` | bass | harmony |
| 808 bass | `bass_808` | bass | harmony |
| Drum machine | `drum_machine` | rhythm | rhythm |
| Synth arpeggio | `arpeggiator` | texture | texture |
| Oud | `oud` | melodic | answer |
| Duduk | `duduk` | melodic | answer |
| Kalimba | `kalimba` | texture | texture |
| Marimba | `marimba` | texture | texture |
| Taiko | `taiko` | rhythm | rhythm |

## Forms

`pop_song`, `mukhda_antara`, `ghazal`, `qawwali`, `rap_song`, `dance_song`, `edm`, `folk_song`, `jazz`, `raag`, `instrumental_song`, `cinematic`, `ambient`, `loop_beat`, `wordless_song`

Source of truth: `app/genres/presets.json`, `app/backend/instruments.py` and `app/backend/song_blueprint.py`.
