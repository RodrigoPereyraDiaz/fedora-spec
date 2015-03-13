Name:		mysql-workbench-community
Version:	6.2.4
Release:	1%{?dist}
Summary:	A MySQL visual database modeling, administration, development and migration tool

Group:		Applications/Databases
License:	GPLv2
URL:		http://wb.mysql.com
Source0:	%{name}-%{version}-src.tar.gz
Source1:    antlr-3.5.2-complete.jar

BuildRequires: cmake >= 2.8
BuildRequires: libzip-devel libxml2-devel
BuildRequires: python-devel >= 2.5
BuildRequires: boost-devel
BuildRequires: gtk2-devel >= 2.20
BuildRequires: gtkmm24-devel
BuildRequires: mesa-libGL-devel
BuildRequires: sqlite-devel
BuildRequires: make
BuildRequires: tar
BuildRequires: gcc-c++
BuildRequires: swig >= 1.3
BuildRequires: proj-devel
BuildRequires: libgnome-keyring-devel libuuid-devel tinyxml-devel vsqlite++-devel ctemplate-devel
BuildRequires: community-mysql-devel gdal-devel libiodbc-devel

#Provides: mysql-workbench = %{version}-%{release}
#Provides: mysql-workbench%{?_isa} = %{version}-%{release}

Requires: python-paramiko
Requires: gnome-keyring
Requires: proj
Requires: gtk2 >= 2.20

Obsoletes: mysql-workbench < 6.1
Conflicts: mysql-workbench-oss
Conflicts: mysql-workbench-com-se
Conflicts: mysql-workbench-gpl
Obsoletes: mysql-workbench-oss
Obsoletes: mysql-workbench-gpl
Conflicts: mysql-workbench-commercial

# Filtering: https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
%global __requires_exclude ^lib(antlr3c_wb|cdbc|grt|linux_utilities|mdcanvasgtk|mdcanvas|mforms|mysqlparser|sqlparser|sqlide|wbbase|wbpublic|wbprivate|wbscintilla|mysqlcppconn|iodbc|iodbcadm|iodbcinst|mysqlclient|gdal|wb.*|db.*)\\.so.*$
%global __requires_exclude %{__requires_exclude}|db.*)\\.so.*$
%global __requires_exclude %{__requires_exclude}|wb.*)\\.so.*$
%global __provides_exclude_from ^(%{_libdir}/mysql.workbench/.*\\.so.*|%{_libdir}/mysql/libmysqlclient\\.so.*|%{mysqlcppconn_dir}/lib/libmysqlcppconn\\.so.*|%{odbc_home}/lib/libiodbc\\.so.*)$

%description
MySQL Workbench is a unified visual tool for database architects, developers, 
and DBAs. MySQL Workbench provides data modeling, SQL development, and 
comprehensive administration tools for server configuration, user 
administration, backup, and much more. MySQL Workbench is available on 
Windows, Linux and Mac OS X.


%prep
%setup -q -n %{name}-%{version}-src
cp %{SOURCE1} .

%build
ANTLR_JAR_PATH=. cmake -DCMAKE_BUILD_TYPE=Release \
       -DREAL_EXECUTABLE_DIR=%{_libexecdir}/mysql-workbench \
       -DUSE_BUNDLED_MYSQLDUMP=1

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
#rm -fr %{buildroot}/usr/share/doc/mysql-workbench

cp -a /usr/lib64/libctemplate.so* %{buildroot}%{_libdir}/mysql-workbench

%files
%defattr(0644, root, root, 0755)
%doc COPYING README

%attr(0755,root,root) %{_bindir}/mysql-workbench
%attr(0755,root,root) %{_bindir}/wbcopytables

%dir %{_libexecdir}/mysql-workbench
%attr(0755,root,root) %{_libexecdir}/mysql-workbench/mysql-workbench-bin
%attr(0755,root,root) %{_libexecdir}/mysql-workbench/wbcopytables-bin
%attr(0755,root,root) %{_libexecdir}/mysql-workbench/iodbcadm-gtk
%attr(0755,root,root) %{_libexecdir}/mysql-workbench/mysql
%attr(0755,root,root) %{_libexecdir}/mysql-workbench/mysqldump

%{_libdir}/mysql-workbench

%{_datadir}/mysql-workbench
%attr(0755,root,root) %{_datadir}/mysql-workbench/extras/*.sh

%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime-info/*
%{_datadir}/mime/packages/*
%{_datadir}/applications/*.desktop

%changelog

