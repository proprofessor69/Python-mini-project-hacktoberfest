from PIL import Image

def img2pdf(img_path, pdf_path):
    images = []

    for file in img_path:
        img = Image.open(file)
        img = img.convert('RGB')
        images.append(img)

    images[0].save(pdf_path, save_all=True, append_images=images[1:])

    print('Done')

# img2pdf(['1.jpg', '2.jpg', '3.jpg'], 'test.pdf')
