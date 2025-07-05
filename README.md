# **Wordle Picture Generator**

Dis ‘ere is da most kunnin’ scrap o’ Python code dis side of Armageddon. It krumps through a list o’ words, smashin’ 'em against a secret Wordle word like a Nob bashin’ heads at roll call.

## ⚙️ Wot It Do

Dis shiny gubbin:

* Loads yer secret settings from a `.env` file (like a Weirdboy peekin’ into da warp)
* Reads a list o' Wordle-words from a file (loot not included)
* Takes in da day’s secret Wordle word (ya gotta provide it yerself, ya lazy grot)
* Runs each word through a series of brutal krump-checks:

  * **Green** (G): Right letter, right spot — a proppa shot
  * **Yellow** (Y): Right letter, wrong spot — still counts as dakka
  * **Grey** (\_): Not in da word — straight to da scrap heap

Then it finds which words make da same flashy pattern as yer fancy “pattern\_to\_match” list. Good fer cheatin’ or just lookin’ smarter than a squig.

## 🔧 ‘Ow to Use It

1. **Install yer bits:**

   ```bash
   pip install python-dotenv
   ```

2. **Make a `.env` file** in da same spot as dis script. Put in dis:

   ```
   DEBUG=True
   INPUT_FILE=wordlist.txt
   ```

3. **Stick yer word list** in a file named `wordlist.txt`, one word per line. Use real words or make up yer own — we ain't picky.

4. **Run da thing:**

   ```bash
   python wordle_krumper.py
   ```

   Den tell it da Wordle solution when it asks.

## 🧠 Da Smart Bitz (a.k.a. Wot’s Goin’ On Inside)

* Uses da sacred logic of da Meks to scan fer color-patterns like:

  ```python
  pattern_to_match = [
      ["_", "_", "Y", "Y", "Y"],
      ["_", "Y", "Y", "G", "G"],
      ["_", "Y", "Y", "Y", "Y"],
      ["_", "Y", "Y", "Y", "Y"],
      ["_", "_", "Y", "Y", "Y"],
      ["_", "_", "Y", "_", "Y"],
  ]
  ```

* Each pattern line means a guess should make dat color result when compared ta da solution.

* It loops through da whole word list like a Stompa in a minefield, findin' matches.

## 🪓 Known Bugz and Fings to Fix

* Ain’t got no input validation — if ya type in zog, ya get zogged.
* Assumes all words be 5 letters long — no short squigs or long squiggoths.
* Only prints one match per pattern — could be more in da list, but we lazy.

## 💥 Sample Output

```
Will be looking for words to match the following pattern:
	 _  _  Y  Y  Y 
	 _  Y  Y  G  G 
	 _  Y  Y  Y  Y 
	 _  Y  Y  Y  Y 
	 _  _  Y  Y  Y 
	 _  _  Y  _  Y 

Found the solution:
	 spork 
	 brink 
	 crank 
	 drank 
	 blurt 
	 clout 
```

Or if it all goes sideways:

```
Could not find solution :(
```

## 📚 Word List

You can nick one from da internets or make yer own. It’s just a plain text file. Orks don’t need fancy databanks.

## ☠️ License

Dis thing’s free ta use, mod, or krump. Just don’t go actin’ like you invented it without sharin’ da teef.

---

Now tell me if ya wants dis README longer, shorter, or more explodey. WAAAGH!
