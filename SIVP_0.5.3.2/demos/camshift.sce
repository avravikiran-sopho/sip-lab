n  = aviopen(pathconvert(getSIVPpath()) + "images" + filesep() + "red-car-video.mpg");

//skip the first 4 frames
im = avireadframe(n);
im = avireadframe(n);
im = avireadframe(n);
im = avireadframe(n);
im = avireadframe(n);
obj_win = camshift(im, [21, 2, 50, 40]); //initialize tracker
while ~isempty(im),
      obj_win = camshift(im); //camshift tracking
      im = rectangle(im, obj_win, [0,255,0]);
      imshow(im);
      im = avireadframe(n);
end;
aviclose(n);
