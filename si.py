# Simple Interest Calculator

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Input values
principal = float(1000)
rate = float("Enter the annual interest rate (in %): ")
time = float("Enter the time (in years): ")

# Calculate interest
interest = calculate_simple_interest(principal, rate, time)

# Display result
print(f"\nSimple Interest = {interest:.2f}")