# Discord-to-Reddit
There are many scripts and automated services that post Reddit Messages to Discord, but none the other way around. This bot is good for updates people are waiting on to both communities, where to origin of the update is in a Discord channel.
<br><br>
Update your Reddit API values and other values and Discord values:
<br><br>
# Initialize Reddit client#
reddit = Reddit(
    client_id='client id',
    client_secret='client secret',
    user_agent='discord:Discord-to-Reddit:v1.0 by /u/ib4error',
    username='reddit username',
    password='reddit password'
)
<br><br>
---------------
<br><br>
#reddit name#
subreddit = reddit.subreddit('reddit name')
<br><br>
---------------
<br><br>
#reddit post title (both bot events)#
post_to_reddit('[Automated] New Subreddit post TITLE here!!',
<br><br>
----------------
<br><br>
#channel ids#
channel = bot.get_channel(DISCORD CHANNELID HERE)
if message.channel.id == DISCORD CHANNELID HERE:
<br><br>
----------------
<br><br>
#discord bot token#
bot.run('DISCORD BOT TOKEN HERE')
