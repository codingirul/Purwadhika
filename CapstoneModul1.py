# Data buku di perpustakaan "DATA SCIENCE LIBRARY"
data_buku = {
    '978-3-16-148410-0': {'judul': 'Python Programming', 'penulis': 'John Doe', 'tahun': 2020, 'status': 'tersedia'},
    '978-1-23-456789-7': {'judul': 'Data Science Handbook', 'penulis': 'Jane Smith', 'tahun': 2018, 'status': 'dipinjam'},
    '978-0-12-345678-9': {'judul': 'Machine Learning Basics', 'penulis': 'Alice Johnson', 'tahun': 2019, 'status': 'tersedia'},
    '978-0-13-110362-7': {'judul': 'Introduction to Algorithms', 'penulis': 'Thomas H. Cormen', 'tahun': 2009, 'status': 'tersedia'},
    '978-0-14-044913-6': {'judul': 'The Art of Computer Programming', 'penulis': 'Donald Knuth', 'tahun': 1968, 'status': 'tersedia'},
    '978-0-262-03384-8': {'judul': 'Artificial Intelligence: A Modern Approach', 'penulis': 'Stuart Russell', 'tahun': 2010, 'status': 'tersedia'},
    '978-0-596-52068-7': {'judul': 'Learning Python', 'penulis': 'Mark Lutz', 'tahun': 2013, 'status': 'dipinjam'},
    '978-1-491-94700-2': {'judul': 'Fluent Python', 'penulis': 'Luciano Ramalho', 'tahun': 2015, 'status': 'tersedia'},
    '978-1-59327-599-0': {'judul': 'Automate the Boring Stuff with Python', 'penulis': 'Al Sweigart', 'tahun': 2015, 'status': 'tersedia'},
    '978-1-59327-603-4': {'judul': 'Python Crash Course', 'penulis': 'Eric Matthes', 'tahun': 2019, 'status': 'dipinjam'}
    }
# Recycle bin untuk menyimpan data buku yang dihapus sementara
recycle_bin = []
#1 Fungsi untuk tampilan main menu
def tampilkan_menu():
    print('''\nSELAMAT DATANG DI "DATA SCIENCE LIBRARY"!\nMAIN MENU:''')
    print("[1] Tampilkan daftar keseluruhan buku atau cari buku (Read)")
    print("[2] Tambahkan Data Buku (Create)")
    print("[3] Edit Data Buku (Update)")
    print("[4] Hapus Buku (Delete)")
    print("[5] Lihat Recycle Bin")
    print("[6] Restore Buku dari Recycle Bin")
    print("[7] Kosongkan Recycle Bin")
    print("[0] Keluar")
#2 Fungsi untuk Read Data
def tampilkan_buku():
    for isbn, info in data_buku.items():
        print(f"ISBN: {isbn}, Judul: {info['judul']}, Penulis: {info['penulis']}, Tahun: {info['tahun']}, Status: {info['status']}")
def cari_buku(kriteria, nilai):
    ditemukan = False
    for isbn, info in data_buku.items():
        if str(info[kriteria]).lower() == nilai.lower():
            print(f"ISBN: {isbn}, Judul: {info['judul']}, Penulis: {info['penulis']}, Tahun: {info['tahun']}, Status: {info['status']}")
            ditemukan = True
    if not ditemukan:
        print("Buku tidak ditemukan.")
def sub_menu_read():
    while True:
        print("\n=== SUB MENU READ ===")
        print("[1] Tampilkan semua buku")
        print("[2] Cari buku berdasarkan kriteria")
        print("[3] Kembali ke MAIN MENU")
        sub_pilihan = input("Pilih sub menu: ")
        if sub_pilihan == '1':
            tampilkan_buku()
        elif sub_pilihan == '2':
            kriteria = input("Cari berdasarkan (isbn/judul/penulis/tahun/status): ").lower()
            if kriteria in ['isbn', 'judul', 'penulis', 'tahun', 'status']:
                nilai = input(f"Masukkan {kriteria}: ")
                cari_buku(kriteria, nilai)
            else:
                print("Kriteria pencarian tidak valid.")
        elif sub_pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
#3 Fungsi untuk Create Data
def tambah_buku():
    while True:
        print("\n=== SUB MENU TAMBAH BUKU ===")
        print("[1] Tambah Buku")
        print("[2] Kembali ke MAIN MENU")
        sub_pilihan = input("Pilih sub menu: ")
        if sub_pilihan == '1':
            isbn = input("Masukkan ISBN: ")
            if isbn in data_buku:
                print("Buku tersebut sudah ada.")
            else:
                judul = input("Masukkan Judul: ")
                penulis = input("Masukkan Penulis: ")
                tahun = input("Masukkan Tahun: ")
                status = input("Masukkan Status: ")
                konfirmasi = input("Apakah Anda yakin buku ini ingin disimpan ke dalam daftar buku? (Ya/Tidak): ").lower()
                if konfirmasi == 'ya':
                    data_buku[isbn] = {'judul': judul, 'penulis': penulis, 'tahun': tahun, 'status': status}
                    print("Buku berhasil ditambahkan.")
                else:
                    print("Buku tidak jadi ditambahkan.")
        elif sub_pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
