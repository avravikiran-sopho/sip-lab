stacksize('max');
mode(-1);
exec('/usr/share/scilab/contrib/sivp/loader.sce');
getd;
pic='inputimage';
RGB=evstr(x_dialog('RGB bands range [1 6] ?','1')); //here only one band value is taken as input
path='/home/priya/Desktop/edge/';
edgetype='prewitt';
thresh=0.02;
direction='horizontal';

[img, RbandVal]=imgdisplay1(pic,RGB,path);
edgeImg = edge2(img,edgetype,thresh,direction);
imwrite(edgeImg,path+'edgeimg.jpg');
