import re

from yt_dlp.extractor.common import InfoExtractor


class MissAVIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?missav\.com/.*/(?P<id>[\w-]+)'
    _TESTS = [{
        'url': 'https://missav.com/en/blk-470-uncensored-leak',
        'md5': 'f1537283a9bc073c31ff86ca35d9b2a6',
        'info_dict': {
            'id': 'blk-470-uncensored-leak',
            'ext': 'mp4',
            'title': 'BLK-470 A Bitch Gal Who Seduces Her Best Friend\'s Boyfriend With A Micro Mini One Piece Dress - Eimi Fukada',
            'description': '',
            'thumbnail': r're:^https?://.*\.jpg$',

        },
    }]

    def _real_extract(self, url):
        
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        url_path = webpage.split("m3u8|")[1].split("|playlist|source")[0]
        url_words = url_path.split('|')
        video_index = url_words.index("video")
        protocol = url_words[video_index-1]
        video_format = url_words[video_index + 1]

        m3u8_url_path = "-".join((url_words[0:5])[::-1])
        base_url_path = ".".join((url_words[5:video_index-1])[::-1])

        formatted_url = "{0}://{1}/{2}/{3}/{4}.m3u8".format(protocol, base_url_path, m3u8_url_path, video_format, url_words[video_index])

        self.to_screen('URL "%s" successfully captured' % formatted_url)

        formats = self._extract_m3u8_formats(formatted_url, video_id, 'mp4', m3u8_id='hls')
        
        
        return {
            'id': video_id,
            'title': self._og_search_title(webpage),
            'description': self._og_search_description(webpage, default=''),
            'thumbnail': self._og_search_thumbnail(webpage, default=None),
            'formats': formats,
            'age_limit': 18,
        }
