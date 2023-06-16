import json

class ProvinsiTidakTersediaError(Exception):
    pass

def get_input():
    input_provinsi = input("Input Provinsi Asal : ")
    try:
        jarak = float(input("Jarak Tempuh (km): "))
    except ValueError:
        raise ValueError("Input jarak harus berupa angka")
    return input_provinsi, jarak


def layanan_mobil_dalam_kota(layanan, input_provinsi, jarak):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)
    
    for item in data1[layanan]:
        if item["layanan"] == "Go Car" or item["layanan"] == "Grab Car" or item["layanan"] == "Car":
            provinsi_data = item["provinsi"]
            if input_provinsi not in provinsi_data:
                raise ProvinsiTidakTersediaError("Provinsi yang anda input tidak terdapat di Pulau Jawa")
            harga_minimum = provinsi_data.get(input_provinsi)["harga_minimum"]
            harga_per_km = provinsi_data.get(input_provinsi)["harga_per_km"]
            if jarak <= 3:
                total_harga = harga_minimum
            else:
                total_harga = harga_minimum + (harga_per_km * jarak)
            return total_harga
        
    raise Exception("Input Anda Tidak Sesuai, Silakan Cek Kembali")

def main():
    try:
        input_provinsi, jarak = get_input()
        harga_MaximCar = layanan_mobil_dalam_kota("maxim", input_provinsi, jarak)
        harga_GoCar = layanan_mobil_dalam_kota("gojek", input_provinsi, jarak)
        harga_GrabCar = layanan_mobil_dalam_kota("Grab", input_provinsi, jarak)
        print("Harga Maxim Car : ", harga_MaximCar)
        print("Harga Go Car : ", harga_GoCar)
        print("Harga Grab Car : ", harga_GrabCar)

    except ProvinsiTidakTersediaError as e:
        print("Terjadi kesalahan : ", str(e))
    except ValueError as e:
        print("Terjadi kesalahan : ", str(e))
    except Exception as e:
        print("Terjadi Kesalahan : ", str(e))

if __name__ == "__main__":
    main()
