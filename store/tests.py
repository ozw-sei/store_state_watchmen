import unittest
from unittest.mock import MagicMock
from store.app_store_ranking import AppStoreRanking


class AppStoreRankingTest(unittest.TestCase):


    def setUp(self):
        self.pockemon_go_app_id = "1094591345"
        self.rank_out_of_range_app_id = "000000000"

    def get_standard_mock(self, app_id):
        stub_file_url = "store/appstore.xml"
        thing = AppStoreRanking(app_id, {})
        thing.get_url = MagicMock(return_value=stub_file_url)
        return thing

    def test_app_store_ranking(self):
        thing = self.get_standard_mock(self.pockemon_go_app_id)
        thing.fetch_ranking()
        rank = thing.rank

        self.assertEqual(rank, 1)

    def test_app_store_ranking_is_out_range(self):
        thing = self.get_standard_mock(self.rank_out_of_range_app_id)

        thing.fetch_ranking()
        rank = thing.rank
        target = thing.target

        self.assertEqual(rank, 0)
        self.assertEqual(target.get("app_id"), None)

    def test_app_store_ranking_taget_is_pockemongo(self):
        thing = self.get_standard_mock(self.pockemon_go_app_id)
        thing.fetch_ranking()
        target = thing.target

        self.assertEqual(target["app_id"], self.pockemon_go_app_id)
