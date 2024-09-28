Name:    kf6
# This version MUST remain in sync with KF6 versions!
Version: 6.6.0
Release: 0%{?dist}
Summary: Filesystem and RPM macros for KDE Frameworks 6
License: BSD-3-Clause
URL:     http://www.kde.org
Source0: %{name}-%{version}.tar.bz2

%description
Filesystem and RPM macros for KDE Frameworks 6

%package rpm-macros
Summary: RPM macros for KDE Frameworks 6
Requires: cmake >= 3
Requires: qt6-rpm-macros >= 6
# misc build environment dependencies
Requires: clang
# for docs generation
Requires: doxygen
#Requires: qt6-doc-devel
#Requires: qt6-qttools

BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 6 packages.

%prep
%setup -q

%install

install -Dpm644 macros.kf6 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6
sed -i \
  -e "s|@@kf6_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf6
