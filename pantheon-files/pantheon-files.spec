%define rev 1957

Summary: Pantheon file manager
Name: pantheon-files
Version: 0.2.3~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-files

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf
Patch0: 00-no-marlincore-C-deps.patch

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gail-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.29
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(granite) >= 0.3.0
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(libnotify) >= 0.7.2
BuildRequires: pkgconfig(pango) >= 1.1.2
BuildRequires: pkgconfig(plank)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(zeitgeist-2.0)


%description
The simple, powerful, and sexy file manager from elementary.
Designed for elementary OS.


%package devel
Summary: pantheon-files development headers
%description devel
The simple, powerful, and sexy file manager from elementary.
This package contains the development headers.


%prep
%setup -q
%patch0 -p1


%build
%cmake
%make_build


%install
%make_install

# this installs libs to /usr/lib ... move them away on x86_64
%ifarch x86_64
mv $RPM_BUILD_ROOT/usr/lib/libpantheon* $RPM_BUILD_ROOT/%{_libdir}/
mv $RPM_BUILD_ROOT/usr/lib/pkgconfig $RPM_BUILD_ROOT/%{_libdir}/
%endif

%find_lang pantheon-files


%check
# this does fail spectacularly
# desktop-file-validate $RPM_BUILD_ROOT/%%{_datadir}/applications/pantheon-files.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files -f pantheon-files.lang
%{_bindir}/pantheon-files
%{_bindir}/pantheon-files-daemon
%{_bindir}/pantheon-files-pkexec

/usr/lib/pantheon-files/
%{_libdir}/gtk-3.0/modules/libpantheon-filechooser-module.so

%{_libdir}/libpantheon-files-core.so.0
%{_libdir}/libpantheon-files-core.so.0.1
%{_libdir}/libpantheon-files-widgets.so.0
%{_libdir}/libpantheon-files-widgets.so.0.1

%{_datadir}/applications/pantheon-files.desktop
%{_datadir}/dbus-1/services/pantheon-files.service
%{_datadir}/glib-2.0/schemas/org.pantheon.files.gschema.xml

%{_datadir}/pantheon-files
%{_datadir}/pixmaps/pantheon-files

%{_datadir}/polkit-1/actions/net.launchpad.pantheon-files.policy


%files devel
%{_includedir}/pantheon-files-core

%{_libdir}/libpantheon-files-core.so
%{_libdir}/libpantheon-files-widgets.so

%{_libdir}/pkgconfig/pantheon-files-core.pc

%{_datadir}/vala/vapi/pantheon-files-core-C.vapi
%{_datadir}/vala/vapi/pantheon-files-core.deps
%{_datadir}/vala/vapi/pantheon-files-core.vapi


%changelog
* Sun Oct 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1957-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1956-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1955-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1953-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1952-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1949-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1948-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1947-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1946-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1944-2
- Fix plugin directory. Update spec.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1944-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1943-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1941-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1937-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev1937-1
- Bump version to 0.2.3.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1937-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1936-1
- Update to new upstream snapshot.

* Sun Aug 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1929-1
- Update to new upstream snapshot.

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1928-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1927-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1926-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.2.2.1~rev1924-1
- Update to new upstream snapshot.

* Sun Aug 16 2015 Fabio Valentini - 0.2.2.1~rev1922-1
- Update to upstream bzr snapshot revno 1922.

* Sat Aug 01 2015 Fabio Valentini - 0.2.2.1~rev1910-1
- Update to bzr snapshot revno 1910.

* Thu Jul 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1901-1
- Update to bzr snapshot revno 1901.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1900-5
- Move libs to usr/lib64 on x86_64.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1900-4
- Fix build.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev1900-3
- Update to bzr snapshot revno 1900.

