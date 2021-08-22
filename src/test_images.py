from Bia import *
import random
import json
import numpy as np
from PIL import Image

f = open("database/images.json","r")
database = json.loads(f.read())
database = list(database.values())[0]
f.close()


size = database["size"]

images_json = database["images"]

data = np.array(images_json[0]["image"])


# print("cururu")
print(data)
img = Image.fromarray(data.astype("uint8"), mode='RGB')
img.show()

