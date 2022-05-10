#parameters, when we use variables inside of a function
def say_hello(name, emoji):
    print(f"Hello, {name} {emoji}")

#arguments - the actual values we provide to a function
name = str(input("Insert your name: "))
emoji = str(input("Insert a smiley emoji: "))
say_hello(name,emoji)

#keyword arguments
say_hello(emoji = ':)', name = 'Bibi')
#I can also give default arguments, in case there was no data input for the arguments
#say_hello(name='Darth Vader', emoji = ':S')