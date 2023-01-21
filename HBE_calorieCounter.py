#Function for Harris-Benedict equation

def calculate_calories(age, weight, height, sex, activity_level):
  #Calculate BMR
  height_feet, height_inches = height
  BMR = 10 * weight + 6.25 * (height_feet * 12 + height_inches) - 5 * age
  if sex == "m":
    BMR += 5
  else:
    BMR -= 161

  #Adjust BMR for activity level
  if activity_level == 1:
    calories = BMR * 1.2
  elif activity_level == 2:
    calories = BMR * 1.375
  elif activity_level == 3:
    calories = BMR * 1.55
  elif activity_level == 4:
    calories = BMR * 1.725
  else:
    calories = BMR * 1.9

  return round(calories)

#Convert to grams function
def convert_macros_to_grams(calories, protein_percent, carb_percent, fat_percent):
    protein_grams = round(calories * protein_percent / 4)
    carb_grams = round(calories * carb_percent / 4)
    fat_grams = round(calories * fat_percent / 9)
    return protein_grams, carb_grams, fat_grams

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
          break
    return value

def get_non_negative_int_one_to_five(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value <= 0:
            print("Sorry, your response must be a number from 1-5.")
            continue
        elif value > 5:
            print("Sorry, your response must be a number from 1-5.")
            continue
        else:
            break
    return value

def get_single_letter(prompt):
    while True:
        try:
            value = str(input(prompt))
        except StringError:
            print("Sorry, I didn't understand that.")
            continue
        if value == 'm':
          break
        elif value == 'f':
          break
        else:
          continue
    return value
#GetInput

print("Welcome, please enter your info.")
age = get_non_negative_int("Age: ")
weight = get_non_negative_int("Weight in lbs: ")
h1 = get_non_negative_int("Height(feet): ")
h2 = get_non_negative_int("height(inches): ")
height = (h1,h2) #(feet, inches)

sex = get_single_letter("Sex (m or f):")

activity_level = get_non_negative_int_one_to_five('1 being couch potato and 5 being elite athlete... \n How active are you? (1-5): ')

#positve number for caloric surplus; negaitve number for caloric defict
cal_imbalance = get_int("What is you desired caloric surplus or defict? \n *write a positive value for surplus \n *write a negative value for defict: ") 


#Edit these percentages to fit your desired workout/ nutrition goal 
#(I'm carb heavy for runing long distance/ I'll change to protien heavy for weightlifting)
protein_percent = 0.35
carb_percent = 0.45
fat_percent = 0.20

#will let you know if your percentages don't add to 100%
if protein_percent + carb_percent + fat_percent != 1:
  print("Your percentages do not equal to 100%")
  print("Your percentages add up to: ", str(round((protein_percent + carb_percent + fat_percent)*100))+'%')



#get you calories
calories = calculate_calories(age, weight, height, sex, activity_level)

#get yo grams bby
protein_grams, carb_grams, fat_grams = convert_macros_to_grams(calories, protein_percent, carb_percent, fat_percent) 

print(" ")
print(" ")
print("Daily caloric needs: ", calories)
print("Daily caloric needs with deficit or surplus: ", calories + cal_imbalance)
print("Daily protien needs in grams: ", protein_grams)
print("Daily carb needs in grams: ", carb_grams)
print("Daily fat needs in grams: ", fat_grams)
print(" ")
print(" ")
