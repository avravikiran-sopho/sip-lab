function colourtransform(pic,RGB,path)
    [img,RbandVal,GbandVal,BbandVal] = imgdisplay1(pic,RGB,path);

img = double(img);
// START transform
[row,col,band]=size(img);


for i=1:size(img,1)
    for j=1:size(img,2)
        r(i,j)=img(i,j,1)/(img(i,j,1)+img(i,j,2)+img(i,j,3));
        g(i,j)=img(i,j,2)/(img(i,j,1)+img(i,j,2)+img(i,j,3));
        b(i,j)=img(i,j,3)/(img(i,j,1)+img(i,j,2)+img(i,j,3));
    end
end
VALUE=(img(:,:,1)+img(:,:,2)+img(:,:,3))./(3*255); // [0 1]


for i=1:size(r,1)
    for j=1:size(r,2)
if(b(i,j)<=g(i,j))
    hue(i,j)=acos(0.5*((r(i,j)-g(i,j))+(r(i,j)-b(i,j)))/sqrt((r(i,j)-g(i,j))^2+(r(i,j)-b(i,j))*(g(i,j)-b(i,j)))); 
else
    hue(i,j)=2*%pi-acos(0.5*((r(i,j)-g(i,j))+(r(i,j)-b(i,j)))/sqrt((r(i,j)-g(i,j))^2+(r(i,j)-b(i,j))*(g(i,j)-b(i,j))));  
end
    vec=[r(i,j),g(i,j),b(i,j)];
    SATURATION(i,j)=(1-3*(min(vec))); //[0 1]
    
    end
end
  imwrite(VALUE,path+'out_VALUE.jpg');
  imwrite(SATURATION,path+'out_SATURATION.jpg');
  imwrite(hue,path+'out_HUE.jpg');
  //composite=cat(3,hue,SATURATION,VALUE);
  composite=zeros(row,col,band);
  composite(:,:,1)=hue;
  composite(:,:,2)=SATURATION;
  composite(:,:,3)=VALUE;
  
   
  imwrite(composite,path+'out_HSV.jpg');
  
clear img;
    img=imread(path+'out_HSV.jpg');
    img=double(img);
    [row,col,band]=size(img);
    
   h=img(:,:,1) ./255;s=img(:,:,2) ./255;i=img(:,:,3) ./255; clear img;
   var1=2*%pi/3;
   var2=2*var1;
   var3=3*var1;
   for p=1:size(i,1)
       for q=1:size(i,2)
           x(p,q)=i(p,q)*(1-s(p,q));
                    
           if(h(p,q)<var1)
               y(p,q)=i(p,q)*(1+((s(p,q)*cos(h(p,q)))/(cos((%pi/3)-h(p,q)))));
               z(p,q)=(3*i(p,q))-(x(p,q)+y(p,q));
               b(p,q)=x(p,q);r(p,q)=y(p,q);g(p,q)=z(p,q);
           elseif((h(p,q)>=var1)&(h(p,q)<var2))
               h1=h(p,q)-var1;
               y(p,q)=i(p,q)*(1+((s(p,q)*cos(h1))/(cos((%pi/3)-h1))));
               z(p,q)=(3*i(p,q))-(x(p,q)+y(p,q));
               r(p,q)=x(p,q);g(p,q)=y(p,q);b(p,q)=z(p,q);
           elseif((h(p,q)>=var2)&(h(p,q)<var3))
               h2=h(p,q)-var2;
               y(p,q)=i(p,q)*(1+((s(p,q)*cos(h2))/(cos((%pi/3)-h2))));
               z(p,q)=(3*i(p,q))-(x(p,q)+y(p,q));
               r(p,q)=z(p,q);g(p,q)=x(p,q);b(p,q)=y(p,q);
           end
       end
   end
  r_min=min(min(r));r_max=max(max(r));const=1/(r_max-r_min);
  for i=1:size(r,1)
      for j=1:size(r,2)
          R(i,j)=uint8(255*(r(i,j)-r_min)*const);
      end
  end
  g_min=min(min(g));g_max=max(max(g));const=1/(g_max-g_min);
  for i=1:size(g,1)
      for j=1:size(g,2)
          G(i,j)=uint8(255*(g(i,j)-g_min)*const);
      end
  end
  b_min=min(min(b));b_max=max(max(b));const=1/(b_max-b_min);
  for i=1:size(b,1)
     for j=1:size(b,2)
          B(i,j)=uint8(255*(b(i,j)-b_min)*const);
      end
  end
   imwrite(R,path+'out_Red.jpg');
  imwrite(G,path+'out_Green.jpg');
  imwrite(B,path+'out_Blue.jpg');
  
  r=linspace(0,1,255)';
g=zeros(255,1);
b=zeros(255,1);
cmap=[r g b];
cmap1=[g r b];
cmap2=[g b r];
im1=ind2rgb(R,cmap);
im2=ind2rgb(G,cmap1);
im3=ind2rgb(B,cmap2);
composite=im1+im2+im3;
  imwrite(composite,path+'out_RGB.jpg');
  
    
      
//END transform
endfunction
