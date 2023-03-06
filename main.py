import base64
import json

from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


'''Converts the book.json to something easier to use and write a new file sample.json'''

with open('raw/book.json') as json_file:
    data = json.load(json_file)

    pages = data['log']['entries']

    bookcontenctList = []

    for page in pages:
        try:
            fileName = page['response']['headers'][5]
            fileContent = page['response']['content']
        except:
            continue

        dictionary = {
            "fileName": fileName,
            "content": fileContent,
        }

        bookcontenctList.append(dictionary)

    # Serializing json
    json_object = json.dumps(bookcontenctList, indent=4)

    # Writing to sample.json
    with open("raw/sample.json", "w") as outfile:
        outfile.write(json_object)


'''Remove all the unnecessary stuff from the sample.json and write to sample2.json'''

with open('raw/sample.json') as json_file:
    data = json.load(json_file)

    bookcontenctList = []

    for page in data:
        if page['content']['mimeType'] != 'image/jpeg':
            continue
        bookcontenctList.append(page)

    # Serializing json
    json_object = json.dumps(bookcontenctList, indent=4)

    # Writing to sample.json
    with open("raw/sample2.json", "w") as outfile:
        outfile.write(json_object)


'''Converts all base64 to images (.png)'''


with open('raw/sample2.json') as json_file:
    data = json.load(json_file)
    count = 0
    for page in data:

        png_recovered = base64.b64decode(page['content']['text'])
        imageName = 'pageImages/' + page['fileName']['value'][-8:]
        with open(imageName, 'wb') as f:
            f.write(png_recovered)
        print("Page ", count, " of ", len(data))
        count = count + 1


'''Writes all pngs to PDF'''

images = [
    Image.open("pageImages/" + f.name)
    for f in os.scandir("pageImages/")
]

pdf_path = "book/deep.pdf"

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
