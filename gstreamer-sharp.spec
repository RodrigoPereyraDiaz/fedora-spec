Name:		gstreamer-sharp
Version:	0.99.0
Release:	1%{?dist}
Summary:	gstreamer bindings for mono

License:	GPL
Group:		Development/Languages
URL:		http://gstreamer.freedesktop.org
Source0:	http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	gtk-sharp3-devel
BuildRequires:	gio-sharp-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	libtool
Requires:	mono-core
Requires:	gstreamer1

%description
GStreamer C sharp bindings. 

%prep
%setup -q -c -n %{name}-%{version}
./autogen.sh

%build
#%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog
* Fri Oct 17 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org>
- initial version
