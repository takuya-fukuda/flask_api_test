from django.shortcuts import render

# Create your views here.
# imageapp/views.py

import os
import shutil
from django.http import HttpResponseBadRequest, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        print(image)
        input_folder = os.path.join(settings.STATIC_ROOT, 'input')
        output_folder = os.path.join(settings.STATIC_ROOT, 'output')
        
        # アップロードされた画像をinputフォルダに保存
        #with open(os.path.join(input_folder, image.name), 'wb') as destination:
        file_path = os.path.join(input_folder, image.name)
        with open(file_path, 'wb') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        # 画像の名前を変更しoutputフォルダに保存
        new_image_name = 'new_' + image.name
        shutil.move(os.path.join(input_folder, image.name), os.path.join(output_folder, new_image_name))
        
        # outputフォルダ内の画像をレスポンスとして返す
        with open(os.path.join(output_folder, new_image_name), 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/jpg')  # 画像のMIMEタイプを設定
        print(response)
        return response
    
    return HttpResponseBadRequest("Invalid request")
