if not exist %cd%\settings.conf (
	type NUL > settings.conf
::	echo he > settings.conf
::	echo hello >> settings.conf
)
if not exist %cd%\settings.conf (
	type NUL > settings.conf
)
if not exist %cd%\token.conf (
	type NUL > token.conf
	echo discord_bot_key=REPLACE_WITH_YOUR_DISCORD_KEY > token.conf
	echo api_key=REPLACE_WITH_YOUR_FFLOGS_KEY >> token.conf
	echo google_drive=REPLACE_WITH_YOUR_GOOGLE_DRIVE_KEY >> token.conf
)
if not exist %cd%\webhooks.conf (
	type NUL > webhooks.conf
)
pip3 install aiohttp discord.py asyncio requests arrow
PAUSE