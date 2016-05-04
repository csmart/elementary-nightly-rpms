Summary:        Gala window manager
Name:           gala
Version:        0.3.0~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/gala

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libmutter) >= 3.14.4
BuildRequires:  pkgconfig(plank) >= 0.3.0

Requires:       hicolor-icon-theme


%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        libs
Summary: Gala window manager libraries
%description    libs
Gala is Pantheon's Window Manager, part of the elementary project. This package contains the shared libraries.


%package        devel
Summary: Gala window manager
%description    devel
Gala is Pantheon's Window Manager, part of the elementary project. This package contains the development headers.


%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
%make_install
%find_lang gala

rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/plank/*.la


%clean
rm -rf %{buildroot}


%post
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/sbin/ldconfig
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post           libs -p /usr/sbin/ldconfig
%postun         libs -p /usr/sbin/ldconfig

%post           devel -p /usr/sbin/ldconfig
%postun         devel -p /usr/sbin/ldconfig


%files       -f gala.lang
%{_bindir}/gala

%{_libdir}/gala/

%{_datadir}/applications/gala.desktop
%{_datadir}/applications/gala-multitaskingview.desktop
%{_datadir}/applications/gala-wayland.desktop
%{_datadir}/gala/
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg


%files          libs
%{_libdir}/libgala.so.0
%{_libdir}/libgala.so.0.0.0


%files          devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
