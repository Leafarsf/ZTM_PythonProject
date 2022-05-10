#We can create descriptions for the functions
def test(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)
test("Hi")
help(test) #this helps to find out what the function does
#or
print(test.__doc__)