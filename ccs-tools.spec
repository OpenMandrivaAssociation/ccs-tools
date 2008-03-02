Summary: TOMOYO Linux tools
%define data 20080131
%define ver  1.5.3

Name: ccs-tools
Version: 1.5.3
Release: %mkrel 1
License: GPL
URL:	http://tomoyo.sourceforge.jp/
Group: System/Kernel
BuildRequires: ncurses-devel
BuildRequires: readline-devel
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
#NoSource: 0

Source0: http://osdn.dl.sourceforge.jp/tomoyo/27220/ccs-tools-%{ver}-%{data}.tar.gz

%description
This is TOMOYO Linux tools.

%prep

%setup -q -n ccstools

%build

%make -s all

%install

%makeinstall -s INSTALLDIR=%{buildroot}

%clean

rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/ccs-init
/sbin/tomoyo-init
/usr/lib/ccs/
%attr(4755,root,root) /usr/lib/ccs/misc/proxy
/usr/sbin/ccs-auditd
/usr/sbin/ccs-ccstree
/usr/sbin/ccs-checkpolicy
/usr/sbin/ccs-domainmatch
/usr/sbin/ccs-editpolicy
/usr/sbin/ccs-editpolicy_offline
/usr/sbin/ccs-findtemp
/usr/sbin/ccs-ld-watch
/usr/sbin/ccs-loadpolicy
/usr/sbin/ccs-pathmatch
/usr/sbin/ccs-patternize
/usr/sbin/ccs-queryd
/usr/sbin/ccs-savepolicy
/usr/sbin/ccs-setlevel
/usr/sbin/ccs-setprofile
/usr/sbin/ccs-sortpolicy
/usr/share/man/man8/ccs-auditd.8.lzma
/usr/share/man/man8/ccs-ccstree.8.lzma
/usr/share/man/man8/ccs-checkpolicy.8.lzma
/usr/share/man/man8/ccs-domainmatch.8.lzma
/usr/share/man/man8/ccs-editpolicy.8.lzma
/usr/share/man/man8/ccs-findtemp.8.lzma
/usr/share/man/man8/ccs-init.8.lzma
/usr/share/man/man8/ccs-ld-watch.8.lzma
/usr/share/man/man8/ccs-loadpolicy.8.lzma
/usr/share/man/man8/ccs-notifyd.8.lzma
/usr/share/man/man8/ccs-pathmatch.8.lzma
/usr/share/man/man8/ccs-patternize.8.lzma
/usr/share/man/man8/ccs-queryd.8.lzma
/usr/share/man/man8/ccs-savepolicy.8.lzma
/usr/share/man/man8/ccs-setlevel.8.lzma
/usr/share/man/man8/ccs-setprofile.8.lzma
/usr/share/man/man8/ccs-sortpolicy.8.lzma
/usr/share/man/man8/init_policy.sh.8.lzma
/usr/share/man/man8/tomoyo-init.8.lzma
/usr/share/man/man8/tomoyo_init_policy.sh.8.lzma
