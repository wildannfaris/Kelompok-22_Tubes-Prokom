import modulsend as ms
import modulcardalam as mcd
import modulcarluar as mcl
import modulride as mr
import modulsend as ms
import modulboxdalam as mbd
import modulboxluar as mbl
import sys
from colorama import init, Fore


init(autoreset=True)

def main():
    print("=============================================================")
    print(Fore.YELLOW + "=========== PROGRAM REKOMENDASI HARGA OJEK ONLINE ===========")
    print(Fore.YELLOW + "Selamat datang di layanan transportasi dan kurir ojek online!")
    print(Fore.YELLOW + "Program    Ini     Akan    Memberikan     Anda    Rekomendasi \nLayanan   Jasa    Ojek    Online      Di      Pulau      Jawa")
    print("\nSilakan pilih jenis layanan yang Anda butuhkan:")
    print(Fore.CYAN + "1. Layanan Transportasi")
    print(Fore.CYAN + "2. Layanan Kurir")
    print(Fore.RED + "0. Keluar")


    while True:
        pilihan = input(Fore.GREEN + "\nMasukkan pilihan Anda (1/2/0): ")
        print(Fore.RESET + "=============================================================")
        
        if pilihan == "1":
            layanan_transportasi()
        elif pilihan == "2":
            layanan_kurir()
        elif pilihan == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
        print("=============================================================")
        
def layanan_kurir():
    print(Fore.RESET + "\n=============================================================")
    print(Fore.YELLOW + "====== DAFTAR LAYANAN KURIR OJEK ONLINE YANG TERSEDIA =======")
    print("\nBerikut Layanan Kurir Ojek Online Yang Tersedia")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Luar Kota")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_kurir = input(Fore.GREEN + "\nMasukkan Layanan (1/2/3/0): ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_kurir == "1":
            layanan_kurir_dalam_kota()
        elif input_kurir == "2":
            layanan_kurir_luar_kota()
        elif input_kurir == "3":
            main()
        elif input_kurir == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
            break

