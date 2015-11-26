%define rev 1874

Summary: Mail is an email client for elementary OS
Name: pantheon-mail
Version: 1.0.0~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1
URL: http://launchpad.net/pantheon-mail

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: vala
BuildRequires: vala-tools

BuildRequires: pkgconfig(gcr-3) >= 3.10.1
BuildRequires: pkgconfig(gee-0.8) >= 0.8.5
BuildRequires: pkgconfig(gio-2.0) >= 2.28.0
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.34.0
BuildRequires: pkgconfig(gmime-2.6) >= 2.6.14
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires: pkgconfig(libcanberra) >= 0.28
BuildRequires: pkgconfig(libnotify) >= 0.7.5
BuildRequires: pkgconfig(libsecret-1) >= 0.11
BuildRequires: pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires: pkgconfig(pango) >= 1.1.2
BuildRequires: pkgconfig(sqlite3) >= 3.7.4
BuildRequires: pkgconfig(webkitgtk-3.0) >= 2.3.0


Requires: contractor


%description
Mail is an email client for elementary OS

Originally written by Yorba (yorba.org)


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang geary


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/geary.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/geary-autostart.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf $RPM_BUILD_ROOT


%post

%postun


%files -f geary.lang
%{_bindir}/geary
%{_bindir}/geary-attach

%{_datadir}/appdata/geary.appdata.xml
%{_datadir}/applications/geary.desktop
%{_datadir}/applications/geary-autostart.desktop
%{_datadir}/contractor/geary-attach.contract
%{_datadir}/geary/
%{_datadir}/gnome/help/geary/*
%{_datadir}/icons/hicolor/scalable/actions/*.svg


%changelog
* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0.0~rev1874-1
- Initial package.


