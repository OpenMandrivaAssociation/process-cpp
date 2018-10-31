%define debug_package %{nil}
%define major 2
%define libname %mklibname process-cpp %{major}
%define devname %mklibname process-cpp -d

Name: process-cpp
Version: 3.0.1
Release: 2
Source0: %{name}-%{version}.tar.xz
Patch0: process-cpp-system-gmock.patch
# Tests themselves are broken...
Patch1: process-cpp-disable-tests.patch
Summary: Convenience library for handling processes in C++11
URL: http://launchpad.net/process-cpp
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: gmock-source
BuildRequires: boost-devel
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: doxygen

%description
Convenience library for handling processes in C++11

%package -n %{libname}
Summary: Convenience library for handling processes in C++11
Group: System/Libraries

%description -n %{libname}
Convenience library for handling processes in C++11

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -qn %{name}
%apply_patches

%cmake -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libprocess-cpp.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libprocess-cpp.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/process-cpp
