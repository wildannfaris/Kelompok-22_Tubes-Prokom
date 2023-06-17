import modulsend as ms
import modulcardalam as mcd
import modulcarluar as mcl
import modulride as mr
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
    print("Berikut ini merupakan jasa layanan kurir ojek online yang \ntersedia di Pulau Jawa")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Luar Kota")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_kurir = input(Fore.GREEN + "\nSilakan Pilih Layanan (1/2/3/0): ")
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
    print("\nBerikut layanan kurir dalam kota yang tersedia di Pulau Jawa")
    print(Fore.CYAN + "1. Reguler (Motor)")
    print(Fore.CYAN + "2. Box (Mobil)")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_dalam_kota = input(Fore.GREEN + "\nSilakan Pilih Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_dalam_kota == "1":
            print(Fore.RESET + "\n==========================================================")
            print(Fore.YELLOW + "================== LAYANAN KURIR REGULER =================")
            print("\nPilih Sesuai Kebutuhan Anda")
            try:
                input_provinsi, jarak = ms.get_input()
                harga_MaximDelivery = ms.layanan_send("maxim", input_provinsi.title(), jarak)
                harga_GoSend = ms.layanan_send("gojek", input_provinsi.title(), jarak)
                harga_GrabSameDay = ms.layanan_send("Grab",input_provinsi.title(), jarak)
                format_harga_MaximDelivery = "Rp {:,}".format(harga_MaximDelivery).replace(',', '.')
                format_harga_GoSend = "Rp {:,}".format(harga_GoSend).replace(',', '.')
                format_harga_GrabSameDay = "Rp {:,}".format(harga_GrabSameDay).replace(',', '.')
                print("\n==========================================================")
                
                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Standar dengan Maxim Delivery   : ", format_harga_MaximDelivery)
                print("Harga Kurir Standar dengan GoSend           : ", format_harga_GoSend)
                print("Harga Kurir Standar dengan Grab Same Day    : ", format_harga_GrabSameDay)
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
            
            except ms.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalah : ", str(e))
            except ValueError as e:
                print(Fore.RED + "Terjadi kesalah : ", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
    

        elif input_dalam_kota == "2":
            print(Fore.RESET + "\n==========================================================")
            print(Fore.YELLOW + "=================== LAYANAN KURIR BOX ===================")
            print("\nPilih Sesuai Kebutuhan")
            try:
                input_ukuran, input_provinsi, jarak = mbd.get_input()
                harga_MaximBox = mbd.layanan_box_dalam_kota("maxim", input_ukuran.lower(), input_provinsi.title(), jarak)
                harga_GoBox = mbd.layanan_box_dalam_kota("gojek", input_ukuran.lower(), input_provinsi.title(), jarak)
                harga_GrabInstant = mbd.layanan_box_dalam_kota("Grab", input_ukuran.lower(), input_provinsi.title(), jarak)
                format_harga_MaximBox = "Rp {:,}".format(harga_MaximBox).replace(',', '.')
                format_harga_GoBox = "Rp {:,}".format(harga_GoBox).replace(',', '.')
                format_harga_GrabInstant = "Rp {:,}".format(harga_GrabInstant).replace(',', '.')
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Box Dalam Kota dengan Maxim Box     : ", format_harga_MaximBox)
                print("Harga Kurir Box Dalam Kota dengan Go Box        : ", format_harga_GoBox)
                print("Harga Kurir Box Dalam Kotab dengan Grab Instant : ", format_harga_GrabInstant)
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

            except mbd.UkuranError as e:
                print(Fore.RED + "Terjadi kesalahan:", str(e))
            except ValueError as e:
                print(Fore.RED + "Terjadi kesalahan:", str(e))
            except mbd.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalahan:", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan:", str(e))
                
        elif input_dalam_kota == "3":
            layanan_kurir()
        elif input_dalam_kota == "0":
            print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
                
        
def layanan_kurir_luar_kota():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "=============== LAYANAN KURIR LUAR KOTA =================")
    print("\nBerikut layanan kurir luar kota yang tersedia di Pulau Jawa")
    print(Fore.CYAN + "1. Box (Mobil)")
    print(Fore.CYAN + "2. Kembali")
    print(Fore.RED + "0. Exit")
    input_luar_kota = input(Fore.GREEN + "\nSilakan Pilih Layanan (1/2/0): ")
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
                format_harga_MaximBox = "Rp {:,}".format(harga_MaximBox).replace(',', '.')
                format_harga_GoBox = "Rp {:,}".format(harga_GoBox).replace(',', '.')
                format_harga_GrabInstant = "Rp {:,}".format(harga_GrabInstant).replace(',', '.')
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Kurir Box Luar Kota dengan Maxim Box    : ", format_harga_MaximBox)
                print("Harga Kurir Box Luar Kota dengan Go Box       : ", format_harga_GoBox)
                print("Harga Kurir Box Luar Kota dengan Grab Instant : ", format_harga_GrabInstant)
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
                    layanan_kurir()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break

            except mbl.ukuranerror as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except mbl.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except mbl.AsalTidakTersedia as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except mbl.TujuanTidakTersedia as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_luar_kota == "2":
            layanan_kurir()
        elif input_luar_kota == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()
            

