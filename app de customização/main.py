import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import ctypes

class CustomizationApp:
    def __init__(self, master):
        self.master = master
        master.title("Customization App")
        master.geometry("400x400")  # Reduzi o tamanho da janela
        master.configure(bg="#f0f0f0")

        self.wallpaper_path = ""

        self.label = tk.Label(master, text="Personalize seu plano de fundo", font=("Helvetica", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Reduzi o tamanho do canvas
        self.canvas = tk.Canvas(master, width=300, height=150, bg="white", borderwidth=2, relief="groove")
        self.canvas.pack(pady=10)

        self.choose_wallpaper_button = tk.Button(master, text="Escolher Papel de Parede", font=("Helvetica", 12),
                                                 command=self.choose_wallpaper, bg="#4caf50", fg="white")
        self.choose_wallpaper_button.pack(pady=10)

        self.apply_button = tk.Button(master, text="Aplicar Configurações", font=("Helvetica", 12),
                                      command=self.apply_settings, bg="#2196f3", fg="white")
        self.apply_button.pack(pady=10)

        self.wallpaper_label = tk.Label(master, text="Papel de Parede Atual: Nenhum", font=("Helvetica", 10), bg="#f0f0f0")
        self.wallpaper_label.pack(pady=5)

    def choose_wallpaper(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")])

        if file_path:
            self.wallpaper_path = file_path
            self.display_wallpaper(file_path)
            self.wallpaper_label.config(text=f"Papel de Parede Atual: {file_path}")

    def display_wallpaper(self, file_path):
        try:
            image = Image.open(file_path)
            image.thumbnail((300, 150))  # Reduz o tamanho da imagem para caber no canvas

            tk_image = ImageTk.PhotoImage(image)

            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
            self.canvas.image = tk_image

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exibir o papel de parede: {e}")

    def apply_settings(self):
        if self.wallpaper_path:
            try:
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, self.wallpaper_path, 3)
                messagebox.showinfo("Sucesso", "Configurações aplicadas com sucesso!")
            except AttributeError:
                messagebox.showerror("Erro", "Esta funcionalidade é suportada apenas no Windows.")
        else:
            messagebox.showwarning("Aviso", "Escolha um papel de parede antes de aplicar as configurações.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomizationApp(root)
    root.mainloop()








