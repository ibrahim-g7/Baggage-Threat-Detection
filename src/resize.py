

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
        f_img = f+"/"+file
        img = Image.open(f_img)
        img = img.resize((448,448))
        img.save(dest+"/"+file)


# %%
resize(hard_test_dir, hard_dir)
# %%
resize(easy_test_dir,easy_dir)

# %%
resize(hidden_test_dir,hidden_dir)

# %%
resize(train_dir,training_dir)
# %%
