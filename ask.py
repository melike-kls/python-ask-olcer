ad1 = input("Adınız: ")
ad2 = input("Kız/Erkek Arkadaşınızın Adı: ")

ask = len(ad1) + len(ad2)
if len(ad1) > len(ad2):
    ask -= 5
else:
    ask += 3
    ask *= 52
    ask = ask / (100 + len(ad2))
if ask>10:
    ask = 10
else:
    ask = round(ask)
print(ad1, "ve ",ad2," aşk puanı ",ask)
