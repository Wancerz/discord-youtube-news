from multiprocessing.spawn import old_main_modules
# from pytube import Channel
# from pytube import YouTube
import pytube
from json_functions import json_functions

class youtube_search:

    def __init__(self) -> None:
        self.video_comparison()
        pass


    def json_video_info(self):

        old_video_data = json_functions().open_json("last_video_informations")
        # print(old_video_data)
        return old_video_data

    def new_video_info(self):

        channel = pytube.Channel('https://www.youtube.com/user/rossomakWGE')
        for url in channel.video_urls[:1]:
            new_video_url = url

        yt = pytube.YouTube(new_video_url)
        new_video_data = {}
        new_video_data['video_url'] = new_video_url
        new_video_data['video_name'] = yt.title
        new_video_data['video_id'] = yt.video_id
        return new_video_data

    def  video_comparison(self):

        old_video_data = self.json_video_info()
        new_video_data = self.new_video_info()
        if old_video_data['video_url'] != new_video_data['video_url'] and old_video_data['video_id'] != new_video_data['video_id']:
            json_functions.save_json("last_video_informations",new_video_data)
            print(new_video_data)
            print("lala")
        return new_video_data




