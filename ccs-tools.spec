%define  date 20090528

Summary:	TOMOYO Linux tools
Name:		ccs-tools
Version:	1.6.8
Release:	7
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://tomoyo.sourceforge.jp/
Source0:	http://osdn.dl.sourceforge.jp/tomoyo/27220/%{name}-%{version}-%{date}.tar.gz
Source1:	README.ccs-tools.urpmi
Source2:	tomoyo.logrotate
Source3:	tomoyo.init
Patch0:		ccs-tools-dont-use-chown.patch
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)
Requires(pre,post):	rpm-helper

%description
TOMOYO Linux is an extension for Linux to provide Mandatory Access Control
(MAC) functions. This package contains the tools needed to configure, 
activate and manage the TOMOYO Linux MAC system and policies.

%prep
%setup -qn ccstools
%apply_patches
sed -i s,"CFLAGS=","CFLAGS?=",g Makefile

%build
%setup_compile_flags
%make -s all

%install
%makeinstall -s INSTALLDIR=%{buildroot}
install -m 644 %{SOURCE1} README.install.urpmi
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tomoyo
mkdir -p %{buildroot}%{_initrddir}
install -m 700 %{SOURCE3} %{buildroot}%{_initrddir}/ccs-auditd
mkdir -p %{buildroot}%{_logdir}/tomoyo

%post
%_post_service ccs-auditd

%preun
%_preun_service ccs-auditd

%files
%doc README.install.urpmi
%{_sysconfdir}/logrotate.d/tomoyo
%attr(700,root,root) %{_initrddir}/ccs-auditd
%attr(700,root,root) /sbin/ccs-init
%attr(700,root,root) /sbin/tomoyo-init
%{_exec_prefix}/lib/ccs/
%{_sbindir}/ccs-auditd
%{_sbindir}/ccs-ccstree
%{_sbindir}/ccs-checkpolicy
%{_sbindir}/ccs-domainmatch
%{_sbindir}/ccs-editpolicy
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
%{_mandir}/man8/ccs-auditd.8*
%{_mandir}/man8/ccs-ccstree.8*
%{_mandir}/man8/ccs-checkpolicy.8*
%{_mandir}/man8/ccs-domainmatch.8*
%{_mandir}/man8/ccs-editpolicy.8*
%{_mandir}/man8/ccs-editpolicy-agent.8*
%{_mandir}/man8/ccs-findtemp.8*
%{_mandir}/man8/ccs-init.8*
%{_mandir}/man8/ccs-ld-watch.8*
%{_mandir}/man8/ccs-loadpolicy.8*
%{_mandir}/man8/ccs-notifyd.8*
%{_mandir}/man8/ccs-pathmatch.8*
%{_mandir}/man8/ccs-patternize.8*
%{_mandir}/man8/ccs-queryd.8*
%{_mandir}/man8/ccs-savepolicy.8*
%{_mandir}/man8/ccs-setlevel.8*
%{_mandir}/man8/ccs-setprofile.8*
%{_mandir}/man8/ccs-sortpolicy.8*
%{_mandir}/man8/init_policy.sh.8*
%{_mandir}/man8/tomoyo-init.8*
%{_mandir}/man8/tomoyo_init_policy.sh.8*
%{_logdir}/tomoyo/

