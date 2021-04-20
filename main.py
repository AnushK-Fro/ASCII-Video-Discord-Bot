import os, random, requests, cv2, youtube_dl, sys, time
from discord.ext import commands
from PIL import Image
from discord_webhook import DiscordWebhook

TOKEN = "" # Discord Bot Token to listen for commands
channel_id = "" # Discord Channel ID to play the video
discord_tokens = ["Discord Token 1", "Discord Token 2"] # Put in Discord Bot tokens and invite them all into a server
WIDTH = 60 # Image Width

bot = commands.Bot(command_prefix='c!') # Bot Prefix

options = {
    'format': 'bestvideo+bestaudio/best' # Youtube DL options (not working)
}

#ASCII_CHARS = ['⠀','⠄','⠆','⠖','⠶','⡶','⣩','⣪','⣫','⣾','⣿']
ASCII_CHARS = ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ' ', '@'] # ASCII Characters Used (Can also use other character set, both are fine)
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]

def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]

    return '\n'.join(new_image)

def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return
    image = do(image)

    return image

frames = []

for i in range(0, int((len(os.listdir("3/")))/4)+1):
    path = "1/frame" + str(i*4)+".jpg" #<--- path to folder containing every frame of the video
    frames.append(runner(path))

print("Finished storing frames!")
print(len(discord_tokens) + " tokens are available to use!")

@bot.command(name='play', help='Play a video in ASCII')
async def play(ctx):
    # Folder
    video_id = "1"
    with youtube_dl.YoutubeDL(options) as ydl:
        # Beta - Non functional
        #info = ydl.extract_info(video, download=True)
        #filename = ydl.prepare_filename(info)
        #filename = filename.split(".", 1)[0]
        #filename = filename + ".mkv"
        #os.system("mv" + ' "' + filename + '" ' + video_id + " && cd " + video_id + " && ffmpeg -i" + ' "' + filename + '" ' + "-vsync 0 " + video_id + "\%d.png")
        try:
            # Set current directory to folder
            os.chdir(video_id)
        except:
            pass
        start = False
        arrayval = 0
        frame_num = 0
        for filen in os.listdir("."):
            frame_num = frame_num + 1
            try:
                img = Image.open(filen)
            except:
                return
            if start == False:
                arrayval = arrayval + 1
                if arrayval == len(discord_tokens):
                    arrayval = 1
                payload = {
                    'content': "Frame " + str(frame_num) + "/" + str(int(len(os.listdir("."))-1)) + "```" + frames[frame_num] + "```"
                }
                header = {
                    'authorization': 'Bot ' + discord_tokens[arrayval]
                }
                r = requests.post("https://discord.com/api/v8/channels/" + channel_id + "/messages", data=payload, headers=header)

bot.run(TOKEN)
