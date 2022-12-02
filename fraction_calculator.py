# Make four operations with fractions.

print("\033[33m=== Fraction Calculator ===\033[0m")

print("What operation do you want?")
print("[1] Sum")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")
operation = input("Your choice: ")
while int(operation) not in range(1, 5) or len(operation) != 1:
    print("\033[31mInvalid operation.\033[0m")
    operation = input("Your choice: ")
operation = int(operation)

first_fraction = {}
first_fraction["numerator"] = int(input("First fraction numerator: "))
first_fraction["denominator"] = int(input("First fraction denominator: "))

second_fraction = {}
second_fraction["numerator"] = int(input("Second fraction numerator: "))
second_fraction["denominator"] = int(input("Second fraction denominator: "))


def is_equal_denomitors(first, second):
    return True if first["denominator"] == second["denominator"] else False


def to_sum(first, second):
    result = {}
    if is_equal_denomitors(first, second):
        result["numerator"] = first["numerator"] + second["numerator"]
        result["denominator"] = first["denominator"]
        return result

    result["numerator"] = (
        (first["numerator"] * second["denominator"]) +
        (second["numerator"] * first["denominator"])
    )
    result["denominator"] = first["denominator"] * second["denominator"]
    return result


def to_substract(first, second):
    result = {}
    if is_equal_denomitors(first, second):
        result["numerator"] = first["numerator"] - second["numerator"]
        result["denominator"] = first["denominator"]
        return result

    result["numerator"] = (
        (first["numerator"] * second["denominator"]) -
        (second["numerator"] * first["denominator"])
    )
    result["denominator"] = first["denominator"] * second["denominator"]
    return result


def to_multiplication(first, second):
    result = {}
    result["numerator"] = first["numerator"] * second["numerator"]
    result["denominator"] = first["denominator"] * second["denominator"]
    return result


def to_division(first, second):
    result = {}
    result["numerator"] = first["numerator"] * second["denominator"]
    result["denominator"] = first["denominator"] * second["numerator"]
    return result


def to_print_result(first, second, operation:str, result):
    print("\033[32m===\033[0m")
    print(f'Result: ({first["numerator"]} / {first["denominator"]}) {operation} ({second["numerator"]} / {second["denominator"]}) = (\033[32m{result["numerator"]} / {result["denominator"]}\033[0m)')
    print("\033[32m===\033[0m")


if operation == 1:
    result = to_sum(first_fraction, second_fraction)
    to_print_result(first_fraction, second_fraction, '+', result)

if operation == 2:
    result = to_substract(first_fraction, second_fraction)
    to_print_result(first_fraction, second_fraction, '-', result)

if operation == 3:
    result = to_multiplication(first_fraction, second_fraction)
    to_print_result(first_fraction, second_fraction, 'x', result)

if operation == 4:
    result = to_division(first_fraction, second_fraction)
    to_print_result(first_fraction, second_fraction, '/', result)

