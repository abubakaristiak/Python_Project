# from sketchpy import canvas

# pen = canvas.sketch_from_image('wazida_02.jpg')

# pen.draw()

import os
from sketchpy import canvas

image_path = 'E:\VS code\python Projcet\Draw sketch\wazida_01.png'


if not os.path.isfile(image_path):
    print(f"Error: File {image_path} does not exist.")
else:
    
    pen = canvas.sketch_from_image(image_path)
    pen.draw()
