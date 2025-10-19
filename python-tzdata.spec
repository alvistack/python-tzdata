# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-tzdata
Epoch: 100
Version: 2025.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Provider of IANA time zone data
License: Apache-2.0
URL: https://github.com/python/tzdata/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
This is a Python package containing zic-compiled binaries for the IANA
time zone database. It is intended to be a fallback for systems that do
not have system time zone data installed (or don't have it installed in
a standard location), as a part of PEP 615.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-tzdata
Summary: Provider of IANA time zone data
Requires: python3
Provides: python3-tzdata = %{epoch}:%{version}-%{release}
Provides: python3dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tzdata) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-tzdata
This is a Python package containing zic-compiled binaries for the IANA
time zone database. It is intended to be a fallback for systems that do
not have system time zone data installed (or don't have it installed in
a standard location), as a part of PEP 615.

%files -n python%{python3_version_nodots}-tzdata
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-tzdata
Summary: Provider of IANA time zone data
Requires: python3
Provides: python3-tzdata = %{epoch}:%{version}-%{release}
Provides: python3dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tzdata) = %{epoch}:%{version}-%{release}

%description -n python3-tzdata
This is a Python package containing zic-compiled binaries for the IANA
time zone database. It is intended to be a fallback for systems that do
not have system time zone data installed (or don't have it installed in
a standard location), as a part of PEP 615.

%files -n python3-tzdata
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-tzdata
Summary: Provider of IANA time zone data
Requires: python3
Provides: python3-tzdata = %{epoch}:%{version}-%{release}
Provides: python3dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tzdata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tzdata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tzdata) = %{epoch}:%{version}-%{release}

%description -n python3-tzdata
This is a Python package containing zic-compiled binaries for the IANA
time zone database. It is intended to be a fallback for systems that do
not have system time zone data installed (or don't have it installed in
a standard location), as a part of PEP 615.

%files -n python3-tzdata
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
