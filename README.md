# Architecture

I used CNN after converting the text into character-wise embeddings, it's a very good architecture for misspellings, You don't need to apply any text preprocessing, and very powerful
code:

https://www.kaggle.com/code/salmamohsen/names

I used 6 convolution layers:

Layer|output Feature|Kernel|Pool|


|1|256|7|3|

|2|256|7|3|

|3|256|7|N/A|

|4|256|7|N/A|

|5|256|7|N/A|

|6|256|7|N/A|

and 3 fully connected layers:

|Layer|Output Units|

|7|1024|

|8|100|

|9|1|

# Results
loss: 0.0107 - Accuracy: 0.9969 on the training dataset

loss: 0.5383 - Accuracy: 0.9337 on test dataset

# dependencies
NumPy

pandas

sklearn (to split dataset)

Tensorflow 

flask

# the app 
to run the app 
```bash
python app.py
```
should open it in the browser 
## Docker
to build docker image to need to open shell in the workink dir
use the command

```bash
docker build -t nlpapp .
```
it will bulid an image containing all depadancies under name nlpapp , then run this image to make container
