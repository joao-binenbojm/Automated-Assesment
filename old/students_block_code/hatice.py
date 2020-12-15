# Your code is here!
annual_salary = 120000
portion_saved = 0.1
total_cost = 1000000
down_payment = total_cost * 0.25
r = 0.04

current_savings = 0
n_months = 0
while current_savings < down_payment:
    n_months += 1
    current_savings += (r/12)*current_savings + portion_saved * (annual_salary/10)  # intentionally wrong calc
