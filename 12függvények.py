from unittest import result


def print_employee_data(name: str, year_of_birth: int, actual_year: int):
    print("Name:", name)
    print("Age:", actual_year - year_of_birth)

def calculate_age(year_of_birth: int, actual_year: int):
    return actual_year - year_of_birth


print_employee_data("John", 1970, 2022)
print_employee_data("Jack", 1980, 2022)
print_employee_data("Jane", 1990, 2022)

print(calculate_age(2012, 2022))

result = calculate_age(2011, 2022)
print(f"A gyerek {result} éves")

