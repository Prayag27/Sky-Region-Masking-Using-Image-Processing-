# Sky-Region-Masking-Using-Image-Processing-

Description:

Sky region masking by detecting Horizon Line in an Image using Image Processing.

1. Image Selection: Select an Image which has a clear distinction between land and sky region.
Preferably, choose one in which the horizon line spans the entire width of the image. Load the image from the memory, it is saved as img1.jpg.

2. Convert to Grayscale: An image is made up of multiple pixels. Each pixel contains RGB information. For our purpose, we don't need this information. Therefore, less information
needs to be processed in grayscale. Write this image in the memory. In this example it is saved as img2.png

3. Detect Contour Lines: We use Sobel operator to detect the contour lines. 
We do this for both the axes. There will be two images, each for x and y-axes namely x.png and y.png.
To get an understanding of how Sobel Operator works, refer to this video:
https://www.youtube.com/watch?v=uihBwtPIBxM

4. Superimpose these images: We superimpose both these images to get the final image with all the edges highlighted. This is saved as Sobel_final.png

5. Thresholding: This is the last step. We separate the light and darker regions via thresholding. The sky region is masked in white.

