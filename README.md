# ASCII-Video-Discord-Bot
Plays a video in ASCII in a Discord channel.

# How do I use it?
You will need to create a bunch of Discord bots in the Discord developer dashboard. This is technically API Abuse and may result in your Discord account being terminated.

Go into the 1 directory, put in an mp4 file. Modify the contents of video.py and insert the name of the mp4 file. Then, in main.py, update TOKEN variable with one of the Discord bot tokens. Add the channel_id for the channel you want the video to play in. Lastly, add in the Discord tokens for your remaining bots in the discord_tokens section. You can optionally modify the image width.

# Disclaimer
Some of the code was taken from https://github.com/NPCat/bad-apple-bot. Namely, the ASCII conversion part and the video to frames code. My bot is simply an extension of that bot which can play in real time. 
