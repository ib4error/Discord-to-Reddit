import discord
from discord.ext import commands
from praw import Reddit
from discord import Intents
import asyncio
import re

# Initialize Discord client with intents
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize Reddit client
reddit = Reddit(
    client_id='client id',
    client_secret='client secret',
    user_agent='discord:Discord-to-Reddit:v1.0 by /u/ib4error',
    username='reddit username',
    password='reddit password'
)

def remove_custom_emoji(text):
    emoji_pattern = re.compile("<:[a-zA-Z0-9_-]+:[0-9]+>")
    return emoji_pattern.sub("", text)

def post_to_reddit(title, selftext):
    subreddit = reddit.subreddit('reddit name')
    
    # Remove custom emoji from the selftext
    cleaned_selftext = remove_custom_emoji(selftext)
    
    subreddit.submit(title, selftext=cleaned_selftext)

@bot.event
async def on_ready():
    await asyncio.sleep(5)  # Increase the delay to 5 seconds (or adjust as needed)
    print(f'We have logged in as {bot.user}')

    channel = bot.get_channel(DISCORD CHANNELID HERE)  # Replace with your channel ID
    last_message = None
    async for message in channel.history(limit=1):
        last_message = message

    if last_message is not None:
        username = str(last_message.author)  # Get the username as a string
        post_to_reddit('[Automated] New Subreddit post TITLE here!!', f'{username}: {last_message.content}')
    else:
        print('No messages found in the channel.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == DISCORD CHANNELID HERE:  # Replace with your channel ID
        username = str(message.author)  # Get the username as a string
        post_to_reddit('[Automated] New Subreddit post TITLE here!!', f'{username}: {message.content}')

    await bot.process_commands(message)

bot.run('Discord BOT TOKEN HERE')
