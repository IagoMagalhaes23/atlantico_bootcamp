# Import the required module
import matplotlib.pyplot as plt
from PDI.src.pdi_utils import show_image, load_chest_ray_x
from skimage.filters.rank import equalize

chest_xray_image = load_chest_ray_x()
# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq =  plt.hist(chest_xray_image)
xray_image_eq = equalize(xray_image_eq)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')