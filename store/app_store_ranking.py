import feedparser
import re

APP_STORE = 1


class AppStoreRanking:

    BASE_URL = "https://itunes.apple.com/jp/rss/topfreeapplications/limit={0}/genre=6014/xml"

    def __init__(self, _appId, opt):
        self.appId = _appId
        self.store_type = opt.get('store_type', APP_STORE)
        self.limit = opt.get('limit', 100)
        self.data = []
        self.rank = 0
        self.target = {}

    def get_url(self):
        _url = self.BASE_URL.format(self.limit)
        return _url

    def fetch_ranking(self):
        url = self.get_url()

        self.data = self.fetch_parse_xml(url)
        return self.data

    def fetch_parse_xml(self, url):
        parsed = feedparser.parse(url)
        return [self.__build_dict(e, i + 1) for i, e in enumerate(parsed.entries)]

    @staticmethod
    def __extract_app_id(raw_id):
        pattern = 'id([0-9]+)'
        app_id = re.findall(pattern, raw_id)[0]
        return app_id

    def __build_dict(self, entry, rank):
        d = dict()
        app_id = self.__extract_app_id(entry.id)

        d['store_type'] = self.store_type
        d['app_id'] = app_id
        d['title'] = entry.title
        d['rights'] = entry.rights
        d['content'] = entry.content
        d['rank'] = rank

        if app_id == str(self.appId):
            self.rank = rank
            self.target = d

        return d
