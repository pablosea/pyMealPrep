#Function fo Harris-Benedict equation
def calculate_calories(age, weight, height, gender, activity_level):
  #Calculate BMR
  height_feet, height_inches = height
  BMR = 10 * weight + 6.25 * (height_feet * 12 + height_inches) - 5 * age
  if gender == "male":
    BMR += 5
  else:
    BMR -= 161

  #Adjust BMR for activity level
  if activity_level == "sedentary":
    calories = BMR * 1.2
  elif activity_level == "lightly active":
    calories = BMR * 1.375
  elif activity_level == "moderately active":
    calories = BMR * 1.55
  elif activity_level == "very active":
    calories = BMR * 1.725
  else:
    calories = BMR * 1.9

  return calories

#Convert to grams function
def convert_macros_to_grams(calories, protein_percent, carb_percent, fat_percent):
    protein_grams = calories * protein_percent / 4
    carb_grams = calories * carb_percent / 4
    fat_grams = calories * fat_percent / 9
    return protein_grams, carb_grams, fat_grams

#Hard code your variables lol
age = 0
weight = 0
height = (0,0) #(feet, inches)
gender = "male"
activity_level = "very active"
cal_imbalance = 0 #positve number for caloric surplus; negaitve number for caloric defict 

#Edit these percentages to fit your desired workout/ nutrition goal 
#(I'm carb heavy for runing long distance/ I'll change to protien heavy for weightlifting)
protein_percent = 0.35
carb_percent = 0.50
fat_percent = 0.25

if protein_percent + carbon_percent + fat_percent != 1:
  print("Your percentages do not equal to 100%")

calories = calculate_calories(age, weight, height, gender, activity_level)
protein_grams, carb_grams, fat_grams = convert_macros_to_grams(calories+cal_imbalance, 0.35, 0.5, 0.25) #

print(" ")
print(" ")
print(" ")
print("Daily caloric needs: ", calories-cal_imbalance)
print("Daily protien needs in grams: ", protein_grams)
print("Daily carb needs in grams: ", carb_grams)
print("Daily fat needs in grams: ", fat_grams)
print(" ")
print(" ")
