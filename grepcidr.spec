Summary:	IP addresses grep
Name:		grepcidr
Version:	1.3
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
# Source0-md5:	7ccade25ce9fe6d6a02348ba8e4cf4a3
Patch0:		makefile.diff
Patch1:		find-anywhere.diff
Patch2:		regex.diff
URL:		http://www.pc-tools.net/unix/grepcidr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filter IP addresses matching IPv4 CIDR/network specification.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
