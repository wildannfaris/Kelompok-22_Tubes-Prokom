import json

def get_input():
    input_ukuran = input("Ukuran : ")
    input_provinsi = input("Input Provinsi Asal : ")
    jarak = float(input("Masukkan Jarak (km) : "))
    return input_ukuran, input_provinsi, jarak


def layananboxdalamkota(layanan, input_ukuran, input_provinsi, jarak):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)

        for item in data1[layanan]:
            if item.get("layanan") == "Maxim Box" or item.get("layanan") == "Go Box" or item.get("layanan") == "Grab Instant":
                ukuran_data = item.get("ukuran", {}).get(input_ukuran)
                harga_minimum = ukuran_data.get("provinsi", {}).get(input_provinsi, {}).get("harga_minimum")
                harga_per_km = ukuran_data.get("provinsi", {}).get(input_provinsi, {}).get("harga_per_km")
                if harga_minimum is not None and harga_per_km is not None:
                    total_harga = harga_minimum + (harga_per_km * jarak)
                    return total_harga

    raise Exception("Input Anda Tidak Sesuai, Silakan Cek Kembali")

def main():
    try:
        input_ukuran, input_provinsi, jarak = get_input()
        harga_MaximBox = layananboxdalamkota("maxim", input_ukuran, input_provinsi, jarak)
        harga_GoBox = layananboxdalamkota("gojek", input_ukuran, input_provinsi, jarak)
        harga_GrabInstant = layananboxdalamkota("Grab", input_ukuran, input_provinsi, jarak)
        print("Harga Maxim Box : ", harga_MaximBox)
        print("Harga Go Box : ", harga_GoBox)
        print("Harga Grab Instant : ", harga_GrabInstant)

    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()
    