import os
from datetime import date, timedelta

import responses

from ..src.github import Github, Order, Sort
from ..src.schema import Language

github_client = Github()


class TestGithubClient:
    def test_get_languages(self, mocked_responses):
        languages = github_client.get_languages()
        assert [Language(**{
            'name': 'Assembly', 'number_of_repos': 1,
            'repos': ['https://svn.github.com/dtrupenn/Tetris']})] == languages

    def test_search_repositories(self, mocked_responses):
        repos = github_client.search_repositories(
                q=f"created:>{str(date.today() - timedelta(days=30))}",
                sort=Sort.STARS,
                order=Order.DECE,
            )
        assert repos["items"][0]["full_name"] == 'dtrupenn/Tetris'
        assert repos["total_count"] == 40
        assert False == repos["incomplete_results"]
