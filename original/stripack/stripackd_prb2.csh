#!/bin/csh
#
set echo
#
f90 -c stripackd_prb2.f90
if ( $status != 0 ) exit
#
f90 stripackd_prb2.o -L$HOME/lib/$ARCH -lstripackd
if ( $status != 0 ) exit
#
rm stripackd_prb2.o
mv a.out stripackd_prb2
#
stripackd_prb2 > stripackd_prb2.out
#
if ( $status == 0 ) then
  rm stripackd_prb2
endif
#
echo "Normal end of stripackd_prb2 tests."
