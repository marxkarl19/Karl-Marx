def categorize_car_brands(car_brands):
    vowel_start_brands = []
    consonant_start_brands = []

    for brand in car_brands:
        first_letter = brand[0].lower()

        category = "vowel" 
      if first_letter in "aeiou" 
        else "consonant"
        (vowel_start_brands 
      if category == "vowel" 
        else consonant_start_brands).append(brand)
        print(f"{brand} starts with a {category}.")

    return vowel_start_brands, consonant_start_brands

def display_final_lists(vowel_start_brands, consonant_start_brands):
    print("\nCar brands starting with a vowel:", vowel_start_brands)
    print("Car brands starting with a consonant:", consonant_start_brands)

car_brands = ["Audi", "BMW", "Dodge", "Elantra", "Ford", "Honda", "Infiniti", "Jaguar"]

vowel_brands, consonant_brands = categorize_car_brands(car_brands)
display_final_lists(vowel_brands, consonant_brands)

