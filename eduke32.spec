#
# spec file for package eduke32
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
%define revision 4593

Name:           eduke32
Version:        20140907
Release:        4593
Summary:        Source port of Duke Nukem 3D
License:        GPL-2.0
Group:          Amusements/Games/3D/Shoot
Url:            http://www.eduke32.com/
Source0:        eduke32_src_20140907-4593.tar.xz
Source1:        eduke32_32x32.png
Source2:        eduke32_48x48.png
Source3:        eduke32_64x64.png
Source4:        eduke32_128x128.png
Source5:        eduke32.desktop
Source6:        eduke32-demo-install.sh
# Not really source just to be referenced by spec
Source7:        download_latest_svn
Source8:        eduke32-demo-install.1
Requires:       eduke32_engine = %{version}
#Recommends:     eduke32-gui
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# packaged
# SVN_INFO_START
# Path: eduke32
# URL: https://eduke32.svn.sourceforge.net/svnroot/eduke32/polymer/eduke32
# Repository Root: https://eduke32.svn.sourceforge.net/svnroot/eduke32
# Repository UUID: 1a8010ca-5511-0410-912e-c29ae57300e0
# Revision: 1992
# Node Kind: directory
# Last Changed Author: hendricks266
# Last Changed Rev: 1992
# Last Changed Date: 2011-08-27 07:08:31 +0200 (Sat, 27 Aug 2011)
# 
# SVN_INFO_END

Requires:       SDL2
Requires:       SDL2_mixer
Requires:       flac
Requires:       eduke32_engine = %{version}
BuildRequires:  nasm
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libpng-devel
BuildRequires:  libvpx-devel
BuildRequires:  gtk2-devel
BuildRequires:  flac-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  help2man
BuildRequires:  shared-mime-info

%description
EDuke32 is a source port of the classic PC first person shooter Duke Nukem 3D - Duke3D for short
to Windows, Linux and OS X, which adds a ton of awesome features and
upgrades for regular players and an arsenal of editing functions and
scripting extensions for mod authors and map makers.

%package gui
Summary:        Eduke32 GUI game
Group:          Amusements/Games/3D/Shoot
Requires:       eduke32 = %{version}
Provides:       eduke32_engine = %{version}

%description gui
Eduke32 package with nice simple GTK loader

%package console
Summary:        Eduke32 Console game
Group:          Amusements/Games/3D/Shoot
Requires:       eduke32 = %{version}
Provides:       eduke32_engine = %{version}

%description console
Classic console Eduke32 without GUI launcher

%package mapeditor
Summary:        Eduke32 map editor
Group:          Amusements/Games/3D/Shoot

%description mapeditor
Eduke32 maps editor based on BUILD engine

%prep
%setup -q -n %{name}_%{version}-%{release}
cp %{S:1} .
cp %{S:2} .
cp %{S:3} .
cp %{S:4} .
cp %{S:5} .
cp %{S:6} .
cp %{S:8} .

%build
CFLAGS="%optflags"
export CFLAGS
make HAVE_GTK2=1 RELEASE=1 PRETTY_OUTPUT=0 %{?_smp_mflags}
mv eduke32 eduke32-gui
mv mapster32 mapster32-gui
make veryclean
make HAVE_GTK2=0 RELEASE=1 PRETTY_OUTPUT=0 %{?_smp_mflags}
mv eduke32 eduke32-console
mv mapster32 mapster32-console
touch eduke32
touch mapster32

dos2unix buildlic.txt
# How to make man page :)
function gen_man () {
	B=$1
	echo "#!/bin/sh" > $B.sh
	echo "cat << EOF" >> $B.sh
	DISPLAY= ./$B --help </dev/null |sed -e 's/^-/ -/g' |grep -v "Application parameter" >> $B.sh
	chmod 755 $B.sh
	help2man -N ./$B.sh |gzip -9 - > $B.1.gz
}
gen_man eduke32-gui
gen_man eduke32-console
gen_man mapster32-gui
gen_man mapster32-console

gzip -9f - </dev/null >eduke32.1.gz
gzip -9f - </dev/null >mapster32.1.gz

gzip -9 eduke32-demo-install.1

