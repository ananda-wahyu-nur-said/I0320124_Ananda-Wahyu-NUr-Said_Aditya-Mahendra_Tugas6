batasan_atas = 24
batasan_bawah = 10
print("Bilangan prima antara",batasan_bawah,"and",batasan_atas)
for angka in range(batasan_bawah,batasan_atas + 1):
    if angka > 1:
        for i in range(2,angka):
            if (angka % i) == 0:
                print(angka,'bukan prima')
                break
        else:
            print(angka, 'adalah bilangan prima')