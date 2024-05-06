from PIL import Image

image = Image.open('welcome diamond hands.jpg')

print(f'Current size : {image.size}')

resized_image = image.resize((500, 500))

resized_image.save('welcome back hands500.jpg')