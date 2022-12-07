#%% 
import json
import os

def id_to_label(id):
    if id == 1:
        return "Baton"
    elif id == 2:
        return "Pliers"
    elif id == 3:
        return "Hammer"
    elif id == 4:
        return "Powerbank"
    elif id == 5:
        return "Scissors"
    elif id == 6:
        return "Wrench"
    elif id == 7:
        return "Gun"
    elif id == 8:
        return "Bullet"
    elif id == 9:
        return "Sprayer"
    elif id == 10:
        return "HandCuffs"
    elif id == 11:
        return "Knife"
    elif id == 12:
        return "Lighter"


classes = ['Baton',
 'Pliers',  
 'Hammer',
 'Powerbank',
 'Scissors',
 'Wrench',
 'Gun',
 'Bullet',
 'Sprayer',
 'HandCuffs',
 'Knife',
 'Lighter']

def convert(size,box):
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    return (x,y,w,h)

def convert_annotation(json_dir,destination_dir):
    with open(json_dir,'r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']      
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open(destination_dir+"%s.txt"%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = list(filter(lambda item3: item3['id'] == category_id,data['categories']))
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()

#%% 
convert_annotation('../pidray/annotations/xray_test_hard.json', '../pidray/anno_yolo/hard/')
#%% 
convert_annotation('../pidray/annotations/xray_test_easy.json', '../pidray/anno_yolo/easy/')
#%%
convert_annotation('../pidray/annotations/xray_train.json', '../pidray/anno_yolo/train/')
convert_annotation('../pidray/annotations/xray_test_hidden.json', '../pidray/anno_yolo/hidden/')

