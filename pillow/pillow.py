from PIL import Image
import os

ordner = "../images/"
# thumbnails
bilder = os.listdir(ordner)
for bild in bilder:
    aktuelles_bild = Image.open(ordner + bild)
    aktuelles_bild.thumbnail((120, 120))
    aktuelles_bild.save(ordner + "thumbnail-" + bild)


# grayscale
bilder = os.listdir(ordner)
for bild in bilder:
    aktuelles_bild = Image.open(ordner + bild)
    aktuelles_bild.convert("L").save(ordner + "grayscale-" + bild)

# wasserzeichen
bilder = os.listdir(ordner)
for bild in bilder:
    if not bild.find("python") == 0:
        continue
    hauptbild = Image.open(ordner + bild)
    wasserzeichen = Image.open(ordner + "watermark.png")
    wasserzeichen.thumbnail((hauptbild.size[0], hauptbild.size[1]))
    hauptbild.paste(wasserzeichen, (0, 0), wasserzeichen)
    hauptbild.save(ordner + "watermark-" + bild)

