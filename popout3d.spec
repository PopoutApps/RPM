Name:           popout3d
Version:        1.6.45
Release:        1%{?dist}
Summary:        Pop-out 3D image viewer

License:        GPL-3.0-or-later
URL:            https://github.com/PopoutApps/popout3d
Source0:       https://github.com/PopoutApps/popout3d/archive/refs/tags/v%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: meson
BuildRequires: ninja-build

Requires:      gtk4
Requires:      gdk-pixbuf2
Requires:      glib2
Requires:      hugin
Requires:      python3
Requires:      python3-gobject
Requires:      python3-pillow

%description
Popout3D lets you create stereoscopic images from ordinary photographs.

%check
# No tests available

# Python so nothing to compile.
%global debug_package %{nil}

#%prep
#%setup -q
%prep
%autosetup -n popout3d-%{version}

%build
# No C compilation; only Python and data files
%meson
%install
%meson_install

%files
%license LICENSE
%{_bindir}/popout3d
%{_datadir}/popout3d
%{_datadir}/applications/popout3d.desktop
%{_datadir}/metainfo/popout3d.metainfo.xml
%{_datadir}/icons/hicolor/64x64/apps/com.github.PopoutApps.popout3d.png
%{_datadir}/icons/hicolor/128x128/apps/com.github.PopoutApps.popout3d.png
%{_datadir}/locale/*/LC_MESSAGES/popout3d.mo

%changelog
* Sat Feb 21 2026 Chris <chris@example.com> - 1.6.45-1
* Sun Feb 08 2026 Chris <chris@example.com> - 1.6.45-1
- Initial RPM packaging

