print("==========================================================================")
print("                           ICETEATIC WARNET")
print("==========================================================================")
print("WhatsApp  : 085609075464")
print("Instagram : @IceTeaticwarnet.id")
print("X         : @IceTeaticwarnet.id")
print("Tiktok    : @IceTeaticwar.id")
print("Alamat    : Jl.kumbang, no.8, Jakarta Selatan, Jakarta")
print("--------------------------------------------------------------------------")
print("SEWA KOMPUTER [ NORMAL ]")
print("--------------------------------------------------------------------------")
print("No  -  Kode  -   Jenis          -  Harga Sewa    -  Diskon")
print("--------------------------------------------------------------------------")
print("1.  -  PC1   -   Komputer 1     -  Rp7.000/jam   -  10% jika sewa >=3 jam")
print("2.  -  PC2   -   Komputer 2     -  Rp7.000/jam   -  10% jika sewa >=3 jam")
print("3.  -  PC3   -   Komputer 3     -  Rp7.000/jam   -  10% jika sewa >=3 jam")
print("4.  -  PC4   -   Komputer 4     -  Rp7.000/jam   -  10% jika sewa >=3 jam")
print("5.  -  PC5   -   Komputer 5     -  Rp7.000/jam   -  10% jika sewa >=3 jam")
print("--------------------------------------------------------------------------")
print("")
print("SEWA KOMPUTER [ MEMBER ]")
print("--------------------------------------------------------------------------")
print("No  -  Kode  -   Jenis          -  Harga Sewa    -  Diskon")
print("--------------------------------------------------------------------------")
print("1.  -  PC1   -   Komputer 1     -  Rp6.000/jam   -  25% jika sewa >=3 jam")
print("2.  -  PC2   -   Komputer 2     -  Rp6.000/jam   -  25% jika sewa >=3 jam")
print("3.  -  PC3   -   Komputer 3     -  Rp6.000/jam   -  25% jika sewa >=3 jam")
print("4.  -  PC4   -   Komputer 4     -  Rp6.000/jam   -  25% jika sewa >=3 jam")
print("5.  -  PC5   -   Komputer 5     -  Rp6.000/jam   -  25% jika sewa >=3 jam")
print("--------------------------------------------------------------------------")
nama_op = input("Masukan Kode Operator Warnet : ")
if nama_op == "op1" or nama_op == "OP1" :
    operator = "Bagas"
elif nama_op == "op2" or nama_op == "OP2" :
    operator = "Arul"
elif nama_op == "op3" or nama_op == "OP3" :
    operator = "Erza"
elif nama_op == "op4" or nama_op == "OP4" :
    operator = "Dava"
else :
    exit("Input yang anda masukan salah program dihentikan")
nama_pl = input("Masukan Nama Pelanggan : ")
member = input("Apakah pelanggan join member [Y/N] : ")
if member == "Y" or member == "y" :
    sewa_komputer = input("Masukan kode Komputer[PC1/PC2/PC3/PC4/PC5] : ")
    if sewa_komputer == "PC1" or sewa_komputer == "pc1" :
        jenis = "Komputer 1"
        harga = 6000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else :
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.25
            total = harga_sewa - diskon
    elif sewa_komputer == "PC2" or sewa_komputer == "pc2" :
        jenis = "Komputer 2"
        harga = 6000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.25
            total = harga_sewa - diskon
    elif sewa_komputer == "PC3" or sewa_komputer == "pc3" :
        jenis = "Komputer 3"
        harga = 6000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.25
            total = harga_sewa - diskon
    elif sewa_komputer == "PC4" or sewa_komputer == "pc4" :
        jenis = "Komputer 4"
        harga = 6000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0 
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.25
            total = harga_sewa - diskon
    elif sewa_komputer == "PC5" or sewa_komputer == "pc5" :
        jenis = "Komputer 5"
        harga = 6000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.25
            total = harga_sewa - diskon
    else : 
        exit("Input yang anda masukan salah program dihentikan")
