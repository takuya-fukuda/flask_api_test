from flask import Blueprint, jsonify, request

import os
from pathlib import Path

from . import calculation

api = Blueprint("api", __name__)

# アップロードされたファイルを保存するディレクトリを設定(追加項目)
basedir = Path(__file__).parent.parent
UPLOAD_FOLDER = str(basedir / "data" / "original")

# ファイルの拡張子を制限（追加項目）
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ファイルの拡張子をチェックするヘルパー関数（追加項目）
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.get("/")
def index():
    return jsonify({"column": "value"}), 201

#下記は追加でおこなったもの。画像をサーバ上にUPLOADする処理
@api.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'ファイルが選択されていません'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'ファイル名が空です'}), 400

    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        #file_path = UPLOAD_FOLDER
        file.save(file_path)
        if os.path.exists(file_path):
            print(f'ファイルが保存されました: {file_path}')
            #return jsonify({'message': 'アップロード成功'}), 200
            return calculation.detection(request)
        else:
            print(f'ファイルの保存に失敗しました: {file_path}')
            return jsonify({'message': 'ファイル保存に失敗しました'}), 500
        #return jsonify({'message': 'アップロード成功'}), 200
    else:
        return jsonify({'message': '許可されていないファイル形式です'}), 400


@api.post("/detect")
def detection():
    return calculation.detection(request)
