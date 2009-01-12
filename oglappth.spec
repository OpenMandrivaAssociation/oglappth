Name:			oglappth
Version:		0.98
Release:		%mkrel 1

%define major		2
%define libname 	%mklibname oglappth %major
%define oldlibname	%mklibname oglappth 1
%define develname	%mklibname oglappth -d

Summary:	Libraries for the oglappth chemistry package
License:	GPLv2+
Group:		Sciences/Chemistry
URL:		http://www.uku.fi/~thassine/ghemical
Source0:	http://www.uku.fi/~thassine/projects/download/lib%{name}-%{version}.tar.gz

BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Library for creating portable OpenGL applications with easy-to-code scene 
setup and selection operations.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{oldlibname}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -n lib%{name}-%{version} -q 

%build
%configure2_5x

%make LIBS="-lGL -lGLU"
								
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

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

