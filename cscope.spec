Summary:	cscope - an interactive, screen-oriented tool for browse C source
Summary(pl):	cscope - interaktywny program do przeszukiwania kodu w j�zyku C
Name:		cscope
Version:	15.3
Release:	2
License:	BSD
Group:		Development/Tools
Source0:	ftp://download.sourceforge.net/pub/sourceforge/cscope/%{name}-%{version}.tar.gz
URL:		http://cscope.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	ncurses-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cscope is an interactive, screen-oriented tool that allows the user to
browse through C source files for specified elements of code.

%description -l pl
cscope jest interaktywnym, pe�noekranowym narz�dziem, kt�re pozwala
u�ytkownikowi na przeszukiwanie plik�w z kodem w j�zyku C pod wzgl�dem
okre�lonych element�w.

%prep
%setup -q

%build
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf TODO ChangeLog AUTHORS README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
