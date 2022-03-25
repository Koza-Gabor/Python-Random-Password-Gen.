import random
import math

betu = "abcdefghijklmnopqrstuvwxyz"
szam = "0123456789"
specialis = "@#$%&*"

# jelszó_len=random.randint(8,16)  #felhasználó nélküli bemenet
jelszo_len = int(input("Kérem a jelszó hosszúságát! "))

# jelszó hossza 50-30-20
betu_len = jelszo_len//2
szam_len = math.ceil(jelszo_len*30/100)
specialis_len = jelszo_len-(betu_len+szam_len)


jelszo = []


def alkotni_jelszo(hossz, sor, is_betu=False):
    for i in range(hossz):
        index = random.randint(0, len(sor) - 1)
        karakter = sor[index]
        if is_betu:
            eset = random.randint(0, 1)
            if eset == 1:
                karakter = karakter.upper()
        jelszo.append(karakter)


# betük jelszó
alkotni_jelszo(betu_len, betu, True)
# számok, jelszó
alkotni_jelszo(szam_len, szam)
# specialis karakter, jelszó
alkotni_jelszo(specialis_len, specialis)
# keverje meg a jelszó listát
random.shuffle(jelszo)
# Lista konvertálása
alkotni_jelszo = ""
for i in jelszo:
    alkotni_jelszo = alkotni_jelszo + str(i)
print(alkotni_jelszo)
