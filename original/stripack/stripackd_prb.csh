#!/bin/csh
#
set echo
#
f90 -c -C -fullwarn -g -static -u stripackd_prb.f90
if ( $status != 0 ) exit
#
f90 stripackd_prb.o -L$HOME/lib/$ARCH -lstripackd
if ( $status != 0 ) exit
rm ._*
#
rm stripackd_prb.o
mv a.out stripackd_prb
#
stripackd_prb > stripackd_prb.out
#
if ( $status == 0 ) then
  rm stripackd_prb
endif
#
echo "Normal end of stripackd_prb tests."
