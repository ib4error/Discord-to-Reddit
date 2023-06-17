# Discord-to-Reddit 
There are many scripts and automated services that post Reddit Messages to Discord, but none the other way around. This bot is good for updates people are waiting on to both communities, where to origin of the update is in a Discord channel.
<br><br>
# Update your Reddit API values and other values and Discord values:
## Initialize Reddit client

```python
reddit = Reddit(
    client_id='client id',
    client_secret='client secret',
    user_agent='discord:Discord-to-Reddit:v1.0 by /u/ib4error',
    username='reddit username',
    password='reddit password'
)
```
## reddit name
```python
def post_to_reddit(title, selftext):
    subreddit = reddit.subreddit('reddit name')
```
## reddit post title (both bot events)
```python
@bot.event
async def on_ready():

    #other code in the function

    post_to_reddit('[Automated] NEw Subreddit post TITLE here!!', f'{username}: {last_message.content}')

and
@bot.event
async def on_message(message):

    #other code in the function

post_to_reddit('[Automated] New Subreddit post TITLE here!!', f'{username}: {message.content}')
```
## channel ids
```python
channel = bot.get_channel(DISCORD CHANNELID HERE)  # Replace with your channel ID

and

if message.channel.id == DISCORD CHANNELID HERE:  # Replace with your channel ID
```
## discord bot token
```python
bot.run('DISCORD BOT TOKEN HERE')
```
:shipit: :shipit: :shipit: :shipit: :shipit:
