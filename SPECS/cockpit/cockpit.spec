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
# %setup -q

%build
# ./autogen.sh --sysconfdir=/etc --prefix=/usr --enable-debug --disable-pcp --disable-doc
cd /usr/src/mariner/BUILD/cockpit-1.0.0
make %{?_smp_mflags}

%install
cd /usr/src/mariner/BUILD/cockpit-1.0.0
make install
cat > /etc/pam.d/cockpit << EOF
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
chmod -R go+rx /usr/share/cockpit
chmod o+rx /etc/cockpit

%files
%defattr(-,root,root)
%{_bindir}

%changelog
* Mon Jun 15 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 1.0.0-2
- Adding 'BuildRequires' for the sake of demonstrating external, build-time dependencies.
* Wed Oct 09 2019 Jonathan Slobodzian <joslobo@microsoft.com> 1.0.0-1
- Initial version of demo package

