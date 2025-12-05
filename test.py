#Project mini UAP DPA 2025
#Kelompok AGIT
#Tema : Menghitung gaji freelancer berdasarkan jumlah dan tarif yang diberikan
'''Nama Anggota kelompok :
A.GUSTI SHAFWAN ZAKI    2517052013
RAHUL HUKAMA ZULDA      2517052030
RISTA APRILIA           2517052036'''

def garis():
    print("=" * 45)

data_freelancer = []

def buat_id():
    if not data_freelancer:
        return 1
    else:
        id_terakhir = data_freelancer[-1]["id"]
        return id_terakhir + 1

def total_gaji(jumlah, tarif):
    return jumlah * tarif

def cari_index_by_id(id_cari):
    for i, d in enumerate(data_freelancer):
        if d["id"] == id_cari:
            return i
    return -1

def input_data():
    garis()
    print("INPUT DATA PEKERJA FREELANCE")
    garis()
    nama = input("Nama freelancer         : ").strip()
    pekerjaan = input("Kategori pekerjaan      : ").strip()
    
    try:
        jumlah = int(input("Jumlah yang dikerjakan : "))
        tarif = float(input("Tarif per unit (Rp)    : "))
    except ValueError:
        print("Input jumlah/tarif harus berupa angka!")
        return

    total = total_gaji(jumlah, tarif)
    id_terbaru = buat_id()

    data_freelancer.append({
        "id": id_terbaru,
        "nama": nama,
        "pekerjaan": pekerjaan,
        "jumlah": jumlah,
        "tarif": tarif,
        "total": total
    })

    print("\nData berhasil ditambahkan dengan ID:", id_terbaru)

def edit_data():
    garis()
    print("EDIT DATA PEKERJA FREELANCE")
    garis()
    if not data_freelancer:
        print("Belum ada data yang bisa diedit.")
        return

    try:
        id_edit = int(input("Masukkan ID yang ingin diedit: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    index = cari_index_by_id(id_edit)
    if index == -1:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    data = data_freelancer[index]
    print("\nData lama:")
    print(f"Nama       : {data['nama']}")
    print(f"Pekerjaan  : {data['pekerjaan']}")
    print(f"Jumlah     : {data['jumlah']}")
    print(f"Tarif      : {data['tarif']}")
    
    print("\nKosongkan (Enter) jika tidak ingin mengubah.\n")

    nama_baru = input("Nama baru (opsional)       : ").strip()
    pekerjaan_baru = input("Pekerjaan baru (opsional)  : ").strip()
    jumlah_baru_str = input("Jumlah baru (opsional)     : ").strip()
    tarif_baru_str = input("Tarif baru (opsional)      : ").strip()

    if nama_baru != "":
        data["nama"] = nama_baru
    if pekerjaan_baru != "":
        data["pekerjaan"] = pekerjaan_baru
    if jumlah_baru_str != "":
        try:
            data["jumlah"] = int(jumlah_baru_str)
        except ValueError:
            print("Jumlah baru tidak valid, tidak diubah.")
    if tarif_baru_str != "":
        try:
            data["tarif"] = float(tarif_baru_str)
        except ValueError:
            print("Tarif baru tidak valid, tidak diubah.")

    data["total"] = total_gaji(data["jumlah"], data["tarif"])
    print("\nData berhasil diperbarui.")

def hapus_data():
    garis()
    print("HAPUS DATA PEKERJA FREELANCE")
    garis()
    if not data_freelancer:
        print("Belum ada data yang bisa dihapus.")
        return

    try:
        id_hapus = int(input("Masukkan ID yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    index = cari_index_by_id(id_hapus)
    if index == -1:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    konfirmasi = input(f"Yakin ingin menghapus data dengan ID {id_hapus}? (y/n): ").lower()
    if konfirmasi == "y":
        del data_freelancer[index]
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def tampilkan_slip():
    garis()
    print("CETAK SLIP GAJI FREELANCER")
    garis()
    if not data_freelancer:
        print("Belum ada data.")
        return

    try:
        id_cetak = int(input("Masukkan ID freelancer: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    index = cari_index_by_id(id_cetak)
    if index == -1:
        print("Data dengan ID tersebut tidak ditemukan.")
        return

    d = data_freelancer[index]
    garis()
    print("SLIP GAJI FREELANCER")
    garis()
    print(f"ID          : {d['id']}")
    print(f"Nama        : {d['nama']}")
    print(f"Pekerjaan   : {d['pekerjaan']}")
    print(f"Jumlah kerja: {d['jumlah']}")
    print(f"Tarif/unit  : Rp {d['tarif']:,}")
    print(f"Total Gaji  : Rp {d['total']:,}")
    garis()
    print("Terima kasih atas kerja sama Anda.")
    garis()

# ================== MAIN PROGRAM ==================
def main():
    while True:
        garis()
        print("SISTEM GAJI FREELANCE")
        garis()
        print("1. Tambah data pekerjaan")
        print("2. Edit data")
        print("3. Hapus data")
        print("4. Cetak slip gaji freelancer")
        print("0. Keluar")
        garis()

        pilihan = input("Pilih menu (0-5): ")

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

if _name_ == "_main_":
    main()
