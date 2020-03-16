# Generated by go2rpm 1
%bcond_without check

# https://github.com/cubiest/jibberjabber
%global goipath         github.com/cubiest/jibberjabber
Version:                2.0

%gometa

%global common_description %{expand:
Cross Platform locale detection for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Cross Platform locale detection for Golang

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/language)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Mar 16 11:10:04 -05 2020 rafael <rafael@autonomia.digital> - 2.0-1
- Initial package

