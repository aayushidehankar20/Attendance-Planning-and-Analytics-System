# COCOMO Cost Estimation
# Project: Attendance Planning and Analytics System

print("==============================================")
print("       COCOMO COST ESTIMATION")
print("==============================================")
print("Project: Attendance Planning and Analytics System")
print()

# -------------------------------
# Input
# -------------------------------

loc = float(input("Enter estimated Lines of Code (LOC): "))

# Convert LOC into KLOC
kloc = loc / 1000

# -------------------------------
# Basic COCOMO - Organic Mode
# -------------------------------

# Effort in Person-Months
effort = 2.4 * (kloc ** 1.05)

# Development Time in Months
development_time = 2.5 * (effort ** 0.38)

# Average Number of People
staff = effort / development_time

# Cost per Person-Month
cost_per_person_month = float(
    input("Enter cost per person-month (₹): ")
)

# Total Project Cost
total_cost = effort * cost_per_person_month

# -------------------------------
# Display Results
# -------------------------------

print()
print("==============================================")
print("             COCOMO RESULTS")
print("==============================================")

print(f"Estimated LOC          : {loc:.0f}")
print(f"Estimated KLOC         : {kloc:.3f}")
print(f"Effort                 : {effort:.2f} Person-Months")
print(f"Development Time       : {development_time:.2f} Months")
print(f"Average Team Size      : {staff:.2f} Persons")
print(f"Estimated Project Cost : ₹{total_cost:,.2f}")

print("==============================================")
print("COCOMO estimation completed successfully.")
print("==============================================")
