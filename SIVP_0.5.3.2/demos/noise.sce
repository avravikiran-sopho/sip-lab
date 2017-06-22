stacksize("max");
imn = imnoise(imread(pathconvert(getSIVPpath()) + "images" + filesep() + "lena.png"),"gaussian");
imshow(imn);
