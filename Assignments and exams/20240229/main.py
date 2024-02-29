import logging


def sort_employee(e: dict) -> list:
    return sorted(e.items(), key=lambda x: x[1][1], reverse=True)


def get_emp_salary(prompt: str) -> float:
    while True:
        try:
            salary = input(prompt)
            try:
                salary = float(salary)
            except ValueError:
                raise ValueError("Salary must be a number")
            if salary < 0:
                raise ValueError("Salary must be a positive number")
            return salary
        except ValueError as e:
            logging.error(f"An error occurred while getting employee salary: {e}")
            continue


def get_employee(n: int) -> dict:
    emp_num = 0
    employees = dict()

    while emp_num < n:
        try:
            emp_code = input("Enter id: ")
            if emp_code in employees:
                raise ValueError("Employee id already exists")
            
            name = input("Enter name: ")
            salary = get_emp_salary("Enter salary: ")
            
            emp_num += 1
            employees[emp_code] = [name, salary]
        except ValueError as e:
            logging.error(f"An error occurred while getting employees: {e}")
            continue
    
    return employees


def main():
    while True:
        try:
            num_employees = input("Enter the number of employees: ")
            try:
                num_employees = int(num_employees)
            except ValueError:
                raise ValueError("Number of employees must be a number")
            
            if num_employees < 0:
                raise ValueError("Number of employees must be a positive number")

            employees = get_employee(num_employees)

            sorted_employees = sort_employee(employees)
            for employee in sorted_employees:
                print(f"Employee: {employee[0]}, Salary: {employee[1][1]}, Name: {employee[1][0]}")
            
            exit(0)
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted by the user. Exiting.")
            exit(0)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            continue


if __name__ == "__main__":
    main()
