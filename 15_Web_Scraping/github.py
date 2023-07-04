import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(sefl, username):***************
        requests.get(self.api_url+'/users')
    
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
            pass
        if secim =='3':
            pass
        else:
            print('Yanlis secim yaptiniz!')