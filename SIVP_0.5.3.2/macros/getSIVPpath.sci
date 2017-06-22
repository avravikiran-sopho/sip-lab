// Allan CORNET - DIGITEO - 2010

function p = getSIVPpath()
  p = [];
  if isdef('sivplib') then
    [m, mp] = libraryinfo('sivplib');
    p = pathconvert(fullpath(mp + '../'));
  end
endfunction