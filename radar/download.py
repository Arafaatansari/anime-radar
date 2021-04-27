import requests
from tqdm import tqdm

def anime_download(session: requests.Session, url, path_to_file, *, file_desc=None):

    with session.head(url) as head_response:
        r = int(head_response.headers.get('content-length', 0) or 0)    
    
    d = 0
    tqdm_bar = tqdm(desc=file_desc, total=r, unit='B', unit_scale=True)
    
    with open(path_to_file, 'ab') as sw:
        d = sw.tell()
        tqdm_bar.update(d)
        while r > d:
            try:
                for chunks in session.get(url, stream=True, headers={'Range': 'bytes=%d-' % d}).iter_content(0x4000):
                    size = len(chunks)
                    d += size
                    tqdm_bar.update(size)
                    sw.write(chunks)
            except requests.RequestException:
                pass
            
    tqdm_bar.close()