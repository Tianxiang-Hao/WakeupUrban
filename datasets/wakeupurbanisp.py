import os
import random
from os.path import join
import numpy as np
import torch.multiprocessing
from scipy.io import loadmat
from PIL import Image
from torchvision.transforms.functional import to_pil_image
from torch.utils.data import Dataset

def get_wuisp_labeldata():
    cls_names = ['vegetation','isp']
    colormap = np.array([
            [0,255,0],
            [255,0,0],
            [0, 0, 0]])
    return cls_names, colormap

class wakeupurbanisp(Dataset):
    def __init__(self, transforms, split, root, datafrom = 'image'):
        super(wakeupurbanisp, self).__init__()
        self.split = split
        self.root = root
        self.transform = transforms
        self.datafrom = datafrom
        split_files = {
            # "train": ["labelled_train.txt"],
            "train": ["labelled_train.txt", "labelled_val.txt"],
            # "train": ["unlabelled_train.txt"],
            # "val": ["labelled_val.txt"],
            "val": ["labelled_test.txt"],
            "train+val": ["labelled_train.txt", "labelled_val.txt"],
            "test": ["labelled_test.txt"],
            "all": ["all.txt"]
        }
        assert self.split in split_files.keys()

        self.files = []
        for split_file in split_files[self.split]:
            with open(join(self.root, split_file), "r") as f:
                self.files.extend(fn.rstrip() for fn in f.readlines())

        # self.coarse_labels = True
        # self.fine_to_coarse = {0: 0, 4: 0,  # roads and cars
        #                        1: 1, 5: 1,  # buildings and clutter
        #                        2: 2, 3: 2,  # vegetation and trees
        #                        }

    def __getitem__(self, index):
        image_id = self.files[index]
        img = Image.open(join(self.root, self.datafrom, image_id + ".png"))
        label = Image.open(join(self.root, "mask_gt_ISP", image_id + ".png"))
        base_seg = Image.open(join(self.root.replace('/wakeupurbanisp', ''), "SAMoutput_gts_base", image_id + ".png"))

        img, label,base_seg = self.transform(img, label,base_seg)
        # base_seg = self.transform(base_seg)
        # if self.coarse_labels:
        #     new_label_map = torch.ones_like(label)*255
        #     for fine, coarse in self.fine_to_coarse.items():
        #         new_label_map[label == fine] = coarse
        #     label = new_label_map

        # mask = (label > 0).to(torch.float32)
        return img, label, base_seg, image_id

    def __len__(self):
        return len(self.files)
    
classes = ['vegetation','isp']


