%define  date	20130406

%define major	3
%define libname %mklibname ccstools %{major}

Summary:	TOMOYO Linux tools
Name:		ccs-tools
Version:	1.8.3
Release:	6
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://tomoyo.sourceforge.jp/
Source0:	http://osdn.dl.sourceforge.jp/tomoyo/27220/%{name}-%{version}-%{date}.tar.gz
Source1:	README.ccs-tools.urpmi
Source2:	tomoyo.logrotate
Source3:	tomoyo.service
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)
Requires(pre,post):	rpm-helper

%description
TOMOYO Linux is an extension for Linux to provide Mandatory Access Control
(MAC) functions. This package contains the tools needed to configure, 
activate and manage the TOMOYO Linux MAC system and policies.


%package -n %{libname}
Summary:    TOMOYO Linux libraries
Group:      System/Libraries

%description -n %{libname}
TOMOYO Linux is an extension for Linux to provide Mandatory Access Control
(MAC) functions. This package contains the tools needed to configure, 
activate and manage the TOMOYO Linux MAC system and policies.


%prep
%setup -qn %{name}
%apply_patches

%build
sed -i \
	-e "s:gcc:%{__cc}:" \
	-e "s/\(CFLAGS.*:=\).*/\1 %{optflags}/" \
	-e "s:/usr/lib:%{_libdir}:g" \
	Include.make

%setup_compile_flags
%make -s all

%install
%makeinstall -s INSTALLDIR=%{buildroot}
install -m 644 %{SOURCE1} README.install.urpmi
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tomoyo
mkdir -p %{buildroot}%{_unitdir}
install -m 700 %{SOURCE3} %{buildroot}%{_unitdir}/ccs-auditd.service
mkdir -p %{buildroot}%{_logdir}/tomoyo

%post
%_post_service ccs-auditd

%preun
%_preun_service ccs-auditd

%files -n %{libname}
%{_libdir}/libccstools.so.%{major}*

%files
%doc README.install.urpmi
%{_sysconfdir}/logrotate.d/tomoyo
%attr(700,root,root) %{_unitdir}/ccs-auditd.service
%attr(700,root,root) /sbin/ccs-init
%{_libdir}/ccs/
%{_sbindir}/ccs-*
%{_mandir}/man8/ccs*
%{_logdir}/tomoyo/
