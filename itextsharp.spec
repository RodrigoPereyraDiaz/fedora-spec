Name:		itextsharp
Version:	5.5.2
Release:	1%{?dist}
Summary:	itextsharp

Group:		Development/Languages
License:	AGPLv3
URL:		https://github.com/itext/itextsharp
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	mono-devel
BuildRequires:	pkgconfig
Requires:		mono-core

%description

%package devel
Summary: Development files for itextsharp
Group: Development/Languages
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
%{_prefix}/lib/%{name}/%{name}.dll

%files devel
%doc
%{_libdir}/pkgconfig/%{name}.pc

%changelog

