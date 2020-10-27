# Discord-v2
v2 of the Discord bot used to compile FFXIV Ultimate tracker.

The Google Sheets doc this is mainly used for:
https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing

The v1 bot was a NodeJS app that became very bloated and annoying to manage so v2's objective is to be more readable and better handled. The reason behind Python is just that I wanted to do something different. At the start of this project I'm basically looking at beginners guide on Python so the earlier code might look like that.

How to run:
1. There's 2 main scripts: main.py and vector.py.
2. Any private tokens go into 'token.txt' file that's in the root of the repo (not included), delimited by comma and in order of DISCORD,FFLOGS.
3. main.py is an endless loop that always tries to run vector.py whenever vector.py returns.
4. vector.py is the main script and if you want to exit the script on exit, run this.
5. Giving raw FFLogs link in Discord chat provides following output with more detailed info if the instance in question is UCoB, UWU or TEA (or any Ultimate released afterwards).
<img src="https://cdn.discordapp.com/attachments/587267707293007872/767436134451904613/unknown.png" alt="drawing" width="800"/>

Main commands
1. Just FFLogs link provides data about the encounters inside that report
2. .guild [partition] [guild] [server] [region] runs the command 1 on all matching partitions that are listed in guild.
3. .user [partition] [user] is the same as guild but targets specific user.
4. .recrawl, no arguments, digs through logarr.txt file for fflogs links and compiles data with them. Each delimited by line break (Win or UNIX doesn't matter)
5. Names with whitespaces are replaced by _. ex. Up In There becomes Up_In_There.
6. .help gives more help with commands

Output
1. Report ID:      - The ID of the report that is listed in the URL.
2. Total pulls:    - Total amount of pulls that are over 20 seconds long.
3. Start time:     - Start time of first pull in server's local timezone.
4. End time:       - End time of last pull in server's local timezone.
5. Total kills:    - Total number of kills.
6. Raid length:    - Difference between start and end time.
7. Pull length:    - Difference between start and end time minus downtime.
8. Max pull len:   - The length of the longest pull.
9. Avg pull len:   - Average length of all pulls.
10. "Wipes by phase" lists all major Ultimate phases and how many times there was a wipe in each.

Code status:
1. Uses the v1 API for now (JSON return data)
2. Aim is to see how v2 works and possibly switch to it but at first glance is looks wildly different so first I'll get the old system working and then see the improvements on v2 side.
3. Code work and seems to give 100% correct data (TODO UWU intermission unsure) but each check take a very long time so seeking ideas on optimizing that.