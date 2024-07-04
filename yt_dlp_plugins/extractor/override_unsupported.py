from yt_dlp.extractor.unsupported import KnownPiracyIE

class _OverrideKnownPiracyIE(KnownPiracyIE, plugin_name='override_unsupported'):
    URLS = (
        r'dood\.(?:to|watch|so|pm|wf|re)',
        r'viewsb\.com',
        r'filemoon\.sx',
        r'hentai\.animestigma\.com',
        r'gounlimited\.to',
        r'highstream\.tv',
        r'uqload\.com',
        r'vadbam\.net'
        r'vidlo\.us',
        r'wolfstream\.tv',
        r'xvideosharing\.com',
        r'(?:\w+\.)?viidshar\.com',
        r'einthusan\.(?:tv|com|ca)',
    )