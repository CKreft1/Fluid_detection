# Fluid_detection
Used for determining a numerical approximation for the "goodness" of an under-oil microfluidics chip tested with fluorescein dye media.


Really happy with how version 1 turned out. I knew nothing about image processing or computer vision before this project, but it ended up working pretty well. There is a lot of hardcoding present, but so long as the same scope and same mask (and possibly the same image dimensions, but I'm not sure) are used between any two slides that you want to compare, it should work fine. In total, this was a very good second independent coding project, and I'm looking forward to working on it further to add functionalities.
To give an overview of how this code works, the following was my process in writing the code. I started out by splitting the image into its component rgb intensities and thresholding based on the intensity of green. From that I ran a hough circle detection, created a mask onto a blank sheet, inverted the mask, and used boolean to combine the inverted mask with the green threshold to show the remaining pixels that could not be found to be inside a circle (circles being representative of the sections not covered by the mask). Then, I used iteration to count up the number of both thresholded and nonthresholded pixels within the combined image. Finally, I multiplied the dimensions of the image to get area (in number of pixels), and finally I divided number of nonthresholded pixels by area.

The result of all this is a single number between 0 and 1 that is an objective measure of how "good" a treatment method is based on how much fluorescein is present on the PDMS-silane treated area, which should ideally be zero.

I had some issues with writing this. For example, a lot of this is hardcoded, such as the bounds of the hough transformation radius, because otherwise many undesirable circles are detected with large radii. In order for the detection to pick up only on the fluorescein bubbles, I had to hardcode in the radius of the bubbles and exclude all other radii from detection. Because of that, the large center bubble cannot be detected. This isn't an issue so long as you are using the code to compare 2 slides prepared with the same mask, but it still is not ideal.

Also, I would like to mask over the fluorescein deposited at the sides of the mask, because this is not indicative of the treatment quality. This is arguably a bigger deal, because it factors into the final calculation differently depending only on the care with which under oil sweep was performed, not the type of mask.
There are some things I want to improve on. In V2, I would like to add detection for the large bubble at the center of the mask. My idea for how to do this is, so far, find the precise radius in pixels for the center bubble on the image. I would use hough detection to find all the circles in the image with that radius. I have found this invaribly detects both the center bubble and other undesirable circles that are not the center bubble. Then, I would set up a loop using iteration that copies a blank and goes through the list of circles one at a time, comparing to the trhesholded image. Only the center bubble should be entirely composed of thresholded pixels, so another loop could be used to check pixels. I would check if a given pixel is both thresholded and in the mask, and count up the number of pixels for which this is not true. The center bubble should have very few pixels not thresholded but in the mask, so it could be detected like this.

I would also like to use grid detection to make a separate metric that measures the number of bubbles that were expected to be on the slide but were not covered by media, because that is also indicative of how good a treatment is. I'm much less sure how this would be accomplished.

To use this code, just download the image in main and the v1 code to the same folder, and then run the code using either jupyter or visual studio coding environments. VS works better.

To use it with other images aside from the test image, just change the path name in line 5 to whatever image you want to analyze. I'm not sure if python can read non-jpg images, so try to limit it to jpgs.
