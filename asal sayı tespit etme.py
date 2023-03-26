def asal(sayi):
    if sayi == 1:
        return False
    elif sayi== 2:
        return True
    else:
        for i in range (2,sayi):
            if (sayi % i == 0):
                return False
        return True
while True:
    sayi=int(input("Lütfen sayı girin\n"))
    
    if asal(sayi):
        print ("Sayı bir asal sayıdır.")
    else:
        print("Sayı asal değildir.")
