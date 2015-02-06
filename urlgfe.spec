%define Werror_cflags %nil
%define name urlgfe 
%define version 1.0
%define release 8
%define iconname %{name}.png

Summary:   Download manager that uses gtk+2
Name:      %{name}
Version:   %{version}
Release:   %{release}
Group:     Networking/File transfer
License:     GPL
Url:       http://urlget.sourceforge.net/
Source0:  %{name}-%{version}.tar.bz2 
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: openssl-devel 
BuildRequires: imagemagick
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
rm -rfd %{buildroot}/%{name}-%{version}/win32
 
%build 
 
%configure2_5x

%make

 
%install

%makeinstall_std

mkdir -p %{buildroot}%{_liconsdir}/
mkdir -p %{buildroot}%{_miconsdir}/

install -m 644 pixmaps/urlgfe-icon.png %{buildroot}%{_liconsdir}/%{iconname}
convert pixmaps/%{name}-icon.png  -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert pixmaps/%{name}-icon.png  -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 

 
#rm dup docs
rm -rfd %{buildroot}/usr/doc

%find_lang %{name} 

%files -f %{name}.lang
%doc COPYING INSTALL
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png
%{_iconsdir}/*
