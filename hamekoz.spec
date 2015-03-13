Name:           hamekoz
Version:        0.1
Release:        1%{?dist}
Summary:        Librerias de codigo compartido

Group:          Applications/Productivity
License:        GPLv2
URL:            http://github.com/Hamekoz/hamekoz-tiempos
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  mono-devel
BuildRequires:  gtk-sharp2-devel

%description
Calculate differences or time laps between two dates in
days, weeks, months and years

%package devel
Summary:        Development tools for Hamekoz
Group:          Development/Languages
Requires:       hamekoz = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package completes the Hamekoz.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc
%{_libdir}/hamekoz/Hamekoz.Data.dll
%{_libdir}/hamekoz/Hamekoz.Data.dll.mdb
%{_libdir}/hamekoz/Hamekoz.Hasar.dll
%{_libdir}/hamekoz/Hamekoz.Hasar.dll.mdb
%{_libdir}/hamekoz/Hamekoz.Interfaces.dll
%{_libdir}/hamekoz/Hamekoz.Interfaces.dll.mdb
%{_libdir}/hamekoz/Hamekoz.Reportes.dll
%{_libdir}/hamekoz/Hamekoz.Reportes.dll.mdb
%{_libdir}/hamekoz/Hamekoz.UI.Gtk.dll
%{_libdir}/hamekoz/Hamekoz.UI.Gtk.dll.mdb
%{_libdir}/hamekoz/Hamekoz.UI.WinForm.dll
%{_libdir}/hamekoz/Hamekoz.UI.WinForm.dll.mdb
%{_libdir}/hamekoz/itextsharp.dll

%files devel
%{_libdir}/pkgconfig/hamekoz.data.pc
%{_libdir}/pkgconfig/hamekoz.hasar.pc
%{_libdir}/pkgconfig/hamekoz.interfaces.pc
%{_libdir}/pkgconfig/hamekoz.reportes.pc
%{_libdir}/pkgconfig/hamekoz.ui.gtk.pc
%{_libdir}/pkgconfig/hamekoz.ui.winform.pc

%changelog

* Thu Apr 03 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 0.1-1
- First package
