import time
import math
import random

cell_chr = '█'

class progressbar:
	def __init__(self, min=0, max=100, bar_size=50):
		self._min = min
		self._max = max
		self._bar_size = bar_size
		self._value_width = len(str(max))

	def print_progress(self, progress):
		portion_done = (progress - self._min) / (self._max - self._min)
		num_cells = math.floor(portion_done * self._bar_size)
		progress_str = (cell_chr * num_cells).ljust(self._bar_size)

		print(f'\r{self._min}|{progress_str}|{self._max}:{int(progress):{self._value_width}d}', end='')


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











