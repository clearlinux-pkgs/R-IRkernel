Name     : R-IRkernel
Version  : 0.8.11
Release  : 15
URL      : https://github.com/IRkernel/IRkernel/archive/0.8.11.tar.gz
Source0  : https://github.com/IRkernel/IRkernel/archive/0.8.11.tar.gz
Source10 : kernel.js
Source11 : kernel.json
Source12 : logo-64x64.png
Summary  : Native R Kernel for the 'Jupyter Notebook'
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers
BuildRequires : R-IRdisplay
BuildRequires : R-pbdZMQ
BuildRequires : R-jsonlite
BuildRequires : R-uuid
BuildRequires : R-stringi
BuildRequires : R-evaluate

Requires : R-IRdisplay
Requires : R-pbdZMQ
Requires : R-jsonlite
Requires : R-uuid
Requires : R-stringi
Requires : R-evaluate

%description
Native R kernel for Jupyter 

%prep
%setup -q -c -n IRkernel-0.8.11

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485743286

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1485743286
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRkernel-0.8.11
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
mkdir -p %{buildroot}/usr/share/jupyter/kernels/ir
cp %{SOURCE10} %{buildroot}/usr/share/jupyter/kernels/ir/
cp %{SOURCE11} %{buildroot}/usr/share/jupyter/kernels/ir/
cp %{SOURCE12} %{buildroot}/usr/share/jupyter/kernels/ir/

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/IRkernel/
/usr/share/jupyter/kernels/ir
