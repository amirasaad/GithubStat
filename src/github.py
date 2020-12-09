import requests
from datetime import date, timedelta


class Github():

    @staticmethod
    async def get_languages():
        last_30_days = str(date.today() - timedelta(days=30))
        langauges = {}
        # headers = {'Accept': ''}
        url = f'https://api.github.com/search/repositories'
        res = requests.get(url, {
            'q': f'created:>{last_30_days}',
            'sort': 'stars',
            'order': 'desc'
        })
        # print(res.json()['items'])
        for repo in res.json()['items']:
            lang = repo['language']
            if lang in langauges:
                langauges[lang]['name'] = lang
                langauges[lang]['number_of_repos'] += 1
                langauges[lang]['repos'].append(repo['svn_url'])
            else:
                langauges[lang] = {
                    'name': lang,
                    'number_of_repos': 1,
                    'repos': [repo['svn_url']]
                }
        return list(langauges.values())
