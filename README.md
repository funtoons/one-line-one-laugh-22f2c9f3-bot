# One-Line Laugh Writer

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/funtoons/one-line-one-laugh-22f2c9f3-bot/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/funtoons/one-line-one-laugh-22f2c9f3-bot/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

Entry for the [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one funny line — a single joke about a dog that bills its
owner for emotional labour — to `/output/entry.txt`. That line is the whole
entry: at most 200 characters, landing its laugh on a first read.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Determinism

The program is stdlib-only and fully deterministic: the line is a constant,
with no randomness, no network access, no clock reads and no path-dependent
output. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
