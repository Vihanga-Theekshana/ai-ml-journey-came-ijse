def safe_input(prompt, default=""):
    try:
        return input(prompt)
    except EOFError:
        print(f"{prompt}{default} (default)")
        return default


def safe_int_input(prompt, default=0):
    s = safe_input(prompt, str(default))
    try:
        return int(s)
    except Exception:
        return default


def main():
    # Cell 1
    num = safe_input("enter number : ", default="")
    print(num)

    # Cell 2 (expects int)
    num = safe_int_input("enter value :", default=0)
    print(num * 10)

    # Cell 3
    num = safe_input("enter value", default="")
    print(f'num is {num}')

    # Cell 4
    a = 5
    b = 3
    print("value of a is ", a, "value of b is ", b)

    # Cell 6 - f-string example
    a = 10
    b = 20
    print(f'a is {a} b is {b}')

    # Cell 7 - formatting
    accuracy = 1.87646
    print(f'accuracy as persentage {accuracy:.2%}')
    print(f'accuracy as 3 decimal places {accuracy:.3f}')
    print(f'accuracy as 3 decimal places {accuracy:.3}')

    # Cell 8 - boolean logic
    a = 6
    b = 5
    print(not (a == 5 or b == 5))

    # Cell 9 - set type
    s = {1, 2, 3}
    print(type(s))

    # Cell 10 - tuple -> list -> tuple
    tuple_value = (1, 2, 3, 4)
    new_value = list(tuple_value)
    new_value.append(50)
    new_value2 = tuple(new_value)
    print(new_value2)


if __name__ == "__main__":
    main()
