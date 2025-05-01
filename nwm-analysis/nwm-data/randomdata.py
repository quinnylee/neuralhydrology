import os
import random

# directory_path = "/media/volume/NeuralHydrology/Test_Quinn_Data/forty_year_test_data/time_series"
files = []

with open("/media/volume/NeuralHydrology/Test_Quinn_Data/good_al_sites.txt", "r") as good_files:
    files = good_files.read().split('\n')

output_dir = "/media/volume/NeuralHydrology/neuralhydrology/nwm-analysis/nwm-data/al_runs"
train_size = 650
val_size = 150
test_size = 100

sum_size = train_size + val_size + test_size
sample = random.sample(files, sum_size)

train_sample = sample[:train_size]
val_sample = sample[train_size:train_size + val_size]
test_sample = sample[train_size + val_size:]

with open(os.path.join(output_dir, "train0430.txt"), "w") as f:
    for site in train_sample:
        f.write(site.strip('.nc') + "\n")

with open(os.path.join(output_dir, "val0430.txt"), "w") as f:
    for site in val_sample:
        f.write(site.strip('.nc') + "\n")

with open(os.path.join(output_dir, "test0430.txt"), "w") as f:
    for site in test_sample:
        f.write(site.strip('.nc') + "\n")

print("Files have been written to train0430.txt, val0430.txt, and test0430.txt.")
