#different list functions
basket=[1,2,3,4,5]
#adding
new_basket = basket.append(100) #essa função muda a lista no lugar, não reproduz a lista novamente
print(new_basket)
print(basket)
#insertion
basket.insert(3,3.5)
print(basket)
#extending
basket.extend([101,102])
print(basket)
#removing
basket.pop(0) #removes anything that's at the end of it or at the location we've chosen and can be used to return a value
basket.remove(100) #we give the value that we want to remove
print(basket)
#clear
basket.clear()
print(basket)
