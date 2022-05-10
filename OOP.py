# OOP
import sys
class PlayerCharacter:
    #Class Object Attribute, not dynamic, static, unlike the other ones after it
    membership = True
    def __init__(self, name='Anonymous', age=0):
        if(self.membership):
            self.name = name  # attribute
            self.age = age  # attribute

    def shout(self):
        if (self.age > 18):
            print(f"Welcome {self.name}, you are {self.age}. Are you ready to play?")
        else:
            print("You can't play this game according to the law")
            sys.exit('bye')



player1 = PlayerCharacter(input("Insert Player 1 name: "), int(input("Insert Player 1 age: ")))
player2 = PlayerCharacter(input("Insert Player 2 name: "), int(input("Insert Player 2 age: ")))

player1.shout()
player2.shout()
jogar = (input("Type Y or N: "))
if jogar == "y" or jogar == "Y":
    print("*-*" * 10)
    print("Bem vindo ao mundo mágico!")
    print("*-*" * 10)
elif jogar == 'N' or jogar == "n":
        print("*-*" * 10)
        print("Jogo encerrado! Até mais!")
        print("*-*" * 10)
else:
    print("Seleção inválida. Tente novamente.")

# self refers to the PlayerCharacter, self.name refers to the name of it