elif member == "N" or member == "n" :
    sewa_komputer = input("Masukan kode Komputer[PC1/PC2/PC3/PC4/PC5] : ")
    if sewa_komputer == "PC1" or sewa_komputer == "pc1" :
        jenis = "Komputer 1"
        harga = 7000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else :
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.1
            total = harga_sewa - diskon
    elif sewa_komputer == "PC2" or sewa_komputer == "pc2" :
        jenis = "Komputer 2"
        harga = 7000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.1
            total = harga_sewa - diskon
    elif sewa_komputer == "PC3" or sewa_komputer == "pc3" :
        jenis = "Komputer 3"
        harga = 7000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.1
            total = harga_sewa - diskon
    elif sewa_komputer == "PC4" or sewa_komputer == "pc4" :
        jenis = "Komputer 4"
        harga = 7000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.1
            total = harga_sewa - diskon
    elif sewa_komputer == "PC5" or sewa_komputer == "pc5" :
        jenis = "Komputer 5"
        harga = 7000
        jam_sewa = int(input("Masukan Jam sewa : "))
        if jam_sewa == 1 :
            diskon = 0
            total = harga
        elif jam_sewa == 2 :
            diskon = 0
            total = harga * jam_sewa
        else : 
            harga_sewa = harga * jam_sewa
            diskon = harga_sewa * 0.1
            total = harga_sewa - diskon
    else : 
        exit("Input yang anda masukan salah program dihentikan")
else :
    exit("Input yang anda masukan salah program dihentikan")

menu_makanan = []
kode_makanan = []
banyak_pesan_makanan = []
harga_satuan_makanan = []
harga_makanan = []

makanan = input("Ingin pesan makanan [y/n] : ")
if makanan == "y" or makanan =="Y" :
    print("------------------------------------")
    print("DAFTAR MENU ICETEATIC KAFE")
    print("------------------------------------")
    print("              MAKANAN")
    print("------------------------------------")
    print("No   Kode     Menu          Harga   ")
    print("-----------------------------------")
    print("1.   MIKU     Mie Kuah      Rp7.500")
    print("2.   MIGOR    Mie Goreng    Rp7.000")
    print("3.   NASGOR   Nasi Goreng   Rp10.000")
    print("4.   GORE     Gorengan      Rp1.000")
    print("------------------------------------")
    a = int(input("Banyak menu yang dipesan : "))
    for i in range(a) :
        print("Menu makanan ke",i+1)
        kode_makanan.append(input("Pilih kode Makanan : "))
        banyak_pesan_makanan.append(int(input("Ingin pesan berapa porsi : ")))
        if kode_makanan[i] == "MIKU" or kode_makanan[i] == "miku" :
            menu_makanan.append("Mie Kuah")
            harga_satuan_makanan.append(7500 )
            harga_makanan.append(int(7500) * banyak_pesan_makanan[i])
        elif kode_makanan[i] == "MIGOR" or kode_makanan[i] == "migor" :
            menu_makanan.append("Mie Goreng")
            harga_satuan_makanan.append(7000)
            harga_makanan.append(int(7000) * banyak_pesan_makanan[i])
        elif kode_makanan[i] == "NASGOR" or kode_makanan[i] == "nasgor" :
            menu_makanan.append("Nasi Goreng")
            harga_satuan_makanan.append(9000)
            harga_makanan.append(int(10000) * banyak_pesan_makanan[i])
        elif kode_makanan[i] == "GORE" or kode_makanan[i] == "gore" :
            menu_makanan.append("Gorengan")
            harga_satuan_makanan.append(1000)
            harga_makanan.append(int(1000) * banyak_pesan_makanan[i])
        else :
            exit("Input yang anda masukan salah program dihentikan")

kode_minuman = []
banyak_pesan_minuman = []
menu_minuman = []
harga_satuan_minuman = []
harga_minuman = []

