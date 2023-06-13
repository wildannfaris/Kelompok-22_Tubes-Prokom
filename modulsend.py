import json

def get_input():
    input_provinsi = input("Input provinsi: ")
    jarak = float(input("Jarak (km): "))
    return input_provinsi, jarak
    

def layanansend(layanan, input_provinsi, jarak):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)


    for item in data1[layanan]:
        if item["layanan"] == "Go Send" or item["layanan"] == "Grab Same Day" or item["layanan"] == "Maxim Delivery":
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
        harga_MaximDelivery = layanansend("maxim", input_provinsi, jarak)
        harga_GoSend = layanansend("gojek", input_provinsi, jarak)
        harga_GrabSameDay = layanansend("Grab", input_provinsi, jarak)
        print("Harga Maxim Delivery : ", harga_MaximDelivery)
        print("Harga Go Send : ", harga_GoSend)
        print("Harga Grab Same Day : ", harga_GrabSameDay)

    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()