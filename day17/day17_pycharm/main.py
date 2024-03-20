class User:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers+=1
        user.following+=1


u1 = User("jayesh",34)
u2 = User("savan",1)

print(u1.follow(u2))


print(u1.following)
print(u1.followers)
