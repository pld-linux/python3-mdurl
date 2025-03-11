#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Markdown URL utilities
Summary(pl.UTF-8):	Narzędzia do URL-i w formacie Markdown
Name:		python3-mdurl
Version:	0.1.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mdurl/
Source0:	https://files.pythonhosted.org/packages/source/m/mdurl/mdurl-%{version}.tar.gz
# Source0-md5:	f18eca6522b438354be2378f216a5a94
URL:		https://pypi.org/project/mdurl/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:61
# TODO:
#BuildRequires:	python3-flit_core >= 3.2.0
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-randomly
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URL utilities for markdown-it parser.

%description -l pl.UTF-8
Narzędzia do URL-i dla parsera markdown-it.

%prep
%setup -q -n mdurl-%{version}

# setuptools stub
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_randomly" \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/mdurl
%{py3_sitescriptdir}/mdurl-%{version}-py*.egg-info
