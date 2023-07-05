import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'xxxxxxxxxxxx' #https://github.com/settings/tokens

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    
    def createRepository(self, name):
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        
        response = requests.post(self.api_url+'/user/repos', headers=headers, json={
            "name": name,
            "description": "Text repo",
            "homepage": "http://cankoyuncu.com/",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()    

while True:
    secim = input('1-Find User\n2-Get Repo\n3-Create Repo\n4-Exit\nSecim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"Name: {result['name']} Public repos:{result['public_repos']} follower: {result['followers']}")
        if secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        if secim =='3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Yanlis secim yaptiniz!')
