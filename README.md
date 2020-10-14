# Discord-v2
v2 of the Discord bot used to compile FFXIV Ultimate tracker.

The Google Sheets doc this is mainly used for:
https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing

The v1 bot was a NodeJS app that became very bloated and annoying to manage so v2's objective is to be more readable and better handled. The reason behind Python is just that I wanted to do something different. At the start of this project I'm basically looking at beginners guide on Python so the earlier code might look like that.

How to run:
1. There's 2 main scripts: main.py and vector.py.
2. Any private tokens go into 'token.txt' file that's in the root of the repo (not included) delimited by comma.
3. main.py is an endless loop that always tries to run vector.py whenever vector.py returns.
4. vector.py is the main script and if you want to exit the script on exit, run this.
5. Giving raw FFlogs link in Discord chat provides following output with more detailed info if the instance in question is UCoB, UWU or TEA.
<img src="https://github.com/AleXwern/Discord-v2/blob/main/output.png" alt="drawing" width="800"/>

FFlogs API status:
1. Uses the v1 API for now (JSON return data)
2. Aim is to see how v2 works and possibly switch to it but at first glance is looks wildly different so first I'll get the old system working and then see the improvements on v2 side.