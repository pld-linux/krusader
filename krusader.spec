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
Version:	2.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	144af281a102f00847cbd598319d9a50
URL:		http://www.krusader.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Suggests:	arj
Suggests:	bzip2
Suggests:	cfv
Suggests:	coreutils
Suggests:	dpkg
Suggests:	gzip
Suggests:	kde4-kdesdk-kompare
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
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}


%find_lang %{name} --with-kde

# locolor icons are deprecated (see kde .spec-s)
rm -f $RPM_BUILD_ROOT%{_iconsdir}/locolor/*/apps/*.png

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/krusader
%{_libdir}/qt5/plugins/kf5/kio/kio_iso.so
%{_libdir}/qt5/plugins/kf5/kio/kio_krarc.so
%{_sysconfdir}/xdg/kio_isorc
%{_datadir}/metainfo/org.kde.krusader.appdata.xml
%{_datadir}/krusader
%{_datadir}/kxmlgui5/krusader
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/krusader.1*
%lang(ca) %{_mandir}/ca/man1/krusader.1*
%lang(de) %{_mandir}/de/man1/krusader.1*
%lang(it) %{_mandir}/it/man1/krusader.1*
%lang(nl) %{_mandir}/nl/man1/krusader.1*
%lang(pt) %{_mandir}/pt/man1/krusader.1*
%lang(sv) %{_mandir}/sv/man1/krusader.1*
%lang(uk) %{_mandir}/uk/man1/krusader.1*
