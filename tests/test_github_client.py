from datetime import date, timedelta

from src.github import Github


def test_get_langagues():
    languages = Github().get_languages()
    assert isinstance(languages, list)


def test_search_repositories():
    repos = Github().search_repositories(
        q=f"created:>{str(date.today() - timedelta(days=30))}",
        sort="stars",
        order="desc",
    )
    assert "items" in repos
    assert isinstance(repos["items"], list)
    assert "total_count" in repos
    assert "incomplete_results" in repos
