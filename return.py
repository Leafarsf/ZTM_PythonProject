#return is used to return the result back to the caller, a function always has to return!
def sum(num1,num2):
    return num1 + num2
n1 = int(input("Insira um número qualquer: "))
n2 = int(input("Insira outro número: "))
print(sum(n1,n2))