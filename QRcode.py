import qrcode 

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

text = input("Enter the text or URL to encode in the QR code: ")
output_file = "qrcode.png"
generate_qr_code(text, output_file)
print(f"QR code generated and saved as {output_file}") 