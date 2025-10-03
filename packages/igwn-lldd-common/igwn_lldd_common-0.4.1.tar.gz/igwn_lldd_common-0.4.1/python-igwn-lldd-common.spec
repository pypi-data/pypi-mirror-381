# -- metadata

%define srcname igwn-lldd-common
%define distname %{lua:name = string.gsub(rpm.expand("%{srcname}"), "-", "_"); print(name)}
%define version 0.4.1
%define release 1

Name:      python-%{srcname}
Version:   %{version}
Release:   %{release}%{?dist}
Summary:   Kafka clients for delivery of low-latency h(t) data

License:   GPLv3
Url:       https://git.ligo.org/computing/lowlatency/igwn-lldd-common
Source0:   %pypi_source %distname
Packager:  LVC Computing <lvccomputing@ligo.org>
Vendor:    LVC Computing <lvccomputing@ligo.org>
BuildArch: noarch

# rpmbuild dependencies
BuildRequires: python-srpm-macros
BuildRequires: python-rpm-macros
BuildRequires: python3-rpm-macros

# build dependencies
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-setuptools >= 38.2.5
BuildRequires: python%{python3_pkgversion}-wheel

%description
The IGWN - Low Latency Data Distribution (lldd) is software to
distribute low latency data used by the International
Gravitational-Wave Observatory Network (IGWN).

# -- packages

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  Python %{python3_version} library for IGWN LLDD client
Requires: python%{python3_pkgversion}-configargparse
Requires: python%{python3_pkgversion}-gpstime
Requires: python%{python3_pkgversion}-appdirs
Requires: python%{python3_pkgversion}-framel
Requires: python%{python3_pkgversion}-confluent-kafka

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
The IGWN - Low Latency Data Distribution (lldd) is software to
distribute low latency data used by the International
Gravitational-Wave Observatory Network (IGWN).
This package provides the Python %{python3_version} libraries.

%package -n %{srcname}
Summary: Command line utilities for igwn-lldd-common
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: python%{python3_pkgversion}-inotify_simple
%description -n %{srcname}
The IGWN - Low Latency Data Distribution (lldd) is software to
distribute low latency data used by the International
Gravitational-Wave Observatory Network (IGWN).
This package provides the command-line interfaces.

# -- build steps

%prep
%autosetup -n %{distname}-%{version}

%build
%py3_build_wheel

%install
%py3_install_wheel igwn_lldd_common-%{version}-*.whl

%clean
rm -rf $RPM_BUILD_ROOT

# -- files

%files -n %{srcname}
%license LICENSE
%doc README.md
%{_bindir}/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

# -- changelog

%changelog
* Wed May 17 2023 Adam Mercer <adam.mercer@ligo.org> - 0.2.0-1.1
- update for 0.2.0
- fix packaging

* Tue Oct 11 2022 Adam Mercer <adam.mercer@ligo.org> - 0.1.0-1.2
- add missing %{?dist}

* Mon Oct 10 2022 Adam Mercer <adam.mercer@ligo.org> - 0.1.0-1.1
- remove duplicate source line

* Sun Sep 25 2022 LVC Computing <lvccomputing@ligo.org> - 0.1.0-1
- Initial RPM packaging
