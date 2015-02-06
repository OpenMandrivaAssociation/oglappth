%define releasedate	20111012
Name:			oglappth
Version:		1.0.0
Release:		3

%define major		2
%define libname 	%mklibname oglappth %major
%define develname	%mklibname oglappth -d

Summary:	Libraries for the oglappth chemistry package
License:	GPLv2+
Group:		Sciences/Chemistry
URL:		http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:	http://www.bioinformatics.org/ghemical/download/release%{releasedate}/lib%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

%description
Library for creating portable OpenGL applications with easy-to-code scene 
setup and selection operations.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -n lib%{name}-%{version} -q 

%build
%configure2_5x

%make LIBS="-lGL -lGLU"
								
%install
%makeinstall

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.98-3mdv2011.0
+ Revision: 613171
- the mass rebuild of 2010.1 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.98-2mdv2010.1
+ Revision: 440365
- rebuild

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 0.98-1mdv2009.1
+ Revision: 328725
- Name specfile correctly
- Release 0.98

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 0.96-1mdv2008.1
+ Revision: 180142
- import oglappth


* Wed Mar  5 2008 Guillaume Bedot <littletux@mandriva.org> 0.96-1mdv2008.1
- First package of oglappth for contribs
