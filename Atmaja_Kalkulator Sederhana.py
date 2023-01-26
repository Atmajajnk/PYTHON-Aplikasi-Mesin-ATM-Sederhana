# APLIKASI MESIN ATM SEDERHANA ATMAJA JNK
pin = '123456'
saldo = 1000000

def cek_saldo():
    print("Saldo Anda Rp. {}". format(saldo))

tunai = None
pin_lama = None
pin_baru= None
print("=====================================================")
print('Selamat Datang di program ATM, BANK ATMAJA JNK')
print("=====================================================")
for i in range(3):
    print()
    inPin = input("Silahkan masukkan 6 digit pin anda : ")
    if inPin == pin :
        print()
        print("===PIN yang Anda masukkan benar===")
        print()
        break

    else :
        print("PIN salah")
        if i == 2 :
            print("============================================")
            print("===Akun anda kami tangguhkan selama 24 jam===")
            print("============================================")
            quit()

pilihan = 'y'
while (pilihan == 'y'):
    print("""
    MENU
    1. Cek Saldo
    2. Penarikan Tunai
    3. Setor Tunai
    4. Ganti Pin
    5. Keluar
    """)

    menu = input('Silahkan Pilih Menu : ')
    print("===================================================")

    if menu == '1':
        print(f"Sisa saldo anda : Rp. {saldo}")

    elif menu == '2':
        if saldo < 50000:
            print("Maaf, saldo anda tidak mencukupi.")
            print("Silahkan isi saldo terlebih dahulu.")

        else:
            print("Jumlah nominal penarikan sebesar 50000, 100000, 250000, 500000, 1000000")
            tunai = int(input("Jumlah penarikan anda : Rp. "))
            if (tunai == 50000) or (tunai == 100000) or (tunai == 250000) or (tunai == 500000) or (tunai == 1000000):
                saldo = saldo - tunai
                print()
                print(f"Saldo ditarik : Rp. {tunai}")
                print(f"Sisa saldo anda : Rp. {saldo}")
            else:
                print("Nominal tidak diketahui")

    elif menu == '3':
        setor = int(input("Silahkan masukkan nominal yang ingin di setor : Rp. "))
        saldo = saldo + setor
        print()
        print(f"Sisa saldo anda : Rp. {saldo}")

    elif menu =='4':
        pin = '123456'
        pin_lama = pin
        pin_baru = int(input("Masukan Pin baru :"))
        print("Pin ATM sukses diganti menjadi :",pin_baru)
        print("Pin ATM sebelumnya :", pin)

    elif menu == '5':
        print("Anda Telah Keluar dari ATM ATMAJA JNK")
        print()
        print("Terima kasih sudah menggunakan layanan Kami")
        print()

    print("=========================================================")
    pilihan = input("Apakah ingin melanjutkan program (y/n)? ")
    print("=========================================================")