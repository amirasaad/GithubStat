from src.github import Client

github = Client()

def test_get_repos():
    repos = github.repos()