# RepeetCode

A tool (and API) to review completed LeetCode problems. Because I wanted to be able to pull random LeetCode problems for practice, and maybe have a reminder of how to do them.

If someone wants to make a front-end for this, by all means go for it. This was more of a 3 hour frustration project.

Has only been tested on Python 3.10. Should work on later versions. Shouldn't work on prior versions (RE: `match`).

## Installation

To install:

1. Clone RepeetCode:

   ```bash
   git clone --depth 1 https://github.com/Golf0ned/RepeetCode.git
   cd RepeetCode
   ```

2. Make sure you have at least Python 3.10 installed.

3. Happy leetcoding!

## Usage

To use, run `src/runner.py` with your python installation (name may vary):

```bash
python src/runner.py
```

3 options at runtime:

* `q`: Quits the program.
* `a`: Add a problem to your list, with a reminder/hint for yourself.
* `r`: Random problem from your list, ask for hint if necessary.

Data is saved in `data.csv`.
