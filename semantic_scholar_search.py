import os
import ast
import concurrent.futures
from typing import List

from semanticscholar import SemanticScholar

categories = ["technology", "business", "entertainment", "health", "sports", "science"]


def clean_text(text: str) -> str:
    cleaned_text = text.replace(
        "\\n", " "
    )  # Replace newline characters with spaces
    return cleaned_text.strip()


class SemanticScholarSearch(object):
    def __init__(self):
        self.search_client = SemanticScholar()
        self.search_year = os.getenv("SS_SEARCH_YEAR", None)
        self.search_limit = int(os.getenv("SS_SEARCH_LIMIT", 10))
        self.fields_of_study = os.getenv("SS_SEARCH_FIELDS_OF_STUDY", None)
        self.venue = os.getenv("SS_SEARCH_VENUE", None)
        # string with "[]" to list
        self.search_fields_of_study = ast.literal_eval(self.fields_of_study) if self.fields_of_study else None
        self.venue = ast.literal_eval(self.venue) if self.venue else None

    def search_papers_by_keyword(self, query: str) -> List[str]:
        """
        Get all papers for query specified.
        Args:
            query (str) : The query specified.
        Returns:
            list(str): A list of papers for the specified category, sorted by relevant.
        """
        result = self.search_client.search_paper(query=query,
                                                 year=self.search_year,
                                                 fields_of_study=self.search_fields_of_study,
                                                 venue=self.venue,
                                                 fields=['title', 'authors', 'year', 'abstract', 'citationCount', 'url'])
        # sort the result by citations count, descending
        result = sorted(result[:self.search_limit], key=lambda x: int(x["citationCount"]), reverse=True)
        # only keep title, authoirs and abstract
        result = [{"title": x["title"], "year": x['year'], "authors": ",".join([author["name"] for author in x["authors"]]),
                   "abstract": x["abstract"]} for x in result]
        # list to string
        str_result = ""
        for i, paper in enumerate(result):
            str_result += f"[BEGIN]\nTitle: {paper['title']}\nAuthors: {paper['authors']}\nYear: {paper['year']}\nAbstract: {paper['abstract']}\n[END]\n"
        return str_result

    # def search_papers_by_author(self, query: str) -> List[str]:
    #     """
    #     Get all papers for query specified.
    #     Args:
    #         query (str) : The query specified.
    #     Returns:
    #         list(str): A list of papers for the specified category, sorted by relevant.
    #     """
    #     result = self.search_client.search_author(query=query, limit=self.search_limit,
    #                                               year=self.search_year,
    #                                               fields_of_study=self.search_fields_of_study,
    #                                               fields=['title', 'author', 'abstract', 'citationCount', 'url'])
    #
    #     # sort the result by citations count, descending
    #     result = sorted(result, key=lambda x: int(x["citationCount"]), reverse=True)
    #
    #     return result

