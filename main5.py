kelime =input("Please type in a sentence:")
if len(kelime)>0:
    print(kelime[0])


for i in range(1,len(kelime)):
    if kelime[i-1]== " ":
        print(kelime[i])

