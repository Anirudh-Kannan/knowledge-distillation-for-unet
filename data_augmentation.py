import torch
import numpy as np
from PIL import Image

def split_squares(img, pos):
    h = img.shape[1]
    if(pos == 0):
        return img[:, :, :h]
    else:
        return img[:, :, -h:]

def normalize(img):
    return img/255

def hwc_to_chw(img):
    return np.transpose(img, (2, 0, 1))

def reduce_channel(img):
    if(img[:, :, 0] == img[:, :, 1] and img[:, :, 1] == img[:, :, 2]):
        return img[:, :, 0]

def load_data(img_path):
    if img_path.find("train") != -1:
        gt_path = img_path.replace("train", "train_mask")
    elif img_path.find("val") != -1:
        gt_path = img_path.replace("val", "val_mask")
    else:
        gt_path = img_path.replace("test", "test_mask")

    img = Image.open(img_path)#.resize((640, 959))
    gt = Image.open(gt_path)#.resize((640, 959))
    return img, gt
    #add data aug functions
    #return img
        
