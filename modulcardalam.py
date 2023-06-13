import json

def get_input():
    input_provinsi = input("Input provinsi: ")
    jarak = float(input("Jarak (km): "))
    return input_provinsi, jarak


def get_harga_layanan(layanan, input_provinsi, jarak):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)
    
    for item in data1[layanan]:
        if item["layanan"] == "Go Car" or item["layanan"] == "Grab Car" or item["layanan"] == "Car":
            provinsi_data = item["provinsi"]
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
        harga_MaximCar = get_harga_layanan("maxim", input_provinsi, jarak)
        harga_GoCar = get_harga_layanan("gojek", input_provinsi, jarak)
        harga_GrabCar = get_harga_layanan("Grab", input_provinsi, jarak)
        print("Harga Maxim Car : ", harga_MaximCar)
        print("Harga Go Car : ", harga_GoCar)
        print("Harga Grab Car : ", harga_GrabCar)

    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()
    