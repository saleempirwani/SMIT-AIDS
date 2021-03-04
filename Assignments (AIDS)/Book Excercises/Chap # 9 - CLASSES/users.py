class User:
    
    login_attempts = 0
    
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def des_user(self):
        print('first name', self.fname, 'last name', self.lname, 'age:', self.age)
        
    def greet_user(self):
        print('Hello', self.fname, self.lname)
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        

class Privileges:
    
    privileges = ['can add post', 'can delete post', 'can ban user']
    
    def __init__(self):
        pass

    def show_privileges(self):
        for x in self.privileges:
            print(x)


class Admin(User):

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.privileges = Privileges()
        
    def des_user(self):
        print('first name', self.fname, 'last name', self.lname, 'age:', self.age)
        
    def greet_user(self):
        print('Hello', self.fname, self.lname)