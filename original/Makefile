FC = gfortran
FFLAGS = -g -Wall
FCL = $(FC) -Llib -lstripack
FCLD = $(FC) -Llib -lstripackd

STRIPACK_F90S = addnod arc_cosine areas bdyadd bnodes circum covsph crlist \
		delarc delnb delnod edge getnp insert inside intadd intrsc \
		i_swap jrand left lstptr nbcnt nearnd optim \
		scoord store swap swptst timestamp trans trfind trlist \
		trlprt trmesh trplot trprnt voronoi_poly_count vrplot

STRIPACK_F90S_R = $(STRIPACK_F90S) r_pi r3vec_normalize
STRIPACK_F90S_D = $(STRIPACK_F90S) d_pi d3vec_normalize

all: stripack_prb stripack_prb2 stripackd_prb stripackd_prb2

%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@

fsplit: f90split/f90split.o
	$(FC) $< -o bin/fsplit

stripack_prb: stripack/stripack_prb.f90 libstripack
	$(FCL) stripack/stripack_prb.f90 -o bin/stripack_prb
	cd out && ../bin/stripack_prb > stripack_prb.out

stripack_prb2: stripack/stripack_prb2.f90 libstripack
	$(FCL) stripack/stripack_prb2.f90 -o bin/stripack_prb2
	cd out && ../bin/stripack_prb2 > stripack_prb2.out

stripackd_prb: stripack/stripackd_prb.f90 libstripackd
	$(FCLD) stripack/stripackd_prb.f90 -o bin/stripackd_prb
	cd out && ../bin/stripackd_prb > stripackd_prb.out

stripackd_prb2: stripack/stripackd_prb2.f90 libstripackd
	$(FCLD) stripack/stripackd_prb2.f90 -o bin/stripackd_prb2
	cd out && ../bin/stripackd_prb2 > stripackd_prb2.out

init:
	# Run once if you get missing directory errors
	- mkdir bin lib out tmp

clean:
	- rm -rf */*.o
	- rm -rf bin/*
	- rm -rf lib/*
	- rm -rf tmp/*
	- rm -rf out/*

libstripack: stripack/stripack.f90 fsplit
	rm -rf tmp/*.f90 tmp/*.o
	cd tmp && ../bin/fsplit ../stripack/stripack.f90
	for filename in $(STRIPACK_F90S_R); do \
	$(FC) $(FFLAGS) -c tmp/$${filename}.f90 -o tmp/$${filename}.o; \
	done ;
	ar qc lib/libstripack.a tmp/*.o

libstripackd: stripack/stripackd.f90 fsplit
	rm -rf tmp/*.f90 tmp/*.o
	cd tmp && ../bin/fsplit ../stripack/stripackd.f90
	for filename in $(STRIPACK_F90S_D); do \
	$(FC) $(FFLAGS) -c tmp/$${filename}.f90 -o tmp/$${filename}.o; \
	done ;
	ar qc lib/libstripackd.a tmp/*.o
