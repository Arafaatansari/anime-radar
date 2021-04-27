"""
AnimeRadar is an automatic anime downloader which downloads your favorite anime(s) after the upload of its new releases.
"""

from radar.subscriptions import from_file
from radar import *
import requests

if __name__ == '__main__':

    gga = gogoanime.GogoAnimeDataCaller(requests.Session())
    AnimeRadar(gga, download_dir='AnimeRadar - GogoAnime', subscriptions=from_file('subscriptions.txt')).start_radar()