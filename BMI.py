weight = float(input("Zadejte vaší váhu v Kg:\n"))
height = float(input("zadejte svou výšku v metrech:\n"))

BMI = round(weight / (height ** 2),1)


if BMI <= 18.5:
    print(f"Vaše BMI je {BMI}, tedy máte podváhu.")
elif BMI > 18.5 and BMI <= 24.9:
    print(f"Vaše BMI je {BMI}, tedy vše v normalu.")
elif BMI >= 25 and BMI <= 29.9:
    print(f"Vaše BMI je {BMI}, máte nadváhu. ")
elif BMI >= 30 and BMI <= 34.9:
    print(f"Vaše BMI je {BMI}, máte obezitu.") 
else:
    print("Máte extrémní obezitu")
