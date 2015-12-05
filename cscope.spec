Summary:	cscope - an interactive, screen-oriented tool for browse C source
Summary(pl.UTF-8):	cscope - interaktywny program do przeszukiwania kodu w języku C
Name:		cscope
Version:	15.6
Release:	3
License:	BSD
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/cscope/%{name}-%{version}.tar.gz
# Source0-md5:	db87833f90d8267b1fc0c419cfc4d219
Patch0:		%{name}-CVE-2004-2541.patch
URL:		http://cscope.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cscope is an interactive, screen-oriented tool that allows the user to
browse through C source files for specified elements of code.

%description -l pl.UTF-8
cscope jest interaktywnym, pełnoekranowym narzędziem, które pozwala
użytkownikowi na przeszukiwanie plików z kodem w języku C pod względem
określonych elementów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO ChangeLog AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
