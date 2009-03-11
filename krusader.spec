#
# Conditional build:
%bcond_without	libkonq		# importing the right click menu of konqueror
%bcond_with	libkjsembed	# with libkjsembed
#

%define		_state		beta2

Summary:	Krusader is a filemanager for KDE
Summary(pl.UTF-8):	Krusader jest zarządcą plików dla KDE
Name:		krusader
Version:	2.0.0
Release:	0.%{_state}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krusader/%{name}-%{version}-%{_state}.tar.gz
# Source0-md5:	88805a863dc51bf723a6307173f7f044
Patch0:		%{name}-desktop.patch
#Patch2: %{name}-mount.patch
URL:		http://krusader.sourceforge.net/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtSvg-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
%{?with_libkonq:BuildRequires:	kde4-kdebase-devel}
%{?with_libkjsembed:BuildRequires:	kde4-kdebindings-kjsembed-devel}
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Suggests:	bzip2
Suggests:	cfv
Suggests:	coreutils
Suggests:	dpkg
Suggests:	gzip
Suggests:	kdiff3
Suggests:	kde4-kdesdk-kompare
Suggests:	krename >= 3.9.1
Suggests:	lha
Suggests:	md5deep
Suggests:	p7zip
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
%setup -q -n %{name}-%{version}-%{_state}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%doc AUTHORS ChangeLog FAQ README doc/actions_tutorial.txt
%attr(755,root,root) %{_bindir}/krusader
%attr(755,root,root) %{_libdir}/kde4/*.so
%{_datadir}/apps/krusader
%{_datadir}/config/kio_isorc
%{_datadir}/kde4/services/*.protocol
%{_desktopdir}/kde4/*.desktop
%{_iconsdir}/hicolor/*/*
