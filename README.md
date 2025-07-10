# Space to tab delimited converter
A very small python script to convert space delimited txt files into tab delimited txt files, so you can paste into excel at will. I'm sure there's other ways to do this, but this is how I do it, and it's very fast.

The program works by just blunty matching any spaces and replacing them with tabs with a little bit of regex. As a result if you run this on a sentence all those spaces will be tabs too.

I see absolutely no reason the program should cause data issues, but please create a copy of the file you run it on first just in case. 

### Dependencies
Python 3: https://www.python.org/downloads/
(make sure to install with PATH and pip)

The re module should be pre-installed with python. If not, run:
```
python -m pip install re
```
in the command line.
