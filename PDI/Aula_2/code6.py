# Import the module and the rotate and rescale functions
from PDI.src.pdi_utils import show_image,load_rotate_cat

image_cat = load_rotate_cat()
from skimage.transform import rotate, rescale

# Rotate the image 90 degrees clockwise
rotated_cat_image = rotate(image_cat, 90)

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=0.2, anti_aliasing_sigma=0.1)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rescaled_with_aa, 1/4, anti_aliasing=0.2)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")