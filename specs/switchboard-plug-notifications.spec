%global debug_package %{nil}

Summary:        Notification configuration management
Name:           switchboard-plug-notifications
Version:        0.1.0.1~rev%{rev}
Release:        4%{?dist}
License:        GPLv3
URL:            http://launchpad.net/switchboard-plug-notifications

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)


%description
Configure which apps should be allowed to show notifications

A GModule plugin for Switchboard that configures gsettings keys related to the Notifications plugin for Gala.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang notifications-plug


%clean
rm -rf %{buildroot}


%files -f notifications-plug.lang
%{_libdir}/switchboard/personal/pantheon-notifications-plug/


%changelog
* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-3
- Update for packaging changes.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

