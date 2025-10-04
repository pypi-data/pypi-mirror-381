%global majorver 0
%global minorver 1
%global patchver 2
%global basever %{majorver}.%{minorver}.%{patchver}

%global prerel rc2

%if 0%{?prerel:1}
%global pkgver %{basever}~%{prerel}
%global upsver %{basever}-%{prerel}
%else
%global pkgver %{basever}
%global upsver %{basever}
%endif

Name:           test
Version:        %{pkgver}
Release:        1%{?dist}
Summary:        Test package

License:        MIT

Source0:        https://example.com/archive/%{name}/v%{majorver}.%{minorver}/%{name}-v%{upsver}.tar.xz
Patch0:         patch0.patch
Patch1:         patch1.patch
Patch2:         patch2.patch


%description
Test package


%prep
%autosetup -p1 -n %{name}-%{upsver}


%changelog
* Thu Jun 07 2018 Nikola Forró <nforro@redhat.com> - 0.1.2~rc2-1
- first version