%install
# ghost version of files...
install -Dm 0755 eduke32 %{buildroot}%{_bindir}/eduke32
install -Dm 0755 mapster32 %{buildroot}%{_bindir}/mapster32
# shareware demo installer script
install -Dm 0755 eduke32-demo-install.sh %{buildroot}%{_bindir}/eduke32-demo-install
# gui versions of game engine
install -Dm 0755 eduke32-gui %{buildroot}%{_bindir}/eduke32-gui
install -Dm 0755 mapster32-gui %{buildroot}%{_bindir}/mapster32-gui
# console versions of game engine
install -Dm 0755 mapster32-console %{buildroot}%{_bindir}/mapster32-console
install -Dm 0755 eduke32-console %{buildroot}%{_bindir}/eduke32-console
# data files and help files for editor
install -Dm 0644 SEHELP.HLP %{buildroot}%{_datadir}/games/eduke32/sehelp.hlp
install -Dm 0644 STHELP.HLP %{buildroot}%{_datadir}/games/eduke32/sthelp.hlp
install -Dm 0644 m32help.hlp %{buildroot}%{_datadir}/games/eduke32/m32help.hlp
install -Dm 0644 tiles.cfg %{buildroot}%{_datadir}/games/eduke32/tiles.cfg
install -Dm 0644 eduke32_32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eduke32.png
install -Dm 0644 eduke32_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/eduke32.png
install -Dm 0644 eduke32_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/eduke32.png
install -Dm 0644 eduke32_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/eduke32.png
# generated man pages...
# ghosts
install -Dm 0644 eduke32.1.gz %{buildroot}%{_mandir}/man1/eduke32.1.gz
install -Dm 0644 mapster32.1.gz %{buildroot}%{_mandir}/man1/mapster32.1.gz
# real files
install -Dm 0644 eduke32-gui.1.gz %{buildroot}%{_mandir}/man1/eduke32-gui.1.gz
install -Dm 0644 eduke32-console.1.gz %{buildroot}%{_mandir}/man1/eduke32-console.1.gz
install -Dm 0644 mapster32-gui.1.gz %{buildroot}%{_mandir}/man1/mapster32-gui.1.gz
install -Dm 0644 mapster32-console.1.gz %{buildroot}%{_mandir}/man1/mapster32-console.1.gz
install -Dm 0644 eduke32-demo-install.1.gz %{buildroot}%{_mandir}/man1/eduke32-demo-install.1.gz
desktop-file-install eduke32.desktop --dir=%{buildroot}/%{_datadir}/applications/

# on sle 11 it simply does not work for some reason...
%if 0%{?sles_version} > 11

%post
%desktop_database_post

%postun
%desktop_database_postun

%endif

%post gui
%{_sbindir}/update-alternatives --install %{_bindir}/eduke32 eduke32 %{_bindir}/eduke32-gui 11 \
	--slave %{_mandir}/man1/eduke32.1.gz eduke32.1.gz %{_mandir}/man1/eduke32-gui.1.gz

%post console
%{_sbindir}/update-alternatives --install %{_bindir}/eduke32 eduke32 %{_bindir}/eduke32-console 11 \
        --slave %{_mandir}/man1/eduke32.1.gz eduke32.1.gz %{_mandir}/man1/eduke32-console.1.gz    

%post mapeditor
%{_sbindir}/update-alternatives --install %{_bindir}/mapster32 mapster32 %{_bindir}/mapster32-gui 12 \
	--slave %{_mandir}/man1/mapster32.1.gz mapster32.1.gz %{_mandir}/man1/mapster32-gui.1.gz

%{_sbindir}/update-alternatives --install %{_bindir}/mapster32 mapster32 %{_bindir}/mapster32-console 11 \
	--slave %{_mandir}/man1/mapster32.1.gz mapster32.1.gz %{_mandir}/man1/mapster32-console.1.gz

%preun console
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove eduke32 %{_bindir}/eduke32-console
fi

%preun mapeditor
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove mapster32 %{_bindir}/mapster32-gui
fi

%preun gui
if [ "$1" = 0 ] ; then
        %{_sbindir}/update-alternatives --remove eduke32 %{_bindir}/eduke32-gui
fi

%files
%defattr(-,root,root,-)
%{_bindir}/eduke32-demo-install
%dir %{_datadir}/games/eduke32/
%{_datadir}/games/eduke32/m32help.hlp
%{_datadir}/games/eduke32/sehelp.hlp
%{_datadir}/games/eduke32/sthelp.hlp
%{_datadir}/games/eduke32/tiles.cfg
%doc ChangeLog.html ChangeLog buildlic.txt
%{_datadir}/icons/hicolor/32x32/apps/eduke32.png
%{_datadir}/icons/hicolor/48x48/apps/eduke32.png
%{_datadir}/icons/hicolor/64x64/apps/eduke32.png
%{_datadir}/icons/hicolor/128x128/apps/eduke32.png
%{_datadir}/applications/eduke32.desktop
%{_mandir}/man1/eduke32-demo-install.1.gz

%files console
%defattr(-,root,root,-)
%ghost %{_bindir}/eduke32
%ghost %{_mandir}/man1/eduke32.1.gz
%attr(-,root,root) %{_bindir}/eduke32-console
%attr(-,root,root) %{_mandir}/man1/eduke32-console.1.gz

