# Image-Processing

 <b>Lab -1 </b>

Questions

1. Read an image into a variable 
2. Display that image
3. Convert the image into a grayscale image
4. Check the height and width of that image
5. Extract the RGB channels of a given colour image
6. To extract given 100 pixels from a grayscale image
7. Create a new image with every 10th pixel horizontally and 20th pixel vertically.
8. Flip the image vertically
9. Draw the histogram plot of pixel values.

<hr>

<b>Lab -2 </b>

Questions

1. Perform translation, scaling and rotation on an image
2. In a coloured image perform affine transformation
3. In a coloured image extract all R,B and G Perform smoothing (moving avg) on a given image. 
In one case pad rows and columns.
In 2nd case dont allow any extra rows or columns, i.e. do padding in such a way
4. Perform gaussian and compare w moving avg by extracting a small patch
5. Perform median filter on an image
6. If we increase the dimension of a filter, how will it impact the output image?

<hr>

<b> Lab - 3 </b>

Questions

1. Apply the prewitt and sobel filters on random image (that have fews edges), and compare the result with original image. <br>
2. Increase the weight at positions [x,y+1], [x+1,y], [x-1,y], [x, y-1] in 3*3 sobel filter, and infer how it will impact the edge image concerning the benchmark sobel. <br>
3. Apply the LOG filter on the same image that you have taken in Q2, and compare the edge results with output of Q2.<br>


<hr>

<b> Lab -4 </b>

Questions

1. Take a patch of size 5*5 with random intensity values. Apply the x-kernel [-1,0,1] and y-kernel [-1,0,1]^T to get the first order gradient in both the dimensions.<br>
2. Compute the Harris matrix from these computed gradients. <br>
3. Compute the Eigen values and the Eigen vectors for the computed Harris matrix.<br>
4. Based on the computed Eigen values of the Harris matrix, identify whether the output patch is, an edge, a corner, or a flat surface.<br>



<hr>