def layanan_transportasi():
    print(Fore.RESET + "\n=============================================================")
    print(Fore.YELLOW + "=== DAFTAR LAYANAN TRANSPORTASI OJEK ONLINE YANG TERSEDIA ===")
    print("\nBerikut ini merupakan jasa layanan transportasi ojek online \nyang tersedia di Pulau Jawa")
    print(Fore.CYAN + "1. Mobil")
    print(Fore.CYAN + "2. Motor")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_transportasi = input(Fore.GREEN + "\nSilakan Masukkan Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_transportasi == "1":
            transportasi_mobil()
        elif input_transportasi == "2":
            transportasi_motor()
        elif input_transportasi == "3":
            main()
        elif input_transportasi == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()


def transportasi_mobil():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "=============== LAYANAN TRANSPORTASI MOBIL ===============")
    print("\nBerikut layanan transportasi mobil yang tersedia \ndi Pulau Jawa")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Luar Kota")
    print(Fore.CYAN + "3. Kembali")
    print(Fore.RED + "0. Exit")
    input_mobil = input(Fore.GREEN + "\nSilakan Pilih Layanan (1/2/3/0) : ")
    print(Fore.RESET + "==========================================================")
        
    while True:
        if input_mobil == "1":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "=============== LAYANAN MOBIL DALAM KOTA ================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi, jarak = mcd.get_input()
                harga_MaximCar = mcd.layanan_mobil_dalam_kota("maxim", input_provinsi.title(), jarak)
                harga_GoCar = mcd.layanan_mobil_dalam_kota("gojek", input_provinsi.title(), jarak)
                harga_GrabCar = mcd.layanan_mobil_dalam_kota("Grab", input_provinsi.title(), jarak)
                format_harga_MaximCar = "Rp {:,}".format(harga_MaximCar).replace(',', '.')
                format_harga_GoCar = "Rp {:,}".format(harga_GoCar).replace(',', '.')
                format_harga_GrabCar = "Rp {:,}".format(harga_GrabCar).replace(',', '.')
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Mobil Dalam Kota dengan Maxim Car : ", format_harga_MaximCar)
                print("Harga Mobil Dalam Kota dengan Go Car    : ", format_harga_GoCar)
                print("Harga Mobil Dalam Kota dengan Grab Car  : ", format_harga_GrabCar)
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
                    transportasi_mobil()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break
            
            except mcd.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except ValueError as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi Kesalahan : ", str(e))
        
        elif input_mobil == "2":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "================ LAYANAN MOBIL LUAR KOTA =================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi = mcl.get_input1()
                if input_provinsi.title() == "Yogyakarta":
                    print(Fore.RED + "Mohon Maaf Layanan Tidak Tersedia Di Provinsi Ini")
                else:
                    input_asal, input_tujuan = mcl.get_input2()
                    harga_MaximCar = mcl.layanan_mobil_luar_kota("maxim", input_provinsi.title(), input_asal.title(), input_tujuan.title())
                    harga_GoCar = mcl.layanan_mobil_luar_kota("gojek", input_provinsi.title(), input_asal.title(), input_tujuan.title())
                    harga_GrabCar = mcl.layanan_mobil_luar_kota("Grab", input_provinsi.title(), input_asal.title(), input_tujuan.title())
                    format_harga_MaximCar = "Rp {:,}".format(harga_MaximCar).replace(',', '.')
                    format_harga_GoCar = "Rp {:,}".format(harga_GoCar).replace(',', '.')
                    format_harga_GrabCar = "Rp {:,}".format(harga_GrabCar).replace(',', '.')
                    print("\n==========================================================")

                    print("\n==========================================================")
                    print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                    print("Harga Mobil Luar Kota dengan Maxim Car : ", format_harga_MaximCar)
                    print("Harga Mobil Luar Kota dengan Go Car    : ", format_harga_GoCar)
                    print("Harga Mobil Luar Kota dengan Grab Car  : ", format_harga_GrabCar)
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
                        transportasi_mobil()
                    elif layananlain.capitalize() == "Tidak":
                        print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                        sys.exit()
                    else:
                        print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                        break

            except mcl.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except mcl.AsalTidakTersedia as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except mcl.TujuanTidakTersedia as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_mobil == "3":
            layanan_transportasi()
        elif input_mobil == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()

        
