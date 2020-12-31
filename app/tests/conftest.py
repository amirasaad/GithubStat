from datetime import timedelta, date
from pathlib import Path

import pytest
import responses

from app.src.settings import settings
from app.src.github import Sort, Order

github_response_file = Path(__file__).with_name('github_data.json')


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as response:
        with github_response_file.open() as f:
            response.add(
                responses.GET,
                url=f'{settings().GITHUB_BASE_URL}/search/repositories?q=created%3A%3E'
                    f'{str(date.today() - timedelta(days=30))}'
                    f'&sort={Sort.STARS}&order={Order.DECE}',
                body=f.read(),
            )
        yield response
