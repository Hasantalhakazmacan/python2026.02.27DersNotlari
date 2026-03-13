kelime = input("Bir kelime giriniz :")
harf = input("Bir harf giriniz :")

if kelime.find(harf) != -1:
    indis =kelime.find(harf)
    print(kelime[indis:indis+3])

else:
    print("harf mevcut değil")
