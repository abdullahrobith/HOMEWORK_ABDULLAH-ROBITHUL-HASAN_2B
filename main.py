#function untuk menampilkan menu pilihan
def tampilan():
    print(50*'=')
    print('Selamat datang di program manajemen stok barang!')
    print(50*'=')
    print('''pilihan:
          1. Tambah Data Barang
          2. Edit Data
          3. Hapus Data Barang
          4. Cari Data
          5. Tampilkan Data Barang
          6. Tampilkan Jumlah Data
          7. Keluar''')
    

#function rumus rumus
barang = []

def tambah():
    nama = str(input('Masukan Nama Barang : ').title())
    stok = int(input('Masukan Jumlah Stok Barang : '))
    barang_baru = {'Nama barang':nama,'Stok':stok}
    barang.append(barang_baru)
    print('--- DATA BERHASIL DITAMBAHKAN😉 ---')

def edit():
    ubah = int(input('Edit Data Indeks ke : '))
    ganti = str(input('Masukkan Nama Barang : ').title())
    ganti1 = int(input('Masukkan Jumlah Stok Barang : '))
    barang[ubah] = {'Nama barang':ganti,'Stok':ganti1}
    print('--- DATA BERHASIL DIUBAH😉 ---')

def hapus():
    hapus = int(input('Hapus Data Index Ke : '))
    del barang[hapus]
    print('--- DATA BERHASIL DIHAPUS😉 ---')

def tampil():
    print('======= TOKO ELEKTRONIK💻 =======')
    if len(barang) == 0:
        print('--- DATA BARANG KOSONG❌ ---')
    else:
        for a in barang:
            print('📌',a['Nama barang'],':',a['Stok'])

def cari():
    cari = str(input('Cari Nama Barang : ').title())
    print('======= Hasil Pencarian🔍 =======')
    for item in barang:
        if cari in item['Nama barang']:
            nama_terformat = ''.join(item['Nama barang'])
            print(f"{nama_terformat}, Stok : {item['Stok']}")

def jumlah():
    if len(barang) == 0:
        print('--- DATA BARANG KOSONG❌ ---')
    else:
        print('Jumlah data tersimpan : ',len(barang),'barang')


#funtion untuk menjalankan / peng aplikasian dari rumus rumus diatas
def pengaplikasian():
    pilihan = input('Masukan Pilihan [1-7] : ')
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        edit()
    elif pilihan == '3':
        hapus()
    elif pilihan == '4':
        cari()
    elif pilihan == '5':
        tampil()
    elif pilihan == '6':
        jumlah()
    elif pilihan == '7':
        print('=======Program Terhenti😉=======')
        exit()
    else:
        print('''
              Input Yang Anda Masukkan Salah❌
              Harap Masukkan Pilihan Yang Benar [1-7]''')
    