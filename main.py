import os
from user import User
import taxes
from admin import traditional_401k_match_ratio, traditional_401k_match

net_income = 0.0

print('Welcome to Oco.vn - Where Money Go')
print('*********************************')


gross_income = float(input('Enter your gross income: '))
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
state = input('Enter your state: ')
# city = input('Enter your city: ')
# zipcode = input('Enter your zipcode: ')
# address = input('Enter your address: ')
# phone_number = input('Enter your phone number: ')
# email = input('Enter your email: ')
# username = input('Enter your username: ')
# country = input('Enter your country: ')


def max401k():
    global gross_income
    max_401k = 0.0
    employer_contribution = 0.0
    employee_contribution = 0.0

    employer_contribution = gross_income * traditional_401k_match_ratio * traditional_401k_match
    
    employee_contribution = gross_income * traditional_401k_match

    gross_income -= employee_contribution

    max_401k = employer_contribution + employee_contribution
    print(max_401k)
    return max_401k



def maxRothIRA(net_income):
    max_RothIRA = 0.0
    max_RothIRA = 6500
    if net_income > max_RothIRA:
        net_income -= max_RothIRA
    else:
        net_income -= net_income
    return max_RothIRA

def maxHSA():
    global gross_income
    max_HSA = 0.0
    max_HSA = 3500
    if gross_income > max_HSA:
        gross_income -= max_HSA
    else:
        gross_income -= gross_income

    return max_HSA



def totalTaxes():
    state_tax = taxes.stateTax(gross_income, state)
    federal_tax = taxes.federalTax(gross_income)
    total_tax = state_tax + federal_tax
    return total_tax

# def netIncome():
#     net_income = gross_income - totalTaxes()
#     return net_income

if __name__ == '__main__':
    def main():
        max401k()

    

    main()