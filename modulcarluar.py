import json

class ProvinsiTidakTersediaError(Exception):
    pass

class AsalTidakTersedia(Exception):
    pass

class TujuanTidakTersedia(Exception):
    pass

def get_input1():
    input_provinsi = input("Input Provinsi Asal : ")
    return input_provinsi

def get_input2():
    input_asal = input("Kota Asal : ")
    input_tujuan = input("Kota Tujuan : ")
    return input_asal, input_tujuan


def layanan_mobil_luar_kota(layanan, input_provinsi, input_asal, input_tujuan):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)
    
    with open("jarakkotadalamprov.json", "r") as file2:
        data2 = json.load(file2)
    
    provinsi_data = data2.get(input_provinsi)

    if provinsi_data is None:
        raise ProvinsiTidakTersediaError("Provinsi yang anda input tidak terdapat di Pulau Jawa")
    
    if input_asal not in provinsi_data:
        raise AsalTidakTersedia("Asal tidak tersedia dalam provinsi ini")

    if input_tujuan not in provinsi_data[input_asal]:
        raise TujuanTidakTersedia("Tujuan tidak tersedia")

    if input_provinsi == "Yogyakarta":
        print("Mohon Maaf Layanan Tidak Tersedia Di Provinsi Ini")
        return None
    else:
        for item in data1[layanan]:
            if item["layanan"] == "Go Car" or item["layanan"] == "Grab Car" or item["layanan"] == "Car":
                provinsi_data2 = item["provinsi"]
                for asal in provinsi_data:
                    for tujuan in provinsi_data[asal]:
                        jarak = provinsi_data[asal][tujuan]
                        if input_asal == asal and input_tujuan == tujuan:
                            harga_minimum = provinsi_data2.get(input_provinsi)["harga_minimum"]
                            harga_per_km = provinsi_data2.get(input_provinsi)["harga_per_km"]
                            if jarak <= 3:
                                total_harga = harga_minimum
                            else:
                                total_harga = harga_minimum + (harga_per_km * jarak)
                                return total_harga          
    
    raise Exception("Input Anda Tidak Sesuai, Silakan Cek Kembali")


def main():
    try:
        input_provinsi = get_input1()
        if input_provinsi == "Yogyakarta":
            print("Mohon Maaf Layanan Tidak Tersedia Di Provinsi Ini")

        else:
            input_asal, input_tujuan = get_input2()
            harga_MaximCar = layanan_mobil_luar_kota("maxim", input_provinsi, input_asal, input_tujuan)
            harga_GoCar = layanan_mobil_luar_kota("gojek", input_provinsi, input_asal, input_tujuan)
            harga_GrabCar = layanan_mobil_luar_kota("Grab", input_provinsi, input_asal, input_tujuan)
            print("Harga Maxim Car : ", harga_MaximCar)
            print("Harga Go Car : ", harga_GoCar)
            print("Harga Grab Car : ", harga_GrabCar)

    except ProvinsiTidakTersediaError as e:
        print("Terjadi kesalahan : ", str(e))
    except AsalTidakTersedia as e:
        print("Terjadi kesalahan : ", str(e))
    except TujuanTidakTersedia as e:
        print("Terjadi kesalahan : ", str(e))
    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()
