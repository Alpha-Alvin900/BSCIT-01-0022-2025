# Bonus Calculator Program

# i) Ask user for their salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# ii) Determine bonus rate based on years of service
if years_of_service > 10:
    bonus_rate = 0.12   # 12%
elif years_of_service >= 6:
    bonus_rate = 0.10   # 10%
else:
    bonus_rate = 0.08   # 8%

# iii) Compute bonus amount
bonus = salary * bonus_rate

# iv) Compute net salary (salary + bonus)
net_salary = salary + bonus

# v) Display results
print("\n--- Bonus Calculation ---")
print(f"Years of Service: {years_of_service}")
print(f"Bonus Rate: {bonus_rate * 100:.0f}%")
print(f"Bonus Amount: {bonus:.2f}")
print(f"Net Salary (Salary + Bonus): {net_salary:.2f}")

