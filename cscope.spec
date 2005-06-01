Summary:	cscope - an interactive, screen-oriented tool for browse C source
Summary(pl):	cscope - interaktywny program do przeszukiwania kodu w j�zyku C
Name:		cscope
Version:	15.5
Release:	3
License:	BSD
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/cscope/%{name}-%{version}.tar.gz
# Source0-md5:	beb6032a301bb11524aec74bfb5e4840
Patch0:		%{name}-CAN-2004-0996.patch
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

%description -l pl
cscope jest interaktywnym, pe�noekranowym narz�dziem, kt�re pozwala
u�ytkownikowi na przeszukiwanie plik�w z kodem w j�zyku C pod wzgl�dem
okre�lonych element�w.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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
