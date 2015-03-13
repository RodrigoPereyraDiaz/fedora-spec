# rpm does not currently pull debuginfo out of mono packages
%global debug_package %{nil}

Summary:	MonoDevelop gdb Debugger Add-in
Name:		monodevelop-debugger-gdb
Version:	5.0.1
Release:	1%{?dist}
License:	MIT
Group:		Development/Tools
Source:		http://download.mono-project.com/sources/%{name}/%{name}-%{version}-0.tar.bz2
URL:		http://www.monodevelop.com/
BuildRequires:	mono-devel >= 3.0.4
BuildRequires:	monodevelop-devel >= 4.2
BuildRequires:	mono-addins-devel
Requires:	monodevelop >= 4.2
Requires:	gdb
ExclusiveArch:	%ix86 x86_64 ia64 armv4l sparcv9 alpha s390 s390x

%description
Mono gdb Debugger Add-in for MonoDevelop.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Debugger/MonoDevelop.Debugger.Gdb*

%changelog
* Mon Jun 23 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Tue Jan 28 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Thu Nov 21 2013 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2-1
- Update to 4.2

* Fri Oct 14 2011 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 2.8.1-1
- Update to last version

* Mon Sep 12 2011 Christian Krause <chkr@fedoraproject.org> - 2.6-1
- Update to 2.6
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-1
- Bump to 2.4
- Alter BR and R to reflect 2.4

* Sun May 30 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3.1-1
- Bump to 2.4 beta 2

* Tue May 18 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3-1
- Bump to 2.4 beta

* Thu Mar 04 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-2
- Spec file clean up
- Remove BR gdb, added R gdb

* Fri Feb 12 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-1
- Bump to 2.2.1

* Sun Jan 24 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2
- Fix URL and licence
- Fix build problems on x86_64

* Sun Jan 03 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Initial import

