Summary: TOMOYO Linux tools
%define  date 20090528
%define  ver  1.6.8

Name: 	 ccs-tools
Version: %{ver}
Release: %manbo_mkrel 5
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
%doc README.install.urpmi


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.8-3mnb2
+ Revision: 663355
- mass rebuild

* Mon Jun 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6.8-2mnb2
+ Revision: 388063
- Updated README.ccs-tools.urpmi to reference tomoyo 2.2.x which is the
  current used choice in kernel packages.

* Mon Jun 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6.8-1mnb2
+ Revision: 388044
- Updated to version 1.6.8-20090528

* Wed Apr 08 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6.7-1mnb2
+ Revision: 365157
- Updated to 1.6.7-20090401 (to match latest kernel released).
- Rediffed ccs-tools-dont-use-chown.patch

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 1.6.6-2mnb2
+ Revision: 344800
- rebuild for new libreadline

* Tue Feb 17 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.6.6-1mnb2
+ Revision: 342211
- Updated to 1.6.6-20090202

* Thu Sep 04 2008 Thomas Backlund <tmb@mandriva.org> 1.6.4-1mnb2
+ Revision: 280961
- update to 1.6.4 final
- update README.urpmi to point to the online kickstart page

* Fri Aug 29 2008 Thomas Backlund <tmb@mandriva.org> 1.6.3-3mnb2
+ Revision: 277292
- remove /etc/ccs from rpm for now as it triggers /sbin/ccs-init to start

* Thu Aug 28 2008 Thomas Backlund <tmb@mandriva.org> 1.6.3-2mnb2
+ Revision: 276867
- switch to Manbo Core release tags
- use rpm macros
- add initscript for ccs-auditd logging daemon
- fix logrotate install
- add logrotate support
- add /var/log/tomoyo/ to the rpm
- add /etc/ccs to the rpm
- spec fixes
- fix license
- add README.install.urpmi for some important info
- update description
- fix cleaning of buildroot
- fix permissions

* Mon Aug 04 2008 Thomas Backlund <tmb@mandriva.org> 1.6.3-1mdv2009.0
+ Revision: 263589
- update to 1.6.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.5.3-3mdv2009.0
+ Revision: 243443
- rebuild

* Sun Mar 02 2008 Thomas Backlund <tmb@mandriva.org> 1.5.3-1mdv2008.1
+ Revision: 177623
- fix group
- fix build as non-root
- import ccs-tools 1.53, initial spec from TL adapted for mdv
- Created package structure for ccs-tools.

