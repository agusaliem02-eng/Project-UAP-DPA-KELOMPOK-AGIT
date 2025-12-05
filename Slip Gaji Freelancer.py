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

def input_data():
    nama = input('Nama Freelancer    : ')
    divisi = input('Divisi Freelancer    : ')

    try:
        jumlah = int(input('Jumlah yang diselesaikan    : '))
        tarif = float(input('Harga /pcs (Rp.)    : '))
    except ValueError:
        print('Input harus berupa angka!')
        return

    total = hitung_gaji(jumlah,tarif)

    data_freelancer.append({
        "nama": nama,
        "pekerjaan": divisi,
        "jumlah": jumlah,
        "tarif": tarif,
        "total": total
    })

    print('Data berhasil diinput dan tersimpan')

def tampilkan_slip():
    if not data_freelancer:
        print('Data masih kosong, Harap masukan data terlebih dahulu!')
        return

    d = data_freelancer[0]
    garis()
    print("SLIP GAJI FREELANCER")
    garis()
    print(f"Nama        : {d['nama']}")
    print(f"Pekerjaan   : {d['pekerjaan']}")
    print(f"Jumlah kerja: {d['jumlah']}")
    print(f"Tarif/unit  : Rp {d['tarif']:,}")
    print(f"Total Gaji  : Rp {d['total']:,}")
    garis()
    print("Terima kasih atas kerja sama Anda.")
    garis()
    
def main():
    while True:
        garis()
        print("SISTEM GAJI FREELANCE")
        garis()
        print("1. Tambah data pekerjaan")
        print("2. Edit data (berdasarkan nama)")
        print("3. Hapus data (berdasarkan nama)")
        print("4. Cetak slip gaji freelancer (berdasarkan nama)")
        print("0. Keluar")
        garis()

        pilihan = input("Pilih menu (0-4): ")

        if pilihan == "1":
            input_data()
        elif pilihan == "2":
            edit_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            tampilkan_slip()
        elif pilihan == "0":
            garis()
            print("Terima kasih, program selesai.")
            garis()
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
