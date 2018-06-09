#flag
"""import skimage
import os
from skimage import io
f = io.imread('F:\Gate\P3\demo\demo.png')
for i in range(0, 50):
    for j in range(0, 301): 
        f[i][j] = [255, 153, 0]
for i in range(51, 100):
    for j in range(0,301):
        f[i][j] = [255, 255, 255]
for i in range(101, 150):
    for j in range(0, 301):
        f[i][j] = [0, 255, 0]
io.imshow(f)"""


#indoor(a)
"""import skimage
import os
from skimage import io
from skimage import filters
from skimage import color
indoor = io.imread('F:\Gate\P3\demo\indoor1.jpg')
indoor1 = color.rgb2gray(indoor)
edges = filters.sobel(indoor1)
val = filters.threshold_otsu(indoor1)
thres =  indoor1 > val 
val = filters.threshold_otsu(edges)
tedge = edges > val
tedge.sum()
tedge.sum()/(367.0 * 367)"""


#outdoor(a)
"""import skimage
import os
from skimage import io
from skimage import filters
from skimage import color
outdoor = io.imread('F:\Gate\P3\demo\outdoor.jpg')
outdoor = color.rgb2gray(outdoor)
edges = filters.sobel(outdoor)
val = filters.threshold_otsu(outdoor)
thres =  outdoor > val 
val = filters.threshold_otsu(edges)
tedge = edges > val
tedge.sum()"""


#histogram
"""import skimage
import os
from skimage import io
from skimage.morphology import disk
from skimage import filters
from skimage import color
from skimage.filters.rank import mean
from skimage.filters.rank import median
import matplotlib.pyplot as plt

f = io.imread('F:\Gate\P3\demo\outdoor.jpg')
image = color.rgb2gray(f)
plt.hist(image.ravel(), 500, [0,1])
plt.show()"""


#sharpening
import skimage
import os
from skimage import io
from skimage.morphology import disk
from skimage import filters
from skimage import color
from skimage.filters.rank import mean
from skimage.filters.rank import median
f = io.imread('F:\Gate\P3\demo\outdoor.jpg')
image = color.rgb2gray(f)
fil = median(image, disk(20))
fill = median(image, disk(0.9))
io.imshow(fill)