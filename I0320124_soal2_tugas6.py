daftar_nilai = input('Ketikkan semua nilai yang akan dirata-rata dan pisahkan dengan tanda koma tiap-tiap nilai!>')
list_nilai = daftar_nilai.split(',')
list_nilai_akhir = [int(x) for x in list_nilai]

keseluruhan = 0

for nilai in list_nilai_akhir :
    keseluruhan = keseluruhan + nilai
nilai_rata = keseluruhan/len(list_nilai_akhir)

print('jumlah total nilai anda adalah: ', keseluruhan)
print('Rata-rata keseluruhan nilai yang telah di input adalah: ', nilai_rata)