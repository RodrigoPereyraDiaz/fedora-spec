Name:           hamekoz-tiempos
Version:        0.1.1
Release:        6%{?dist}
Summary:        Simple app for calculate difference between two dates

Group:          Applications/Productivity
License:        GPLv2
URL:            http://github.com/Hamekoz/hamekoz-tiempos
Source0:        https://elsupergomez.fedorapeople.org/src/%{name}-%{version}.tar.gz

BuildRequires:  mono-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  desktop-file-utils

%description
Calculate differences or time laps between two dates in
days, weeks, months and years

%prep
%setup -q


%build
%configure --libdir=/usr/lib
make


%install
make install DESTDIR=%{buildroot}

desktop-file-install                                    \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_prefix}/lib/%{name}/%{name}.desktop

install -m 644 bin/Release/hamekoz-tiempos.exe %{buildroot}%{_prefix}/lib/%{name}/

%files
%doc LICENSE
%{_bindir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/%{name}.exe
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Feb 12 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-6
- Change source url.

* Sun Dec 28 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-5
- Fixes for F21

* Wed Aug 20 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-4
- Clean innecesary line

* Wed Jun 25 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-3
- Reactive debug package

* Mon Apr 07 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-2
- Use consistently macros
- Owner hamekoz-tiempos directory

* Mon Apr 07 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.1-1
- Use make_install macro
- Added licence file
- Clean Requieres

* Thu Apr 03 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1.0-1
- First package
