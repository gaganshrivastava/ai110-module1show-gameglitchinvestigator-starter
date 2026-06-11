# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI agent (Claude) to first read the whole project and explain what the
code was doing. After that, I asked it to find and fix all the bugs in the game, move
the game logic into `logic_utils.py`, and make sure the pytest tests passed.

**What did the agent do?**

- Read `app.py`, `logic_utils.py`, the test file, the README, and `requirements.txt`.
- Explained that it was a broken Streamlit number-guessing game.
- Moved the four logic functions out of `app.py` into `logic_utils.py`.
- Fixed the bugs it found:
  - The secret number was being turned into a string on some turns, which made the
    hints lie.
  - The "Higher / Lower" hint messages were backwards.
  - The UI always said "between 1 and 100" even on Easy and Hard.
  - The secret number did not change to match the difficulty range.
  - Out-of-range guesses and typos were being accepted and wasting attempts.
- Installed pytest and ran the tests until all of them passed.
- Added more tests to cover the new code.

**What did you have to verify or fix manually?**

I ran the app myself and noticed the secret number was still outside the range when I
picked Easy. I reported this back to the agent and it found that the secret was only
created once on the first load, so it never updated when I switched difficulty. I also
hit an `ImportError` for `is_in_range` — the agent explained this was not a code bug but
a Streamlit issue where it does not reload imported files, so I had to fully restart the
server (not just click "Rerun"). After restarting, everything worked.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Hints must not be backwards | "Add tests so the wrong hint bug can't come back" | `test_hint_directions` checks "Too High" → Go LOWER and "Too Low" → Go HIGHER | Yes | This locks in the fix so the inverted-hint bug can't return unnoticed. |
| Bad input (letters, empty) | "Test what happens when the input isn't a number" | `test_parse_non_number` and `test_parse_empty_and_none` | Yes | Confirms `parse_guess` returns a friendly error instead of crashing. |
| Guess outside the range | "Make sure out-of-range guesses are caught" | `test_is_in_range` checks values below/above the range | Yes | Backs up the new range check so you can't guess 9999 on Easy. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

_Not attempted for this project._

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

_Not attempted for this project._
