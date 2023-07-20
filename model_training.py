
!git clone https://github.com/dusty-nv/pytorch-classification.git; ls


!cd pytorch-classification; pip install -r requirements.txt

#connect your project to your google drive
from google.colab import drive
drive.mount('/content/drive')

#import the cat_dog project for refrence
!cd pytorch-classification/data; wget https://nvidia.box.com/shared/static/o577zd8yp3lmxf5zhm38svrbrv45am3y.gz -O cat_dog.tar.gz; tar xzf cat_dog.tar.gz

#remove any .ipynb checkpoints that cause errors
!rmdir /content/pytorch-classification/data/.ipynb_checkpoints

!cd pytorch-classification; python3 train.py -b 20 --model-dir=models/steak-rating data/steak-rating

!pip install onnx

#use onnx to export the model
!cd pytorch-classification/; python3 onnx_export.py --model-dir=models/steak-rating