%files gui
%defattr(-,root,root,-)
%ghost %{_bindir}/eduke32
%ghost %{_mandir}/man1/eduke32.1.gz
%attr(-,root,root) %{_bindir}/eduke32-gui
%attr(-,root,root) %{_mandir}/man1/eduke32-gui.1.gz

# both versions of editor are packed but only GUI one is preffered but can be changed
# with use of update-alternatives

%files mapeditor
%defattr(-,root,root,-)
%ghost %{_bindir}/mapster32
%ghost %{_mandir}/man1/mapster32.1.gz
%attr(-,root,root) %{_bindir}/mapster32-gui
%attr(-,root,root) %{_bindir}/mapster32-console
%attr(-,root,root) %{_mandir}/man1/mapster32-gui.1.gz
%attr(-,root,root) %{_mandir}/man1/mapster32-console.1.gz

%changelog
* Sat Aug 27 2011 boris@steki.net
- updated package to 2.0.0 rev 1992
  a lot of fixes
  some highlights
  Engine stuff:
  * Polymer light access to m32script (light[<lightidx>].<field>). As an application, provide a state 'insertlights' that takes the currently active lights and puts them into the map as SEs (e.g. for maphack recovery).
  * Prototype of a mechanism to gray out certain portion of a map, making them inactive to various, but not all, editing operations. Highlighting a set of sectors and pressing Ctrl-R will make the Z bounds be [(least ceiling z), (greatest floor z)] of all selected ones, pressing Ctrl-R when no sectors are highlighted will reset them. Not sure if it's for production use at this stage...
  * The 'align walls' feature [.] now has three independently toggleable behaviours: recurse nextwalls (toggled when Ctrl is pressed), iterate point2s (disabled when Shift is pressed), and also copy pixel width (toggled when Alt is pressed).
  * Make shades clamp instead of overflowing in the editor
  * Add 'r_shadescale_unbounded' cvar. When set to 0, OpenGL renderers should never
    draw completely black objects (currently only implemented for Polymost)
  * sector-like sprite clipping now works with x- xor y-flipped actual sprites
  Mapster32:
  * Add 'r_shadescale' to config
  * In 3D mode, make SPACE behave the same as holding down a mose button: the
    currently pointed-at object is locked. Required some modification of a.m32
    to play well (i.e. not reset SPACE). This is useful by itself but more so
    in conjunction with the next point
  * make Alt behave as a modifier with PGUP/PGDN: when aiming at a 2-sided wall,
    move the other side's sector's ceiling or floor (only this is new).
  * Auto-alignment of walls can be controlled in a finer grained fashion now:
    When pressing '.', only the immediate neighbors get aligned. Use Ctrl-. for
    the old behaviour.
  * When inserting a point in 2D mode, auto-align the neighboring wall
  * corruption checker has been hooked up to loading/saving routines to inform/warn the user
  * also warn if mouse pointer is over corrupt wall which is shown in pink then: you should not move such a wall!
  * faster map loading by deferring polymer_loadboard to 3d mode entrance (also removes some 'glGetTexLevelParameteriv returned GL_FALSE' warnings)
  * more logical maphack light handling, the logic is still a bit dodgy though
  * some menu and misc. function fixup
  * redundancy elimination...
  API:
  * added consts various for 'char *filename' parameters
  * loadboard() now accepts bit 4 for flags (formerly 'fromwhere')
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Tue Nov  2 2010 boris@steki.net
- updated package to 2.0.0 rev 1723
  * Polymost-style HUD model support for Polymer.
    It properly displays all HRP HUD models as far as I can tell.
  * New CON commands
  * mostly multiplayer fixes among other things
  * SDL and menu joystick fixes
  * Link debug builds with -rdynamic in order to get symbol
    names when printing backtraces from the signal handler.
  * Make the "Start" button of the GTK start-up window the default
    button of the window, which means pressing Enter now works at you'd expect.
  + Lot of other bugs fixed
* Tue Jan 19 2010 boris@steki.net
- Added demo files installation script called
  eduke32-demo-install which will download package
  extract it and show its license to user and force
  him to accept terms within
* Tue Jan 19 2010 boris@steki.net
- Added obsolete tag in spec file for removing -common
  package on upgrade
* Mon Jan 18 2010 boris@steki.net
- Removed -common package as it was unnecessary and
  was just confusing
* Sat Jan 16 2010 boris@steki.net
- Added Desktop integration files and icons
* Sat Jan 16 2010 boris@steki.net
- Packages for gui,console and mapeditor are created
  so now it can be selected on install or after can
  be changed with use of update-alternatives
* Fri Jan 15 2010 boris@steki.net
- Created inital rpm package from svn export
