from datetime import date, timedelta

import responses

from ..src.github import Github, Order, Sort

from ..src.settings import settings

responses.add(
    responses.Response(
        method='GET',
        url=settings().GITHUB_BASE_URL
    )
)


class TestGithubClient:

    def test_get_languages(self):
        languages = Github().get_languages()
        assert isinstance(languages, list)

    def test_search_repositories(self):
        repos = Github().search_repositories(
            q=f"created:>{str(date.today() - timedelta(days=30))}",
            sort=Sort.STARS,
            order=Order.DECE,
        )
        print(repos)
        assert "items" in repos
        assert isinstance(repos["items"], list)
        assert "total_count" in repos
        assert "incomplete_results" in repos
