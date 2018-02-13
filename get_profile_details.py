import json
import requests

GITHUB_API_TOKEN = 'YOUR PERSONAL GITHUB DEVELOPER API TOKEN'

def get_advanced_insights_for_github(url):
    profile_url = url
    headers = {'Authorization': 'token %s' %GITHUB_API_TOKEN}
    if profile_url is not None and profile_url:
        github_user_name = str(profile_url).split('github.com/', 1)[1]
        if github_user_name is not None and github_user_name:
            github_api = 'https://api.github.com/users/' + str(github_user_name)
            try:
                github_response = json.loads(requests.get(github_api, headers=headers).content)
                number_of_followers = github_response['followers']
                public_repos = github_response['public_repos']
                git_hub_repo_url = github_api + str('/repos')
                github_repos = json.loads(requests.get(git_hub_repo_url, headers=headers).content)
                repo_list = []
                urls = []
                for repo in github_repos:
                    if (repo['fork'] == False):
                        urls.append([repo['name'], repo['languages_url']])
                        detail = {
                            'repo_id': repo['id'],
                            'repo_name': repo['name'],
                            'stargazers_count': repo['stargazers_count'],
                            'watchers_count': repo['watchers_count'],
                            'language': repo['language'],
                            'forks': repo['forks']
                        }
                        repo_list.append(detail)

                response = {
                    'username': github_user_name,
                    'number_of_followers': number_of_followers,
                    'public_repos': public_repos,
                    'repo_list': repo_list
                }
            except Exception as e:
                return e
    return ({'result': response})

if __name__ == "__main__":
    github_profile_url = 'www.github.com/ajoevarghese'
    print (get_advanced_insights_for_github(github_profile_url))
