# Project-UAP-DPA-KELOMPOK-AGIT


1. Data utama program

data_freelancer = []

Ini adalah list kosong yang akan menampung semua data freelancer.

Setiap elemen di dalamnya adalah dictionary dengan isi:

{
    'nama': ...,
    'divisi': ...,
    'jumlah': ...,
    'tarif': ...,
    'total': ...
}


Jadi data_freelancer itu semacam database kecil di memori.


---

2. Fungsi bantu

garis()

def garis():
    print('=' * 45)

Buat tampilan lebih rapi.

Tinggal dipanggil kalau mau kasih garis pemisah di menu / slip.



---

hitung_gaji(jumlah, tarif)

def hitung_gaji(jumlah,tarif):
    return jumlah * tarif

Fungsi ini cuma menghitung gaji total = jumlah kerja × tarif per unit.

Dipakai di:

input_data() saat pertama kali simpan data

edit_data() saat data pekerjaan diubah




---

cari_index_dari_nama(nama_dicari)

def cari_index_dari_nama(nama_dicari):
    nama_dicari = nama_dicari.lower()
    for i, d in enumerate(data_freelancer):
        if d['nama'] == nama_dicari:
            return i
    return -1

Tujuannya: mencari posisi (index) freelancer di data_freelancer berdasarkan nama.

enumerate(data_freelancer):

i = index (0,1,2,…)

d = dictionary data freelancer.


Kalau ketemu nama yang cocok → kembalikan index-nya.

Kalau tidak ketemu → kembalikan -1 sebagai kode “tidak ditemukan”.


> Catatan kecil: kamu sudah lower() di nama_dicari, tapi di input_data() nama disimpan apa adanya ('nama': nama). Biar aman biasanya:

saat simpan: nama.lower()

saat bandingkan juga pakai .lower()





---

3. Input data baru: input_data()

def input_data():
    nama = input('Nama Freelancer     : ')
    divisi = input('Divisi Freelancer : ')

User memasukkan:

nama freelancer

divisi freelancer



Lalu input angka:

try:
        jumlah = int(input('Jumlah yang diselesaikan    : '))
        tarif = float(input('Harga/pcs (Rp.)           : '))
    except ValueError:
        print('Input harus berupa angka!')
        return input_data()

jumlah = berapa banyak pekerjaan yang diselesaikan.

tarif = harga per unit.

Dibungkus try/except:

kalau user ngisi selain angka → ValueError

program kasih pesan → lalu memanggil lagi input_data() (ulang input).



Hitung total dan simpan:

total = hitung_gaji(jumlah,tarif)

    data_freelancer.append({
        'nama': nama,
        'divisi': divisi,
        'jumlah': jumlah,
        'tarif': tarif,
        'total': total
    })

Data freelancer ditambahkan ke list data_freelancer.

total sudah dihitung dari fungsi hitung_gaji.



---

4. Tampilkan semua data: tampilkan_slip()

def tampilkan_slip():
    if not data_freelancer:
        print("Belum ada data!")
        return

Kalau list kosong → langsung info “Belum ada data!”.


Header tabel:

garis()
    print("DAFTAR DATA FREELANCER (TABEL)")
    garis()

    print(f"{'No':<4} {'Nama':<15} {'Divisi':<15} {'Jumlah':<8} {'Tarif':<20} {'Total':<15}")
    print("-" * 75)

Pakai format string dengan lebar kolom (:<15 dll) biar tabel rapi.


Isi tabel:

for i, d in enumerate(data_freelancer, start=1):
        print(
            f"{i:<4}"
            f"{d['nama']:<15}"
            f"{d['divisi']:<15}"
            f"{d['jumlah']:<8}"
            f"Rp {d['tarif']:<20,}"
            f"Rp {d['total']:<15,}"
        )
        print("\n")

Loop semua data.

start=1 → nomor mulai dari 1.

Angka tarif dan total diformat dengan koma ribuan (pakai :,), misal 1,000,000.



---

5. Edit data: edit_data()

1. Pertama, selalu tampilkan dulu semua data:

tampilkan_slip()
if not data_freelancer:
    print('Data masih kosong...')
    return


2. Minta nama yang mau diedit:

nama_dicari = input("Masukkan nama yang ingin diedit: ").lower()
index = cari_index_dari_nama(nama_dicari)


3. Kalau tidak ketemu:

if index == -1:
    print("Nama tidak ditemukan, cek ulang!")
    return


