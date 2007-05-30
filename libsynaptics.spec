Summary:	libsynaptics - a library for communication with Synaptics touchpad
Summary(pl.UTF-8):	libsynaptics - biblioteka do komunikacji z touchpadami Synaptics
Name:		libsynaptics
Version:	0.14.6c
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://qsynaptics.sourceforge.net/%{name}-%{version}.tar.bz2
# Source0-md5:	fedf8b31171d288954ff2e83b251de44
URL:		http://qsynaptics.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsynaptics is a library for communication with Synaptics touchpads.

%description -l pl.UTF-8
libsynaptics jest biblioteką umożliwiającą komunikację z touchpadami
Synaptics.

%package devel
Summary:	Header files for the libsynaptics library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsynaptics
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	xorg-proto-xproto-devel

%description devel
Header files for the libsynaptics library

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsynaptics

%package static
Summary:	Static libsynaptics library
Summary(pl.UTF-8):	Statyczna biblioteka libsynaptics
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsynaptics library

%description static -l pl.UTF-8
Statyczna biblioteka libsynaptics

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/synaptics

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
