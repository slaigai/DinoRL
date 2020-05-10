import cv2
import time
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('game.png', cv2.IMREAD_GRAYSCALE)
col_sum_white = np.sum(img >= 255//2, axis=0)
col = [i for i in range(col_sum_white.shape[0])]
print(img)

fig, ax1 = plt.subplots()
img_ax = ax1.imshow(img, cmap='gray')

print(ax1.get_yscale())
ax1.autoscaley_on = False

white_count_ax = ax1.twinx()
white_count_ax.plot(col, col_sum_white)

print(white_count_ax.get_yaxis().get_scale())

# plt.show(block=False)
plt.show()


# cv2.imshow('game', img)
# while "Showing image":
#     if cv2.waitKey(25) & 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#         break

plt.close('all')