Summary:	cscope - an interactive, screen-oriented tool for browse C source
Name:		cscope
Version:	15.3
Release:	1
License:	BSD
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
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

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
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
