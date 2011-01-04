#!/bin/csh
#
set echo
#
mkdir temp
cd temp
rm *
f90split ../stripackd.f90
#
foreach FILE (`ls -1 *.f90`)
  f90 -c -C -fullwarn -g -static -u $FILE
  if ( $status != 0 ) exit
  rm $FILE
end
#
ar qc libstripackd.a *.o
rm *.o
#
mv libstripackd.a ~/lib/$ARCH
cd ..
rmdir temp
#
echo "A new version of stripackd has been created."
