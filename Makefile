# Generate stripack python modules

FC = gfortran
FFLAGS = -g -Wall

FF90 = stripack/stripack.f90
DF90 = stripack/stripackd.f90

all: stripack_float stripack_double

stripack_float: stripack/stripack_float.pyf $(FF90)
	cd stripack && f2py -c stripack_float.pyf ../$(FF90)

stripack_double: stripack/stripack_double.pyf $(DF90)
	cd stripack && f2py -c stripack_double.pyf ../$(DF90)

just-once: $(FF90) $(DF90)
	# Generate pyf files - just once for given source file.  This is because you
	# will usually edit the generated .pyf files and so these edits will be
	# wiped out by running this target
	f2py -m stripack_float -h stripack/stripack_float.pyf $(FF90)
	f2py -m stripack_double -h stripack/stripack_double.pyf $(DF90)

clean:
	-rm -rf stripack/stripack_float.so
	-rm -rf stripack/stripack_double.so
	-rm -rf */*.o
	-rm -rf test-bin/*
	-rm -rf test-out/*

# Targets below for regresssion testing fortran code

regression-tests: stripack_prb stripack_prb2 stripackd_prb stripackd_prb2
	cd test-out && for exe in $^ ; do \
	../test-bin/$${exe} > $${exe}.out ; \
	done ;
	diff test-out/stripack_prb.out original/stripack/stripack_prb.out
	diff test-out/stripackd_prb.out original/stripack/stripackd_prb.out

stripack_prb: original/stripack/stripack_prb.o stripack/stripack.o
	$(FC) $^ -o test-bin/$@

stripack_prb2: original/stripack/stripack_prb2.o stripack/stripack.o
	$(FC) $^ -o test-bin/$@

stripackd_prb: original/stripack/stripackd_prb.o stripack/stripackd.o
	$(FC) $^ -o test-bin/$@

stripackd_prb2: original/stripack/stripackd_prb2.o stripack/stripackd.o
	$(FC) $^ -o test-bin/$@

# Pattern rule for building f90 .o files
%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@
