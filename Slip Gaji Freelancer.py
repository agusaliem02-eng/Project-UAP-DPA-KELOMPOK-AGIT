# Project mini UAP DPA 2025
# Kelompok AGIT
# Tema : Menghitung gaji freelancer berdasarkan jumlah dan tarif yang diberikan
# Nama Anggota:
# A. GUSTI SHAFWAN ZAKI  2517052013
# RAHUL HUKAMA ZULDA     2517052030
# RISTA APRILIA          2517052036

def garis():
    print('=' * 45)

data_freelancer=[]

def hitung_gaji(jumlah,tarif):
    return jumlah * tarif

def cari_index_dari_nama(nama_dicari):
    nama_dicari = nama_dicari.lower()
    for i, d in enumerate(data_freelancer):
        if d['nama'] == nama_dicari:
            return i
    return -1
    
def input_data():
    nama = input('Nama Freelancer     : ')
    divisi = input('Divisi Freelancer : ')

    try:
        jumlah = int(input('Jumlah yang diselesaikan    : '))
        tarif = float(input('Harga/pcs (Rp.)           : '))
    except ValueError:
        print('Input harus berupa angka!')
        return input_data()

    total = hitung_gaji(jumlah,tarif)

    data_freelancer.append({
        'nama': nama,
        'divisi': divisi,
        'jumlah': jumlah,
        'tarif': tarif,
        'total': total
    })

    print('Data berhasil diinput dan tersimpan')
    print("\n")
    
def tampilkan_slip():
    if not data_freelancer:
        print("Belum ada data!")
        return

    garis()
    print("DAFTAR DATA FREELANCER (TABEL)")
    garis()

    # Header tabel
    print(f"{'No':<4} {'Nama':<15} {'Divisi':<15} {'Jumlah':<8} {'Tarif':<20} {'Total':<15}")
    print("-" * 75)

    # Isi tabel
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

def edit_data():
    tampilkan_slip()
    if not data_freelancer:
        print('Data masih kosong, Harap masukan data terlebih dahulu!')
        return
    
    nama_dicari = input("Masukkan nama yang ingin diedit: ").lower()
    index = cari_index_dari_nama(nama_dicari)

    if index == -1:
        print("Nama tidak ditemukan, cek ulang!")
        return

    d = data_freelancer[index]

    print("\nData ditemukan. Isi baru (kosongkan jika tidak ingin mengubah):")
    print(f"Nama lama      : {d['nama']}")
    print(f"Divisi lama    : {d['divisi']}")
    print(f"Jumlah lama    : {d['jumlah']}")
    print(f"Tarif lama     : {d['tarif']}")

    # Input baru dengan opsi skip
    nama_baru = input("Nama baru     : ").strip()
    if nama_baru:
        d['nama'] = nama_baru.lower()

    divisi_baru = input("Divisi baru   : ").strip()
    if divisi_baru:
        d['divisi'] = divisi_baru

    jumlah_baru = input("Jumlah baru   : ").strip()
    if jumlah_baru:
        try:
            d['jumlah'] = int(jumlah_baru)
        except ValueError:
            print("Jumlah harus angka! Data tidak berubah.")
            return

    tarif_baru = input("Tarif baru    : ").strip()
    if tarif_baru:
        try:
            d['tarif'] = float(tarif_baru)
        except ValueError:
            print("Tarif harus angka! Data tidak berubah.")
            return

    # Hitung ulang total
    d['total'] = hitung_gaji(d['jumlah'], d['tarif'])

    print("\nData berhasil diperbarui.")
    print("\n")
    tampilkan_slip()
    print("\n")

def cetak_slip():
    tampilkan_slip()
    if not data_freelancer:
        print('Data masih kosong, Harap masukan data terlebih dahulu!')
        return

    nama_dicari = input('Masukan nama yang akan dicari    :')
    index = cari_index_dari_nama(nama_dicari)
    if index == -1:
        print('Nama tidak ditemukan, harap cek ulang!')
        return
        
    d = data_freelancer[index]
    garis()
    print('SLIP GAJI FREELANCER')
    garis()
    print(f'Nama        : {d['nama']}')
    print(f'Divisi      : {d['divisi']}')
    print(f'Jumlah kerja: {d['jumlah']}')
    print(f'Tarif/unit  : Rp {d['tarif']:,}')
    print(f'Total Gaji  : Rp {d['total']:,}')
    garis()
    print('Terima kasih atas kerja sama Anda.')
    garis()
    print("\n")

def hapus_data():
    tampilkan_slip()
    if not data_freelancer:
        print('Data masih kosong, Harap masukan data terlebih dahulu!')
        return
    
    nama_dicari = input('Masukan nama yang akan dicari    :')
    index = cari_index_dari_nama(nama_dicari)
    if index == -1:
        print('Nama tidak ditemukan, harap cek ulang!')
        return
    
    confirm = input('Apakah anda yakin ingin menghapus data ini (y/n)  : ').lower()
    if confirm == 'y':
        del data_freelancer[index]
        print('Data berhasil dihapus')
        print("\n")
    else:
        print('Data batal dihapus')
        print("\n")
        return main()
        print("\n")

    
def main():
    while True:
        garis()
        print('SISTEM GAJI FREELANCE')
        garis()
        print('1. Tambah data pekerjaan')
        print('2. Tampilkan data freelancer')
        print('3. Edit data sesuai nama')
        print('4. Cetak slip gaji freelancerEdit data sesuai nama')
        print('5. Hapus data sesuai nama')
        print('0. Keluar')
        garis()

        pilihan = input('Pilih menu (0-5): ')

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
            print("\n")
            break
        else:
            print('Pilihan tidak valid.')
            print("\n")

if __name__ == '__main__':
    main()










