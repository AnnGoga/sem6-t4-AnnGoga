import pyqrcode
import pyzbar 
from PIL import Image, ImageDraw
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
    image = Image.open(file)  # Открываем изображение.
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    for i in range(int(width / 2)):
        for j in range(int(height / 2)):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (255, 20, 147))

    for i in range(int(width / 2), width):
        for j in range(int(height / 2), height):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (0, 191, 255))

    for i in range(int(width / 2)):
        for j in range(int(height / 2), height):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (0, 255, 127))
    image.save("multicolored_qrcode.png", "PNG")
    del draw


if __name__ == "__main__":
    string = ""
    with open("Shake.txt", encoding='utf-8') as f:
        for line in f:
            string += line

    text_to_qrcode(string, (23, 23, 23), (51, 161, 201), "png")

    print('Расшифровка:', decode_qrcode("qrcode.png"))

    color_qrcode("qrcode.png", (255, 130, 171))

    print('Расшифровка после перекрашивания:', decode_qrcode("multicolored_qrcode.png"))
