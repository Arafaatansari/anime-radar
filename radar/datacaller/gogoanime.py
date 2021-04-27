import re
from random import choice
from pathlib import Path

import lxml.html as htmlparser

from ..ratelimits import fetch_proxies
from ..download import anime_download
from . import DataCaller

def sanitize_filename(f):
    return ''.join(' - ' if _ in '<>:"/\\|?*' else _ for _ in f)

ajax_parse = lambda dt: (dt.get('source', [{}])[0].get('file'), dt.get('source_bk', [{}])[0].get('file'))

class GogoAnimeDataCaller(DataCaller):
    """
    A datacaller class for GogoAnime.
    """
    use_proxies = False    
    content_ajax = "https://ajax.gogo-load.com/ajax/page-recent-release.html"
    
    content_base = "https://www1.gogoanime.ai"
    max_pages = 10
    
    def get(self):
        
        proxies = {'https': "https://%s/" % choice(fetch_proxies())} if self.use_proxies else {}
        current = 1
        
        while current <= self.max_pages:
            with self.session.get(self.content_ajax, params={'type': '1', 'page': str(current)}, proxies=proxies) as response:
                content_parsed = htmlparser.fromstring(response.text)
            for li in content_parsed.xpath('//div[@class="last_episodes loaddub"]/ul/li'):
                
                if not (c := re.findall(r'Episode (\d+)', li.xpath('p[@class="episode"]')[0].text)):
                    continue
                
                anc = li.xpath('p[@class="name"]/a')[0]
                
                yield {anc.get('title', ''): {'url': self.content_base + (anc.get('href', '')), 'episode': int(c[0])}}
                
            current += 1
            
    def download(self, base_download_folder, anime_name, url, episode):

        with self.session.get(url) as response:
            content_parsed = htmlparser.fromstring(response.text)

        streaming = content_parsed.xpath('//div[@class="play-video"]/iframe')[0].get('src')
        
        with self.session.get('https:%s' % streaming.replace('streaming', 'ajax')) as response:
            content = response.json()
        
        source_1, source_2 = ajax_parse(content)
        
        base = Path(base_download_folder)
        base.mkdir(exist_ok=True)
        
        download_file =  base / sanitize_filename(anime_name)
        download_file.mkdir(exist_ok=True)
        
        anime_download(self.session, source_1, download_file / ("E%02d.mp4" % episode), file_desc="%s, E%02d.mp4" % (anime_name, episode))