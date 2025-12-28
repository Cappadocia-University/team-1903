import tkinter as tk
from tkinter import messagebox

class MagicSquareGenerator:
    """Sihirli Kare mantığını hesaplayan sınıf (Back-end)"""
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def generate(self):
        row, col = 0, self.size // 2
        for num in range(1, self.size * self.size + 1):
            self.grid[row][col] = num
            old_row, old_col = row, col
            row = (row - 1) % self.size
            col = (col - 1) % self.size
            if self.grid[row][col] != 0:
                row = (old_row + 1) % self.size
                col = old_col
        return self.grid

def draw_grid_window(n, matrix):
    """
    Hesaplanan matrisi ayrı bir pencerede görsel olarak çizer (Front-end).
    Tkinter kullandığımız için ekstra kuruluma gerek yoktur.
    """
    # Ana pencereyi oluştur
    window = tk.Tk()
    window.title(f"{n}x{n} Sihirli Kare")
    
    # Pencere arkaplan rengi
    window.configure(bg="#f0f0f0")

    # Başlık Yazısı
    lbl_title = tk.Label(window, text=f"Sihirli Kare (N={n})", font=("Arial", 16, "bold"), bg="#f0f0f0")
    lbl_title.pack(pady=10)

    # Karelerin tutulacağı çerçeve (Frame)
    frame_grid = tk.Frame(window, bg="black", bd=2)
    frame_grid.pack(padx=20, pady=20)

    # Matrisi görsel kutucuklara dökme
    for i in range(n):
        for j in range(n):
            deger = matrix[i][j]
            
            # Her bir sayı için bir etiket (Label) oluştur
            cell = tk.Label(
                frame_grid, 
                text=str(deger), 
                font=("Helvetica", 14, "bold"),
                width=4,   # Genişlik
                height=2,  # Yükseklik
                relief="solid", # Kenarlık
                borderwidth=1,
                bg="white", # Kutu rengi
                fg="#333"   # Yazı rengi
            )
            # Grid yöntemiyle yan yana ve alt alta diz
            cell.grid(row=i, column=j, padx=1, pady=1)

    # Bilgilendirme notu
    magic_sum = n * (n**2 + 1) // 2
    lbl_info = tk.Label(window, text=f"Satır/Sütun Toplamı: {magic_sum}", font=("Arial", 10), bg="#f0f0f0", fg="blue")
    lbl_info.pack(pady=5)

    # Pencereyi açık tut
    window.mainloop()

# --- ANA PROGRAM ---
if __name__ == "__main__":
    try:
        # 1. Kullanıcıdan veriyi al
        print("\n--- SİHİRLİ KARE OLUŞTURUCU ---")
        girdi = input("Karenin boyutunu giriniz (Tek sayı, örn: 3, 5): ").strip()
        n = int(girdi)

        if n % 2 == 0 or n < 1:
            print("HATA: Lütfen pozitif bir TEK sayı giriniz!")
        else:
            # 2. Hesaplamayı yap
            generator = MagicSquareGenerator(n)
            sonuc_matrisi = generator.generate()
            
            print(f"\n{n}x{n} tablosu hesaplandı. Pencere açılıyor...")
            
            # 3. Görsel pencereyi aç
            draw_grid_window(n, sonuc_matrisi)

    except ValueError:
        print("Hata: Lütfen sayısal bir değer giriniz.")