minuman = input("Ingin pesan minuman [y/n] : ")
if minuman == "y" or minuman == "Y" :
    print("------------------------------------")
    print("DAFTAR MENU ICETEATIC KAFE")
    print("------------------------------------")
    print("               MINUMAN              ")
    print("------------------------------------")
    print("No   Kode     Menu          Harga")
    print("-----------------------------------")
    print("1.   ESTE     Es Teh Manis  Rp5.000")
    print("2.   TEANG    Teh Anget     Rp5.000")
    print("3.   KOHI     Kopi Hitam    Rp6.000")
    print("4.   KOSU     Kopi Susu     Rp6.500")
    print("------------------------------------")
    b = int(input("Banyak menu yang dipesan : "))
    for c in range(b) :
        print("Menu minuman ke",c+1)
        kode_minuman.append(input("Pilih kode minuman : "))
        banyak_pesan_minuman.append(int(input("Ingin pesan berapa gelas : ")))
        if kode_minuman[c] == "ESTE" or kode_minuman[c] == "este" :
            menu_minuman.append("Es Teh Manis")
            harga_satuan_minuman.append(5000)
            harga_minuman.append(int(5000) * banyak_pesan_minuman[c])
        elif kode_minuman[c] == "TEANG" or kode_minuman[c]== "teang" :
            menu_minuman.append("Teh Anget   ")
            harga_satuan_minuman.append(5000)
            harga_minuman.append(int(5000) * banyak_pesan_minuman[c])
        elif kode_minuman[c] == "KOHI" or kode_minuman[c]== "kohi" :
            menu_minuman.append("Kopi Hitam  ")
            harga_satuan_minuman.append(6000)
            harga_minuman.append(int(6000) * banyak_pesan_minuman[c])
        elif kode_minuman[c] == "KOSU" or kode_minuman[c]== "kosu" :
            menu_minuman.append("Kopi susu   ")
            harga_satuan_minuman.append(6500)
            harga_minuman.append(int(6500) * banyak_pesan_minuman[c])
        else :
            exit("Input yang anda masukan salah program dihentikan")

print("=" * 79)
print("                              ICETEATIC WARNET")
print("=" * 79)
print("WhatsApp  : 085609075464")
print("Instagram : @IceTeaticwarnet.id")
print("X         : @IceTeaticwarnet.id")
print("Tiktok    : @IceTeaticwar.id")
print("Alamat    : Jl.kumbang, no.8, Jakarta Selatan, Jakarta")
print("-" * 79)
print("Nama Operator Warnet :", operator)
print("Nama Pelanggan :", nama_pl)
print("-" * 79)
print("PEMBAYARAN")
print("-" * 79)
print("Sewa\t\t-  Harga\t-  Jam Sewa\t-  Diskon\t-  Total")
print("-" * 79)
print("%s\t-  Rp.%i/jam\t-  %ijam\t\t-  Rp.%i\t-  Rp.%i" % (jenis,harga,jam_sewa,diskon,total))
if makanan == "Y" or makanan == "y"  or minuman == "Y" or makanan == "y" :
    print("=" * 62)
    print("Menu\t\t-  Harga\t-  Banyak Pesan")
    print("-" * 62)

if makanan == "Y" or makanan == "y" :
    for e in range(a) :
        print("%s\t-  Rp.%i\t-  %i\t\t\t\t-  Rp.%i" % (menu_makanan[e],
        harga_satuan_makanan[e],banyak_pesan_makanan[e],harga_makanan[e]))

if minuman == "Y" or minuman == "y" :
    for d in range(b) :
        print("%s\t-  Rp.%i\t-  %i\t\t\t\t-  Rp.%i" % (menu_minuman[d],
        harga_satuan_minuman[d],banyak_pesan_minuman[d],harga_minuman[d]))

menu_ma = sum(harga_makanan)
menu_mi = sum(harga_minuman)
total_bayar = total + menu_ma + menu_mi
print("----------------------------------------------------------------------------- +")
print("                                                     Total Bayar : Rp.",int(total_bayar))
uang_bayar = int(input("                                                           Bayar : Rp. "))
while uang_bayar < total_bayar :
            print("           Pembayaran Harus lebih Besar atau sama dengan Tagihan")
            uang_bayar = int(input("                        Masukkan Kembali Nominal Uang Pembayaran : Rp. "))
uang_kembali = uang_bayar - total_bayar
print("                                                         Kembali : Rp.",int(uang_kembali))



        


    

