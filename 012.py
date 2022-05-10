basket = ['a','b','x','c','d','e','d',]
#basket.sort() #it sorts the list in order
print(basket)
#or
print(sorted(basket)) #this one does not change the list like basket.sort, it creates a new copy like
#new_basket = sorted(basket)
#to copy
print(basket.copy())
#to reverse the list
basket.sort()
basket.reverse() #or print(basket[::-1)
print(basket)