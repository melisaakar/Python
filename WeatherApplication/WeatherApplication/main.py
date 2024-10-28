from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests


def get_hava_durumu():
    api_key = "YOUR_API_KEY"  # Buraya kendi API anahtarını ekle
    sehir = sehriyazEntry.get()

    if not sehir:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin.")
        return

    try:
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}"
        response = requests.get(api_url)

        if response.status_code != 200:
            messagebox.showerror("Hata", "Hava durumu verisi alınamadı. Lütfen şehir adını kontrol edin.")
            return

        hava_durumu_verisi = response.json()

        turkce_durumlar = {
            'clear sky': 'Açık Gökyüzü',
            'few clouds': 'Az Bulutlu',
            'scattered clouds': 'Parçalı Bulutlu',
            'broken clouds': 'Kırık Bulutlu',
            'overcast clouds': 'Kapalı Bulutlu',
            'light rain': 'Hafif Yağmurlu',
            'moderate rain': 'Orta Şiddetli Yağmurlu',
            'heavy intensity rain': 'Yoğun Yağmurlu',
            'very heavy rain': 'Çok Yoğun Yağmurlu',
        }

        durum = hava_durumu_verisi['weather'][0]['description']
        turkce_durum = turkce_durumlar.get(durum.lower(), durum)

        sıcaklık = hava_durumu_verisi['main']['temp'] - 273.15  # Kelvin'den Celsius'a çevir
        yeni_sıcaklık = int(sıcaklık)

        # Sıcaklık ve durumu içeren dikdörtgeni oluştur
        canvas.delete("all")
        canvas.create_rectangle(10, 10, 300, 70, fill="white smoke")
        canvas.create_text(155, 40, text=f"Sıcaklık: {yeni_sıcaklık}°C\nDurum: {turkce_durum}", font=("Arial", 10), anchor="center")

        # Şehire özel resmi göster
        if sehir.lower() in ["istanbul", "ankara", "bursa", "antalya"]:
            show_image(f"{sehir.lower()}.jpeg")

    except Exception as e:
        messagebox.showerror("Hata", f"Hava durumu alınırken bir hata oluştu:\n{e}")

def show_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 190), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

screen = Tk()
screen.title("Hava Durumu Uygulaması")
screen.minsize(width=390, height=400)
screen.config(padx=20, pady=20)

sehriyazEntry = Entry(width=20)
sehriyazEntry.pack()

havaDurumGösterButon = Button(text="Havayı Göster", command=get_hava_durumu)
havaDurumGösterButon.pack()

canvas = Canvas(screen, width=300, height=80)
canvas.pack()

image_label = Label(screen)
image_label.pack()

screen.mainloop()
