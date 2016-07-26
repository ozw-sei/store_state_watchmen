import unittest
from unittest.mock import MagicMock

from store.app_store_ranking import AppStoreRanking


class AppStoreRankingTest(unittest.TestCase):
    def setUp(self):
        stub_file_url = "appstore.xml"
        self.app_id = "1094591345"  # pockemon go
        self.thing = AppStoreRanking(self.app_id, {})
        self.thing.get_url = MagicMock(return_value=stub_file_url)

    def test_app_store_ranking(self):
        self.thing.fetch_ranking()
        rank = self.thing.rank

        self.assertEqual(rank, 1)

    def test_app_store_ranking_taget_is_pockemongo(self):
        self.thing.fetch_ranking()
        target = self.thing.target

        self.assertEqual(target["app_id"], self.app_id)
