import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

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
steps = 50  # Jumlah langkah dalam animasi

# Membuat figur
fig, ax = plt.subplots(figsize=(8, 8))
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_title("Animasi Transformasi 2D: Translasi dan Skaling")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis('equal')

# Garis objek
line_awal, = ax.plot([], [], 'bo-', label="Objek Awal")
line_translasi, = ax.plot([], [], 'go-', label="Translasi")
line_skaling, = ax.plot([], [], 'ro-', label="Skaling")
ax.legend()

# Inisialisasi frame awal
def init():
    line_awal.set_data(objek_awal[0], objek_awal[1])
    line_translasi.set_data([], [])
    line_skaling.set_data([], [])
    return line_awal, line_translasi, line_skaling

# Fungsi pembaruan frame
def update(frame):
    # Hitung translasi dan skaling bertahap
    dx_step = dx * (frame / steps)
    dy_step = dy * (frame / steps)
    sx_step = 1 + (sx - 1) * (frame / steps)
    sy_step = 1 + (sy - 1) * (frame / steps)

    objek_translasi = translasi(objek_awal, dx_step, dy_step)
    objek_skaling = skaling(objek_awal, sx_step, sy_step)

    # Perbarui data garis
    line_translasi.set_data(objek_translasi[0], objek_translasi[1])
    line_skaling.set_data(objek_skaling[0], objek_skaling[1])
    return line_translasi, line_skaling

# Membuat animasi
ani = FuncAnimation(fig, update, frames=steps + 1, init_func=init, blit=True, interval=50)

plt.show()
