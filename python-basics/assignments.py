# Name : Clement Ngotho
# Date : 16/02/2026
# Program calculate the income tax

salary = int(input("Enter your salary:"))

if salary < 50000:
    tax = (2.5 * salary) / 100
    net_salary = salary - tax

print(f"Gross salary = {salary}")
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}")

