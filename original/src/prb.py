import numpy as np
import stripack.stripack_double as sp

'''
program stripack_prb
!
!*******************************************************************************
!
!! STRIPACK_PRB is a test routine for STRIPACK.
!
!
!  This driver tests software package STRIPACK for constructing a 
!  Delaunay triangulation and Voronoi diagram of a set of nodes on 
!  the surface of the unit sphere.
!
!  All STRIPACK subprograms are tested.
!
!  By default, a triangulation is created from a set of N nodes consisting 
!  of the north pole and N-1 points uniformly distributed around the 
!  60-degree parallel (with constant longitudinal separation).  
!
!  The data is stored as RLAT(I), RLON(I), which are the nodal coordinates 
!  in degrees latitude (-90 to 90) and degrees longitude (-180 to 180).
!
  implicit none
!
  integer, parameter :: nmax = 200
'''
nmax = 200
'''
  integer, parameter :: nrow = 9
'''
nrow = 9
'''
!
  real a
  real al
  real area
  real areas
  real ds(nmax)
'''
ds = np.zeros(nmax)
'''
  real elat
  real elon
  integer ier
  integer iflag
  logical inside
  integer iwk(2*nmax)
'''
iwk = np.zeros(2*nmax,dtype='i4')
'''
  integer k
  integer ksum
  integer kt
  integer lbtri(6,nmax)
'''
lbtri = np.array((6,nmax), dtype='i4')
'''
  integer lend(nmax)
'''
lend = np.zeros(nmax,dtype='i4')
'''
  integer lin
  integer list(6*nmax)
'''
list = np.zeros(6*nmax,dtype='i4')
'''
  integer listc(6*nmax)
'''
listc = np.zeros(6*nmax,dtype='i4')
'''
  integer lnew
  integer lp
  integer lpl
  integer, parameter :: lplt = 3
  integer, parameter :: lplv = 4
  integer lptr(6*nmax)
  integer ltri(nrow,2*nmax-4)
  integer lw
  integer n
  integer n0
  integer n1
  integer n2
  integer n3
  integer na
  integer nb
  integer nearnd
  integer nn
  integer nt
  logical numbr
  integer nv
  integer vnmax
  real p(3)
'''
p = np.zeros(3)
'''
  real, parameter :: pltsiz = 7.5E+00
  real rc(2*nmax-4)
'''
rc = np.zeros(2*nmax-4)
'''
  real rlat(nmax)
'''
rlat = np.zeros(nmax)
'''
  real rlon(nmax)
'''
rlon = np.zeros(nmax)
'''
  real sc
  character ( len = 80 ) trplot_file_name
  character ( len = 80 ) trplot_title
  real v1(3)
'''
v1 = np.zeros(3)
'''  
  real v2(3)
'''
v2 = np.zeros(3)
'''  
  real v3(3)
'''
v3 = np.zeros(3)
'''  
  real vlat
  real vlon
  real vnrm
  character ( len = 80 ) vrplot_file_name
  character ( len = 80 ) vrplot_title
  real x(nmax)
'''
x = np.zeros(nmax)
'''  
  real xc(2*nmax-4)
'''
xc = np.zeros(2*nmax-4)
'''  
  real y(nmax)
'''
y = np.zeros(nmax)
'''  
  real yc(2*nmax-4)
'''
yc = np.zeros(2*nmax-4)
'''  
  real z(nmax)
'''
z = np.zeros(nmax)
'''  
  real zc(2*nmax-4)
'''
zc = np.zeros(2*nmax-4)
'''  
!
! store nmax in variable so it is mutable.  Otherwise, when nmax is used as a
! mutable variable in subroutines, nasty errors can result in gfortran at least
!
  vnmax = nmax
!
  call timestamp ( )
'''
sp.timestamp()
'''
  write ( *, '(a)' ) ' '
  write ( *, '(a)' ) 'STRIPACK_PRB'
  write ( *, '(a)' ) '  Tests for STRIPACK.'
'''
print ' '
print '  prb.py'
print '  Tests for PYSTRIPACK.'
'''
!
!  Generate the default set of nodes as latitudinal and longitudinal
!  coordinates. 
!
  n = 9
'''
n = 9

