%global commit 67612cd00452b07c83e914e0fcb9d5b4ecddf577
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     gstreamer-sharp
Version:  1.3.91
Release:  1.20150302git%{shortcommit}%{?dist}
Summary:  gstreamer bindings for mono

License:  GPL
Group:    Development/Languages
URL:      http://gstreamer.freedesktop.org
#Source0:	http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.gz
Source0:  https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gtk-sharp3-devel
BuildRequires:  gio-sharp-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  libtool
BuildRequires:  monodoc-devel
Requires:       mono-core
Requires:       gstreamer1

%description
GStreamer C sharp bindings.

%prep
%setup -qn %{name}-%{commit}
#%setup -q -c -n %{name}-%{version}
./autogen.sh

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog
* Fri Oct 17 2014 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org>
- initial version
