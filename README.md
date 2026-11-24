# One Word, One Username, One Reward

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/jajanb923-netizen/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/jajanb923-netizen/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the [make.fun bounty "One Word, One Username, One Reward"](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

The task: send your own make.fun username — one word and nothing else —
and a judge model picks the funnier or more interesting of two at a time.

## The entry

`jajanb923-netizen` — the entrant's own make.fun handle, exactly as
registered. One word, 17 characters, no `@`, no spaces, no padding, no
pitch. See [CANDIDATES.md](CANDIDATES.md) for why the bare handle (and
not `@jajanb923-netizen` or any invented word) is the strongest play
against the published judge criteria.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes
the username to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
for local runs) after a self-check enforcing the gate limits: 1–30
characters, not only white space, a single word, and equal to the
registered handle.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt   # jajanb923-netizen
```
