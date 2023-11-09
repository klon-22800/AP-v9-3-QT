import os
import csv

from typing import Optional


class Iterator:
    def __init__(self, folder_path: str,  num_class: str) -> None:
        """constructor of Iterator

        Args:
            folder_path (str): path to source directory
            num_class (_type_): class label
        """
        self.counter = 0
        self.num_class = num_class
        self.path = os.path.join(folder_path, self.num_class)
        self.data = os.listdir(self.path)
        self.limit = len(self.data)

    def __next__(self) -> Optional[str]:
        """The function returns the next element path by class label

        Raises:
            StopIteration: exeption, when iteration is end

        Returns:
            Optional[str]: path to file
        """
        if self.counter < self.limit:
            path = os.path.join(self.path, self.data[self.counter])
            self.counter += 1
            return path
        else:
            raise StopIteration


def main() -> None:
    class_5 = Iterator("5")

    for i in range(1002):
        print(next(class_5))


if __name__ == '__main__':
    main()