#4 Fungsi untuk Update Data
def edit_data_buku():
    while True:
        print("\n=== SUB MENU EDIT DATA BUKU ===")
        print("[1] Edit Data Buku")
        print("[2] Kembali ke MAIN MENU")
        sub_pilihan = input("Pilih sub menu: ")
        if sub_pilihan == '1':
            isbn = input("Masukkan ISBN buku yang ingin diedit: ")
            if isbn in data_buku:
                info = data_buku[isbn]
                print(f"ISBN: {isbn}, Judul: {info['judul']}, Penulis: {info['penulis']}, Tahun: {info['tahun']}, Status: {info['status']}")
                konfirmasi = input("Lanjutkan edit data buku? (Ya/Tidak): ").lower()
                if konfirmasi == 'ya':
                    key = input("Masukkan key yang ingin diupdate (judul/penulis/tahun/status): ").lower()
                    if key in ['judul', 'penulis', 'tahun', 'status']:
                        nilai_baru = input(f"Masukkan update baru untuk {key}: ")
                        konfirmasi_update = input("Apakah Anda yakin ingin mengupdate data ini? (Ya/Tidak): ").lower()
                        if konfirmasi_update == 'ya':
                            data_buku[isbn][key] = nilai_baru
                            print("Data berhasil diperbaharui.")
                        else:
                            print("Data tidak jadi diperbaharui.")
                    else:
                        print("Key tidak valid.")
                else:
                    print("Edit data buku dibatalkan.")
            else:
                print("Buku tidak ditemukan.")
        elif sub_pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
#5 Fungsi untuk Delete Data
def hapus_buku():
    while True:
        print("\n=== SUB MENU HAPUS BUKU ===")
        print("[1] Hapus Data Buku")
        print("[2] Kembali ke MAIN MENU")
        sub_pilihan = input("Pilih sub menu: ")
        if sub_pilihan == '1':
            isbn = input("Masukkan ISBN buku yang ingin dihapus: ")
            if isbn in data_buku:
                info = data_buku[isbn]
                print(f"ISBN: {isbn}, Judul: {info['judul']}, Penulis: {info['penulis']}, Tahun: {info['tahun']}, Status: {info['status']}")
                konfirmasi = input("Apakah Anda yakin ingin menghapus data ini dan memasukkannya ke dalam recycle bin? (Ya/Tidak): ").lower()
                if konfirmasi == 'ya':
                    recycle_bin.append((isbn, data_buku[isbn]))
                    del data_buku[isbn]
                    print("Data berhasil dihapus dan dipindahkan ke recycle bin.")
                else:
                    print("Data tidak jadi dihapus.")
            else:
                print("Buku tidak ditemukan.")
        elif sub_pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
#6 Fungsi untuk melihat isi Recycle Bin
def lihat_recycle_bin():
    if recycle_bin:
        for isbn, info in recycle_bin:
            print(f"ISBN: {isbn}, Judul: {info['judul']}, Penulis: {info['penulis']}, Tahun: {info['tahun']}, Status: {info['status']}")
    else:
        print("Recycle bin kosong.")
#7 Fungsi untuk mengembalikan data yang dihapus
def restore_buku(isbn):
    for item in recycle_bin:
        if item[0] == isbn:
            data_buku[isbn] = item[1]
            recycle_bin.remove(item)
            print("Buku berhasil direstore dari recycle bin.")
            return
    print("Buku tidak ditemukan di recycle bin.")
#8 Fungsi untuk menghapus data dengan permanen / mengosongkan Recycle Bin
def kosongkan_recycle_bin():
    konfirmasi = input("Apakah Anda yakin ingin mengosongkan recycle bin? Data akan terhapus secara permanen. (Ya/Tidak): ").lower()
    if konfirmasi == 'ya':
        recycle_bin.clear()
        print("Recycle bin berhasil dikosongkan.")
    else:
        print("Recycle bin tidak jadi dikosongkan.")
#9 Fungsi untuk mengeksekusi program dan menginput angka pada MAIN MENU
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            sub_menu_read()
        elif pilihan == '2':
            tambah_buku()
        elif pilihan == '3':
            edit_data_buku()
        elif pilihan == '4':
            hapus_buku()
        elif pilihan == '5':
            lihat_recycle_bin()
        elif pilihan == '6':
            isbn = input("Masukkan ISBN buku yang ingin direstore: ")
            restore_buku(isbn)
        elif pilihan == '7':
            kosongkan_recycle_bin()
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()