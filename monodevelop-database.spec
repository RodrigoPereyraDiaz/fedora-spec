# rpm does not currently pull debuginfo out of mono packages
%global debug_package %{nil}

Summary:        MonoDevelop Database Add-in
Name:           monodevelop-database
Version:        5.7
Release:        1%{?dist}
License:        MIT
Group:          Development/Tools
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.0.660.tar.bz2
URL:            http://www.monodevelop.com
BuildRequires:  mono-devel >= 3.0.4
BuildRequires:  monodevelop-devel >= 5.0
BuildRequires:  mono-addins-devel >= 1.0
BuildRequires:  intltool
BuildRequires:  gtk-sharp2-devel
BuildRequires:  mono-data-postgresql mono-data-sqlite
Requires:       monodevelop >= 5.0
ExclusiveArch:  %ix86
ExclusiveArch:  x86_64
ExclusiveArch:  ia64
ExclusiveArch:  armv4l
ExclusiveArch:  sparcv9
ExclusiveArch:  alpha
ExclusiveArch:  s390
ExclusiveArch:  s390x

#Package Devel
%description
Database Add-in for MonoDevelop.

%package devel
Summary:        Development files for MonoDevelop Database Add-in
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Database Add-in for MonoDevelop. Development package.

Contains development files for %{name}.

%prep
%setup -q

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -o -type l|sed '
s:'"%{buildroot}"'::
s:\(.*/lib/monodevelop/AddIns/MonoDevelop.Database/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:
s:^\([^%].*\)::
s:%lang(C) ::
/^$/d' > %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database

%files devel
%defattr(-,root,root,-)
%{_prefix}/lib/pkgconfig/monodevelop-database.pc

%changelog
* Fri Jan 16 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 5.7-1
- Update to 5.7

* Mon Oct 20 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 5.5-1
- Update to 5.5

* Mon Jun 23 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Tue Jan 28 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Thu Nov 21 2013 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 4.2-1
- Update to 4.2

* Fri Oct 14 2011 - Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> - 2.8.1-1
- Update upstream version

* Fri Jun 18 2010 - Claudio Rodrigo Pereyra Diaz <claudio@pereyradiaz.com.ar> - 2.4
- Update upstream version

* Thu Mar 04 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-6
- More spec file clean up
- Fix for language file

* Sat Feb 20 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-5
- More lang file fixes
- Spec file cleanup

* Sat Feb 13 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-4
- Remove gettext patch
- Use fix from anki package

* Tue Feb 02 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-3
- Fix gettext problem

* Sun Jan 24 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2
- Fix URL and licence

* Sun Jan 03 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Initial import
- Fix the usual fixed points for installs to make it 64 bit happy
- Fix the locale files so they're also in the right place
