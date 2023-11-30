# flask_api_test
javascript⇒flaskAPI  
  
■仕様について  
index_v3.htmlをブラウザで開く  
画像をアップロードし、AI判定ボタンを押すと、判定画像（BBOX付）が返ってくる  
  
■APIについて  
PythonAPIの代表としてFlask,Djangoの両方で実装できるように記載  
  
■モデルのダウンロード方法  
mkdir flask_api
cd flask_api
python3 -m venv 

.venv/bin/activate.ps1  

pip install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html Previous versions of PyTorch  

pip install torch torchvision torchaudio

import torch  
import torchvision  
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)  
torch.save(model, "model.pt")  
ls  
  
■DjangoのAPIフォルダについて  
AIようには作られていないので、カスタマイズしてください  
画像をアップロードし、画像名を変えて返すだけのAPIになっています。

