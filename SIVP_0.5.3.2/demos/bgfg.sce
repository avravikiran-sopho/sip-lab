n    = aviopen(pathconvert(getSIVPpath()) + "images" + filesep() + "video.avi");
im   = avireadframe(n);
fgim = uint8(zeros( size(im,1), size(im,2), 3)) ;
fg   = detectforeground(im, 'LI');//create background model

while ~isempty(im)
    fg = detectforeground(im);//get the foreground mask
    fgim(:,:,1)=fg;
    fgim(:,:,2)=fg;
    fgim(:,:,3)=fg;
    imshow([im; fgim]);
    im = avireadframe(n);
end

aviclose(n);
