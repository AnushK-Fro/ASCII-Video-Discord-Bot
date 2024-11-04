# ASCII-Video-Discord-Bot

This bot allows you to play a video in **ASCII art** within a Discord channel. It's a creative and fun way to display videos in a unique format using Discord bots. It should be able to achieve around 10 fps depending on various factors.

> ⚠️ **Deprecated Notice**  
> This project is no longer maintained and may not function as intended. Use at your own risk.

## How to Use

### Requirements:
- You will need to create multiple Discord bots via the [Discord Developer Portal](https://discord.com/developers/applications).
- Be mindful that running this bot might cause a significant load on the Discord API due to the volume of requests, potentially leading to **rate limits**.

### Setup:
1. **Place the video**:  
   Navigate to the `1` directory and place an `.mp4` file that you want to convert and play.

2. **Modify the script**:  
   Open the `video.py` file and update it with the name of your `.mp4` file.

3. **Configure the bot**:  
   In `main.py`, do the following:
   - Set the `TOKEN` variable with one of your Discord bot tokens.
   - Provide the `channel_id` for the Discord channel where you want to stream the video.
   - Add the Discord bot tokens for your remaining bots in the `discord_tokens` section.
   - (Optional) Adjust the `image width` parameter to change the size of the ASCII output.

### Running the Bot:
Once the setup is complete, run the script and the bot will start sending ASCII-rendered video frames to the specified Discord channel.
