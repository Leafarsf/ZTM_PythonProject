#global is the keyword we use to assign a global parameter to a function. Ex:
total = 0
def count():
    global total
    total += 1
    return total
print(count())

