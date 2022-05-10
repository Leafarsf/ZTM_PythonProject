#Walrus is this := I can use this to assign variables as part of a larger expression ex:
a = 'hellooooooo'
if ((n :=len(a))> 10):
    print(f"Too long {n} elements")
while ((n :=len(a)) > 1):
    print(n)
    a = a[:-1]