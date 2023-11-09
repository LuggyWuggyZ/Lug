#Program 8 Basic ; Luigi Zemlickas ; Matteo Marchetti; 11/8/2023

# Prompt the user to enter outstanding debt on their credit card
debt = float(input("Outstanding balance on your credit card: "))

# Prompt the user to enter the annual interest rate as a percentage
interest_rate = float(input("Annual interest rate (as a percentage): "))

# Prompt the user to enter the minimum monthly payment as a decimal
monthly_payment = float(input("Minimum monthly payment (as a decimal): "))

# Function to calculate the number of months required to pay off the debt
def calculatePayments(debt, interestRate, monthlyPayment, monthsRequired=0):
    # Base Case
    if debt <= 0:
        return monthsRequired
    # Recursive Step
    else:
        # Calculate the monthly interest based on the annual interest rate
        interest = debt * (interestRate / 12 / 100)
        # Add the interest and subtract the monthly payment from the debt
        debt += interest
        debt -= monthlyPayment
        # Increment the number of months required
        monthsRequired += 1
        # Recursively call the function for the next month
        return calculatePayments(debt, interestRate, monthlyPayment, monthsRequired)

# Calculate the number of months to pay off the debt and display the result
print("It will take " + str(calculatePayments(debt, interest_rate, monthly_payment)) + " months to pay off the debt.")
