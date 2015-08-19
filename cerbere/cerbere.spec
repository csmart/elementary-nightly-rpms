%define rev 49

Summary: A simple service to relaunch Pantheon components like the panel, dock, etc.
Name: cerbere
Version: 0.2.1~rev%{rev}
Release: 1%{?dist}
License: GPLv2
URL: http://launchpad.net/cerbere

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)


%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a predefined list of processes (configurable through dconf) and relaunches them if they end. This is helpful to keep the panel, dock, and wallpaper running, even if they crash or are killed by another process.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files
%{_bindir}/cerbere

%{_datadir}/applications/cerbere.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml

%changelog
* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev49-1
- Initial package.


