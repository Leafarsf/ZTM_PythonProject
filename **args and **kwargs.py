#*args and **kwargs
#*args are used to tell a funcion that we've defined that we can use more than a parameter ex:
def count_number(*args, **kwargs):
    return sum(args) + 100 + sum(items in kwargs.values())
print(count_number(5,5)) #I can put as many as I want here
#**kwargs are used to define keywords inside of a function
print(count_number(5,5, num1=2, num2=2))

#Rules: 1st params, 2nd *args, 3rd default params, **kwargs