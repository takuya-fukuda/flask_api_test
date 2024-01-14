from stegano import lsb
import sys

class Sutegano():
    def detect_malware_in_image(image_path):
        try:
            # 隠されたデータを抽出
            hidden_data = lsb.reveal(image_path)

            if hidden_data is not None:
                print("マルウェアの可能性があります。処理を中断します。")
                return 0  # 処理を中断
            else:
                print("隠されたデータはありません。")
                return 1

        except IndexError:
            # 隠されたデータが抽出できなければ、マルウェアはないとみなす。
            print("隠されたデータの検出が不可能です。")
            return 1
        except Exception as e:
            print("管理者に問い合わせ")
            return 2

# 画像ファイルのパス
#image_path = 'test.jpg'
#Sutegano.detect_malware_in_image(image_path)
