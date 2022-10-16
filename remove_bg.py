from rembg import remove
from PIL import Image

# TODO: Fix and improve

input_path = 'input.jpg'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
