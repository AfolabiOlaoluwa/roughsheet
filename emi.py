# Updated loan details
import pandas as pd

loan_amount = 10_000_000
interest_rate_annual = 0.05
loan_tenure_years = 5
loan_tenure_months = loan_tenure_years * 12
management_fee = loan_amount * 0.01

# Monthly interest rate
interest_rate_monthly = interest_rate_annual / 12

# Monthly repayment (EMI) formula: EMI = [P * r * (1+r)^n] / [(1+r)^n - 1]
emi = (loan_amount * interest_rate_monthly * (1 + interest_rate_monthly) ** loan_tenure_months) / \
      ((1 + interest_rate_monthly) ** loan_tenure_months - 1)

# Amortization schedule
schedule = []
outstanding_principal = loan_amount

for month in range(1, loan_tenure_months + 1):
    interest_payment = outstanding_principal * interest_rate_monthly
    principal_payment = emi - interest_payment
    closing_balance = outstanding_principal - principal_payment

    schedule.append({
        "Month": month,
        "Opening Balance": outstanding_principal,
        "Interest Payment": interest_payment,
        "Principal Payment": principal_payment,
        "Total Payment": emi,
        "Closing Balance": closing_balance
    })

    # Update outstanding principal
    outstanding_principal = closing_balance

# Convert to DataFrame
amortization_schedule_28 = pd.DataFrame(schedule)

# Calculate totals for summary
total_interest_paid = amortization_schedule_28["Interest Payment"].sum()
total_principal_paid = amortization_schedule_28["Principal Payment"].sum()
total_payments = amortization_schedule_28["Total Payment"].sum()

# Summary and file creation
file_path_28 = "~/PycharmProjects/roughsheet/data/las_28_percent.csv"
amortization_schedule_28.to_csv(file_path_28, index=False)

# Calculate the sum of the Total Payment column
print(f"Total Principal Paid: ₦{total_principal_paid:,.2f}")
print(f"Total Interest Paid: ₦{total_interest_paid:,.2f}")
print(f"Total Payments: ₦{total_payments:,.2f}")
# print(file_path_28)
