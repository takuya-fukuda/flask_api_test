from flask import Blueprint, jsonify, request

from pathlib import Path
import PIL

basedir = Path(__file__).parent.parent

'''
本来の関数
def load_image(request, reshaped_size=(256, 256)):
    """画像の読み込み"""
    #filename = request.json["filename"]
    dir_image = str(basedir / "data" / "original" /filename)
    image_obj = PIL.Image.open(dir_image).convert('RGB')
    image = image_obj.resize(reshaped_size)
    return image, filename
'''

def load_image(request, reshaped_size=(256, 256)):
    """画像の読み込み"""
    #filename = request.json["filename"]
    file = request.files['file']
    filename = file.filename
    dir_image = str(basedir / "data" / "original" /filename)
    image_obj = PIL.Image.open(dir_image).convert('RGB')
    image = image_obj.resize(reshaped_size)
    return image, filename