def layanan_kurir_dalam_kota():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "=============== LAYANAN KURIR DALAM KOTA =================")
    print("\nBerikut Layanan Kurir Dalam Kota Yang Tersedia")
    print(Fore.CYAN + "1. Standar (Motor)")
    print(Fore.CYAN + "2. Box (Mobil)")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_dalam_kota = input(Fore.GREEN + "\nPilih Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_dalam_kota == "1":
            print(Fore.RESET + "\n==========================================================")
            print(Fore.YELLOW + "================== LAYANAN KURIR STANDAR =================")
            print("\nPilih Sesuai Kebutuhan Anda")
            try:
                input_provinsi, jarak = ms.get_input()
                harga_MaximDelivery = ms.layanansend("maxim", input_provinsi.title(), jarak)
                harga_GoSend = ms.layanansend("gojek", input_provinsi.title(), jarak)
                harga_GrabSameDay = ms.layanansend("Grab",input_provinsi.title(), jarak)
                print("\n==========================================================")
                
                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Standar dengan Maxim Delivery   : Rp", harga_MaximDelivery)
                print("Harga Kurir Standar dengan GoSend           : Rp", harga_GoSend)
                print("Harga Kurir Standar dengan Grab Same Day    : Rp", harga_GrabSameDay)
                print()

                if harga_MaximDelivery<harga_GoSend and harga_MaximDelivery<harga_GrabSameDay:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Kurir Termurah Adalah \nMaxim Delivery")
                elif harga_GrabSameDay<harga_MaximDelivery and harga_GrabSameDay<harga_GoSend:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Kurir Termurah Adalah \nGrab Same Day")
                elif harga_GoSend<harga_MaximDelivery and harga_GoSend<harga_GrabInstant:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Kurir Termurah Adalah \nGo Send")
                print("==========================================================")

                layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                if layananlain.capitalize() == "Ya":
                    layanan_kurir_dalam_kota()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break
            
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
    

        elif input_dalam_kota == "2":
            print(Fore.RESET + "\n==========================================================")
            print(Fore.YELLOW + "=================== LAYANAN KURIR BOX ===================")
            print("\nPilih Sesuai Kebutuhan")
            try:
                input_ukuran, input_provinsi, jarak = mbd.get_input()
                harga_MaximBox = mbd.layananboxdalamkota("maxim", input_ukuran.lower(), input_provinsi.title(), jarak)
                harga_GoBox = mbd.layananboxdalamkota("gojek", input_ukuran.lower(), input_provinsi.title(), jarak)
                harga_GrabInstant = mbd.layananboxdalamkota("Grab", input_ukuran.lower(), input_provinsi.title(), jarak)
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Box Dalam Kota dengan Maxim Box     : Rp", harga_MaximBox)
                print("Harga Kurir Box Dalam Kota dengan Go Box        : Rp", harga_GoBox)
                print("Harga Kurir Box Dalam Kotab dengan Grab Instant : Rp", harga_GrabInstant)
                print()

                if harga_MaximBox<harga_GoBox and harga_MaximBox<harga_GrabInstant:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nMaxim Box")
                elif harga_GrabInstant<harga_MaximBox and harga_GrabInstant<harga_GoBox:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGrab Instant")
                elif harga_GoBox<harga_MaximBox and harga_GoBox<harga_GrabInstant:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGo Box")
                print("==========================================================")
                
                layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                if layananlain.capitalize() == "Ya":
                    layanan_kurir_dalam_kota()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break

            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_dalam_kota == "3":
            layanan_kurir()
        elif input_dalam_kota == "0":
            print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
                
        
def layanan_kurir_luar_kota():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "=============== LAYANAN KURIR LUAR KOTA =================")
    print("\nBerikut Layanan Kurir Dalam Kota Yang Tersedia")
    print(Fore.CYAN + "1. Box (Mobil)")
    print(Fore.CYAN + "2. Kembali")
    print(Fore.RED + "0. Exit")
    input_luar_kota = input(Fore.GREEN + "\nPilih Layanan (1/2/0): ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_luar_kota == "1":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "=================== LAYANAN KURIR BOX ===================")
                print("\nPilih Sesuai Kebutuhan")
                input_ukuran, input_provinsi, input_asal, input_tujuan = mbl.get_input()
                harga_MaximBox = mbl.layananboxluarkota("maxim", input_ukuran.lower(), input_provinsi.title(), input_asal.title(), input_tujuan.title())
                harga_GoBox = mbl.layananboxluarkota("gojek", input_ukuran.lower(), input_provinsi.title(), input_asal.title(), input_tujuan.title())
                harga_GrabInstant = mbl.layananboxluarkota("Grab", input_ukuran.lower(), input_provinsi.title(), input_asal.title(), input_tujuan.title())
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Box Luar Kota dengan Maxim Box    : Rp", harga_MaximBox)
                print("Harga Kurir Box Luar Kota dengan Go Box       : Rp",harga_GoBox)
                print("Harga Kurir Box Luar Kota dengan Grab Instant : Rp",harga_GrabInstant)
                print()

                if harga_MaximBox<harga_GoBox and harga_MaximBox<harga_GrabInstant:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nMaxim Box")
                elif harga_GrabInstant<harga_MaximBox and harga_GrabInstant<harga_GoBox:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGrab Instant")
                elif harga_GoBox<harga_MaximBox and harga_GoBox<harga_GrabInstant:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGo Box")
                print("==========================================================")

                layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                if layananlain.capitalize() == "Ya":
                    layanan_kurir_dalam_kota()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break

            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_luar_kota == "2":
            layanan_kurir()
        elif input_luar_kota == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
            

def layanan_transportasi():
    print(Fore.RESET + "\n=============================================================")
    print(Fore.YELLOW + "== DAFTAR LAYANAN TRANSPORTASI OJEK ONLINE YANG TERSEDIA ===")
    print("\nBerikut Layanan Kurir Ojek Online Yang Tersedia")
    print(Fore.CYAN + "1. Mobil")
    print(Fore.CYAN + "2. Motor")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_transportasi = input(Fore.GREEN + "\nMasukkan Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_transportasi == "1":
            transportasi_mobi()
        elif input_transportasi == "2":
            transportasi_motor()
        elif input_transportasi == "3":
            main()
        elif input_transportasi == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()

def transportasi_mobi():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "============== LAYANAN TRANSPORTASI MOBIL ===============")
    print("\nPilih Sesuai Kebutuhan")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Luar Kota")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_mobil = input(Fore.GREEN + "\nPilih Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")
        
    while True:
        if input_mobil == "1":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "=============== LAYANAN MOBIL DALAM KOTA ================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi, jarak = mcd.get_input()
                harga_MaximCar = mcd.get_harga_layanan("maxim", input_provinsi.title(), jarak)
                harga_GoCar = mcd.get_harga_layanan("gojek", input_provinsi.title(), jarak)
                harga_GrabCar = mcd.get_harga_layanan("Grab", input_provinsi.title(), jarak)
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Mobil Dalam Kota dengan Maxim Car : Rp", harga_MaximCar)
                print("Harga Mobil Dalam Kota dengan Go Car    : Rp", harga_GoCar)
                print("Harga Mobil Dalam Kota dengan Grab Car  : Rp", harga_GrabCar)
                print()

                if harga_MaximCar<harga_GoCar and harga_MaximCar<harga_GrabCar:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nMaxim Car")
                elif harga_GrabCar<harga_MaximCar and harga_GrabCar<harga_GoCar:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGrab Car")
                elif harga_GoCar<harga_MaximCar and harga_GoCar<harga_GrabCar:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGo Car")
                print("==========================================================")

                layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                if layananlain.capitalize() == "Ya":
                    layanan_kurir_dalam_kota()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break
            
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
        
        elif input_mobil == "2":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "=============== LAYANAN MOBIL LUAR KOTA =================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi = mcl.get_input1()
                if input_provinsi.title() == "Yogyakarta":
                    print(Fore.RED + "Mohon Maaf Layanan Tidak Tersedia Di Provinsi Ini")
                else:
                    input_asal, input_tujuan = mcl.get_input2()
                    harga_MaximCar = mcl.get_harga_layanan("maxim", input_provinsi, input_asal, input_tujuan)
                    harga_GoCar = mcl.get_harga_layanan("gojek", input_provinsi, input_asal, input_tujuan)
                    harga_GrabCar = mcl.get_harga_layanan("Grab", input_provinsi, input_asal, input_tujuan)
                    print("\n==========================================================")

                    print("\n==========================================================")
                    print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                    print("Harga Mobil Luar Kota dengan Maxim Car : Rp", harga_MaximCar)
                    print("Harga Mobil Luar Kota dengan Go Car    : Rp", harga_GoCar)
                    print("Harga Mobil Luar Kota dengan Grab Car  : Rp", harga_GrabCar)
                    print()

                    if harga_MaximCar<harga_GoCar and harga_MaximCar<harga_GrabCar:
                        print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nMaxim Car")
                    elif harga_GrabCar<harga_MaximCar and harga_GrabCar<harga_GoCar:
                        print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGrab Car")
                    elif harga_GoCar<harga_MaximCar and harga_GoCar<harga_GrabCar:
                        print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGo Car")
                    print("==========================================================")

                    layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                    if layananlain.capitalize() == "Ya":
                        layanan_kurir_dalam_kota()
                    elif layananlain.capitalize() == "Tidak":
                        print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                        sys.exit()
                    else:
                        print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                        break

            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_mobil == "3":
            layanan_transportasi()
        elif input_mobil == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()

        
def transportasi_motor():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "============== LAYANAN TRANSPORTASI MOTOR ===============")
    print("\nPilih Sesuai Kebutuhan")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Kembali")
    print(Fore.RED + "0. Exit")
    input_motor = input(Fore.GREEN + "\nPilih Layanan (1/2/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_motor == "1":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "=============== LAYANAN MOTOR DALAM KOTA ================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi, jarak = mr.get_input()
                harga_MaximBike = mr.get_harga_layanan("maxim", input_provinsi.title(), jarak)
                harga_GoRide = mr.get_harga_layanan("gojek", input_provinsi.title(), jarak)
                harga_GrabBike = mr.get_harga_layanan("Grab", input_provinsi.title(), jarak)
                print("\n==========================================================")

                print("\n==========================================================")
                print("Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Motor Dalam Kota dengan Maxim Bike : Rp", harga_MaximBike)
                print("Harga Motor Dalam Kota dengan Go Ride    : Rp", harga_GoRide)
                print("Harga Motor Dalam Kota dengan Grab Bike  : Rp", harga_GrabBike)
                print()

                if harga_MaximBike<harga_GoRide and harga_MaximBike<harga_GrabBike:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nMaxim Bike")
                elif harga_GrabBike<harga_MaximBike and harga_GrabBike<harga_GoRide:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGrab Bike")
                elif harga_GoRide<harga_MaximBike and harga_GoRide<harga_GrabBike:
                    print(Fore.GREEN + "Rekomendasi Jasa Layanan Termurah Adalah \nGo Ride")
                print("==========================================================")

                layananlain = input(Fore.YELLOW + "\nApakah Anda Ingin Mengecek Layanan Lain? (Ya/Tidak) : ")
                if layananlain.capitalize() == "Ya":
                    layanan_kurir_dalam_kota()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break
    
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_motor == "2":
            layanan_kurir()
        elif input_motor == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()


if __name__ == "__main__":
    main()
