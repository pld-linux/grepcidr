Summary:	IP addresses grep
Name:		grepcidr
Version:	2.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
# Source0-md5:	228b0665d02c7767027245f9f608b4cb
URL:		http://www.pc-tools.net/unix/grepcidr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filter IP addresses matching IPv4 CIDR/network specification.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man1/*.1*
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
