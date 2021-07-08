Summary:        A package to provide cockpit for mariner
Name:           cockpit
Version:        1.0.0
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/cockpit-project/cockpit
Group:          Applications/Text
Vendor:         Microsoft
Distribution:   Mariner
Source0:        http://dev.azure.com/mariner-org/mariner/_git/samples/%{name}-%{version}.tar.gz

BuildRequires: gcc

%description
cockpit for mariner

%prep
%setup -q

%build
./autogen.sh --sysconfdir=/etc --prefix=/usr --enable-debug --disable-pcp --disable-doc
make %{?_smp_mflags}

%install
make install

%files
%defattr(-,root,root)
%{_bindir}

%changelog
* Mon Jun 15 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 1.0.0-2
- Adding 'BuildRequires' for the sake of demonstrating external, build-time dependencies.
* Wed Oct 09 2019 Jonathan Slobodzian <joslobo@microsoft.com> 1.0.0-1
- Initial version of demo package

