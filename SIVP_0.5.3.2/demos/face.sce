stacksize("max");
im = imread(pathconvert(getSIVPpath()) + "images" + filesep() + "people.jpg")
face = detectfaces(im);
[m,n] = size(face);
for i=1:m,
    im = rectangle(im, face(i,:), [0,255,0]);
end;
imshow(im);
