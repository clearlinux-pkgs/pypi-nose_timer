#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nose_timer
Version  : 1.0.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/ee/fc/ad961aa29606e20b3c85f739ab7d2e5abe0c285310c468a5850dcaf9c720/nose-timer-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ee/fc/ad961aa29606e20b3c85f739ab7d2e5abe0c285310c468a5850dcaf9c720/nose-timer-1.0.1.tar.gz
Summary  : A timer plugin for nosetests
Group    : Development/Tools
License  : MIT
Requires: pypi-nose_timer-license = %{version}-%{release}
Requires: pypi-nose_timer-python = %{version}-%{release}
Requires: pypi-nose_timer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(nose)

%description
==========

%package license
Summary: license components for the pypi-nose_timer package.
Group: Default

%description license
license components for the pypi-nose_timer package.


%package python
Summary: python components for the pypi-nose_timer package.
Group: Default
Requires: pypi-nose_timer-python3 = %{version}-%{release}

%description python
python components for the pypi-nose_timer package.


%package python3
Summary: python3 components for the pypi-nose_timer package.
Group: Default
Requires: python3-core
Provides: pypi(nose_timer)
Requires: pypi(nose)

%description python3
python3 components for the pypi-nose_timer package.


%prep
%setup -q -n nose-timer-1.0.1
cd %{_builddir}/nose-timer-1.0.1
pushd ..
cp -a nose-timer-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656391540
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nose_timer
cp %{_builddir}/nose-timer-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nose_timer/218d8eca50e1cca1d8c154b6e3ff8096a06d5927
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nose_timer/218d8eca50e1cca1d8c154b6e3ff8096a06d5927

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
