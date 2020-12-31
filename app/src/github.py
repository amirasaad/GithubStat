from os import environ as env
from datetime import date, timedelta
from enum import Enum
from typing import Dict, List

import requests
from .schema import Language

GITHUB_BASE_URL = env.get('GITHUB_BASE_URL', 'https://api.github.com')


class Order(Enum):
    DECE = 'desc'
    ASC = 'asc'


class Sort(Enum):
    STARS = 'stars'
    FORKS = 'forks'
    UPDATED = 'updated'
    HELP_WANTED_ISSUES = 'help-wanted-issues'


class Github:
    """
    A GitHub client
    
    """

    def __init__(self, base_url=None, oauth_token=None):
        self.base_url = GITHUB_BASE_URL if base_url is None else base_url
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        if oauth_token is not None:
            self.headers['Authorization'] = f'Authorization: {oauth_token}'

    def search_repositories(self, q: str, sort: Sort, order: Order):
        """
        Search github repositories

        calls: `GET /search/repositories <http://developer.github.com/v3/search>`_
        :param q: str
        :param sort: Sort
        :param order: Order
        :return JSON response
        """
        return self._get('/search/repositories', {'q': q, sort: sort, order: order})

    def get_languages(self) -> List[Language]:
        """
        Return list of languages used by the 100 trending public repos on GitHub.
        """
        last_30_days = str(date.today() - timedelta(days=30))
        res = self.search_repositories(
            q=f"created:>{last_30_days}", sort=Sort.STARS, order=Order.DECE
        )
        return self._group_by_language(res['items'])

    def _get(self, url: str, query: Dict) -> Dict:
        """
        Utility function to send get request
        """
        full_url = f'{self.base_url}{url}'
        response = requests.get(full_url, query, headers=self.headers)
        return response.json()

    def _group_by_language(self, repos_list: List) -> List[Language]:
        """
        Utility function to group list of repos by language
        """
        languages = {}
        for repo in repos_list:
            lang = repo["language"]
            if lang in languages:
                languages[lang]["name"] = lang
                languages[lang]["number_of_repos"] += 1
                languages[lang]["repos"].append(repo["svn_url"])
            else:
                languages[lang] = {
                    "name": lang,
                    "number_of_repos": 1,
                    "repos": [repo["svn_url"]],
                }
        return list(languages.values())
