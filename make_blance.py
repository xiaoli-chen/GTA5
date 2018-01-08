import sys
import os
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
from getkeys import key_map

#pthon make_blance 1 46 "bal"
def main(start_idx, end_idx, save_to):
    current_idx = 1
    data_to_save = []

    for i in range(start_idx, end_idx+1):
        file_name = 'data/training_data-{idx}.npy'.format(idx=i)
        if os.path.isfile(file_name):
            b_data = balance_data(file_name)
            data_to_save = data_to_save + b_data

            if len(data_to_save) >= 500:
                new_file = '{save}/training_data-{idx}.npy'.format(save=save_to, idx=current_idx)
                np.save(new_file, data_to_save)
                print('SAVED', new_file)
                data_to_save = []
                current_idx += 1
        else:
            print('File does not exist!', file_name)

    if len(data_to_save) > 0:
        new_file = '{save}/training_data-{idx}.npy'.format(save=save_to, idx=current_idx)
        np.save(new_file, data_to_save)


def balance_data(file_path):
    print("starting to balance file:",file_path)
    train_data = np.load(file_path)
    df = pd.DataFrame(train_data)

    new_data = {}
    for key in key_map.keys():
        new_data[key] = []

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        for key,value in key_map.items():     
            if choice == value:
                print('find',key,value,choice)                   
                new_data[key].append([img,choice])

    cnt_forward_left= len(new_data['WA'])
    cnt_forward_right = len(new_data['WD'])
    max_len = max(cnt_forward_left,cnt_forward_right)
    forwards = new_data['W'][:max_len]
    lefts = new_data['A'][:len(forwards)]
    rights = new_data['D'][:len(forwards)]
    empties = new_data['default'][:len(forwards)]
    default = new_data['NK'][:len(forwards)]

    final_data = forwards + lefts + rights +empties + default + new_data['WA'] + new_data['WD'] + new_data['SA'] + new_data['SD']

    shuffle(final_data)

    return final_data

if __name__ == '__main__':
   start = sys.argv[1]
   end = sys.argv[2]
   path_to_save = sys.argv[3]
   print(start,end,path_to_save)
   main(int(start),int(end),path_to_save)     