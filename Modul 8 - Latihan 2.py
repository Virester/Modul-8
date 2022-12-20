

def power(a,b):
    if a == 0 and b == 0:
        return " ERROR "
    elif b == 0:
        return 1
    elif b < 0:
        y = -(b)
        x = power(a,y)
        return 1/x
    else:
        return a * power(a,b-1)
    

while True:
    print("\nIni merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    x = (input("Masukkan Angka: "))
    if x == "":
        print("Program Selesai")
        break
    else:
        y = (input("Masukkan Pangkatnya: "))
        x,y = int(x), int(y)
        print("Hasilnya adalah: " + str(power(x,y)))
