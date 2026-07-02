#Challenge: BMI Calculator (Imperial → Metric)
#BMI is calculated as:
#BMI = weight (kg) / height (m)²
#Print = Weight: 72.57 kg, Height: 1.75 m, BMI: 23.63

weight_lbs = 160
height_ft = 5
height_in = 9

#weight_kg — convert pounds to kg (1 lb = 0.453592 kg)
#height_total_inches — combine feet and inches into total inches (1 ft = 12 in)
#height_m — convert total inches to meters (1 inch = 0.0254 m)
#bmi — using the formula above (remember: height squared — you can use ** 2 in Python for that)

weight_kg = (weight_lbs * 0.453592)
height_total_inches = (height_ft * 12) + height_in
height_m = (height_total_inches * 0.0254)
bmi = (round(weight_kg / (height_m ** 2), 2))

print(f"Your Height is {round(height_m, 2)}m")
print(f"Your Weight is {round(weight_kg, 2)}kg")
print(f"Your BMI is {bmi}")
