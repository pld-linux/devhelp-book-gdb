Summary:	DevHelp book: gdb
Summary(pl):	Ksi±¿ka do DevHelpa o gdb
Name:		devhelp-book-gdb
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdb.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp

%description
DevHelp book about gdb.

%description -l pl
Ksi±¿ka do DevHelpa o gdb.

%prep
%setup -q -c -n gdb-5.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gdb-5.0,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gdb.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
