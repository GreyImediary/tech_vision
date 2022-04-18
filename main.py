from skimage import img_as_float
from skimage.io import imread
from skimage.metrics import structural_similarity as structural_similarity
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio


def calculate_quality_data(image, noise_image, title_text):
    image_float = img_as_float(imread(image))
    noise_float = img_as_float(imread(noise_image))

    mse = mean_squared_error(image_float, noise_float)
    psnr = peak_signal_noise_ratio(image_float, noise_float)
    ssim = structural_similarity(image_float, noise_float, channel_axis=2)

    print(title_text)
    print(f"MSE = {mse}")
    print(f"PSNR = {psnr}")
    print(f"SSIM = {ssim}")
    print("---------------------------------\n")

# First low detailed image

calculate_quality_data('imgs/low_det/low_first.jpg',
                       'imgs/low_det/low_det_with_noise/low_first_noise.jpg',
                       "First low detailed image:"
                       )

# Second low detailed image

calculate_quality_data('imgs/low_det/low_second.jpg',
                       'imgs/low_det/low_det_with_noise/low_second_noise.jpg',
                       "Second low detailed image:"
                       )

# Third low detailed image

calculate_quality_data('imgs/low_det/low_third.jpg',
                       'imgs/low_det/low_det_with_noise/low_third_noise.jpg',
                       "Third low detailed image:"
                       )

# --------------------------------------------------------

# First middle detailed image

calculate_quality_data('imgs/mid_det/mid_first.jpg',
                       'imgs/mid_det/mid_det_with_noise/mid_first_noise.jpg',
                       "First mid detailed image:"
                       )
# Second middle detailed image

calculate_quality_data('imgs/mid_det/mid_second.jpg',
                       'imgs/mid_det/mid_det_with_noise/mid_second_noise.jpg',
                       "Second mid detailed image:"
                       )

# Third low detailed image

calculate_quality_data('imgs/mid_det/mid_third.jpg',
                       'imgs/mid_det/mid_det_with_noise/mid_third_noise.jpg',
                       "Third mid detailed image:"
                       )

# --------------------------------------------------------

# First high detailed image

calculate_quality_data('imgs/high_det/high_first.jpg',
                       'imgs/high_det/high_det_with_noise/high_first_noise.jpg',
                       "First high detailed image:"
                       )

# Third high detailed image

calculate_quality_data('imgs/high_det/high_second.jpg',
                       'imgs/high_det/high_det_with_noise/high_second_noise.jpg',
                       "Second high detailed image:"
                       )

# Third high detailed image

calculate_quality_data('imgs/high_det/high_third.jpg',
                       'imgs/high_det/high_det_with_noise/high_third_noise.jpg',
                       "Third high detailed image:"
                       )
