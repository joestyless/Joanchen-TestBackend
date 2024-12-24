def hitung_gaji(jam_kerja, tarif_per_jam):
    if jam_kerja > 40:
        lembur = jam_kerja - 40
        gaji = (40 * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
    else:
        gaji = jam_kerja * tarif_per_jam
    return gaji

# Input
jam = int(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))
print("Gaji total:", hitung_gaji(jam, tarif))
