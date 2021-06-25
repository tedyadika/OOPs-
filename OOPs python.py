class Player:

    def __init__(self, name , age):
        self.name = name
        self.age = age

        if  age < 18:
            print( 'Warning you are not old enough to play')
             
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age 


    def fight (self):
        print (self.name + ' is fighing ')


    def jump(self):
        print(self.name+ ' is jumping ')
    
    def stop(self):
        print(self.name + ' is Stoping')


