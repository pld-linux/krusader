Summary:	Krusader is a filemanager for KDE 3
Summary(pl):	Krusader jest zarz±dc± plików dla KDE 3
Name:		krusader
Version:	1.11
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://krusader.sourceforge.net
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Krusader is a filemanager for KDE 3, patterned after old-school managers like
midnight commander and norton commander. It features basically all your
file-management needs, plus extensive archive handling, mounted filesystems
support, ftp and much much more.  It is (almost) completely customizable, very
user friendly, fast and damn good looking :-). You should give it a try.

%description -l pl
Krusader jest zarz±dc± plików dla KDE 3, wzorowanym na takich zarz±dcach "starej
szko³y", jak Midnight Commander czy Norton Commander. Zaspokaja w zasadzie
wszystkie podstawowe potrzeby w zarz±dzaniu plików, dodatkowo obs³uguje archiwa,
montowanie systemów plików, ftp i o wiele, wiele wiêcej. Jest (prawie) ca³kowicie
ustawialny, bardzo przyjazny dla u¿ytkownika, szybki i cholernie ³adny :-). Powiniene¶
go wypróbowaæ.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/bin/krusader
%{_applnkdir}/Utilities/krusader.desktop
%{_prefix}/share/apps/krusader/icons/hicolor/16x16/actions/*
%{_prefix}/share/apps/krusader/icons/hicolor/22x22/actions/*
%{_prefix}/share/apps/krusader/icons/hicolor/32x32/actions/*
%{_prefix}/share/apps/krusader/konfig_small.jpg
%{_prefix}/share/apps/krusader/about.png
%{_prefix}/share/apps/krusader/krusaderui.rc
/usr/share/doc/kde/HTML/en/krusader/*
%{_pixmapsdir}/hicolor/32x32/apps/krusader2.png
%{_pixmapsdir}/hicolor/32x32/apps/krusader.png
%{_pixmapsdir}/locolor/16x16/apps/krusader.png
%{_prefix}/share/locale/cs/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/de/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/dk/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/es/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/fr/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/pl/LC_MESSAGES/krusader.mo
%{_prefix}/share/locale/sv/LC_MESSAGES/krusader.mo
%{_prefix}/share/mimelnk/application/x-ace.desktop
