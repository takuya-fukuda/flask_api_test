from flask import Blueprint, jsonify, request

import os
from pathlib import Path

from . import calculation
from .sutegano import Sutegano

api = Blueprint("api", __name__)

#特定のWebサイトからのみＡＰＩ実行可能にする
allowed_referer = "file:///C:/Users/taku/flaskbook_api/test.html"

#APIキーを持ったサイトからのアクセスに限定する
api_key = "password"

# アップロードされたファイルを保存するディレクトリを設定(追加項目)
basedir = Path(__file__).parent.parent
UPLOAD_FOLDER = str(basedir / "data" / "original")

# ファイルの拡張子を制限（追加項目）
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}

# ファイルの拡張子をチェックするヘルパー関数（追加項目）
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@api.get("/")
#APIkeyを用いたテストにより変更します
#@api.route("/", methods=['POST'])
@api.post("/")
def index():
    # リクエストヘッダーからAPIキーを取得
    provided_api_key = request.headers.get('X-API-Key')
    # APIキーチェック
    if provided_api_key and provided_api_key == api_key:
        print("success")
        return jsonify({"column": "testAPI"}), 201
    else:
        # 不正なAPIキーの場合はアクセスを拒否
        print("failed")
        return jsonify({'error': 'Unauthorized'}), 401

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

        #ステガノグラフィ対策
        st = Sutegano()
        chk = Sutegano.detect_malware_in_image(file_path)
        
        if chk == 0:
            print(chk)
            return jsonify({'message': '画像ファイルにマルウェア感染の可能性を検出しました'}), 500

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
