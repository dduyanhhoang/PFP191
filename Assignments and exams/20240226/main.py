def get_employee(n: int) -> dict:
    employees = dict()

    for _ in range(n):
        id = input("Enter id: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        employees[id] = [name, int(age), float(salary)]


def sort_employee(e: dict) :
    pass


def main():
    num_employees = 10
    employees = get_employee(10)


if __name__ == "__main__":
    main()