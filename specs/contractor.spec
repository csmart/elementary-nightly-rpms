Summary:        Desktop-wide extension service
Name:           contractor
Version:        0.3.1~rev%{rev}
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/contractor

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus


%description
An extension service that allows apps to use the exposed functionality of registered apps. This way, apps don't have to have the functions hard coded into them.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/contractor


%clean
rm -rf %{buildroot}


%files
%doc HACKING

%{_bindir}/contractor

%{_datadir}/contractor/
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-2
- Update for packaging changes.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-1
- Update to latest snapshot.

* Sun Feb 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev138-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev137-1
- Update to new upstream snapshot.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-3
- Fix build, oops ...

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-2
- Update spec file to use more macros.

* Sat Jul 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3.1~rev136-1
- Initial package.


