# Import the required module
from skimage.filters import rank
from PDI.src.pdi_utils import show_image,  load_aerial_image
image_aerial = load_aerial_image()

# Use histogram equalization to improve the contrast
image_eq =  rank.equalize(image_aerial)

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')