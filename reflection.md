# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked normal on the surface but it was impossible to
play. The secret number seemed to change every time I clicked Submit, so I could never
win. The hints were also wrong — when my guess was too high, it told me to go higher.
On top of that, when I picked the Easy level, the secret number was still outside the
1–20 range that the screen showed me.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when the secret is 50 | Hint says "Go LOWER" | Hint said "Go HIGHER" (backwards) | None |
| Same guess on different turns | Secret stays the same all game | Secret seemed to change between turns, so I couldn't win | None |
| Pick "Easy" difficulty | Secret is between 1 and 20 | Secret was a number higher than 20 (e.g. 73) | None |
| Type "abc" or a huge number | App rejects it, attempt not wasted | It was accepted and used up an attempt | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude (an AI coding agent) on this project. A correct suggestion was that the
"secret keeps changing" bug came from the code turning the secret into a string on
some turns; the AI removed that and forced both values to integers, and I verified it by
opening the Developer Debug Info and seeing the same secret all game while the hints
became correct. A more misleading moment was when the app threw an `ImportError` for
`is_in_range` — at first it looked like the AI's code was broken, but it explained the
real reason was that Streamlit does not reload imported files, and restarting the server
fixed it. So I learned to not always trust that an error means the code itself is wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by actually playing the game and using the Developer Debug Info
panel to compare the secret number, my guess, and the hint. For automated testing, I ran
`pytest tests/` and all 14 tests passed, including ones that check the hints point the
right way and that out-of-range guesses are caught. One useful test was
`test_hint_directions`, which proves "Too High" tells the player to go LOWER — this makes
sure the backwards-hint bug can never quietly come back. The AI helped me by writing
extra tests for input parsing, the range check, and scoring, and explaining what each one
was protecting against.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would tell my friend that Streamlit runs the whole script again from top to bottom
every single time you click a button or change something. Because of that, any normal
variable gets created fresh and forgets its old value. To make the app remember things
like the secret number, the score, and how many attempts you've made, you have to store
them in `st.session_state`, which survives between reruns. I also learned that editing a
separate file like `logic_utils.py` does not reload automatically — you have to restart
the server for those changes to take effect.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is writing small tests for my logic and running `pytest` after
every fix, because passing tests gave me confidence that a bug was actually gone and not
just hidden. Next time I would test the app by actually running it earlier instead of
trusting that the code "looks fixed," since I only caught the Easy-range bug by playing
the game myself. This project changed how I think about AI-generated code: it can write a
lot quickly, but it can also produce confident-looking code that is full of bugs, so I
always need to read it, run it, and test it before trusting it.
