import qrcode
image = qrcode.make("https://thornim.github.io/portfolio-sante/")
type(image)
file_name = "code.png"
image.save(file_name)

print("QR code créé avec succès")