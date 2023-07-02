import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepo:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)
            print(self.users)


    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("User created!")

    def login(self, username, password):    
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login succesfull!')
                return
        print('Your login details are incorrect. please try again or sign up.')

        
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logout is succesfull!')
    
    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Failed to login!')

    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(list, file)

repo = UserRepo()

while True:
    print('Menu'.center(50,'*'))
    secim = input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nYour Choice: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repo.register(user)
        elif secim == '2':
            if repo.isLoggedIn:
                print('You are already logged in!')
            else:
                username = input('username: ')
                password = input('password: ')
                repo.login(username, password)

        elif secim == '3':
            repo.logout()
        elif secim == '4':
            repo.identity()
        else:
            print ('Invalid login information, please try again.')