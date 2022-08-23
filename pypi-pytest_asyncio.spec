#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_asyncio
Version  : 0.19.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/43/1c/4293ce5ddfd1db78fbf192bd3c47183c9ecc2816b8de382ed1b2491c7cea/pytest-asyncio-0.19.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/1c/4293ce5ddfd1db78fbf192bd3c47183c9ecc2816b8de382ed1b2491c7cea/pytest-asyncio-0.19.0.tar.gz
Summary  : Pytest support for asyncio
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pytest_asyncio-license = %{version}-%{release}
Requires: pypi-pytest_asyncio-python = %{version}-%{release}
Requires: pypi-pytest_asyncio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(pytest)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
pytest-asyncio: pytest support for asyncio
==========================================

%package license
Summary: license components for the pypi-pytest_asyncio package.
Group: Default

%description license
license components for the pypi-pytest_asyncio package.


%package python
Summary: python components for the pypi-pytest_asyncio package.
Group: Default
Requires: pypi-pytest_asyncio-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_asyncio package.


%package python3
Summary: python3 components for the pypi-pytest_asyncio package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_asyncio)
Requires: pypi(pytest)

%description python3
python3 components for the pypi-pytest_asyncio package.


%prep
%setup -q -n pytest-asyncio-0.19.0
cd %{_builddir}/pytest-asyncio-0.19.0
pushd ..
cp -a pytest-asyncio-0.19.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657894943
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_asyncio
cp %{_builddir}/pytest-asyncio-0.19.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_asyncio/92a74693f02c8e78dd90b2014c52bc35a95bab86
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_asyncio/92a74693f02c8e78dd90b2014c52bc35a95bab86

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
