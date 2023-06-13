import json

def get_input():
    input_ukuran = input("ukuran : ")
    input_provinsi = input("Input provinsi: ")
    input_asal = input("asal : ")
    input_tujuan = input("tujuan : ")
    return input_ukuran, input_provinsi, input_asal, input_tujuan


def layananboxluarkota(layanan, input_ukuran, input_provinsi, input_asal, input_tujuan):
    with open("daftarharga.json", "r") as file1:
        data1 = json.load(file1)

    with open("jarakkotaluarprov.json", "r") as file2:
        data2 = json.load(file2)

    provinsi_data = data2.get(input_provinsi)

    for asal in provinsi_data:
        for tujuan in provinsi_data[asal]:
            jarak = provinsi_data[asal][tujuan]

            for item in data1[layanan]:
                if item.get("layanan") == "Maxim Box" or item.get("layanan") == "Go Box" or item.get("layanan") == "Grab Instant":
                    ukuran_data = item.get("ukuran", {}).get(input_ukuran)
                    if ukuran_data is not None and input_asal == asal and input_tujuan == tujuan:
                        harga_minimum = ukuran_data.get("provinsi", {}).get(input_provinsi, {}).get("harga_minimum")
                        harga_per_km = ukuran_data.get("provinsi", {}).get(input_provinsi, {}).get("harga_per_km")
                        if harga_minimum is not None and harga_per_km is not None:
                            if jarak <= 3:
                                total_harga = harga_minimum
                            else:
                                total_harga = harga_minimum + (harga_per_km * jarak)
                            return total_harga
                        
    raise Exception("Input Anda Tidak Sesuai, Silakan Cek Kembali")

def main():
    try : 
        input_ukuran, input_provinsi, input_asal, input_tujuan = get_input()
        harga_MaximBox = layananboxluarkota("maxim", input_ukuran, input_provinsi, input_asal, input_tujuan)
        harga_GoBox = layananboxluarkota("gojek", input_ukuran, input_provinsi, input_asal, input_tujuan)
        harga_GrabInstant = layananboxluarkota("Grab", input_ukuran, input_provinsi, input_asal, input_tujuan)
        print("Harga Maxim Box : ", harga_MaximBox)
        print("Harga Go Box : ",harga_GoBox)
        print("Harga Grab Instant : ",harga_GrabInstant)

    except Exception as e:
        print("Terjadi kesalahan : ", str(e))

if __name__ == "__main__":
    main()
    