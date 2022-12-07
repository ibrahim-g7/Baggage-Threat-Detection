

#%%
import PIL
import os
import os.path
from PIL import Image

#%% 
train_dir = '../pidray/train'
easy_test_dir = '../pidray/easy'
hard_test_dir = '../pidray/hard'
hidden_test_dir = '../pidray/hidden'

# %%
training_dir = '../data/train'
easy_dir = '../data/easy'
hard_dir = '../data/hard'
hidden_dir = '../data/hidden'


# %%

def resize(f, dest):
    for file in os.listdir(f):
        f_img = dest+"/"+file
        img = Image.open(f_img)
        img = img.resize((2296,1724))
        img.save(f_img)


# %%
resize(hard_test_dir, hard_dir)