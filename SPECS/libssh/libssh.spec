Summary:        A package to provide libssh for mariner
Name:           libssh
Version:        0.9.5
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/cockpit-project/cockpit
Group:          Applications/Text
Vendor:         Microsoft
Distribution:   Mariner
Source0:        http://dev.azure.com/mariner-org/mariner/_git/samples/%{name}-%{version}.tar.xz

BuildRequires:  build-essential, cmake
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  krb5-devel
BuildRequires:  openssh-clients
BuildRequires:  openssh-server

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
# cd libssh-0.9.5/build
cd build
make DESTDIR=%{buildroot} install
chmod a+x /usr/include/libssh

%files
# %defattr(775,root,root,775)
/usr/include/libssh
/usr/lib64/cmake/libssh
/usr/lib64/libssh.so
/usr/lib64/libssh.so.4
/usr/lib64/libssh.so.4.8.6
/usr/lib64/pkgconfig/libssh.pc