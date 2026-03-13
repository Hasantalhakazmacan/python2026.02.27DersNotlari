while True:
    sayi = int(input("Bir sayı giriniz"))
    sayi1 =1

    if sayi<=0:
        break 

    fact =1
    
    for i in range(1,sayi+1):
        fact = fact*i
    print(fact)
