FC = gfortran
FFLAGS = -g -Wall

STRIPACK_F90S = addnod arc_cosine areas bdyadd bnodes circum covsph crlist \
		delarc delnb delnod edge getnp insert inside intadd intrsc \
		i_swap jrand left lstptr nbcnt nearnd optim r3vec_normalize \
		r_pi scoord store swap swptst timestamp trans trfind trlist \
		trlprt trmesh trplot trprnt voronoi_poly_count vrplot 

%.o: %.f90
	$(FC) $(FFLAGS) -c $< -o $@

fsplit: f90split/f90split.o
	$(FC) $< -o $@

clean:
	- rm *.f90
	- rm -rf */*.o
	- rm fsplit
	- rm libstripack.a
	- rm stirpack_prb*
	- rm -rf temp

libstripack.a: stripack/stripack.f90 fsplit
	- rm -rf temp
	- mkdir temp
	cd temp && ../fsplit ../stripack/stripack.f90
	for filename in $(STRIPACK_F90S); do \
	$(FC) $(FFLAGS) -c temp/$${filename}.f90 -o temp/$${filename}.o; \
	done ;
	ar qc libstripack.a temp/*.o

stripack-test: libstripack.a stripack/stripack_prb.o
	$(FC) -o stripack_prb stripack/stripack_prb.o -L. -lstripack
	./stripack_prb > stripack_prb.out

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
