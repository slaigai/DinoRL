import time
import math
import random

cell_chr = '█'


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


class bcolors:
    WHITE = '\033[915m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class progressbar:
    def __init__(self, min=0, max=100, bar_size=50):
        self._min = min
        self._max = max
        self._bar_size = bar_size
        self._value_width = len(str(max))

    def print_progress(self, progress):
        portion_done = (progress - self._min) / (self._max - self._min)
        portion_done = clamp(portion_done, 0, 1)
        num_cells = math.floor(portion_done * self._bar_size)
        progress_str = (cell_chr * num_cells).ljust(self._bar_size)
        if portion_done == 1:
            color = bcolors.OKGREEN
        elif portion_done >= 0.25:
            color = bcolors.WHITE
        else:
            color = bcolors.FAIL

        print(color + f'\r{self._min}|{progress_str}|{self._max}:{int(progress):{self._value_width}d}' +
              bcolors.ENDC,
              end='')


if __name__ == '__main__':
    sleep_interval = 0.1

    max_fps = 1000
    min_fps = 0
    bar_size = 10
    pb = progressbar(min=min_fps, max=max_fps, bar_size=bar_size)

    while True:
        time.sleep(sleep_interval)
        fps = random.randint(0, max_fps)

        pb.print_progress(fps)











