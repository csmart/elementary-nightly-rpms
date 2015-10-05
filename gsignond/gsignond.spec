%define rev b12650ac
%define date 150926

Summary: Online Accounts Sign-on glib daemon
Name: gsignond
Version: 1.0.4~git%{date}~%{rev}
Release: 1%{?dist}
License: LGPLv2.1
URL: http://01.org/gSSO

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: libtool

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.30
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(sqlite3)


%description
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements. The original SSO daemon is written using Qt.


%package devel
Summary: libgsignon-glib development headers
%description devel
gSSO is a glib-based reimplementation of the single sign-on daemon and authentication plugins with advanced access control and other improvements. The original SSO daemon is written using Qt. This package contains the development headers. 


%prep
%setup -q


%build
# main.c:129:5: format not string literal
export CFLAGS="-Wno-error -fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

gtkdocize
autoreconf --install
%configure
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/gsignond/gplugins/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
%postun
/sbin/ldconfig


%post devel
/sbin/ldconfig
%postun devel
/sbin/ldconfig


%files
%config %{_sysconfdir}/gsignond.conf

%{_bindir}/gsignond
%{_libdir}/gsignond/

%{_libdir}/libgsignond-common.so.0
%{_libdir}/libgsignond-common.so.0.0.0

 %{_datadir}/dbus-1/interfaces/*.xml


%files devel
%{_includedir}/gsignond

%{_libdir}/libgsignond-common.so
%{_libdir}/pkgconfig/gsignond.pc


%changelog
* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.4~git150920~b12650ac-1
- Try to fix f23-x64 build.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.4~git150919~b12650ac-1
- Udpate to git snapshot of 1.0.4.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Initial package.


