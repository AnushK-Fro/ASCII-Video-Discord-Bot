# ASCII-Video-Discord-Bot
Plays a video in ASCII in a Discord channel.

# Deprecated Notice
This script is deprecated and is not being maintained anymore. 

# How do I use it?
You will need to create some Discord bots in the Discord developer dashboard. Please note that this might put load on the Discord API while the script runs, and may result in a ratelimit due to the amount of requests it sends.

Go into the 1 directory, put in an mp4 file. Modify the contents of video.py and insert the name of the mp4 file. Then, in main.py, update TOKEN variable with one of the Discord bot tokens. Add the channel_id for the channel you want the video to play in. Lastly, add in the Discord tokens for your remaining bots in the discord_tokens section. You can optionally modify the image width.

# Disclaimer
Some of the code was taken from https://github.com/NPCat/bad-apple-bot. Namely, the ASCII conversion part and the video to frames code. My bot is simply an extension of that bot which can play in real time, rather than one frame every few minutes.
