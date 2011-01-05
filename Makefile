# Generate stripack python modules

FF90 = original/stripack/stripack.f90
DF90 = original/stripack/stripackd.f90
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
