Summary:	Krusader is a filemanager for KDE 3
Summary(pl):	Krusader jest zarz±dc± plików dla KDE 3
Name:		krusader
Version:	1.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3450c67d2b7d5409fe82b7436b7b7204
URL:		http://krusader.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3.0.3
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
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
mv $RPM_BUILD_ROOT%{_applnkdir}/Applications/krusader.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities/krusader.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krusader
%dir %{_datadir}/apps/krusader
%dir %{_datadir}/apps/krusader/icons
%dir %{_datadir}/apps/krusader/icons/hicolor
%dir %{_datadir}/apps/krusader/icons/hicolor/*
%dir %{_datadir}/apps/krusader/icons/hicolor/*/actions
%{_datadir}/apps/krusader/icons/hicolor/16x16/actions/*
%{_datadir}/apps/krusader/icons/hicolor/22x22/actions/*
%{_datadir}/apps/krusader/icons/hicolor/32x32/actions/*
%{_datadir}/apps/krusader/konfig_small.jpg
%{_datadir}/apps/krusader/about.png
%{_datadir}/apps/krusader/krusaderui.rc
%{_applnkdir}/Utilities/krusader.desktop
%{_pixmapsdir}/hicolor/32x32/apps/krusader2.png
%{_pixmapsdir}/hicolor/32x32/apps/krusader.png
%{_pixmapsdir}/locolor/16x16/apps/krusader.png
%{_datadir}/mimelnk/application/x-ace.desktop
