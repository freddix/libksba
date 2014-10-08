Summary:	CMS and X.509 access library
Name:		libksba
Version:	1.3.1
Release:	1
License:	LGPL v3+ or GPL v2+ (libraries), GPL v3+ (the rest)
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libksba/%{name}-%{version}.tar.bz2
# Source0-md5:	9be95245fcfa9d56f56853078ef2650b
URL:		http://www.gnupg.org/related_software/libksba/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSBA is a library to make the tasks of working with X.509
certificates, CMS data and related data more easy.

%package devel
Summary:	Header files to develop KSBA applications
License:	LGPL v3+ or GPL v2+ (libraries), GPL v3+ (manual)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpg-error-devel

%description devel
Header files to develop KSBA applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%{__rm} $RPM_BUILD_ROOT%{_infodir}/dir
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
# note: COPYING specifies license types, doesn't contain LGPL/GPL text
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libksba.so.8
%attr(755,root,root) %{_libdir}/libksba.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksba-config
%attr(755,root,root) %{_libdir}/libksba.so
%{_infodir}/ksba.info*
%{_includedir}/ksba.h
%{_aclocaldir}/ksba.m4

