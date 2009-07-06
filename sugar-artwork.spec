# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-artwork
Version: 0.84.1
Release: %mkrel 3
Summary: Artwork for Sugar look-and-feel
License: LGPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar-artwork/sugar-artwork-0.84.1.tar.bz2

Requires: gtk+2 >= 2.9.0
Requires: sugar-base >= 0.84.0

BuildRequires: perl-XML-Parser  
BuildRequires: gtk+2-devel >= 2.9.0
BuildRequires: icon-naming-utils  
BuildRequires: icon-slicer  
BuildRequires: python  
BuildRequires: xcursorgen  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Contains the themes and icons that make up the Sugar default look and feel.

%prep
%setup -q -n sugar-artwork-0.84.1


%build
%define __libtoolize true
%configure
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/gtk-2.0/*/engines/*.la


%clean
rm -rf %{buildroot}

%post
%update_icon_cache sugar

%postun
%clean_icon_cache sugar

%files 
%defattr(-,root,root,-)
%{_datadir}/icons/*
%{_datadir}/themes/*
%{_libdir}/gtk*/*/engines/*
%doc COPYING NEWS README

