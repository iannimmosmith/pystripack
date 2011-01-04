#!/bin/csh
#
set echo
#
f90 -c -C -fullwarn -g -static -u stripack_prb.f90
if ( $status != 0 ) exit
#
f90 stripack_prb.o -L$HOME/lib/$ARCH -lstripack
if ( $status != 0 ) exit
rm ._*
#
rm stripack_prb.o
mv a.out stripack_prb
#
stripack_prb > stripack_prb.out
#
if ( $status == 0 ) then
  rm stripack_prb
endif
#
echo "Normal end of stripack_prb tests."
