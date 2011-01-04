#!/bin/csh
#
set echo
#
f90 -c stripack_prb2.f90
if ( $status != 0 ) exit
#
f90 stripack_prb2.o -L$HOME/lib/$ARCH -lstripack
if ( $status != 0 ) exit
#
rm stripack_prb2.o
mv a.out stripack_prb2
#
stripack_prb2 > stripack_prb2.out
#
if ( $status == 0 ) then
  rm stripack_prb2
endif
#
echo "Normal end of stripack_prb2 tests."