4. Kalau ketemu, ambil datanya:

d = data_freelancer[index]


5. Tampilkan data lama + minta data baru (boleh kosong = tidak diubah):

nama_baru = input("Nama baru     : ").strip()
if nama_baru:
    d['nama'] = nama_baru.lower()

divisi_baru = input("Divisi baru   : ").strip()
if divisi_baru:
    d['divisi'] = divisi_baru


6. Untuk jumlah dan tarif, dicek lagi apakah angka:

jumlah_baru = input("Jumlah baru   : ").strip()
if jumlah_baru:
    try:
        d['jumlah'] = int(jumlah_baru)
    except ValueError:
        print("Jumlah harus angka! Data tidak berubah.")
        return


7. Setelah mungkin ada perubahan → hitung ulang total:

d['total'] = hitung_gaji(d['jumlah'], d['tarif'])


8. Lalu tampilkan data terbaru dengan tampilkan_slip().




---

6. Cetak slip 1 orang: cetak_slip()

1. Tampilkan dulu semua data:

tampilkan_slip()
if not data_freelancer:
    print('Data masih kosong...')
    return


2. Minta nama yang akan dicetak slipnya:

nama_dicari = input('Masukan nama yang akan dicari    :')
index = cari_index_dari_nama(nama_dicari)


3. Kalau tidak ada, kasih info.


4. Kalau ada, tampilkan format slip:

d = data_freelancer[index]
garis()
print('SLIP GAJI FREELANCER')
garis()
print(f'Nama        : {d["nama"]}')
print(f'Divisi      : {d["divisi"]}')
print(f'Jumlah kerja: {d["jumlah"]}')
print(f'Tarif/unit  : Rp {d["tarif"]:,}')
print(f'Total Gaji  : Rp {d["total"]:,}')
garis()
print('Terima kasih atas kerja sama Anda.')
garis()



> Di koding yang kamu kirim, bagian f'Nama        : {d['nama']}' bakal error karena kutipnya tabrakan. Harusnya pakai kutip luar "..." atau escape, misal:

print(f"Nama        : {d['nama']}")




---

7. Hapus data: hapus_data()

1. Tampilkan data dulu.


2. Cek kalau list kosong → keluar fungsi.


3. Minta nama yang mau dihapus.


4. Cari index pakai cari_index_dari_nama.


5. Kalau ketemu, konfirmasi:

confirm = input('Apakah anda yakin ingin menghapus data ini (y/n)  : ').lower()
if confirm == 'y':
    del data_freelancer[index]
    print('Data berhasil dihapus')
else:
    print('Data batal dihapus')
    return main()



del data_freelancer[index] → benar-benar menghapus elemen pada posisi itu.


> Catatan: return main() di else sebenarnya tidak perlu, karena kamu sudah punya while True di main(). Cukup return saja.




---

8. Fungsi utama: main()

def main():
    while True:
        garis()
        print('SISTEM GAJI FREELANCE')
        garis()
        print('1. Tambah data pekerjaan')
        print('2. Tampilkan data freelancer')
        print('3. Edit data sesuai nama')
        print('4. Cetak slip gaji freelancer')
        print('5. Hapus data sesuai nama')
        print('0. Keluar')
        garis()

        pilihan = input('Pilih menu (0-5): ')

while True: → program jalan terus sampai user pilih "0. Keluar".

Baca pilihan user, lalu:


if pilihan == '1':
            input_data()
        elif pilihan == '2':
            tampilkan_slip()
        elif pilihan == "3":
            edit_data()
        elif pilihan == "4":
            cetak_slip()
        elif pilihan =='5':
            hapus_data()
        elif pilihan == '0':
            garis()
            print('Terima kasih, program selesai.')
            garis()
            break
        else:
            print('Pilihan tidak valid.')

Setiap menu mengarah ke fungsi yang sesuai.

Kalau pilih 0 → cetak pesan terima kasih, lalu break dari loop → program selesai.


Di bawah, kamu panggil:

main()

Artinya, begitu file ini dijalankan, langsung masuk ke menu utama.



---

Ringkasan singkat

Program ini adalah aplikasi menu berbasis teks untuk:

Menyimpan data freelancer dalam list of dict.

Menghitung gaji per freelancer berdasarkan jumlah kerja × tarif.

Menampilkan data dalam bentuk tabel rapi.

Mengedit data dengan nama sebagai kunci.

Mencetak slip gaji 1 orang.

Menghapus data tertentu dari list.
