import os
from user import User
import taxes
import admin
net_income = 0.0

#TODO: Add more deductions
standard_deduction = 12200.0



gross_income = float(input('Enter your gross income: '))
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
# state = input('Enter your state: ')
# city = input('Enter your city: ')
zipcode = input('Enter your zipcode: ')
# address = input('Enter your address: ')
# phone_number = input('Enter your phone number: ')
# email = input('Enter your email: ')
# username = input('Enter your username: ')
# country = input('Enter your country: ')






def totalTaxes():
    total_taxes = taxes.IncomeTax(gross_income, zipcode).calculate()
    return total_taxes

# def netIncome():
#     net_income = gross_income - totalTaxes()
#     return net_income

if __name__ == '__main__':
    def main():
        taxes.IncomeTax(gross_income, zipcode, filing_status="'Single'").federalTax()
    main()