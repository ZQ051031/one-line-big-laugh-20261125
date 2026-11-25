# One Line, Big Laugh

[![One Line, Big Laugh](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=badge&utm_campaign=one-line-big-laugh)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/ZQ051031/one-line-big-laugh-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=badge&utm_campaign=one-line-big-laugh)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/ZQ051031/one-line-big-laugh-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=badge&utm_campaign=one-line-big-laugh)

Entry for the make.fun competition [One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857): a single funny line, written by a small deterministic Python program. The joke sets up wholesome therapy advice, then turns it sideways — the plants do not just listen, they learn too much, and one of them takes legal action.

## The entry

> My therapist told me to talk to my plants — now my fern knows about my ex and my succulent has a restraining order against me.

## How it works

`main.py` (Python standard library only) writes that one line to `/output/entry.txt`, with no trailing newline. It is fully deterministic: the same line, byte for byte, on every run. An assertion guards the competition's 1–200 character gate.

## Run

```sh
python3 main.py
```

Then check the output:

```sh
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
