Name:		freesynd
Version:	0.6
Release:	1%{?dist}
Summary:	A free cross-platform reimplementation of the classic Bullfrog game, Syndicate

Group:		Games
License:	GLPv2
URL:		http://freesynd.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  cmake, cmake-fedora, SDL_mixer-devel
Requires:	libSDL-1.2, libSDL_mixer, libSDL_image, libpng

%description
FreeSynd is released under the GNU General Public Licence, version 2.
Thanks to Tomasz Lis for some preliminary work on the level files. His code is
used under GNU General Public Licence, version 2 or later with permission from
author.
Some code is based on "libsyndicate" library by Paul Chavent. It is
re-licensed under GNU General Public Licence, version 2. Original license
and code is located in svn source/trunk/libsyndicate/.
See the file "COPYING" for informations on this licence.
ConfigFile code is from Richard J. Wagner. For Licence information, see comments 
in files config.cpp and config.h.

%prep
%setup -q
ln -s /usr/include/SDL/SDL_mixer.h src/
ln -s /usr/include/SDL/SDL_types.h src/

%build
cmake src
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/%{name}
%{_bindir}/dump
%{_datadir}/%{name}


%changelog
