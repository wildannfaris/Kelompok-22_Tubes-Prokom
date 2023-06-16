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

def layanan_motor(layanan, input_provinsi, jarak):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)

    for item in data1[layanan]:
        if item["layanan"] == "Go Ride" or item["layanan"] == "Grab Bike" or item["layanan"] == "Bike":
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
        harga_MaximBike = layanan_motor("maxim", input_provinsi, jarak)
        harga_GoRide = layanan_motor("gojek", input_provinsi, jarak)
        harga_GrabBike = layanan_motor("Grab", input_provinsi, jarak)
        print("Harga Maxim Bike : ", harga_MaximBike)
        print("Harga Go Ride : ", harga_GoRide)
        print("Harga Grab Bike : ", harga_GrabBike)
    
    except ProvinsiTidakTersediaError as e:
        print("Terjadi kesalah : ", str(e))
    except ValueError as e:
        print("Terjadi kesalah : ", str(e))
    except Exception as e:
        print("Terjadi kesalahan : ", str(e))


if __name__ == "__main__":
    main()
