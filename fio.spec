%define name fio
%define version 1.16
%define release %mkrel 1

Summary: A flexible I/O tester/benchmarker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: 	System/Kernel and hardware 
Url: http://git.kernel.dk/?p=fio.git;a=summary
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libaio-devel

%description
fio is an I/O tool meant to be used both for benchmark and 
stress/hardware verification.
It has support for 9 different types of I/O engines
(sync, mmap, libaio, posixaio, SG v3, splice, null, network, syslet),
I/O priorities (for newer Linux kernels), rate I/O, forked or threaded jobs,
and much more. It can work on block devices as well as files.
fio accepts job descriptions in a simple-to-understand text format.
Several example job files are included. 
fio displays all sorts of I/O performance information.
It supports Linux, FreeBSD, and OpenSolaris.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fio
%{_bindir}/fio_generate_plots

%changelog
