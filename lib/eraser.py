import os
import glob

class Eraser:
    def __init__(self):
        files = glob.glob('/output/*.wav')
        # for f in files:
        # self.path = os.path.join('../output/', '*.wav')
        self.path = glob.glob('/output/*.wav')
    
    def execute(self):
        os.remove(self.path)

    def print_path(self):
        print(self.path)