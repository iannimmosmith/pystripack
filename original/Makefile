FC = gfortran

%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@

fsplit: f90split/f90split.o
	$(FC) $< -o $@

clean:
	- rm *.f90
	- rm fsplit

libstripack.a: stripack/stripack.f90 fsplit
	- mkdir temp
	cd temp &&  rm * ; ../fsplit ../stripack/stripack.f90

#foreach FILE (`ls -1 *.f90`)
#	$(FC) -c -C -fullwarn -g -static -u $FILE
#	if ( $status != 0 ) exit
#	rm $FILE
#end

##
#ar qc libstripack.a *.o
#rm *.o
##
#mv libstripack.a ~/lib/$ARCH
#cd ..
#rmdir temp
##
#echo "A new version of stripack has been created."
