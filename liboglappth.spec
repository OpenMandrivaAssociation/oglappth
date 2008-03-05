%define	major 1
%define	libname %mklibname oglappth %major
%define develname %mklibname oglappth -d

Name: oglappth
Summary: Libraries for the oglappth chemistry package
Version: 0.96
Release: %mkrel 1
Source0: http://www.uku.fi/~thassine/projects/download/lib%{name}-%{version}.tar.gz
URL: http://www.uku.fi/~thassine/ghemical
License: GPLv2+
Group: Sciences/Chemistry
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mesaglut-devel

%description
Library for creating portable OpenGL applications with easy-to-code scene 
setup and selection operations.

%package -n %{libname}
Summary: Dynamic libraries from %{name}
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary: Header files and static libraries from %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -n lib%{name}-%{version} -q 

%build
%configure2_5x

%make
								
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS ChangeLog
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

