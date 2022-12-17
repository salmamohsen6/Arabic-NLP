from flask import Flask,render_template,request
import tensorflow as tf
import numpy as np
import os


def preprocess_single_input(input):
    arabic_letters = ['ئ', 'ا', 'ب', 'ت', 'ة', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
                      'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'ى', 'ء', 'آ', 'أ', 'ؤ', 'إ', 'ؤ']
    char_to_idx_map = {char: (idx + 1) for idx, char in enumerate(arabic_letters)}

    def text_to_vect(input, char_to_idx_map):
        name_idx_representation = []
        for t in input:
            t
            if t in char_to_idx_map:
                name_idx_representation.append(char_to_idx_map[t])
            else:
                name_idx_representation.append(0)
            print(name_idx_representation)
            #print(1)
        return np.array(name_idx_representation)

    def pading_AND_OHE(input):
        m = 100
        padded = np.pad(input, (0, m - len(input)), 'constant')
        b = np.zeros((m, 38))
        b[np.arange(m), padded] = 1
        return b

    preprocessed_input1 = text_to_vect(input, char_to_idx_map)
    preprocessed_input= pading_AND_OHE(preprocessed_input1)
    return np.expand_dims(preprocessed_input, axis=0)

def load_saved_model():
    model = tf.keras.Sequential()
    # conv block 1
    model.add(tf.keras.layers.Conv1D(256, 7, input_shape=(100, 38), padding='valid'))
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.MaxPool1D(3))

    # conv block 2
    model.add(tf.keras.layers.Conv1D(256, 7, padding='valid'))
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.MaxPool1D(3))

    # conv block 3
    model.add(tf.keras.layers.Conv1D(256, 7, padding='valid'))
    model.add(tf.keras.layers.ReLU())

    # conv block 4
    model.add(tf.keras.layers.Conv1D(256, 7, padding='same'))
    model.add(tf.keras.layers.ReLU())

    # conv block 5
    model.add(tf.keras.layers.Conv1D(256, 7, padding='same'))
    model.add(tf.keras.layers.ReLU())

    # conv block 6
    model.add(tf.keras.layers.Conv1D(256, 7, padding='same'))
    model.add(tf.keras.layers.ReLU())

    # dense layers
    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(1024, activation=None))
    model.add(tf.keras.layers.ReLU())
    model.add(tf.keras.layers.Dropout(0.5))

    model.add(tf.keras.layers.Dense(100, activation='relu', kernel_initializer='he_uniform'))

    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    
    #loading model wights
    dir_pth= os.path.dirname(os.path.realpath('__file__'))
    model_pth='model_weights.h5'
    abs_file_path = os.path.join(dir_pth, model_pth)
    
    model.load_weights(abs_file_path)
    
    
    return model

def make_predicts(data):
    model=load_saved_model()
    data_after = preprocess_single_input(data)
    output=model.predict(data_after)
    #print(data_after)
    #print(output)
    return output[0][0]


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        name = request.form['message']
        
        my_prediction = make_predicts(name).item()
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)
