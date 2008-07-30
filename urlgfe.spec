%define name urlgfe 
%define version 1.0
%define release %mkrel 4
%define iconname %{name}.png

Summary:   Download manager that uses gtk+2
Name:      %{name}
Version:   %{version}
Release:   %{release}
Group:     Networking/File transfer
License:     GPL
Url:       http://urlget.sourceforge.net/
Source:  %{name}-%{version}.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: openssl-devel 
BuildRequires: ImageMagick
BuildRequires: pcre-devel
BuildRequires: desktop-file-utils
Requires: wget
Obsoletes: urlget
Provides: urlget

%description
UrlGfe is a download manager that uses gtk+2
 User can classify URLs before downloading.	
 Every category has independent configuration.	
 Batch mode can generate URLs. 
 Import URLs from .html files. 
 Export URLs ( for wget -i )

Formerly urlget

%prep
%setup -q -n %{name}-%{version}
rm -rfd $RPM_BUILD_ROOT/%{name}-%{version}/win32
 
%build 
 
%configure2_5x

%make

 
%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

install -m 644 pixmaps/urlgfe-icon.png %{buildroot}%{_liconsdir}/%{iconname}
convert pixmaps/%{name}-icon.png  -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert pixmaps/%{name}-icon.png  -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 

 
#rm dup docs
rm -rfd $RPM_BUILD_ROOT/usr/doc

%find_lang %{name} 

%clean
#rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING INSTALL
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png
%{_iconsdir}/*


