# Discord-v2
v2 of the Discord bot used to compile FFXIV Ultimate tracker.

The Google Sheets doc this is mainly used for:
https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing

The v1 bot was a NodeJS app that became very bloated and annoying to manage so v2's objective is to be more readable and better handled. The reason behind Python is just that I wanted to do something different. At the start of this project I'm basically looking at beginners guide on Python so the earlier code might look like that.

How to run:
1. There's 2 main scripts: main.py and vector.py.
2. main.py is an endless loop that always tries to run vector.py whenever vector.py returns.
3. vector.py is the main script and if you want to exit the script on exit, run this.