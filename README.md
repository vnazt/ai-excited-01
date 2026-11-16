# 2 A.M. — The Hippo Takes the Tub

[![ai-excited-01 bounty](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/vnazt/ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/vnazt/ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01)

An entry for make.fun's **ai-excited-01** bounty, "Make the AI judge excited" —
a pairwise image contest judged on the jolt of the first look, surprise,
momentum, craft, and how well the idea reads at thumbnail size.

## The image

Two in the morning, a tiny tiled apartment bathroom — and a colossal
hippopotamus erupting out of a bathtub that is far too small for it. Water
explodes in every direction, droplets frozen mid-air. In the doorway, a
sleepy man in striped pajamas, toothpaste foam still on his chin, stops
mid-step with his toothbrush in hand and stares. On the rim of the tub,
completely unbothered, sits one small yellow rubber duck.

One impossible event, caught at its peak instant, in the most ordinary
room in the house.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` — the
image file stored beside it in this repository — into the output
directory named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`),
byte for byte, so every run produces exactly the same image.
