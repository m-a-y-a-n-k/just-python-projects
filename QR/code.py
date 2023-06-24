import qrcode as QR
from PIL import Image

qr = QR.QRCode(
    version=1, 
    error_correction=QR.constants.ERROR_CORRECT_H,
    box_size=50,
    border=10,
)

qr.add_data("https://www.spotify.com/us/download/android/")
qr.make(fit=True)

image = qr.make_image(fill_color="darkgreen", back_color="seagreen")

image.save("download_spotify.png")