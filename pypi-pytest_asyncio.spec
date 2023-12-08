#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-pytest_asyncio
Version  : 0.23.2
Release  : 55
URL      : https://files.pythonhosted.org/packages/1e/4a/9ed4762a08facf8dfb2e31b0393913e3dce391a7735e0965c0f2e66f0938/pytest-asyncio-0.23.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/1e/4a/9ed4762a08facf8dfb2e31b0393913e3dce391a7735e0965c0f2e66f0938/pytest-asyncio-0.23.2.tar.gz
Summary  : Pytest support for asyncio
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pytest_asyncio-license = %{version}-%{release}
Requires: pypi-pytest_asyncio-python = %{version}-%{release}
Requires: pypi-pytest_asyncio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pytest-asyncio
==============
.. image:: https://img.shields.io/pypi/v/pytest-asyncio.svg
:target: https://pypi.python.org/pypi/pytest-asyncio
.. image:: https://github.com/pytest-dev/pytest-asyncio/workflows/CI/badge.svg
:target: https://github.com/pytest-dev/pytest-asyncio/actions?workflow=CI
.. image:: https://codecov.io/gh/pytest-dev/pytest-asyncio/branch/main/graph/badge.svg
:target: https://codecov.io/gh/pytest-dev/pytest-asyncio
.. image:: https://img.shields.io/pypi/pyversions/pytest-asyncio.svg
:target: https://github.com/pytest-dev/pytest-asyncio
:alt: Supported Python versions
.. image:: https://img.shields.io/badge/Matrix-%23pytest--asyncio-brightgreen
:alt: Matrix chat room: #pytest-asyncio
:target: https://matrix.to/#/#pytest-asyncio:matrix.org

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
%setup -q -n pytest-asyncio-0.23.2
cd %{_builddir}/pytest-asyncio-0.23.2
pushd ..
cp -a pytest-asyncio-0.23.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702070955
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_asyncio
cp %{_builddir}/pytest-asyncio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_asyncio/92a74693f02c8e78dd90b2014c52bc35a95bab86 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
