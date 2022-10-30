print("Vítejte na horské dráze")
height = int(input("Jaká je vaše výška v cm?\n"))

bill = 0

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je váš věk?\n"))
    if age <= 12:
        bill = 50
        print("Cena lístku je: 50Kč.")
    elif age < 18:
        bill = 100
        print("Cena lístku je 100Kč. ")    
    else:
        bill = 150
        print("Cena lístku je: 150Kč.")

    photo = input("Chcete se nechat vyfotit?\n")
    if photo == "ano":
        bill += 40
    print(f"Celková cena k zaplacení je {bill} Kč. ")    

else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")