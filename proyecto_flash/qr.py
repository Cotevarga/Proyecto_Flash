import qrcode

url = "https://proyecto-flash-lvn3.onrender.com"

# Configuración del código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generar y guardar la imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_flash_amor.png")

print("⚡ ¡Código QR generado con éxito como 'qr_flash_amor.png'! ⚡")