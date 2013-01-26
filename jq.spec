Name:		jq
Version:	1.2
Release:	1%{?dist}
Summary:	jq is like sed for JSON data

Group:		Development/Tools
License:	MIT
URL:		http://stedolan.github.com/jq
# wget https://github.com/stedolan/jq/tarball/jq-1.2 -O $RPM_SOURCE_DIR/jq-1.2.tar.gz
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	flex, bison, python, gcc, make

%description
jq is like sed for JSON data

%prep
%setup -q -n stedolan-jq-1e8c524

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 jq %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/jq
