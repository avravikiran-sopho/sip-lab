function img=test(pic,RGB,edgetype,thresh,direction,path)
stacksize('max');
getd;
// Display mode
mode(-1);

// Display warning for floating point exception
ieee(1);
[img, RbandVal]=imgdisplay1(pic,RGB,path);
edgeImg = edge2(img,edgetype,thresh,direction);
imwrite(edgeImg,path+'edgeimg.jpg');
endfunction
