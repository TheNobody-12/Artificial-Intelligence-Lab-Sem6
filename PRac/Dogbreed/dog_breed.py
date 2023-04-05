import numpy as np
import streamlit as st
import cv2

from keras.models import load_model

model = load_model('dogbreed.h5')

CLASS_NAMES = ['Scottish Deerhound', 'Maltese Dog', 'Bernese Mountain Dog']

st.title('Dog Breed Prediction')
st.markdown('Upload Dog Image')

dog_image = st.file_uploader('Upload Image')
submit = st.button('Predict')

if submit:
    if dog_image is not None:
        # convert image into opencv image
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        # display the image
        st.image(opencv_image, channels='BGR')
        # resize the image
        opencv_image = cv2.resize(opencv_image, (224, 224))
        # convert image to 4 dimension
        opencv_image.shape = (1, 224, 224, 3)
        # make prediction
        y_pred = model.predict(opencv_image)

        st.title(str("The Dog Breed is " + CLASS_NAMES[np.argmax(y_pred)] + "??"))