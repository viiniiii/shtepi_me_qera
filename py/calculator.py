def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operators = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,

}
def calculator():
    num1 = float(input("Vendosni numrin e pare: "))
    should_continue = True
    while should_continue:
        num2 = float(input("Vendosni numrin e dyte: "))
        for key in operators:
            print (key)
        operator_symbol = input("Zgjidhni veprimin: ")
        rez = operators[operator_symbol](num1,num2)
        print(f"{num1} {operator_symbol} {num2} = {rez}")
        if input("Vendos 'y' per te vazhduar ose 'n' per te ndaluar: ") == 'y':
            num1 = rez
        else: 
            should_continue = False
            calculator()

calculator()