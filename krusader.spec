Summary:	Krusader is a filemanager for KDE 3
Summary(pl):	Krusader jest zarz±dc± plików dla KDE 3
Name:		krusader
Version:	1.30
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a4f248257f7b30d995caa4dcb014d1ca
Patch0:		%{name}-doc.patch
URL:		http://krusader.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	pcre-devel
BuildRequires:	qt-devel >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

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
%setup -q -n %{name}-%{version}
%patch -p1

%build
export QTDIR=%{_prefix}
export KDEDIR=%{_prefix}
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Applications/krusader.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Utilities/krusader.desktop

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
%{_applnkdir}/Utilities/krusader.desktop
%{_pixmapsdir}/hicolor/32x32/apps/krusader2.png
%{_pixmapsdir}/hicolor/32x32/apps/krusader.png
%{_pixmapsdir}/locolor/16x16/apps/krusader.png
%{_mandir}/man1/krusader.1*
