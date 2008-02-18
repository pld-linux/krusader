#
# Conditional build:
%bcond_without	libkonq		# importing the right click menu of konqueror
%bcond_without	libkjsembed	# with libkjsembed
#
Summary:	Krusader is a filemanager for KDE 3
Summary(pl.UTF-8):	Krusader jest zarządcą plików dla KDE 3
Name:		krusader
Version:	1.80.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krusader/%{name}-%{version}.tar.gz
# Source0-md5:	32bfaf4de7ca62e0f612357f4aa065a9
Patch0:		kde-ac260-lt.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-mount.patch
URL:		http://krusader.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_libkonq:BuildRequires:	kdebase-devel}
%{?with_libkjsembed:BuildRequires:	kdebindings-kjsembed-devel}
BuildRequires:	kdelibs-devel >= 3.5.0-4
BuildRequires:	qt-devel >= 6:3.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	with_ccache

%description
Krusader is a filemanager for KDE 3, patterned after old-school
managers like midnight commander and norton commander. It features
basically all your file-management needs, plus extensive archive
handling, mounted filesystems support, FTP and much much more. It is
(almost) completely customizable, very user friendly, fast and damn
good looking :-). You should give it a try.

%description -l pl.UTF-8
Krusader jest zarządcą plików dla KDE 3, wzorowanym na takich
zarządcach "starej szkoły", jak Midnight Commander czy Norton
Commander. Zaspokaja w zasadzie wszystkie podstawowe potrzeby w
zarządzaniu plików, dodatkowo obsługuje archiwa, montowanie systemów
plików, FTP i o wiele, wiele więcej. Jest (prawie) całkowicie
ustawialny, bardzo przyjazny dla użytkownika, szybki i cholernie ładny
:-). Powinieneś go wypróbować.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
cp -f /usr/share/automake/config.sub admin
export QTDIR=%{_prefix}
export KDEDIR=%{_prefix}
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-kiotar \
	%{!?with_libkonq:--without-konqueror} \
	%{!?with_libkjsembed:--without-javascript} \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applications/kde/krusader.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/krusader.desktop
mv -f $RPM_BUILD_ROOT%{_datadir}/applications/kde/krusader_root-mode.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/krusader_root-mode.desktop
%find_lang %{name} --with-kde

# locolor icons are deprecated (see kde .spec-s)
rm -f $RPM_BUILD_ROOT%{_iconsdir}/locolor/*/apps/*.png

# confilicts with krusader
rm $RPM_BUILD_ROOT%{_libdir}/kde3/kio_tar.so

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO doc/actions_tutorial.txt
%attr(755,root,root) %{_bindir}/krusader
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/krusader
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop
%{_datadir}/config/kio_isorc
%{_datadir}/services/*.protocol
%{_desktopdir}/krusader*.desktop
%{_iconsdir}/crystalsvg/*/apps/*.png
%{_mandir}/man1/krusader.1*
