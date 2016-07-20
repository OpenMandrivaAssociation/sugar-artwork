# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details
%define _disable_ld_no_undefined 1

Name:		sugar-artwork
Version:	0.108.1
Release:	1
Summary:	Artwork for Sugar look-and-feel
License:	LGPLv2+
Group:		Graphical desktop/Other
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/sucrose/glucose/sugar-artwork/sugar-artwork-%{version}.tar.xz

Requires:	gtk+2.0 >= 2.9.0
Requires:	sugar-base >= 0.88.0

BuildRequires:	perl-XML-Parser  
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	icon-naming-utils  
BuildRequires:	icon-slicer  
BuildRequires:	python2
BuildRequires:	xcursorgen

%description
Contains the themes and icons that make up the Sugar default look and feel.

%prep
%setup -q

%build
%define __libtoolize true
%configure
make

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/gtk-2.0/*/engines/*.la

%files 
%{_datadir}/icons/*
%{_datadir}/themes/*
%{_libdir}/gtk*/*/engines/*
%doc COPYING NEWS README
