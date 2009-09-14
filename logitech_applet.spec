%define name logitech_applet
%define version 0.4test1
%define release  %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Command line tool for Logitech mouse
License:	GPL
Group:		System/Configuration/Hardware
Source:		http://www.frogmouth.net/%{name}-%{version}.tar.bz2
# (abel) MX518 support
Patch0:		logitech_applet-0.4-mx518.patch.bz2
# (abel) More verbose error reporting for smart scroll
Patch1:		logitech_applet-0.4-verbose-report.patch.bz2
URL:		http://freshmeat.net/projects/logitech_applet/
BuildRequires:  libusb0.1-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Logitech Mouse Applet is a small command line tool for setting 
the special features that are available on some Logitech mice. 
It is particularly useful to those who want to switch their mouse 
to 800cpi instead of the default 400cpi.

%prep
%setup -q
%patch0 -p1 -b .mx518
%patch1 -p1 -b .verbose

%build
%configure2_5x --bindir=%{_sbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc INSTALL README AUTHORS ChangeLog
%{_sbindir}/%{name}

