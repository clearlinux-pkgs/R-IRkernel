Name     : R-IRkernel
Version  : 1.3
Release  : 53
URL      : https://cran.r-project.org/src/contrib/IRkernel_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/IRkernel_1.3.tar.gz
Source10 : kernel.js
Source11 : kernel.json
Source12 : logo-64x64.png
Summary  : Native R Kernel for the 'Jupyter Notebook'
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers
BuildRequires : buildreq-R
BuildRequires : R-IRdisplay
BuildRequires : R-crayon
BuildRequires : R-digest
BuildRequires : R-evaluate
BuildRequires : R-jsonlite
BuildRequires : R-pbdZMQ
BuildRequires : R-repr
BuildRequires : R-uuid
Requires : R-IRdisplay
Requires : R-crayon
Requires : R-digest
Requires : R-evaluate
Requires : R-jsonlite
Requires : R-pbdZMQ
Requires : R-repr
Requires : R-uuid

%description
Native R kernel for Jupyter 

%prep
%setup -q -c -n IRkernel

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578276581

%install
export SOURCE_DATE_EPOCH=1578276581
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRkernel
rm -f %{buildroot}/usr/share/R/library/R.css
mkdir -p %{buildroot}/usr/share/jupyter/kernels/ir
cp -v %{SOURCE10} %{buildroot}/usr/share/jupyter/kernels/ir/
cp -v %{SOURCE11} %{buildroot}/usr/share/jupyter/kernels/ir/
cp -v %{SOURCE12} %{buildroot}/usr/share/jupyter/kernels/ir/

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc IRkernel || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/IRkernel/
/usr/share/jupyter/kernels/ir
