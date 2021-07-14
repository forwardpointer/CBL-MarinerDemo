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

BuildRequires:  build-essential
BuildRequires:  krb5-devel, polkit-devel, pam-devel, gnutls-devel
BuildRequires:  gettext, e2fsprogs-devel, glib-devel, systemd-devel
BuildRequires:  cmake, zlib-devel, openssl-devel
BuildRequires:  which, git, nodejs >= 14
BuildRequires:  json-glib-devel, libssh

%description
cockpit for mariner

%prep
%setup -q
mkdir -p %{buildroot}/etc/pam.d

%build
./autogen.sh --sysconfdir=/etc --prefix=/usr --enable-debug --disable-pcp --disable-doc
# npm install -g n
# n stable
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
cat > %{buildroot}/etc/pam.d/cockpit << EOF
    #%PAM-1.0 
    # this MUST be first in the "auth" stack as it sets PAM_USER 
    # user_unknown is definitive, so die instead of ignore to avoid subsequent modules mess up the error code 
    -auth      [success=done new_authtok_reqd=done user_unknown=die default=ignore]   pam_cockpit_cert.so 
    auth       substack     system-auth 
    auth       optional     pam_ssh_add.so 
    account    required     pam_nologin.so 
    account    include      system-account 
    password   include      system-password 
    session    required     pam_loginuid.so 
    session    optional     pam_keyinit.so force revoke 
    session    optional     pam_ssh_add.so 
    session    include      system-session 
EOF
chmod -R go+rx %{buildroot}/usr/share/cockpit
chmod o+rx %{buildroot}/etc/cockpit

%files
# %defattr(-,root,root)
/usr/share/cockpit
/etc/cockpit
/etc/pam.d/cockpit
/usr/share/metainfo/*cockpit*.xml
/usr/share/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy
/usr/share/pixmaps/cockpit*.png
/usr/lib/tmpfiles.d/cockpit-tempfiles.conf
/lib/systemd/system/cockpit*.socket
/lib/systemd/system/cockpit*.service
/lib/systemd/system/system-cockpithttps.slice

# %files
# %license LICENSE

# %changelog
# * Fri July 09 2021 Shane Guan <shaneguan@microsoft.com> 1.0.0-1
# - Initial version of cockpit package

