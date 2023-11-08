import os
import csv


def get_absolute_paths(num_mark: int, folder_name: str) -> list[str]:
    """
    The function gets absolute paths to files and returns an array with them
    """
    absolute_path = os.path.abspath(f'{folder_name}')
    class_path = os.path.join(absolute_path, str(num_mark))
    names = os.listdir(class_path)
    absolute_paths = []
    for name in names:
        absolute_paths.append(os.path.join(class_path, name))
    return absolute_paths


def get_relative_paths(num_mark: int, folder_name: str) -> list[str]:
    """
    The function gets relative paths to files and returns an array with them
    """
    relative_path = os.path.relpath(f'{folder_name}')
    class_path = os.path.join(relative_path, str(num_mark))
    names = os.listdir(class_path)
    relative_paths = []
    for name in names:
        relative_paths.append(os.path.join(class_path, name))
    return relative_paths


def make_csv(folder_name: str) -> None:
    """
    The function writes data to a csv file in the following format: absolute path, relative path, class label
    """
    f = open("paths.csv", 'w')
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    for i in range(1, 6):
        absolute_paths = get_absolute_paths(i, f'{folder_name}')
        relative_paths = get_relative_paths(i, f'{folder_name}')
        for absolute_path, relative_path in zip(absolute_paths, relative_paths):
            writer.writerow([absolute_path, relative_path, str(i)])
