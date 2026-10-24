# Twelve briefs. Twelve first takes.

Real local ACE-Step 1.5 turbo performances: one fixed seed per brief, no artistic retries. The complete set is retained for evaluation. Musical ratings remain pending.

**24:30 of music · 7:08 batch wall time · 5:41 engine subprocess time** on an M5 Pro with 48 GB unified memory. Listening copies are 192 kbps MP3, 48 kHz stereo; target -16 LUFS ±0.5 LU and ≤ -1.5 dBTP. These are recorded results from one run, not a performance guarantee.

[Play all](listen_all.m3u) · [Technical measurements and hashes](manifest.json) · [Blank listening ratings](ratings.csv)

| # | Listen | Request | Seed |
| --- | --- | --- | --- |
| 1 | [River waking up](audio/01_river_waking_up_bansuri_instrumental.mp3) | 120 s · 78 BPM · 4/4 · instrumental | 1821732005 |
| 2 | [Midnight café](audio/02_midnight_cafe_jazz_sax_instrumental.mp3) | 90 s · 116 BPM · 4/4 · instrumental | 1628324191 |
| 3 | [Rise of the mountain](audio/03_rise_of_the_mountain_cinematic_orchestral_instrumental.mp3) | 120 s · 140 BPM · 4/4 · instrumental | 965746278 |
| 4 | [Lanterns in the rain](audio/04_lanterns_in_the_rain_piano_cello_waltz_instrumental.mp3) | 90 s · 66 BPM · 3/4 · instrumental | 841152641 |
| 5 | [थोड़ी देर और](audio/05_thodi_der_aur_hindi_male_ballad.mp3) | 150 s · 76 BPM · 4/4 · sung | 1905625906 |
| 6 | [बात अधूरी](audio/06_baat_adhuri_hindi_female_ghazal.mp3) | 120 s · 68 BPM · 6/8 · sung | 309512692 |
| 7 | [यहीं कहीं](audio/07_yahin_kahin_duet_hindi_duet.mp3) | 150 s · 88 BPM · 4/4 · sung | 1756718358 |
| 8 | [Run Toward the Light](audio/08_run_toward_the_light_english_male_rock.mp3) | 120 s · 132 BPM · 4/4 · sung | 1561407237 |
| 9 | [My Own Sunrise](audio/09_my_own_sunrise_english_female_soul_pop.mp3) | 120 s · 96 BPM · 4/4 · sung | 619618584 |
| 10 | [आज की रात](audio/10_aaj_ki_raat_hindi_female_party.mp3) | 120 s · 124 BPM · 4/4 · sung | 580143580 |
| 11 | [After the Rain](audio/11_after_the_rain_english_female_edm.mp3) | 150 s · 126 BPM · 4/4 · sung | 220652654 |
| 12 | [अपनी राह](audio/12_apni_raah_rap_hindi_male_rap.mp3) | 120 s · 92 BPM · 4/4 · sung | 1456075399 |

## What is preserved

The saved plans, captions, engine requests, seeds, lyric words and MP3 bytes are unchanged from the original run. Minimal songwriter records preserve the original sheets without private call logs. Per-take technical records omit machine-specific source paths. Native FLACs and private engine logs are not distributed.

Engine: `acestep-v15-turbo`, shift 3.0, eight steps, no 5Hz LM. Actual inference used MPS and the native MLX DiT backend. Each completed engine record reported unchanged checkpoints and no outbound network attempts. Source/weight revisions and decoded measurements are in manifest.json.

## Listening questions

- Does the lead keep its intended role, and does the melody develop and return?
- Are the requested groove, meter and arrangement audible?
- Are Hindi diction and sung phrases clear? Do the duet voices hand off distinctly?
- Does the rap contrast conversational verses with a genuinely sung hook?
- Do the endings feel complete?

Track 4 has about 6.8% quiet duration in the native file (6.5% in the MP3), above the 5% warning level. All twelve decoded correctly at their requested lengths with no full-scale clipping; all copies met the stated loudness/peak targets. Text concerns preserved for listening: #6 long couplet lines, #10 an awkward ढोल phrase, #11 repeated “puddles”.

Technical checks cannot score musical quality. Leave ratings blank until you listen. This fixed-seed diversity showcase does not establish a general shift3 advantage.

Running the showcase prepare/render commands skips these recorded completed takes. Use a new spec ID/output folder for an explicitly chosen future trial; do not clear these statuses to regenerate them.
