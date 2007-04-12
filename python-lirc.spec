%define pkgname pylirc

Summary: Python lirc module. 
Name: python-lirc
Version: 0.0.4
Release: %mkrel 5
Source0: %{pkgname}-%{version}.tar.bz2
License: LGPL
URL: http://pylirc.sourceforge.net/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: lirc-devel
BuildRequires: python-devel

%description
Python module for lirc support

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


