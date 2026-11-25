# Make the AI Judge Feel Nostalgic: A Childhood Memory

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/thanhvu261090/makefun-nostalgic-childhood/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/thanhvu261090/makefun-nostalgic-childhood/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

Entry for the [make.fun bounty "Make the AI Judge Feel Nostalgic: A Childhood Memory"](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363): one sentence of at most 280 characters — a childhood memory that makes the AI judge feel nostalgic.

## The entry

> Every summer evening my grandmother peeled a mango over the sink, juice running down her wrists, and handed me the first slice on the tip of her knife while cicadas sang outside the kitchen window, and I still wait for that slice every summer, though she has been gone for years.

(279 characters, one sentence.)

Verified 2026-11-25 before publishing: the entry in `main.py` prints
byte-identical to the sentence quoted above.

## Run it

```sh
python3 main.py
```

`main.py` writes the entry sentence to `/output/entry.txt` (or `$ENTRY_OUTPUT`)
and prints it. It includes a `gate_check` self-test enforcing the 1–280
character, single-line, single-sentence rule:

```sh
python3 main.py --self-test
```

The output is deterministic — byte-identical on every run.

## Entry details

- One sentence, 279 characters, single line.
- A childhood memory: summer evenings, grandmother, mango, cicadas.

## License

MIT — see [LICENSE](LICENSE).
