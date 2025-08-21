import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

my_cal_dictionary = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
"We are only storing function not using so just write down the names:"
def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("Please input the first number: "))

    while should_accumulate:

        for key in my_cal_dictionary:
            print(key)
        operator = input("Please enter the mathematical operator: ")

        second_number = float(input("Please input the second number: "))
        answer = my_cal_dictionary[operator](first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {answer}")

        user_continue = input(f"Do you want to continue operations with {answer}, Type 'yes' or 'no' ")

        if user_continue == "yes":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
