# Write a program q7_generate_payroll.py that reads the following information and prints a payroll statement

# Sample input:
# Enter name: Lim Ah Seng
# Enter number of hours worked weekly: 10
# Enter hourly pay rate: 6.75
# Enter CPF contribution rate(%): 20

# Sample output:
# Payroll statement for Lim Ah Seng
# Number of hours worked in week: 10
# Hourly pay rate: $6.75
# Gross pay = $67.50
# CPF contribution at 20% = $13.50
# Net pay = $54.00

name = str(input("Enter name: "))
hours = float(input("Enter number of hours worked weekly: "))
rate = float(input("Enter hourly pay rate: "))
cpf = float(input("Enter CPF contribution rate(%)"))

print("Payroll statement for " + name)
print("Number of hours worked in week: " + str(hours))
print("Hourly pay rate: $" + "{0:.2f}".format(rate))
print("Gross pay = $" + ("{0:.2f}".format(rate) * hours)) # can't multiply sequence by non-int of type 'float'
print("CPF contribution at 20% = $" + ("{0:.2f}".format(rate) * hours) / 100 * 20)
print("Net pay = $" + (("{0:.2f}".format(rate) * hours) - ("{0:.2f}".format(rate) * hours) / 100 * 20))
