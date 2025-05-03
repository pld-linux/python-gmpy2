#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_with	tests	# unit tests (many inf or nan sign differences)

Summary:	Python interface to GMP/MPIR, MPFR and MPC libraries
Summary(pl.UTF-8):	Interfejs do bibliotek GMP/MPIR, MPFR oraz MPC
Name:		python-gmpy2
Version:	2.1.5
Release:	4
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/gmpy2/
Source0:	https://files.pythonhosted.org/packages/source/g/gmpy2/gmpy2-%{version}.tar.gz
# Source0-md5:	0cd8e9d89c2f9d018eb52d2983abaeb4
URL:		https://pypi.org/project/gmpy2/
BuildRequires:	gmp-devel
BuildRequires:	libmpc-devel >= 1.0.3
BuildRequires:	mpfr-devel
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	libmpc >= 1.0.3
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gmpy2 is an optimized, C-coded Python extension module that supports
fast multiple-precision arithmetic. gmpy2 is based on the original
gmpy module. gmpy2 adds support for correctly rounded
multiple-precision real arithmetic (using the MPFR library) and
complex arithmetic (using the MPC library).

%description -l pl.UTF-8
gmpy2 to zoptymalizowany, napisany w C moduł rozszerzenia Pythona,
obsługujący szybką arytmetykę wielokrotnej precyzji. Moduł gmpy2 jest
oparty na oryginalnym module gmpy. Dodaje obsługę poprawnie
zaokrąglanej arytmetyki rzeczywistej wielokrotnej precyzji (przy
użyciu biblioteki MPFR) oraz arytmetyki zespolonej (przy użyciu
biblioteki MPC).

%package apidocs
Summary:	API documentation for Python gmpy2 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona gmpy2
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python gmpy2 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona gmpy2.

%prep
%setup -q -n gmpy2-%{version}

%build
%py_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} test/runtests.py
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/gmpy2
%attr(755,root,root) %{py_sitedir}/gmpy2/gmpy2.so
%{py_sitedir}/gmpy2/__init__.py[co]
%{py_sitedir}/gmpy2/*.pxd
%{py_sitedir}/gmpy2/gmpy2.h
%{py_sitedir}/gmpy2-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
