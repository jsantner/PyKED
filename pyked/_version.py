__version_info__ = (0, 1, 3, 'a3')
__version__ = '.'.join(map(str, __version_info__[:3]))
if len(__version_info__) == 4:
    __version__ += __version_info__[-1]
