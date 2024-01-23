import os


# Enter the file path and name of the file you want to change
file_path = "../images/train_svm/07495321/"
train_dir = os.listdir(file_path)
count = 0

for person in train_dir:
    # Enter the new name you want to give the file
    old_file_name = os.path.join(file_path, f"Wilson Eduardo_{count}.jpg")
    new_file_name = os.path.join(file_path, f"Wilson_Eduardo_{count}.jpg")
    # # Use the os.rename() method to change the file name
    os.rename(old_file_name, new_file_name)
    count += 1
print("File names have been changed successfully!")