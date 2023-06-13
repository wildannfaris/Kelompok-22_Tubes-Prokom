import json

def get_input1():
    input_provinsi = input("Input provinsi: ")
    return input_provinsi

def get_input2():
    input_asal = str(input("Asal : "))
    input_tujuan = str(input("Tujuan : "))
    return input_asal, input_tujuan


def get_harga_layanan(layanan, input_provinsi, input_asal, input_tujuan):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)
    
    with open("jarakkotadalamprov.json", "r") as file2:
        data2 = json.load(file2)
    
    provinsi_data = data2.get(input_provinsi)

    if input_provinsi() == "Yogyakarta":
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
            harga_MaximCar = get_harga_layanan("maxim", input_provinsi, input_asal, input_tujuan)
            harga_GoCar = get_harga_layanan("gojek", input_provinsi, input_asal, input_tujuan)
            harga_GrabCar = get_harga_layanan("Grab", input_provinsi, input_asal, input_tujuan)
            print("Harga Maxim Car : ", harga_MaximCar)
            print("Harga Go Car : ", harga_GoCar)
            print("Harga Grab Car : ", harga_GrabCar)

    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()
    