Summary:	A 2-player tank game
Summary(pl.UTF-8):   2-osobowa gra, w której walczy się czołgiem
Name:		tickletankle
Version:	0.8
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://triskam.virtualave.net/tickletankle/%{name}-%{version}.tar.gz
# Source0-md5:	f64fe890c0de4ae88505b7c07dd8d12d
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://triskam.virtualave.net/tickletankle/tickletankle.html
Requires:	tk >= 8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_bindir	%{_prefix}/games

%description
A 2-player tank game that can be played locally or across the Internet
or a LAN. You can play against a human player or a computer-controlled
opponent (AI player). The objective of the game is to bomb the other
player away.

%description -l pl.UTF-8
2-osobowa gra, w której walczy się czołgiem. Grać można lokalnie,
przez Internet lub LAN. Przeciwnikiem może być człowiek, lub gracz
sterowany przez komputer. Celem gry jest zbombardowanie przeciwnika.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install %{name}.tcl $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
