#
# Conditional build:
%bcond_with	libkonq		# importing the right click menu of konqueror
%bcond_with	libkjsembed	# with libkjsembed
#
Summary:	Krusader is a filemanager for KDE 3
Summary(pl):	Krusader jest zarz±dc± plików dla KDE 3
Name:		krusader
Version:	1.60.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krusader/%{name}-%{version}.tar.gz
# Source0-md5:	95f7900799bbd2810e6ac06fbf628536
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-mount.patch
Patch2:		%{name}-gcc34.patch
URL:		http://krusader.sourceforge.net/
BuildRequires:	automake
%{?with_libkonq:BuildRequires:	kdebase-devel}
%{?with_libkjsembed:BuildRequires:	kdebindings-kjsembed-devel}
BuildRequires:	kdelibs-devel >= 3.3
BuildRequires:	qt-devel >= 3.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krusader is a filemanager for KDE 3, patterned after old-school
managers like midnight commander and norton commander. It features
basically all your file-management needs, plus extensive archive
handling, mounted filesystems support, FTP and much much more. It is
(almost) completely customizable, very user friendly, fast and damn
good looking :-). You should give it a try.

%description -l pl
Krusader jest zarz±dc± plików dla KDE 3, wzorowanym na takich
zarz±dcach "starej szko³y", jak Midnight Commander czy Norton
Commander. Zaspokaja w zasadzie wszystkie podstawowe potrzeby w
zarz±dzaniu plików, dodatkowo obs³uguje archiwa, montowanie systemów
plików, FTP i o wiele, wiele wiêcej. Jest (prawie) ca³kowicie
ustawialny, bardzo przyjazny dla u¿ytkownika, szybki i cholernie
³adny :-). Powiniene¶ go wypróbowaæ.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
#%%patch2 -p0

%build
%{!?with_libkonq:%{__sed} -i 's,have_libkonq=yes,have_libkonq=no,' configure*}
%{!?with_libkjsembed:%{__sed} -i 's,have_libkjsembed=yes,have_libkjsembed=no,' configure*}
cp -f /usr/share/automake/config.sub admin
export QTDIR=%{_prefix}
export KDEDIR=%{_prefix}
%configure \
	--disable-rpath \
	--disable-debug \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/krusader.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/krusader.desktop
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/krusader_root-mode.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/krusader_root-mode.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krusader
%attr(755,root,root) %{_libdir}/kde3/kio_krarc.so
%attr(755,root,root) %{_libdir}/kde3/kio_iso.so
%{_libdir}/kde3/kio_krarc.la
%{_libdir}/kde3/kio_iso.la
%{_datadir}/apps/krusader
%{_datadir}/services/krarc.protocol
%{_datadir}/services/iso.protocol
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop
%{_datadir}/config/kio_isorc
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man1/krusader.1*
