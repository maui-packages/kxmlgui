# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kxmlgui

# >> macros
# << macros

# >> bcond_with
# << bcond_with

# >> bcond_without
# << bcond_without

Summary:    KDE Frameworks 5 Tier 3 solution for generating UI
Version:    5.2.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kxmlgui.yaml
Source101:  kxmlgui-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kitemviews-devel
BuildRequires:  kconfig-devel
BuildRequires:  kglobalaccel-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  attica-devel

%description
KDE Frameworks 5 Tier 3 solution for generating UI


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kitemviews-devel
Requires:   kconfig-devel
Requires:   kglobalaccel-devel
Requires:   kconfigwidgets-devel
Requires:   ki18n-devel
Requires:   kiconthemes-devel
Requires:   ktextwidgets-devel
Requires:   kwidgetsaddons-devel
Requires:   kwindowsystem-devel
Requires:   attica-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5XmlGui.so.*
%{_kf5_configdir}/ui/ui_standards.rc
%{_kf5_libexecdir}/ksendbugmail
%{_kf5_datadir}/kxmlgui/
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kxmlgui_version.h
%{_kf5_includedir}/KXmlGui
%{_kf5_libdir}/libKF5XmlGui.so
%{_kf5_cmakedir}/KF5XmlGui
%{_kf5_mkspecsdir}/qt_KXmlGui.pri
# >> files devel
# << files devel
