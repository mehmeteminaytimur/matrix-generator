matrisListesi  = []
while True:
    
    try:    
        satirSayisi = int(input("Satır elaman sayısı: "))
        if (satirSayisi < 1 or satirSayisi > 5):
            print("Girilen sayı 1-5 arasında bir tam sayı olmalıdır.")
        else:
            break
    except ValueError:
        print("Lütfen bir doğal sayı giriniz.")
    
while True:
    
    try:      
        sutunSayisi = int(input("Sütun elaman sayısı: "))
        if( sutunSayisi < 1 or sutunSayisi > 5) :
            print("Girilen sayı 1-5 arasında bir tam sayı olmalıdır.")
        else:
            break
    except ValueError:
        print("Lütfen bir doğal sayı giriniz.")

    
counter = 0
while counter<(satirSayisi*sutunSayisi):

    try: 
        matrisElemanları = int(input(f"Sayı {counter+1}: "))
        counter+=1
        matrisListesi.append(matrisElemanları)
    except ValueError: 
        print("Lütfen bir tamsayı giriniz.")

for i in range(satirSayisi):
    for j in range(sutunSayisi):
        print(matrisListesi[i*sutunSayisi + j],end=" ")
    
    print()