def transportasi_motor():
    print(Fore.RESET + "\n==========================================================")
    print(Fore.YELLOW + "=============== LAYANAN TRANSPORTASI MOTOR ===============")
    print("\nBerikut layanan transportasi motor yang tersedia di Pulau Jawa")
    print(Fore.CYAN + "1. Dalam Kota")
    print(Fore.CYAN + "2. Kembali")
    print(Fore.RED + "0. Exit")
    input_motor = input(Fore.GREEN + "\nSilakan Pilih Layanan (1/2/0) : ")
    print(Fore.RESET + "==========================================================")

    while True:
        if input_motor == "1":
            try:
                print(Fore.RESET + "\n==========================================================")
                print(Fore.YELLOW + "================ LAYANAN MOTOR DALAM KOTA ================")
                print("\nPilih Sesuai Kebutuhan")
                input_provinsi, jarak = mr.get_input()
                harga_MaximBike = mr.layanan_motor("maxim", input_provinsi.title(), jarak)
                harga_GoRide = mr.layanan_motor("gojek", input_provinsi.title(), jarak)
                harga_GrabBike = mr.layanan_motor("Grab", input_provinsi.title(), jarak)
                format_harga_MaximBike = "Rp {:,}".format(harga_MaximBike).replace(',', '.')
                format_harga_GoRide = "Rp {:,}".format(harga_GoRide).replace(',', '.')
                format_harga_GrabBike = "Rp {:,}".format(harga_GrabBike).replace(',', '.')
                print("\n==========================================================")

                print("\n==========================================================")
                print(Fore.BLUE + "Berikut Adalah Beberapa Perbandingan Harga \nLayanan Yang Dapat Kami Berikan\n")
                print("Harga Motor Dalam Kota dengan Maxim Bike : ", format_harga_MaximBike)
                print("Harga Motor Dalam Kota dengan Go Ride    : ", format_harga_GoRide)
                print("Harga Motor Dalam Kota dengan Grab Bike  : ", format_harga_GrabBike)
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
                    layanan_transportasi()
                elif layananlain.capitalize() == "Tidak":
                    print(Fore.GREEN + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
                    sys.exit()
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
                    break
    
            except mr.ProvinsiTidakTersediaError as e:
                print(Fore.RED + "Terjadi kesalah : ", str(e))
            except ValueError as e:
                print(Fore.RED + "Terjadi kesalah : ", str(e))
            except Exception as e:
                print(Fore.RED + "Terjadi kesalahan : ", str(e))

        elif input_motor == "2":
            layanan_transportasi()
        elif input_motor == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            sys.exit()


if __name__ == "__main__":
    main()
