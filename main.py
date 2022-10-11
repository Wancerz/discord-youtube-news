from discord.ext import tasks
from yt_search import youtube_search

import discord


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        # if youtube_search.video_comparison() is True:
        #     data =  youtube_search.video_comparison()
        #     url = data['video_ url']
        # channel = discord.get_channel('960256204775489618')  # channel ID goes here
        # url = "aaa"
        # await channel.send(url)
        channel = self.get_channel(960256204775489618)  # channel ID goes here
        self.counter += 1
        data =  youtube_search().video_comparison()
        url = data['video_url']
        # url = "aaa"
        await channel.send(url)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in


client = MyClient(intents=discord.Intents.default())
client.run('x')