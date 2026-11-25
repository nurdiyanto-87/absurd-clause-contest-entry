# The Absurd Clause Contest

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/nurdiyanto-87/absurd-clause-contest-entry/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/nurdiyanto-87/absurd-clause-contest-entry/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1) on make.fun: a program that writes one original absurd clause, buried deep inside a terms-of-service agreement, to `/output/entry.txt`.

## The clause

> You agree that your left shoe remains the property of the Company and may be repossessed at any time by a representative wearing the right shoe.

## Run it

```sh
python3 main.py
```

Writes the clause to `/output/entry.txt` (creating the directory if needed), prints it, and self-checks that it is UTF-8, a single line, a single sentence, and 1–200 characters. Pure Python standard library only — no third-party packages, no network, deterministic output.
