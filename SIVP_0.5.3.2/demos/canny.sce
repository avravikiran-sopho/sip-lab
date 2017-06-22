im  = imread(pathconvert(getSIVPpath()) + "images" + filesep() + "lena.png")
imc = edge(rgb2gray(im),'canny');
imshow(imc);
