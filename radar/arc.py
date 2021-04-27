import logging
import time

infinity = float('inf')

class AnimeRadar:
    """
    An AnimeRadar class.
    """
    def __init__(self, data_caller, delay=600,
                 *, download_dir, subscriptions):
        
        self.data_caller = data_caller
        self.delay = delay
        self.download_dir = download_dir
        self.subscriptions = subscriptions
    
        self.logger = logging.getLogger('AnimeRadar @ 0x%16X' % id(self))
        
        self.cache = []
        
    def start_radar(self, *, duration=infinity):
        """
        The main radar activation call.
        
        `duration` is the time, in seconds, that is going to serve as the time limit of the radar.
        """
        
        self.logger.info('Radar has started and is expected to be called %s.' % ('infinitely' if duration == infinity else 'for the next %ds' % duration))
        
        start = time.time()
        extract_data = lambda ad: (ad.get('url', ''), ad.get('episode', 1)) 

        while ((current_time := time.time()) - start) <= duration:
                        
            for content in self.data_caller.get():
                for anime, anime_data in content.items():
                    if not (data := extract_data(anime_data)) in self.cache and AnimeRadar.in_subscriptions(self.subscriptions, anime):
                        self.logger.debug("Downloading %s, episode: %s." % data)
                        self.data_caller.download(self.download_dir, anime, *data)
                        self.cache.append(data)
            
            if not (time.time() - current_time) > self.delay:
                time.sleep(self.delay - (time.time() - current_time))
                
    @staticmethod
    def in_subscriptions(subscriptions, text):
        
        if not subscriptions:
            return True
        
        for p in subscriptions:
            if isinstance(p, str):
                if text.lower() == p.lower():
                    return True
                continue
            
            if p.findall(text):
                return True
            
        return False