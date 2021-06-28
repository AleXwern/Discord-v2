#!/bin/sh
sudo apt install python3 python3-pip -y
pip3 install aiohttp discord.py asyncio requests arrow
mkdir -p logs
if [ ! -f webhooks.conf ];
then
    echo "Did not find webhooks.conf -> Creating new one."
    touch webhooks.conf
fi
if [ ! -f settings.conf ];
then
    echo "Did not find settings.conf -> Creating new one."
    touch settings.conf
fi
if [ ! -f token.conf ];
then
    echo "Did not find token.conf -> Creating new one."
    echo "discord_bot_key=REPLACE_WITH_YOUR_DISCORD_KEY\n" > token.conf
    echo "api_key=REPLACE_WITH_YOUR_FFLOGS_KEY\n" >> token.conf
    echo "google_drive=REPLACE_WITH_YOUR_GOOGLE_DRIVE_KEY\n" >> token.conf
fi