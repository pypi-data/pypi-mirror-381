import cv2
from os import listdir, mkdir
from os.path import isdir, join, isfile
import os

# input_folder = '/home/wenshan/projects/MyPaper/TartanAirV2/v2_teaser_1'
# output_folder = '/home/wenshan/workspace/tartanairpy/docs/images/env_snapshot'

# images = listdir(input_folder)
# images = [ff for ff in images if ff.endswith('.png')]

# images.sort()

# for image in images:
#     img_path = input_folder + '/' + image
#     img = cv2.imread(img_path)
#     if img is None:
#         print(f"Failed to read image {img_path}")
#         continue
    
#     # Resize the image to 512x512
#     img_resized = cv2.resize(img, (100, 100))
    
#     envname = image.split('_')[0]  # Assuming the environment name is the first part of the filename
#     # Save the resized image
#     output_path = output_folder + '/' + envname + '.png'
#     cv2.imwrite(output_path, img_resized)
#     print(f"Saved resized image to {output_path}")

from os.path import isfile, join

input_folder = '/media/datasets/TartanAir/tartanair_v2/'
output_folder = '/home/wenshan/workspace/tartanairpy/segfiles'

envs = listdir(input_folder)
for env in envs:
    print(f"Processing environment: {env}")
    env_path = input_folder + env
    seg_file = env_path + '/analyze/seg.yaml'
    if not isfile(seg_file):
        print(f"Segment file not found for {env}, skipping.")
        continue

    out_env_path = join(output_folder, env)
    if not isdir(out_env_path):
        print(f"  Creating output directory: {out_env_path}")
        mkdir(out_env_path)
    cmd = "cp " + seg_file + " " + out_env_path
    print(f"  Executing command: {cmd}")
    os.system(cmd)

    seg_file2 = env_path + '/seg_label.json'
    cmd = "cp " + seg_file2 + " " + out_env_path
    os.system(cmd)

    seg_file3 = env_path + '/seg_label_map.json'
    cmd = "cp " + seg_file3 + " " + out_env_path
    print(f"  Executing command: {cmd}")
    os.system(cmd)
