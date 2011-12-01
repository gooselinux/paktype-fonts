%define fontname paktype
%define	fontconf	67-%{fontname}
%define fontdir %{_datadir}/fonts/%{fontname}
%define	paktype	paktype-20061222

# Common description
%define common_desc \
The paktype-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

Name:	%{fontname}-fonts
Version:	2.0
Release:	8%{?dist}
License:	GPLv2 with exceptions
Source:	%{paktype}.tar.gz
Source1:	%{fontconf}-naqsh.conf
Source2:	%{fontconf}-tehreer.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	dos2unix 
BuildRequires:	fontpackages-devel
Group:	User Interface/X
Summary:	Fonts for Arabic from PakType
URL:	https://sourceforge.net/projects/paktype/
 
%description
%common_desc

%package common
Summary:	Common files for paktype-fonts
Group:	User Interface/X
Requires:	fontpackages-filesystem
%description	common
%common_desc

%package -n %{fontname}-naqsh-fonts
Summary:	Naqsh Fonts for Arabic from PakType
Group:	User Interface/X
Requires:	%{name}-common = %{version}-%{release}
License:	GPLv2 with exceptions
Provides:	%{fontname}-fonts = %{version}-%{release}
Obsoletes: %{fontname}-fonts < 2.0-4
%description -n %{fontname}-naqsh-fonts
The paktype-naqsh-fonts package contains fonts for the display of\
Arabic from the PakType by Lateef Sagar.

%_font_pkg -n naqsh -f %{fontconf}-naqsh.conf PakTypeNaqsh.ttf

%package -n %{fontname}-tehreer-fonts
Summary: Tehreer Fonts for Arabic from PakType
Group: User Interface/X
Requires: %{name}-common = %{version}-%{release}
License: GPLv2 with exceptions
Provides: %{fontname}-fonts = %{version}-%{release}
Obsoletes: %{fontname}-fonts < 2.0-4
%description -n %{fontname}-tehreer-fonts
The paktype-tehreer-fonts package contains fonts for the display of\
Arabic from the PakType by Lateef Sagar.

%_font_pkg -n tehreer -f %{fontconf}-tehreer.conf PakTypeTehreer.ttf

%prep
%setup -q -n %{paktype}
find . -not -name \*.ttf -type f -exec dos2unix -k {} \;

%build
echo "Nothing to do in Build."

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-naqsh.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tehreer.conf

for fconf in %{fontconf}-naqsh.conf \
		%{fontconf}-tehreer.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

%clean
rm -rf %{buildroot}


%files common
%defattr(-,root,root,-)
%doc *.txt
%dir %{fontdir}

%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> 2.0-8
- Resolves: bug 586900

* Thu Mar 04 2010 Pravin Satpute <psatpute@redhat.com> 2.0-7
- fixed type in .conf file
- Resolves: bug 570404

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com> 2.0-6
- added conf file for each subpackage
- Resolves: bug 568643

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0-5.1
- Rebuilt for RHEL 6

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 2.0-5
- Bump for F12 mass rebuild

* Thu Jul 9 2009 Pravin Satpute <psatpute@redhat.com> 2.0-4
- updated as per new font packaging guideline

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 2.0-2.fc8
- Changed license to include font exception and removed fonts.cache-1 file

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 2.0-1.fc8
- Initial packaging for split from fonts-arabic 
