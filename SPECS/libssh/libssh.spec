Summary:        A package to provide cockpit for mariner
Name:           cockpit
Version:        0.9.5
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/cockpit-project/cockpit
Group:          Applications/Text
Vendor:         Microsoft
Distribution:   Mariner
Source0:        http://dev.azure.com/mariner-org/mariner/_git/samples/%{name}-%{version}.tar.xz

BuildRequires:  build-essential
BuildRequires:  gettext

%description
libssh

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr .. 
make

%install
make install
chmod a+x /usr/include/libssh

%files
%license LICENSE

%changelog
* Fri July 09 2021 Shane Guan <shaneguan@microsoft.com> 1.0.0-1
- Initial version of libssh package

