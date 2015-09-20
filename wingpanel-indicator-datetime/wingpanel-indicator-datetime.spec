%define rev 80
%define debug_package %{nil}

Summary: A datetime indicator for wingpanel
Name: wingpanel-indicator-datetime
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-ayatana

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) 
BuildRequires: pkgconfig(indicator3-0.4)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A datetime indicator for wingpanel


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang datetime-indicator

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%files -f datetime-indicator.lang
%{_libdir}/wingpanel/libdatetime.so


%changelog
* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev80-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev79-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev78-2
- Release bump for wingpanel soname change.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev78-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev77-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev77-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev75-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev74-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to bzr snapshot revno 63.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to bzr snapshot revno 55.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Initial package.


