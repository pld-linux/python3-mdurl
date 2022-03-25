#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Markdown URL utilities
Summary(pl.UTF-8):	Narzędzia do URL-i w formacie Markdown
Name:		python3-mdurl
Version:	0.1.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mdurl/
Source0:	https://files.pythonhosted.org/packages/source/m/mdurl/mdurl-%{version}.tar.gz
# Source0-md5:	148af8104f656a6fd70877505bc3fa2c
URL:		https://pypi.org/project/mdurl/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-randomly
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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

# (extracted from pyproject.toml - keep in sync!)
cat >setup.cfg <<'EOF'
[metadata]
name = mdurl
version = %{version}
description = Markdown URL utilities
author = Taneli Hukkinen
author_email = hukkin@users.noreply.github.com
license = MIT
license_file = LICENSE
classifiers =
    License :: OSI Approved :: MIT License
    Operating System :: MacOS
    Operating System :: Microsoft :: Windows
    Operating System :: POSIX :: Linux
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Topic :: Software Development :: Libraries :: Python Modules
    Typing :: Typed
[options]
packages = find:
package_dir =
    =src
python_requires = >=3.6
[options.packages.find]
where=src
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
