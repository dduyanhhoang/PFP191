def get_employee(n: int) -> dict:
    emp_num = 0
    employees = dict()

    while emp_num < n:
        try:
            emp_code = input("Enter id: ")
            if emp_code in employees:
                raise ValueError("Employee id already exists")
            
            name = input("Enter name: ")

            salary = input("Enter salary: ")
            try:
                salary = float(salary)
            except ValueError:
                raise ValueError("Salary must be a number")
            
            if salary < 0:
                raise ValueError("Salary must be a positive number")
            
            emp_num += 1
            employees[emp_code] = [name, salary]
        except ValueError as e:
            print(e)
            continue
    
    return employees

def sort_employee(e: dict) -> list:
    return sorted(e.items(), key=lambda x: x[1][1], reverse=True)


def main():
    try:
        num_employees = input("Enter the number of employees: ")
        try:
            num_employees = int(num_employees)
        except ValueError:
            raise ValueError("Number of employees must be a number")

        employees = get_employee(num_employees)

        sorted_employees = sort_employee(employees)
        for _ in sorted_employees:
            print(f"Employee: {_[0]}, Salary: {_[1][1]}, Name: {_[1][0]}")
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupted by the user. Exiting.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
