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
BuildRequires:  meson, ninja-build, gettext, glib-devel

%define _unpackaged_files_terminate_build 0

%description
json-glib

%prep
%setup -q
mkdir -p %{buildroot}/usr/lib/pkgconfig/

%build
meson _build .
cd _build
ninja

%install
cd _build
DESTDIR=%{buildroot} meson install
ln -s %{buildroot}/usr/local/lib/pkgconfig/json-glib-1.0.pc %{buildroot}/usr/lib/pkgconfig/json-glib-1.0.pc
ln -s %{buildroot}/usr/local/lib/libjson-glib-1.0.so.0 %{buildroot}/usr/lib/libjson-glib-1.0.so.0
ln -s %{buildroot}/usr/local/lib/libjson-glib-1.0.so %{buildroot}/usr/lib/libjson-glib-1.0.so

%files
# %defattr(775,root,root,775)
/usr/local/lib/pkgconfig/json-glib-1.0.pc
/usr/lib/pkgconfig/json-glib-1.0.pc
/usr/local/lib/libjson-glib-1.0.so
/usr/lib/libjson-glib-1.0.so
/usr/local/lib/libjson-glib-1.0.so
/usr/lib/libjson-glib-1.0.so.0
/usr/local/bin/json-glib-format
/usr/local/bin/json-glib-validate
/usr/local/lib/libjson-glib-1.0.so.0.600.3
/usr/local/include/json-glib-1.0
/usr/local/libexec/installed-tests/json-glib-1.0
/usr/local/share/installed-tests/json-glib-1.0