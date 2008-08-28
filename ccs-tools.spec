Summary: TOMOYO Linux tools
%define  date 20080715
%define  ver  1.6.3

Name: 	 ccs-tools
Version: 1.6.3
Release: %mkrel 1
License: GPLv2
URL:	 http://tomoyo.sourceforge.jp/
Group:	 System/Kernel and hardware
BuildRequires: ncurses-devel
BuildRequires: readline-devel
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
#NoSource: 0

Source0: http://osdn.dl.sourceforge.jp/tomoyo/27220/ccs-tools-%{ver}-%{date}.tar.gz
Source1: README.ccs-tools.urpmi
Source2: tomoyo.logrotate
Source3: tomoyo.init
Patch0:  ccs-tools-dont-use-chown.patch

%description
TOMOYO Linux is an extension for Linux to provide Mandatory Access Control
(MAC) functions. This package contains the tools needed to configure, 
activate and manage the TOMOYO Linux MAC system and policies.

%prep
%setup -q -n ccstools
%patch0 -p1 

%build
%make -s all

%install
rm -rf %{buildroot}
%makeinstall -s INSTALLDIR=%{buildroot}
install -m 644 %{SOURCE1} README.install.urpmi
mkdir -p %{buildroot}%{_sysconfdir}/ccs/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tomoyo
mkdir -p %{buildroot}%{_initrddir}
install -m 700 %{SOURCE3} %{buildroot}%{_initrddir}/ccs-auditd
mkdir -p %{buildroot}%{_logdir}/tomoyo

%clean
rm -rf %{buildroot}

%post
%_post_service ccs-auditd

%preun
%_preun_service ccs-auditd

%files
%defattr(-,root,root)
%attr(700,root,root) %{_sysconfdir}/ccs/
%{_sysconfdir}/logrotate.d/tomoyo
%attr(700,root,root) %{_initrddir}/ccs-auditd
%attr(700,root,root) /sbin/ccs-init
%attr(700,root,root) /sbin/tomoyo-init
/usr/lib/ccs/
%attr(4755,root,root) /usr/lib/ccs/misc/proxy
%attr(4755,root,root) /usr/lib/ccs/misc/force-logout
%{_sbindir}/ccs-auditd
%{_sbindir}/ccs-ccstree
%{_sbindir}/ccs-checkpolicy
%{_sbindir}/ccs-domainmatch
%{_sbindir}/ccs-editpolicy
%{_sbindir}/ccs-editpolicy_offline
%{_sbindir}/ccs-findtemp
%{_sbindir}/ccs-ld-watch
%{_sbindir}/ccs-loadpolicy
%{_sbindir}/ccs-pathmatch
%{_sbindir}/ccs-patternize
%{_sbindir}/ccs-queryd
%{_sbindir}/ccs-savepolicy
%{_sbindir}/ccs-setlevel
%{_sbindir}/ccs-setprofile
%{_sbindir}/ccs-sortpolicy
%{_mandir}/man8/ccs-auditd.8.lzma
%{_mandir}/man8/ccs-ccstree.8.lzma
%{_mandir}/man8/ccs-checkpolicy.8.lzma
%{_mandir}/man8/ccs-domainmatch.8.lzma
%{_mandir}/man8/ccs-editpolicy.8.lzma
%{_mandir}/man8/ccs-findtemp.8.lzma
%{_mandir}/man8/ccs-init.8.lzma
%{_mandir}/man8/ccs-ld-watch.8.lzma
%{_mandir}/man8/ccs-loadpolicy.8.lzma
%{_mandir}/man8/ccs-notifyd.8.lzma
%{_mandir}/man8/ccs-pathmatch.8.lzma
%{_mandir}/man8/ccs-patternize.8.lzma
%{_mandir}/man8/ccs-queryd.8.lzma
%{_mandir}/man8/ccs-savepolicy.8.lzma
%{_mandir}/man8/ccs-setlevel.8.lzma
%{_mandir}/man8/ccs-setprofile.8.lzma
%{_mandir}/man8/ccs-sortpolicy.8.lzma
%{_mandir}/man8/init_policy.sh.8.lzma
%{_mandir}/man8/tomoyo-init.8.lzma
%{_mandir}/man8/tomoyo_init_policy.sh.8.lzma
%{_logdir}/tomoyo/
%doc README.install.urpmi
