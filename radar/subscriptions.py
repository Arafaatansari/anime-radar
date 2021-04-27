import re

def from_file(filepath):
    """
    Create just a subscription thingy subscriptions for your anime.
    """
    with open(filepath, 'r') as sr:
        return [p if not p.startswith('regexp:') else re.compile(p.removeprefix('regexp:'), re.I) for p in sr.readlines()]