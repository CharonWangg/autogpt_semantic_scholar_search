import json
import os
import unittest

import pytest

from semantic_scholar_search import SemanticScholarSearch


class TestSemanticScholarSearch(unittest.TestCase):
    def setUp(self):
        # os.environ["SS_SEARCH_YEAR"] = "2023"
        os.environ["SS_SEARCH_LIMIT"] = '100'
        os.environ["SS_SEARCH_FIELDS_OF_STUDY"] = "['Computer Science']"
        self.plugin = SemanticScholarSearch()

    def tearDown(self):
        os.environ.pop("SS_SEARCH_LIMIT", None)
        os.environ.pop("SS_SEARCH_FIELDS_OF_STUDY", None)
        os.environ.pop("SS_SEARCH_VENUE", None)
        os.environ.pop("SS_SEARCH_YEAR", None)

    def test_semantic_scholar_search_by_keyword(self):
        query = "continual learning"
        try:
            res = self.plugin.search_papers_by_keyword(query)
            print(res)
        except requests.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code, 401)



if __name__ == "__main__":
    unittest.main()
