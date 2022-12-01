import os, random, json
import meme_generator

generation_amount = int(input("how many memes to generate: "))

source_images_folder = "source_images"
source_text_file = "source_text.json"

def get_random_image_path():
    random_image_path = str(
        source_images_folder
        +"/"+
        random.choice(os.listdir(source_images_folder))
    )
    return(random_image_path)

def get_top_text():
    source_text_data = open(source_text_file)
    source_text = json.load(source_text_data)
    text = random.choice(source_text["top_text"])
    source_text_data.close()
    return(text)

def get_bottom_text():
    source_text_data = open(source_text_file)
    source_text = json.load(source_text_data)
    text = random.choice(source_text["bottom_text"])
    source_text_data.close()
    return(text)

for i in range(generation_amount):
    meme_generator.generate_meme(
        get_random_image_path(),
        get_top_text(),
        get_bottom_text()
    )