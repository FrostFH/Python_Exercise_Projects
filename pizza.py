
# Návštěvník si nejdříve zvolí velikost pizzy (S, M, L). Za velikost S se platí 100 Kč, za M 150 Kč a za L 200 Kč.
# Poté se zeptáte, zda chce feferonky. Pokud ano, tak u velikosti S se bude platit 20 Kč navíc a u velikostí M a L 30 Kč navíc.
# Poté se ještě zeptáte, zda chce návštěvník sýr navíc. Pokud ano, tak si připlatí dalších 15 Kč.



choice = input("Jakou chcete velikost pizzy? Na výběr je S, M, L \n")

s = 100
m = 150
l = 200

peppers_s = 20
peppers_m = 30
peppers_L = 30
cheese_price = 15

if choice == "S":
    print(f"Cena za velikost S je {s}Kč\n")
    peppers = input("Budete chtít feferonky? ano/ne\n")
    cheese = input("Budete chtít navíc sýr? ano/ne\n")

    if peppers =="ano" and cheese == "ano":
        price = s + peppers_s + cheese_price
        print(f"Cena za pizzu velikosti S s feferonkami a sýrem je {price}Kč\n")
    elif peppers == "ano" and cheese =="ne":
        price = s + peppers_s
        print(f"Cena za pizzu velikosti S s feferonkami je {price}Kč")
    elif peppers == "ne" and cheese =="ano":
        price = s + cheese
        print(f"Cena za pizzu velikosti S je {price}Kč ")
    else:
        print(f"Cena za pizzu je {s}") 

elif choice == "M":
    print(f"Cena za velikost M je {m}Kč\n") 
    peppers = input("Budete chtít feferonky? ano/ne\n")
    cheese = input("Budete chtít navíc sýr? ano/ne\n")

    if peppers == "ano" and cheese == "ano":
        price = m + peppers_m + cheese_price     
        print(f"Cena za pizzu s feferonkami a sýrem je {price}Kč \n")
    elif peppers == "ano" and cheese == "ne":
        price = m + peppers_m
        print(f"Cena za pizzu s feferonkami je {price}Kč\n")
    elif peppers == "ne" and cheese == "ano":
        price = m + cheese_price
        print(f"Cena za pizzu se sýrem je {price}Kč\n")
    else:
        print(f"Cena za pizzu velikosti M je {m}Kč\n")

else:
    print(f"Cena za velikost L je {l}Kč\n")
    peppers = input("Budete chtít feferonky? ano/ne\n")
    cheese = input("Budete chtít navíc sýr? ano/ne\n")

    if peppers == "ano" and cheese =="ano":
        price = l + peppers_L + cheese_price
        print(f"Cena za pizzu s ferefonkami a sýrem je {price}Kč\n")
    elif peppers == "ano" and cheese == "ne":
        price = l + peppers
        print(f"Cena za pizzu s feferonkami je {price}Kč\n")
    elif peppers == "ne" and cheese =="ano":
        price = l + cheese_price
        print(f"Cena za pizzu se sýrem je {price}Kč\n")        
    else:
        print(f"Cena za pizzu velikosti L je {l}Kč.")    