# Discord-v2
v2 of the Discord bot used to compile FFXIV Ultimate tracker.

The Google Sheets doc this is mainly used for:
https://docs.google.com/spreadsheets/d/1Xrb5CjEM74nQhiQ9Jx6H6wOnpfMIgOZR2oYEBxSqG1A/edit?usp=sharing

The v1 bot was a NodeJS app that became very bloated and annoying to manage so v2's objective is to be more readable and better handled. The reason behind Python is just that I wanted to do something different. At the start of this project I'm basically looking at beginners guide on Python so the earlier code might look like that.
Plan is to make this as standalone script too but for now you'll need to use this as Discord bot only.

NOTE! Everytime there's a mention of FFlogs link it means the full URL with HTTPS and everything and not just the report code. It's just easier to slap the entire URL and make the bot do the work. Note also that the characters after the code don't matter as the bot just looks at the expected position where the 16 character code is.
Example of minimum length URL: https://www.fflogs.com/reports/xHY8WMrnBwq9RKt4

Requirements and setup:
1. discord and aiohttp Python packages and Python 3 (you can install these with pip install in CMD)
2. Create 'token.conf' in the repository root. NOTE THE CHANGED NAME FROM OLD VERSION
3. Create Discord bot and get the authentication token for it and paste it into token.txt followed by a newline.
4. Before FFlogs keys put 'api_key='
5. Get FFLogs V1 Client Key from your FFlogs account's setting and put it onto the file after the 'api_key='
6. The bot should work now when you run vector.py.
7. If you have any webhooks you can send data to you can list them in webhooks.conf delimited by a linebreak.

How to run:
1. There's 2 main scripts: main.py and vector.py.
2. main.py is an endless loop that always tries to run vector.py whenever vector.py returns.
3. vector.py is the main script and if you want to exit the script on exit, run this.
4. Giving raw FFLogs link in Discord chat provides following output with more detailed info if the instance in question is UCoB, UWU or TEA (or any Ultimate released afterwards).
<img src="https://cdn.discordapp.com/attachments/587267707293007872/767436134451904613/unknown.png" alt="drawing" width="800"/>

Main commands
1. Just FFLogs link provides data about the encounters inside that report
2. .guild [partition] [guild] [server] [region] runs the command 1 on all matching partitions that are listed in guild.
3. .user [partition] [user] is the same as guild but targets specific user.
4. .recrawl, no arguments, digs through logarr.txt file for fflogs links and compiles data with them. Each delimited by line break (Win or UNIX doesn't matter)
5. Names with whitespaces are replaced by _. ex. Up In There becomes Up_In_There.
6. .help gives more help with commands
7. .hook N sets current POST webhook to index N from list. Default is -1 aka none
8. .send sends last compiled encounter data to current set webhook

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
1. Uses the v1 API for now. It's deprecated but working so It'll do for now.
2. Aim is to see how v2 works and possibly switch to it but at first glance is looks wildly different so first I'll get the old system working and then see the improvements on v2 side.
