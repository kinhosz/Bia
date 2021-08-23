from Bia import *
import random
import json
import numpy as np
from PIL import Image
import string

f = open("database/images.json","r")
database = json.loads(f.read())
database = list(database.values())[-1]
f.close()


size = database["size"]

images_json = database["images"]

for item in np.array(images_json):
    data = np.array(item["image"])
    img = Image.fromarray(data.astype("uint8"), mode='RGB')
    img.save("bank/{}.jpg".format(item["label"]))


