Summary:	DevHelp book: gdb
Summary(pl):	Ksi±¿ka do DevHelpa o gdb
Name:		devhelp-book-gdb
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gdb.tar.gz
# Source0-md5:	843112723f8388463848e0ac60563ced
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gdb.

%description -l pl
Ksi±¿ka do DevHelpa o gdb.

%prep
%setup -q -c -n gdb-5.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0/gdb-5.0.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
