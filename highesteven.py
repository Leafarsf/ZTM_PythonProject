def highest_even(li):
    evens_list = []
    for n in li:
        if n % 2 == 0:
            evens_list.append(n)
    return max(evens_list)

print(highest_even([10,1,2,3,4,8,11]))