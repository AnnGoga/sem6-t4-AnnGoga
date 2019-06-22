import pyqrcode
import pyzbar 
import PIL
import png

def text_to_qrcode(text, module_color, background, file_format='eps', scale=6):
    qr = pyqrcode.create(text)
    if file_format == 'png':
        qr.png('qrcode.png', scale=scale, module_color=module_color, background=background)
    elif file_format == 'eps':
        qr.eps('qrcode.eps', scale=scale, module_color=module_color, background=background)
    elif file_format == 'svg':
        qr.svg('qrcode.svg', scale=scale, module_color=module_color, background=background)


def decode_qrcode(file):
    result = decode(Image.open(file))
    return result[0].data


def color_qrcode(file, background):
    image = Image.open(file)  
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)  
    width = image.size[0] 
    height = image.size[1]  
    pix = image.load()  

if __name__ == "__main__":
    string = ""
    with open("Shake.txt", encoding='utf-8') as f:
        for line in f:
            string += line

    text_to_qrcode(string, (23, 23, 23), (51, 161, 201), "png")

    print('Расшифровка:', decode_qrcode("qrcode.png"))

    color_qrcode("qrcode.png", (255, 130, 171))
