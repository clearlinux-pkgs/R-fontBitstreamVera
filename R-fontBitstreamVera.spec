#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fontBitstreamVera
Version  : 0.1.1
Release  : 30
URL      : https://cran.r-project.org/src/contrib/fontBitstreamVera_0.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fontBitstreamVera_0.1.1.tar.gz
Summary  : Fonts with 'Bitstream Vera Fonts' License
Group    : Development/Tools
License  : OFL-1.0
BuildRequires : buildreq-R

%description
license for the 'fontquiver' package.

%prep
%setup -q -c -n fontBitstreamVera
cd %{_builddir}/fontBitstreamVera

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641018649

%install
export SOURCE_DATE_EPOCH=1641018649
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontBitstreamVera
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontBitstreamVera
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontBitstreamVera
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fontBitstreamVera || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fontBitstreamVera/DESCRIPTION
/usr/lib64/R/library/fontBitstreamVera/LICENCE
/usr/lib64/R/library/fontBitstreamVera/Meta/Rd.rds
/usr/lib64/R/library/fontBitstreamVera/Meta/features.rds
/usr/lib64/R/library/fontBitstreamVera/Meta/hsearch.rds
/usr/lib64/R/library/fontBitstreamVera/Meta/links.rds
/usr/lib64/R/library/fontBitstreamVera/Meta/nsInfo.rds
/usr/lib64/R/library/fontBitstreamVera/Meta/package.rds
/usr/lib64/R/library/fontBitstreamVera/NAMESPACE
/usr/lib64/R/library/fontBitstreamVera/fonts/Makefile
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-VERSION
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/COPYRIGHT.TXT
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/README.TXT
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/RELEASENOTES.TXT
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/Vera.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/Vera.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraBI.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraBI.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraBd.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraBd.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraIt.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraIt.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoBI.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoBI.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoBd.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoBd.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoIt.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMoIt.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMono.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraMono.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraSe.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraSe.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraSeBd.ttf
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/VeraSeBd.woff
/usr/lib64/R/library/fontBitstreamVera/fonts/bitstream-vera-fonts/local.conf
/usr/lib64/R/library/fontBitstreamVera/help/AnIndex
/usr/lib64/R/library/fontBitstreamVera/help/aliases.rds
/usr/lib64/R/library/fontBitstreamVera/help/fontBitstreamVera.rdb
/usr/lib64/R/library/fontBitstreamVera/help/fontBitstreamVera.rdx
/usr/lib64/R/library/fontBitstreamVera/help/paths.rds
/usr/lib64/R/library/fontBitstreamVera/html/00Index.html
/usr/lib64/R/library/fontBitstreamVera/html/R.css
