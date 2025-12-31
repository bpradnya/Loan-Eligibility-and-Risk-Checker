
def loan(P, r, n):
    """Calculate EMI and print loan details. Returns the EMI."""
    if (1 + r) ** n == 1: 
        EMI = P * r
    else:
        m=r/1200
        t=n*12
        EMI = (P * m * ((1 + (m)) ** (t))) / (((1 + m) ** (t)) - 1)
    total_pay = EMI * n* 12
    total_interest = total_pay - P
    print(f"EMI: {round(EMI, 2)}")
    print(f"Total Payment: {round(total_pay, 2)}")
    print(f"Total Interest to be paid: {round(total_interest, 2)}")
    return EMI

def check_eligibility_and_adjust(P, r, n, initial_emi):
    """Handle eligibility check and allow user to adjust loan parameters if needed."""
    monthly_income = float(input("Enter Your Monthly Income: "))
    existing_emi = float(input("Enter your Existing EMI (if any, else enter 0): "))
    max_allowed_emi = 0.4 * monthly_income
    available_emi = max_allowed_emi - existing_emi
    current_P = P
    current_n = n*12
    current_emi = initial_emi
    
    if available_emi >= current_emi:
        print("Congratulations! You are Eligible for the Loan")
        return current_emi, monthly_income, existing_emi, True, current_P, current_n
    
    else:
        print(f"Sorry! You are Not Eligible for this Loan")
        print(f"Your Maximum allowed EMI is: {round(available_emi, 2)}")
        
        while True:
            print("\nChoose a way to become Eligible:")
            print("1. Increase Tenure")
            print("2. Reduce Loan Amount")
            print("3. Exit without loan")
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == "1":
                current_n = float(input("Enter new Tenure (in years): "))
                current_emi = loan(current_P, r, (current_n))   
            elif choice == "2":
                current_P = float(input("Enter new Loan Amount: "))
                current_emi = loan(current_P, r, (current_n))   
            elif choice == "3":
                print("Loan application cancelled.")
                return None, monthly_income, existing_emi, False, current_P, current_n
            else:
                print("Invalid choice. Please try again.")
                continue
            if current_emi <= available_emi:
                print("You are now Eligible for the Loan!")
                return current_emi, monthly_income, existing_emi, True, current_P, current_n
            else:
                print(f"Still not eligible. Current EMI: {round(current_emi, 2)} > Max allowed: {round(available_emi, 2)}")
                print("Try adjusting again.\n")

def loan_risk(final_emi, monthly_income, existing_emi):
    """Assess loan risk based on total EMI burden."""
    total_emi = final_emi + existing_emi
    emi_ratio = total_emi / monthly_income
    
    if emi_ratio <= 0.30:
        print("Risk Level: LOW RISK")
    elif emi_ratio <= 0.40:
        print("Risk Level: MEDIUM RISK")
    else:
        print("Risk Level: HIGH RISK")

# Main Program
print("=== Loan EMI Calculator ===\n")
P = float(input("Enter Loan Amount (Principal): "))
r = float(input("Enter Annual Interest Rate : ")) 
n = float(input("Enter Tenure (in Years): "))

print("\n--- Initial Loan Calculation ---")
initial_emi = loan(P, r, n)

print("\n--- Eligibility Check ---")
result = check_eligibility_and_adjust(P, r, n, initial_emi)

if result[3]:  # if eligible
    final_emi, monthly_income, existing_emi, is_eligible, current_P, current_n = result
    print("\n--- Loan Risk Assessment ---")
    loan_risk(final_emi, monthly_income, existing_emi)
else:
    print("Risk not evaluated since loan is not eligible.")