Summary:	DevHelp book: gdb
Summary(pl):	Ksi±¿ka do DevHelp'a o gdb
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

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gdb

%description -l pl
Ksi±¿ka do DevHelp o gdb

%prep
%setup -q -c gdb-5.0 -n gdb-5.0

%build
mv -f book gdb-5.0
mv -f book.devhelp gdb.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gdb.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gdb-5.0/* $RPM_BUILD_ROOT%{_prefix}/books/gdb-5.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
