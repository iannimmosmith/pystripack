#!/bin/csh
#
set echo
#
mkdir temp
cd temp
rm *
f90split ../stripack.f90
#
foreach FILE (`ls -1 *.f90`)
  f90 -c -C -fullwarn -g -static -u $FILE
  if ( $status != 0 ) exit
  rm $FILE
end
#
ar qc libstripack.a *.o
rm *.o
#
mv libstripack.a ~/lib/$ARCH
cd ..
rmdir temp
#
echo "A new version of stripack has been created."
