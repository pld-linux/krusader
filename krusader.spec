#
# TODO:
# - review BRs
#
# Conditional build:
%bcond_without	libkonq		# importing the right click menu of konqueror
%bcond_with	libkjsembed	# with libkjsembed
#

Summary:	Krusader is a filemanager for KDE
Summary(pl.UTF-8):	Krusader jest zarządcą plików dla KDE
Name:		krusader
Version:	2.9.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	0304b6ed7c31436d03feaffd7e6db9f1
URL:		http://www.krusader.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules
BuildRequires:	kf6-karchive-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kbookmarks-devel
BuildRequires:	kf6-kcodecs-devel
BuildRequires:	kf6-kcompletion-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kiconthemes-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-kitemviews-devel
BuildRequires:	kf6-kjobwidgets-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-kparts-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-ktextwidgets-devel
BuildRequires:	kf6-kwallet-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	kf6-kxmlgui-devel
BuildRequires:	kf6-solid-devel
BuildRequires:	kf6-sonnet-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel
BuildRequires:	qt6-build
BuildRequires:	qt6-qmake
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sed >= 4.0
BuildRequires:	xz
BuildRequires:	zlib-devel
Suggests:	arj
Suggests:	bzip2
Suggests:	cfv
Suggests:	coreutils
Suggests:	dpkg
Suggests:	gzip
Suggests:	kdiff3
Suggests:	krename >= 3.9.1
Suggests:	lha
Suggests:	md5deep
Suggests:	p7zip
Suggests:	rar
Suggests:	tar
Suggests:	unace
Suggests:	unarj
Suggests:	unrar
Suggests:	unzip
Suggests:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	with_ccache

%description
Krusader is a filemanager for KDE, patterned after old-school managers
like midnight commander and norton commander. It features basically
all your file-management needs, plus extensive archive handling,
mounted filesystems support, FTP and much much more. It is (almost)
completely customizable, very user friendly, fast and damn good
looking :-). You should give it a try.

%description -l pl.UTF-8
Krusader jest zarządcą plików dla KDE, wzorowanym na takich zarządcach
"starej szkoły", jak Midnight Commander czy Norton Commander.
Zaspokaja w zasadzie wszystkie podstawowe potrzeby w zarządzaniu
plików, dodatkowo obsługuje archiwa, montowanie systemów plików, FTP i
o wiele, wiele więcej. Jest (prawie) całkowicie ustawialny, bardzo
przyjazny dla użytkownika, szybki i cholernie ładny :-). Powinieneś go
wypróbować.

%prep
%setup -q

%build
%cmake \
	-B build \
	-G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{name} --with-kde

# locolor icons are deprecated (see kde .spec-s)
rm -f $RPM_BUILD_ROOT%{_iconsdir}/locolor/*/apps/*.png

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/krusader
/etc/xdg/kio_isorc
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_iso.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_krarc.so
%{_desktopdir}/org.kde.krusader.desktop
%{_datadir}/krusader
%{_datadir}/kxmlgui5/krusader
%{_datadir}/metainfo/org.kde.krusader.appdata.xml
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/krusader.1*
%lang(ca) %{_mandir}/ca/man1/krusader.1*
%lang(de) %{_mandir}/de/man1/krusader.1*
%lang(it) %{_mandir}/it/man1/krusader.1*
%lang(nl) %{_mandir}/nl/man1/krusader.1*
%lang(pt) %{_mandir}/pt/man1/krusader.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/krusader.1*
%lang(sv) %{_mandir}/sv/man1/krusader.1*
%lang(uk) %{_mandir}/uk/man1/krusader.1*
