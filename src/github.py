from datetime import date, timedelta
from enum import Enum
from typing import Dict, List

import requests
from .schema import Langauge

GITHUB_BASE_URL = 'https://api.github.com'

class Order(Enum):
    DECE = 'desc'
    ASC = 'asc'


class Sort(Enum):
    STARS = 'stars'
    FORKS = 'forks'
    UPDATED = 'updated'
    HELP_WANTED_ISSUES = 'help-wanted-issues'

class Github:
    def __init__(self, base_url=None, oauth_token=None):
        if base_url is None:
            self.base_url = GITHUB_BASE_URL
        else:
            self.base_url = base_url
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        if oauth_token is not None:
            self.headers['Authorization': oauth_token]

    def search_repositories(self, q: str, sort: Sort, order: Order):
        """
        Search github repositories

        calls: `GET /search/repositories <http://developer.github.com/v3/search>`_
        :param q: str
        :param sort: Sort
        :param order: Order
        :return JSON response
        """
        response = self._get('/search/repositories', {'q': q, sort: sort, order: order})

        return response


    def get_languages(self) -> List[Langauge]:
        """
        Return list of langauges used by the 100 trending public repos on GitHub.
        """
        last_30_days = str(date.today() - timedelta(days=30))
        res = self.search_repositories(
            q=f"created:>{last_30_days}", sort=Sort.STARS, order=Order.DECE
        )
        return self._group_by_langauge(res['items'])

    def _get(self, url: str, query: Dict) -> Dict:
        """
        Utility function to send get request
        """
        full_url = f'{self.base_url}{url}'
        response = requests.get(full_url, query, headers=self.headers)
        return response.json()

    def _group_by_langauge(self, repos_list: List) -> List[Langauge]:
        """
        Utitly function to group list of repos by langague
        """
        langauges = {}
        for repo in repos_list:
            lang = repo["language"]
            if lang in langauges:
                langauges[lang]["name"] = lang
                langauges[lang]["number_of_repos"] += 1
                langauges[lang]["repos"].append(repo["svn_url"])
            else:
                langauges[lang] = {
                    "name": lang,
                    "number_of_repos": 1,
                    "repos": [repo["svn_url"]],
                }
        return list(langauges.values())
