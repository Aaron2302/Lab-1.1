#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#9/13/18
#Traverse a directory and classify images within the directory as either a cat or a dog and place their file paths into seperate lists
import os
import random

def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2
    else:
        return random.random() / 2


def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    if len(file_list) > 0:                                      #Classifies images in the current directory if there are any and adds their file path to the list
        for file in range(len(file_list)):
            if classify_pic(file_list[file]) >= 0.5:
                dog_list.append(path +'/' + file_list[file])
            else:
                cat_list.append(path + '/' + file_list[file])


    if len(dir_list) > 0:                                       #Checks any directories within the current directory and adds the resulting lists to the current lists
        for directory in range(len(dir_list)):
            cat_list2, dog_list2 = process_dir(path + '/' + dir_list[directory])
            cat_list += cat_list2
            dog_list += dog_list2

    return cat_list, dog_list

def main():
    start_path = './' # current directory

    cat_list , dog_list = process_dir(start_path)
    print("Cat List")
    print_list(cat_list)
    print("Dog List")
    print_list(dog_list)


def print_list(list):
    for item in range(len(list)):
        print(list[item])
    print()

main()
