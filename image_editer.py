import os
import torchvision.transforms as transforms 
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader 
from torchvision import utils 

data_path = '/home/nvidia/jetson-inference/python/training/classification/data/steak-rating/test'


transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.GaussianBlur(5),
    transforms.Resize(300),
    transforms.ToTensor()

])

dataset = ImageFolder(data_path)

save_path = '/home/nvidia/jetson-inference/python/training/classification/data/images'
os.makedirs(save_path, exist_ok=True)

for i, (image, label) in enumerate(dataset):

    save_subfolder = dataset.classes[label]
    save_folder_path = os.path.join(save_path, save_subfolder)
    os.makedirs(save_folder_path, exist_ok=True)

    for j in range(100):
        augmented_image = transform(image)
        save_filename = f'{save_subfolder}_{i}_{j}.jpg'
        save_filepath = os.path.join(save_folder_path, save_filename)
        utils.save_image(augmented_image, save_filepath)


