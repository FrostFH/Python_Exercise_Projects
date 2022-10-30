year = int(input("zadejte rok:\n"))

if year % 4 == 0 and year % 100 != 0:
    print(f"Rok {year} je přestupný")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"Rok {year} je přestupný")   
else:
    print(f"Rok {year} není přestupný")    