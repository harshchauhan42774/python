
def emi(p, r, t):
    r = r / 12 / 100  # Convert annual rate to monthly and percentage to decimal
    t = t * 12  # Convert years to months
    e = p * r * (pow(1 + r, t) / (pow(1 + r, t) - 1))
    return e

principle = float(input('Enter principal amount: '))
rate = float(input('Enter annual interest rate (in percentage): '))
time = float(input('Enter loan duration in years: '))

monthly_emi = emi(principle, rate, time)
print('Monthly EMI is:', monthly_emi)


#output
# Enter principal amount: 500
# Enter annual interest rate (in percentage): 1
# Enter loan duration in years: 1
# Monthly EMI is: 41.892705777902634