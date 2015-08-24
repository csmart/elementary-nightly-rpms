%define rev 74
%define debug_package %{nil}

Summary: A power indicator for wingpanel
Name: wingpanel-indicator-power
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-power

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A power indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang power-indicator

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f power-indicator.lang
%{_libdir}/wingpanel/libpower.so
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.power.gschema.xml


%changelog
* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev73-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.1~rev71-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.1~rev70-2
- Add BRs libbamf3, libgtop-2.0.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev70-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to bzr snapshot revno 63.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Initial package.


