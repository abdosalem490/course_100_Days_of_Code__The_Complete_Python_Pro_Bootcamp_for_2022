# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightFloat = float(height)
weightFloat = float(weight)

BMI = int((weightFloat / (heightFloat ** 2)))

print(BMI)