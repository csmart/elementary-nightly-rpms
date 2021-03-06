Summary:        Granite Toolkit
Name:           granite
Version:        0.3.1~rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            http://launchpad.net/granite

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires: hicolor-icon-theme


%description
Granite is a library of toolkit addons to GTK+ and is part of the elementary project.


%package devel
Summary: Granite Toolkit development headers
%description devel
Granite is a library of toolkit addons to GTK+ and is part of the elementary project.
This package contains files needed for developing with granite.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang granite


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/granite-demo.desktop


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f granite.lang
%doc AUTHORS HACKING NEWS README
%license COPYING

%{_libdir}/libgranite.so.3
%{_libdir}/libgranite.so.3.0.1
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg


%files devel
%{_bindir}/granite-demo

%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc

%{_includedir}/granite/

%{_datadir}/applications/granite-demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev945-1
- Update to latest snapshot.

* Wed Jun 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev944-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-2
- Update for packaging changes.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev943-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev942-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev941-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev941-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev940-2
- Update for packaging changes.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev940-1
- Update to new upstream snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev939-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev938-1
- Update to new upstream snapshot.

* Wed Apr 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev937-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev936-1
- Update to new upstream snapshot.

* Tue Apr 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev935-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev934-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev933-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev931-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev930-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev929-1
- Update to new upstream snapshot.

* Wed Feb 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev928-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev927-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev926-1
- Update to new upstream snapshot.

* Fri Jan 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev925-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev924-1
- Update to new upstream snapshot.

* Fri Jan 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev922-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev920-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev918-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev917-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev916-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev914-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev913-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev912-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev911-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev907-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev906-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev905-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev904-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev902-1
- Update to new upstream snapshot.

* Fri Nov 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev900-1
- Update to new upstream snapshot.

* Thu Nov 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev899-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev894-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev893-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev892-1
- Update to new upstream snapshot.

* Tue Nov 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev891-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev890-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev889-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev888-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev887-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev886-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev885-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev883-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev882-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev880-1
- Update to new upstream snapshot.

* Wed Oct 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev879-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev878-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev877-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev876-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev875-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev874-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev873-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev872-2
- Update spec for soname bump.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev872-1
- Bump version to 0.3.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev872-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev871-1
- Update to new upstream snapshot.

* Wed Aug 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev866-1
- Update to new upstream snapshot.

* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev865-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev864-1
- Update to new upstream snapshot.

* Thu Jun 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev861-1
- Update to bzr snapshot revno861.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev839-5
- Update to latest bzr snapshot.

* Sun Feb 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev831-4
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.0~rev829-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev826-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev825-1
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.2.3~rev825-1
- Initial package (new).
