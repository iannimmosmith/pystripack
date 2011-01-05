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

all: tests

tests: stripack_prb stripack_prb2 stripackd_prb stripackd_prb2
	cd out && for exe in $^ ; do \
	../bin/$${exe} > $${exe}.out ; \
	done ;

stripack_prb: stripack/stripack_prb.o stripack/stripack.o
	$(FC) $^ -o bin/$@

stripack_prb2: stripack/stripack_prb2.o stripack/stripack.o
	$(FC) $^ -o bin/$@

stripackd_prb: stripack/stripackd_prb.o stripack/stripackd.o
	$(FC) $^ -o bin/$@

stripackd_prb2: stripack/stripackd_prb2.o stripack/stripackd.o
	$(FC) $^ -o bin/$@

# Pattern rule for building f90 o files
%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@

clean:
	- rm -rf */*.o
	- rm -rf bin/stripack*
	- rm -rf out/stripack*
	# These because of older make targets
	- rm -rf bin/fsplit
	- rm -rf lib/*
	- rm -rf tmp/*

# unused
fsplit: f90split/f90split.o
	$(FC) $^ -o bin/$@

# unused
libstripack: stripack/stripack.f90 fsplit
	rm -rf tmp/*.f90 tmp/*.o
	cd tmp && ../bin/fsplit ../stripack/stripack.f90
	for filename in $(STRIPACK_F90S_R); do \
	$(FC) $(FFLAGS) -c tmp/$${filename}.f90 -o tmp/$${filename}.o; \
	done ;
	ar qc lib/libstripack.a tmp/*.o

# unused
libstripackd: stripack/stripackd.f90 fsplit
	rm -rf tmp/*.f90 tmp/*.o
	cd tmp && ../bin/fsplit ../stripack/stripackd.f90
	for filename in $(STRIPACK_F90S_D); do \
	$(FC) $(FFLAGS) -c tmp/$${filename}.f90 -o tmp/$${filename}.o; \
	done ;
	ar qc lib/libstripackd.a tmp/*.o
