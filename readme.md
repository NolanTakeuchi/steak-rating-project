# Project Name
Steak Rating Project


Add short description of project here > 
This program takes in an image of a steak and tells the user how that steak is cooked. The 6 options are raw, rare, medium-rare, medium, medium-well, and well-done. The image will fal into one of the 6 categories


![This is an image of a steak cooked well-done and the program classified the image as well-done with high accuracy(!([https://github.com/NolanTakeuchi/steak-rating-project/assets/139922542/88b964f6-6be4-4b6e-bb9c-3be9bf995228](https://imgur.com/v7ka28o))
)


## The Algorithm
Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 

After entering an image into the files and changing to the correct directory so the code knows where the image is and where to put it after the program runs. The code will output the image into the desired file with the predictionof how the steak is cooked.


## Running this project
1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

imagenet.py --model=(path to resnet18.onnx file)resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=(path to labels.txt file)labels.txt  (path to desired image)  (path to location where you want your image)

To run the project enter this code into the terminal.  The first section called imagenet.py should be the path that leads to your model which is the trained ai. The next section called labels should lead to your labels.txt file which contains the names of all of the possible categories. The next section is the image you want to test and the final section is where you want the final image to go. 




[View a video explanation here]
()
