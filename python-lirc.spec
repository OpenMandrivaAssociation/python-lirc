%define pkgname pylirc

Summary: Python lirc module
Name: python-lirc
Version: 0.0.5
Release: 5
Source0: %{pkgname}-%{version}.tar.bz2
License: LGPL
URL: http://pylirc.sourceforge.net/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: lirc-devel
BuildRequires: python-devel

%description
Python module for lirc support.

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




%changelog
* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.0.5-4mdv2011.0
+ Revision: 591929
- Rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.0.5-3mdv2010.0
+ Revision: 442291
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.0.5-2mdv2009.1
+ Revision: 319621
- rebuild for python 2.6
- correct summary and description

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.5-1mdv2008.0
+ Revision: 52597
- update to new version 0.0.5


* Thu Dec 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.4-5mdv2007.0
+ Revision: 96916
- Rebuild against new python
- Import python-lirc

* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 0.0.4-3mdk
- Rebuild

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.0.4-2mdk
- Rebuild for new python