'''
  rlat(1) = 90.0E+00
  rlat(2:n) = 60.0E+00
'''
rlat[0] = 90.
rlat[1:] = 60.
'''
  rlon(1) = 0.0E+00
'''
rlon[0] = 0.
'''
  do k = 2, n
    rlon(k) = real ( k - 2 ) * 360.0E+00 / real ( n - 1 )
  end do
'''
rlon[1:n]=np.linspace(n-2,0,n-1)*360./(n-1)
'''
  if ( n < 3 .or. nmax < n ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  The value of N is illegal.'
    write ( *, '(a,i6,a)' ) '  3 <= N <= NMAX = ', nmax, ' is required.'
    write ( *, '(a,i6)' ) '  Input N = ', n
    stop
  end if
'''
if n<3 or nmax < n:
    print ''
    print 'STRIPACK_PRB - Fatal error!'
    print '  The value of N is illegal.'
    print '  3 <= N <= NMAX = ', nmax, ' is required.'
    print '  Input N = ', n
    raise RuntimeError('')
'''

!
!  Set X and Y to the values of RLON and RLAT, respectively,
!  in radians.  (RLON and RLAT are saved for printing by TRPRNT).
!
  sc = atan ( 1.0E+00 ) / 45.0E+00
'''
sc = np.arctan (1.0) /45.
'''
  do k = 1, n
    x(k) = sc * rlon(k)
    y(k) = sc * rlat(k)
  end do
'''
x = sc*rlon
y = sc*rlat
'''
!
!  Transform spherical coordinates X and Y to Cartesian
!  coordinates (X,Y,Z) on the unit sphere (X**2 + Y**2 + Z**2 = 1).
!
  call trans ( n, y, x, x, y, z )
'''
sp.trans ( y[0:n], x[0:n], x, y, z,  n=9 )
'''  
  
!
!  Create the triangulation.
!
  call trmesh ( n, x, y, z, list, lptr, lend, lnew, iwk, iwk(n+1), ds, ier )

'''
sp.trmesh ( n, x, y, z, list, lptr, lend, lnew, iwk, iwk(n+1), ds, ier )
'''
  if ( ier == -2 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a)' ) '  Error in TRMESH.'
    write ( *, '(a)' ) '  The first three nodes are collinear.'
    stop
  else if ( ier > 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  Error in TRMESH.'
    write ( *, '(a)' ) '  Duplicate nodes encountered.'
    stop
  end if
!
!  Print the spherical coordinates and adjacency information.
!
!  IFLAG > 0 indicates that RLON and RLAT only are to be printed.
!
  iflag = 1

  call trprnt ( n, rlon, rlat, z, iflag, list, lptr, lend )
'''
sp.trprnt ( n, rlon, rlat, z, iflag, list, lptr, lend )
'''
!
!  Test TRLIST and TRLPRT by creating and printing a triangle list.
!
  call trlist ( n, list, lptr, lend, nrow, nt, ltri, ier )

  call trlprt ( n, rlon, rlat, z, iflag, nrow, nt, ltri )
!
!  Test TRPLOT by plotting the portion of the triangulation contained 
!  in the hemisphere centered at E = (ELAT,ELON), where ELAT and ELON
!  are taken to be the center of the range of
!  the nodal latitudes and longitudes.
!
  elat = minval ( rlat(1:n) )
  vlat = maxval ( rlat(1:n) )
  elon = minval ( rlon(1:n) )
  vlon = maxval ( rlon(1:n) )

  elat = ( elat + vlat ) / 2.0E+00
  elon = ( elon + vlon ) / 2.0E+00
  a = 90.0E+00
  numbr = n <= 200

  trplot_title = '(Triangulation created by STRIPACK_PRB)'

  trplot_file_name = 'stripack_prb_del.eps'

  open ( lplt, file = trplot_file_name )

  call trplot ( lplt, pltsiz, elat, elon, a, n, x, y, z, list, &
    lptr, lend, trplot_title, numbr, ier )

  if ( ier == 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'TRPLOT created the triangulation plot file: ' // &
      trim ( trplot_file_name )
  else
    write ( *, '(a)' ) ' '
    write ( *, '(a,i6)' ) 'TRPLOT returned error code ', ier
  end if
!
!  Test AREAS by computing and printing the area of the
!  convex hull of the nodes (sum of triangle
!  areas) relative to the total surface area (4*Pi).
!
  area = 0.0E+00

  do kt = 1, nt
    n1 = ltri(1,kt)
    n2 = ltri(2,kt)
    n3 = ltri(3,kt)
    v1(1) = x(n1)
    v1(2) = y(n1)
    v1(3) = z(n1)
    v2(1) = x(n2)
    v2(2) = y(n2)
    v2(3) = z(n2)
    v3(1) = x(n3)
    v3(2) = y(n3)
    v3(3) = z(n3)
    area = area + areas ( v1, v2, v3 )
  end do

  area = area / ( 16.0E+00 * atan ( 1.0E+00 ) )

  write ( *, '(a)' ) ' '
  write ( *, '(a,f8.2)' ) '  Relative area of convex hull = ', area
!
!  Test BNODES.  The ordered sequence of boundary nodes is stored in IWK.
!
  call bnodes ( n, list, lptr, lend, iwk, nb, na, nt )

  write ( *, '(a)' ) ' '
  write ( *, '(a)' ) '  Output from BNODES:'
  write ( *, '(a,i6)' ) '  Number of boundary nodes = ', nb
  write ( *, '(a,i6)' ) '  Number of arcs =           ', na
  write ( *, '(a,i6)' ) '  Number of triangles =      ', nt
!
!  Test GETNP by ordering the nodes on distance from N0 and verifying 
!  the ordering.  
!
!  The sequence of nodal indexes is stored in IWK, and the values of an
!  increasing function (the negative cosine) of angular distance is
!  stored in DS.
!
  n0 = n / 2
  iwk(1) = n0
  ds(1) = -1.0E+00
  ksum = n0

  do k = 2, n

    call getnp ( x, y, z, list, lptr, lend, k, iwk, ds(k), ier )

    if ( ier /= 0  .or.  ds(k) < ds(k-1) ) then
      write ( *, '(a)' ) ' '
      write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
      write ( *, '(a)' ) '  Error in GETNP.'
      stop
    end if

    ksum = ksum + iwk(k)

  end do
!
!  Test for all nodal indexes included in IWK.
!
  if ( ksum /= ( n * ( n + 1 ) ) / 2 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  Error in GETNP.'
    stop
  end if
!
!  Test NEARND by verifying that the nearest node to K is
!  node K for K = 1 to N.
!
  do k = 1, n

    p(1) = x(k)
    p(2) = y(k)
    p(3) = z(k)

    n0 = nearnd ( p, 1, n, x, y, z, list, lptr, lend, al )

    if ( n0 /= k .or. al > 0.001E+00 ) then
      write ( *, '(a)' ) ' '
      write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
      write ( *, '(a)' ) '  Error in NEARND.'
      stop
    end if

  end do
!
!  Test DELARC by removing a boundary arc if possible.
!  The last two nodes define a boundary arc
!  in the default data set.
!
  n1 = n-1
  n2 = n
  call delarc ( n, n1, n2, list, lptr, lend, lnew, ier )

  if ( ier == 1  .or.  ier == 4 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a,i6)' ) '  DELARC returned error code ', ier
    stop
  end if

  if ( ier /= 0 ) then

    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) '  Subroutine DELARC was not tested.'
    write ( *, '(a,i6,a,i6,a)' ) '  Nodes ', n1, ' and ', n2, &
      ' do not form a removable boundary arc.'
  else

    call trmesh ( n, x, y, z, list, lptr, lend, lnew, iwk, iwk(n+1), ds, &
      ier )

  end if
!
!  Test CRLIST, VRPLOT, and SCOORD by constructing and
!  plotting the Voronoi diagram, and printing
!  the Voronoi region boundary (ordered
!  sequence of Voronoi vertices) associated with N0.
!
!  Note that the triangulation data structure
!  is altered if NB > 0.
!
  call crlist ( n, nmax, x, y, z, list, lend, lptr, lnew, &
    lbtri, listc, nb, xc, yc, zc, rc, ier )

  if ( ier /= 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a,i6)' ) '  CRLIST returned error code ', ier
    stop
  end if
!
!  Use the same parameter values that were used for the
!  triangulation plot (except the output unit and title).
!
  nt = 2 * n - 4

  vrplot_file_name = 'stripack_prb_vor.eps'

  vrplot_title = '(Voronoi diagram created by STRIPACK_PRB)'

  open ( lplv, file = vrplot_file_name )

  call vrplot ( lplv, pltsiz, elat, elon, a, n, x, y, z, nt, listc, &
    lptr, lend, xc, yc, zc, vrplot_title, numbr, ier )

  if ( ier == 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'VRPLOT created the Voronoi plot file: ' // &
      trim ( vrplot_file_name )
  else
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a,i6)' ) '  VRPLOT returned error code ', ier
  end if

  n0 = 1

  write ( *, '(a)' ) ' '
  write ( *, '(a,i6)' ) '  Voronoi region for node ', n0
  write ( *, '(a)' ) ' '
  write ( *, '(a)' ) '     Triangle     Latitude     Longitude' // &
    '     Circumradius'
  write ( *, '(a)' ) ' '
!
!  Initialize for loop on Voronoi vertices (triangle circumcenters).  
!  The number of vertices is accumulated in NV, and the vertex indexes
!  are stored in IWK.  The vertices are converted to latitude and longitude 
!  in degrees for printing.
!
  nv = 0
  lpl = lend(n0)
  lp = lpl

  do

    lp = lptr(lp)
    kt = listc(lp)
    nv = nv + 1
    iwk(nv) = kt
    call scoord ( xc(kt), yc(kt), zc(kt), vlat, vlon, vnrm )
    vlat = vlat / sc
    vlon = vlon / sc
    write ( *, '(i13,f13.6,f14.6,f17.6)' ) kt, vlat, vlon, rc(kt)

    if ( lp == lpl ) then
      exit
    end if

  end do
!
!  Test INSIDE by checking for node N0 inside its Voronoi region.
!
  p(1) = x(n0)
  p(2) = y(n0)
  p(3) = z(n0)

  if ( .not. inside ( p, 2*nmax-4, xc, yc, zc, nv, iwk, ier ) ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a)' ) '  Error in INSIDE.'
    write ( *, '(a)' ) '  A node is not contained in its Voronoi region.'
    write ( *, '(a,i6)' ) '  Node index = ', n0
  end if

  if ( ier /= 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  Error in INSIDE.'
    write ( *, '(a,i6)' ) '  IER = ', ier
    stop
  end if
!
!  Recreate the triangulation and test the error flag.
!
  call trmesh ( n, x, y, z, list, lptr, lend, lnew, iwk, iwk(n+1), ds, ier )

  if ( ier == -2 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Warning!'
    write ( *, '(a)' ) '  Error in TRMESH.'
    write ( *, '(a)' ) '  The first three nodes are collinear.'
    stop
  else if ( ier > 0 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  Error in TRMESH.'
    write ( *, '(a)' ) '  Duplicate nodes encountered.'
    stop
  end if
!
!  Test EDGE by forcing an edge between nodes N1=1 and N2=N. 
!
  n1 = 1
  n2 = n

  call edge ( n1, n2, x, y, z, vnmax, iwk, list, lptr, lend, ier )

  if ( ier /= 0 .and. ier /= 5 ) then
    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
    write ( *, '(a)' ) '  Error in EDGE.'
    write ( *, '(a,i6)' ) '  IER = ', ier
    stop
  end if
!
!  Test DELNOD by removing nodes 4 to N (in reverse order). 
!
  if ( n <= 3 ) then

    write ( *, '(a)' ) ' '
    write ( *, '(a)' ) '  Subroutine DELNOD was not tested, because'
    write ( *, '(a)' ) '  the number of nodes N is too small.'

  else

    nn = n

    do

      call delnod ( nn, nn, x, y, z, list, lptr, lend, lnew, vnmax, iwk, ier )

      if ( ier /= 0 .and. ier /= 5 ) then
        write ( *, '(a)' ) ' '
        write ( *, '(a)' ) 'STRIPACK_PRB - Fatal error!'
        write ( *, '(a,i6)' ) '  DELNOD returned IER = ', ier
        stop
      end if

      if ( nn <= 3 ) then
        exit
      end if

    end do

  end if

  write ( *, '(a)' ) ' '
  write ( *, '(a)' ) 'STRIPACK_PRB'
  write ( *, '(a)' ) '  Normal end of execution.'

  stop
end
'''