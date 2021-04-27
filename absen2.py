daftar= []
jumlah = int(input('Jumlah nama siswa yang di inginkan : '))
for i in range(jumlah):
    nama = input('Masukan nama mahasiswa : ')
    daftar.append(nama)
hitung = 0
hadir = 0
for mhs in daftar:
    print('Apakah ', mhs, 'Hadir dipertemuan ini ?')
    hitung = hitung + 1

    presensi = input('( Ya atau Tidak ) ? ')
    if presensi == 'Ya':
        hadir = hadir + 1
    elif presensi == 'Y':
        hadir = hadir + 1
    elif presensi == 'y':
        hadir = hadir + 1
print('Jumlah siswa Keseluruhan : ', hitung)
print('jumlah hadir dipertemuan : ', hadir)
absen = hitung - hadir
print('Jumlah yang tidak hadir dipertemuan : ', absen)