import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk translasi objek
def translasi(koordinat, dx, dy):
    translasi_matrix = np.array([[1, 0, dx],
                                 [0, 1, dy],
                                 [0, 0, 1]])
    koordinat = np.vstack((koordinat, np.ones((1, koordinat.shape[1]))))
    hasil_translasi = np.dot(translasi_matrix, koordinat)
    return hasil_translasi[:2]

# Fungsi untuk skaling objek
def skaling(koordinat, sx, sy):
    skaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    koordinat = np.vstack((koordinat, np.ones((1, koordinat.shape[1]))))
    hasil_skaling = np.dot(skaling_matrix, koordinat)
    return hasil_skaling[:2]

# Koordinat objek awal (segitiga)
objek_awal = np.array([[0, 1, 0.5, 0],  # x-koordinat
                       [0, 0, 1, 0]])   # y-koordinat

# Parameter translasi dan skaling
dx, dy = 2, 3  # Translasi
sx, sy = 2, 1.5  # Skaling

# Lakukan translasi
objek_translasi = translasi(objek_awal, dx, dy)

# Lakukan skaling
objek_skaling = skaling(objek_awal, sx, sy)

# Visualisasi
plt.figure(figsize=(8, 8))
plt.plot(objek_awal[0], objek_awal[1], 'bo-', label="Objek Awal")
plt.plot(objek_translasi[0], objek_translasi[1], 'go-', label="Setelah Translasi")
plt.plot(objek_skaling[0], objek_skaling[1], 'ro-', label="Setelah Skaling")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Transformasi 2D: Translasi dan Skaling")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.show()
