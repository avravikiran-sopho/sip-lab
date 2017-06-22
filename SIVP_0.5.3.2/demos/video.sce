filename = pathconvert(getSIVPpath()) + "images" + filesep() + "video.mpg";
n        = aviopen(filename);

for idx=1:100 do
    im=avireadframe(n);
    imshow(im);
end

aviclose(n);
