import os
import random

directory_path = "/media/volume/NeuralHydrology/Test_Quinn_Data/CAMELS_data/time_series"
files = os.listdir(directory_path)

output_dir = "/media/volume/NeuralHydrology/neuralhydrology/nwm-analysis/nwm-data/conus_runs"
train_size = 445
val_size = 125
test_size = 68

sum_size = train_size + val_size + test_size
sample = random.sample(files, sum_size)

train_sample = sample[:train_size]
val_sample = sample[train_size:train_size + val_size]
test_sample = sample[train_size + val_size:]

with open(os.path.join(output_dir, "train0502.txt"), "w") as f:
    for site in train_sample:
        f.write(site.strip('.nc') + "\n")

with open(os.path.join(output_dir, "val0502.txt"), "w") as f:
    for site in val_sample:
        f.write(site.strip('.nc') + "\n")

with open(os.path.join(output_dir, "test0502.txt"), "w") as f:
    for site in test_sample:
        f.write(site.strip('.nc') + "\n")

print("Files have been written to train0502.txt, val0502.txt, and test0502.txt.")
