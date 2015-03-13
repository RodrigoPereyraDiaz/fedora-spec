Name:		mysql-connector-net
Version:	6.9.5
Release:	1%{?dist}
Summary:	Mono ADO.NET driver for MySql

Group:		Development/Languages
License:	GPLv2
URL:		http://dev.mysql.com/downloads/connector/net/
Source0:	http://cdn.mysql.com/Downloads/Connector-Net/%{name}-%{version}-noinstall.zip

Requires:	mono-data

%description
Connector/Net is a fully-managed ADO.NET driver for MySQL.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_prefix}/lib/mono/2.0/
mkdir -p %{buildroot}/%{_prefix}/lib/mono/4.0/
mkdir -p %{buildroot}/%{_prefix}/lib/mono/4.5/

install -m 644 v2.0/MySql.Data.dll %{buildroot}%{_prefix}/lib/mono/2.0/
install -m 644 v4.0/MySql.Data.dll %{buildroot}%{_prefix}/lib/mono/4.0/
install -m 644 v4.5/MySql.Data.dll %{buildroot}%{_prefix}/lib/mono/4.5/

gacutil -i v4.0/MySql.Data.dll -f -package mysql-connector-net -root %{buildroot}/%{_prefix}/lib/mono/gac
#gacutil -i v4.0/MySql.Data.Entity.dll -f -package mysql-connector-net -root %{buildroot}/%{_prefix}/lib/mono/gac
#gacutil -i v4.0/MySql.Web.dll -f -package mysql-connector-net -root %{buildroot}/%{_prefix}/lib/mono/gac

%files
%doc CHANGES COPYING README
%{_prefix}/lib/mono/gac/*
#%{_prefix}/lib/mono/mysql-net-connector/*
%{_prefix}/lib/mono/?.?/*

%changelog
* Thu Nov 21 2013 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 6.7.4-1
- Initial packaging
