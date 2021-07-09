Summary:        A package to provide json-glib for mariner
Name:           json-glib
Version:        1.0.0
Release:        2%{?dist}
License:        MIT
URL:            https://gitlab.gnome.org/GNOME/json-glib/
Group:          Applications/Text
Vendor:         Microsoft
Distribution:   Mariner
Source0:        http://dev.azure.com/mariner-org/mariner/_git/samples/%{name}-%{version}.tar.gz

BuildRequires:  build-essential
BuildRequires:  meson, ninja, gettext

%description
json-glib

%prep
%setup -q

%build
meson _build .
cd _build
ninja
meson install

%install
meson install
ln -s /usr/local/lib/pkgconfig/json-glib-1.0.pc /usr/lib/pkgconfig/json-glib-1.0.pc
ln -s /usr/local/lib/libjson-glib-1.0.so.0 /usr/lib/libjson-glib-1.0.so.0
ln -s /usr/local/lib/libjson-glib-1.0.so /usr/lib/libjson-glib-1.0.so

%files
%license LICENSE

%changelog
* Fri July 09 2021 Shane Guan <shaneguan@microsoft.com> 1.0.0-1
- Initial version of json-glib package

