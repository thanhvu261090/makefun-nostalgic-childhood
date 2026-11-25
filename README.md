# Make the AI Judge Feel Nostalgic: A Childhood Memory

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/thanhvu261090/makefun-nostalgic-childhood/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/thanhvu261090/makefun-nostalgic-childhood/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

Entry for the [make.fun bounty "Make the AI Judge Feel Nostalgic: A Childhood Memory"](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363).
The brief is simple: one sentence, at most 280 characters, that brings back
a childhood memory. The house judge reads the lines two at a time and picks
the one that stirs the deeper nostalgia.

## The entry

> Every summer evening my grandmother peeled a mango over the sink, juice running down her wrists, and handed me the first slice on the tip of her knife while cicadas sang outside the kitchen window, and I still wait for that slice every summer, though she has been gone for years.

279 characters, one sentence, one line. The memory is a summer evening in a
grandmother's kitchen: mango juice, a knife-tip first slice, cicadas outside
the window — and the wait for that slice, every summer since.

## How it works

`main.py` (Python 3, standard library only) holds the entry as one fixed
string, validates it against the bounty gates, then prints it byte-for-byte
to stdout and writes it — with no trailing newline — to the harness output
file (`/output/entry.txt`, or `$ENTRY_OUTPUT` when set).

```sh
python3 main.py
```

Check the entry against every gate before submitting:

```sh
python3 main.py --self-test
```

The self-test reports the character count, the 280-character limit, the
single-line and single-sentence checks, and the UTF-8 check, then prints
`self-test PASSED` only when all of them hold. The output is deterministic:
the same sentence, byte-identical, on every run.

After writing the output file, `main.py` reads it back and compares it with
the entry string, so a partial or re-encoded write fails loudly instead of
reaching the judge as a corrupted line.

## Entry details

- One sentence, 279 characters, single line, no leading/trailing space.
- A childhood memory: summer evenings, grandmother, mango, cicadas.
- No dependencies beyond the Python 3 standard library.

## License

MIT License — see [LICENSE](LICENSE). SPDX-License-Identifier: MIT.
