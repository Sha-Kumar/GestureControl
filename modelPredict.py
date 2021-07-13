import keras
import numpy as np
from keras.preprocessing import image

# Model
model = keras.models.load_model('SecondMode')
# Mention name of the disease into list.
Classes = ["five","four","one","three","two"]

# Pre-Processing test data same as train data.
img_width=256
img_height=256
# opt = keras.optimizers.Adam(lr=0.001)
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])


def prepare(img):
    img=img.resize((256,256))
    img.save('file.jpg')
    x = image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    x = x/255
    return x
    

def classifier(img) :
    img = img.convert('RGB')
    result = np.argmax(model.predict([prepare(img)]), axis=-1)
    return Classes[int(result)]




# def prepare(img_path):
#     img = image.load_img(img_path, target_size=(256, 256))
#     img=img.resize((256,256))
#     x = image.img_to_array(img)
#     x=np.expand_dims(x,axis=0)
#     x = x/255
#     return x
    
# result = np.argmax(model.predict([prepare('D:\SHASHANK\Tenserflow\GestureControl\Datasets\\test\\five\\1.jpg')]),axis=-1)
# print (Classes[int(result)])
# img = image.load_img('D:\SHASHANK\Tenserflow\GestureControl\Datasets\\train\\one\\1.jpg', target_size=(256, 256))
# img.show()
