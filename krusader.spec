Summary:	Krusader is a filemanager for KDE 3
Summary(pl):	Krusader jest zarz±dc± plików dla KDE 3
Name:		krusader
Version:	1.40
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krusader/%{name}-%{version}.tar.gz
# Source0-md5:	9fe6f4ccdd9b8a5a1ff2e331ba449ff8
Patch0:		%{name}-doc.patch
Patch1:		%{name}-gcc34.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-bogus_locale.patch
URL:		http://krusader.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	pcre-devel
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krusader is a filemanager for KDE 3, patterned after old-school
managers like midnight commander and norton commander. It features
basically all your file-management needs, plus extensive archive
handling, mounted filesystems support, ftp and much much more. It is
(almost) completely customizable, very user friendly, fast and damn
good looking :-). You should give it a try.

%description -l pl
Krusader jest zarz±dc± plików dla KDE 3, wzorowanym na takich
zarz±dcach "starej szko³y", jak Midnight Commander czy Norton
Commander. Zaspokaja w zasadzie wszystkie podstawowe potrzeby w
zarz±dzaniu plików, dodatkowo obs³uguje archiwa, montowanie systemów
plików, ftp i o wiele, wiele wiêcej. Jest (prawie) ca³kowicie
ustawialny, bardzo przyjazny dla u¿ytkownika, szybki i cholernie
³adny :-). Powiniene¶ go wypróbowaæ.

%prep
%setup -q

#%%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f po/jp.*
mv -f po/{dk,da}.po

%build
cp -f /usr/share/automake/config.sub admin
export QTDIR=%{_prefix}
export KDEDIR=%{_prefix}
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/krusader.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/krusader.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krusader
%attr(755,root,root) %{_libdir}/kde3/kio_krarc.so
%{_libdir}/kde3/kio_krarc.la
%{_datadir}/apps/krusader
%{_datadir}/services/krarc.protocol
#%%{_datadir}/mimelnk/application/x-ace.desktop # Exists in kdelibs
%{_desktopdir}/krusader.desktop
%{_iconsdir}/hicolor/32x32/apps/krusader_red.png
%{_iconsdir}/hicolor/32x32/apps/krusader.png
%{_mandir}/man1/krusader.1*
