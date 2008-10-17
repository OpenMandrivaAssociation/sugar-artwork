%define commitid c77b345c02
%define alphatag 20080709git%{commitid}

Summary: Artwork for Sugar look-and-feel
Name: sugar-artwork
Version: 0.82.3
Release: 1
#Release: 2.%{alphatag}
URL: http://dev.laptop.org
# git clone git://dev.laptop.org/artwork
# cd sugar
# git-checkout %{commitid}
#Source0: %{name}-%{version}-git%{commitid}.tar.bz2
Source0: http://dev.laptop.org/pub/sugar/sources/%{name}/%{name}-%{version}.tar.bz2 
Group: User Interface/Desktops
License: LGPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel >= 2.9.0
BuildRequires: xcursorgen
BuildRequires: perl-XML-Parser
BuildRequires: python
BuildRequires: icon-naming-utils

Requires: gtk2 >= 2.9.0

%description
sugar-artwork contains the themes and icons that make up the OLPC default 
look and feel.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/sugar || :

%files
%defattr(-,root,root)
%doc README COPYING

%{_datadir}/icons/sugar
%{_datadir}/themes/sugar
%{_datadir}/themes/sugar-xo
%{_libdir}/gtk-2.0/*/engines/*.so

