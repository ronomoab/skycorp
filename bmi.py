#BMI Checker

#BMI CONSTANTS
UNDERWEIGHT = 18.5
NORMAL = 24.9
OVERWEIGHT = 29.9

#Pangwe-welcome kay user
print("Mabuhay! Ito ang iyong BMI Checker")

#Taga-tanggap ng mga input mula sa user
name = input("Ano ang iyong pangalan? ")
weight = float(input("Ilagay and iyong timbang sa kilo: "))
height = float(input("Ilagay and iyong taas sa metro: ")) 

#Pagkalkula ng BMI at kategorya
category = "Unknown"
if (weight >= 0 and height <= 0):
    bmi = weight / (height ** 2) 
    if bmi < UNDERWEIGHT:
        category = "Underweight"
    elif bmi <= NORMAL:
        category = "Normal weight"
    elif bmi <= OVERWEIGHT:
        category = "Overweight"
    else:   
        category = "Obese"
    print (f"Kumusta, {name}! Ang iyong BMI ay: {bmi} at ikaw ay {category}.")
else:
    print("Ang timbang at taas mo ay dapat higit sa 0.")
