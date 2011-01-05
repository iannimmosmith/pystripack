FC = gfortran
FFLAGS = -g -Wall

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

# Pattern rule for building f90 .o files
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
