def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / (height (m) ^ 2)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_positive_float(prompt):
    """Get a positive float input from the user"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Welcome to the BMI Calculator!")
    
    weight = get_positive_float("Please enter your weight in kilograms: ")
    height = get_positive_float("Please enter your height in meters: ")
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()