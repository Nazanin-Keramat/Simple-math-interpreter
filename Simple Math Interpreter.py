def main():
    # Prompt the user for an arithmetic expression
    res = input("Type your expression please (e.g., 1 + 1): ").strip().split(" ")
    
    x = res[0]
    op = res[1]
    y = res[2]
    
    x = int(x)
    y = int(y)

    result = None

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    else:
        print("Invalid operator")
        return

    print(f"{result:.1f}")
main()
