# Steak Rating Project


This program takes in an image of a steak and tells the user how that steak is cooked. The 6 options are raw, rare, medium-rare, medium, medium-well, and well-done. The image will fall into one of the 6 categories


This is an image of a steak cooked well-done and the program classified the image as well-done with high accuracy(([https://github.com/NolanTakeuchi/steak-rating-project/assets/139922542/88b964f6-6be4-4b6e-bb9c-3be9bf995228](https://imgur.com/v7ka28o))


## The Algorithm

I decided to use imagenet and got 10-13 images from the internet of steaks and different ways they could be cooked.  I then used a program I coded in vscode to multiply those images a hundred times with each copy being a little different with rotations and blur applied to each one. This program used pytorch comands and the jetsen-nano to edit the pictures. I moved the images into google colab and used the code that was created for the cat_dog project and edited it to run for my code. I used it to train my model then exported the model back to vscode. In vscode you can test images to tell how the steak is cooked by inputing code into the jetson nano terminal.

After entering an image into the files and changing to the correct directory so the code knows where the image is and where to put it after the program runs. The code will output the image into the desired file with the prediction of how the steak is cooked. The image is compared to the trained model in order to tell how the steak is cooked

cat_dog project outline:

https://colab.research.google.com/gist/Charlotteec/d625a314ed1ea177e632c210e06c8b28/train_model_backup.ipynb

## Running this project

imagenet.py --model=(path to resnet18.onnx file)resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=(path to labels.txt file)labels.txt  (path to desired image)  (path to location where you want your image output)

To run the project enter this code into the jetsen nano terminal.  The first section called imagenet.py should be the path that leads to your model which is the trained ai. The next section called labels should lead to your labels.txt file which contains the names of all of the possible categories. The next section is the image you want to test and the final section is where you want the final image to go. 



View a video explanation here:

(https://youtu.be/XiGrIgH5exw)
