# Voter Eligibility Program with free-form country and hidden ID/Passport rules

# Step 1: Check age
age = int(input("Enter your age: "))
if age < 18:
    print("You are not eligible to vote: Must be 18 years or older.")
    exit()  # Stop the program immediately

# Step 2: Ask for citizenship (free-form)
country = input("Enter your country of citizenship: ").strip().lower()
eligible_countries = ["kenya", "uganda", "tanzania"]
if country not in eligible_countries:
    print("You are not eligible to vote: Only Kenyan, Ugandan, or Tanzanian citizens are allowed.")
    exit()  # Stop the program immediately

# Step 3: Check ID or Passport number
id_number = input("Enter your ID number or Passport number: ").strip()
if not (id_number.isdigit() and len(id_number) == 10):
    print("You are not eligible to vote.")
else:
    print("Hongera! You qualify to be a voter.")
