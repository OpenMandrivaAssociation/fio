Summary: A flexible I/O tester/benchmarker
Name: fio
Version:	3.41
Release:	1
#Source0: https://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
Source0:  https://github.com/axboe/fio/archive/%{version}/%{name}-%{name}-%{version}.tar.gz
# Fix --version, needed by kdiskmark
Patch0: fio-version.patch
License: GPLv2
Group: System/Kernel and hardware
Url: https://github.com/axboe/fio

BuildRequires: libaio-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(python)

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
%autosetup -p1

pathfix.py -i %{__python3} -pn \
 tools/fio_jsonplus_clat2csv \
 tools/fiologparser.py \
 tools/hist/*.py \
 tools/plot/fio2gnuplot \
 t/steadystate_tests.py

%build
%set_build_flags
# --enable-native adds -march=native to compiler flags.
# Obviously not what we want in a distro build
./configure --disable-native --extra-cflags="%{optflags}"
%make_build

%install
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%doc HOWTO* README* COPYING REPORTING-BUGS
%doc examples
%{_bindir}/fio
%{_bindir}/fio_generate_plots
%{_bindir}/fio_jsonplus_clat2csv
%{_bindir}/fio-btrace2fio
%{_bindir}/fio-dedupe
%{_bindir}/fio-genzipf
%{_bindir}/fio-histo-log-pctiles.py
%{_bindir}/fio-verify-state
%{_bindir}/fio2gnuplot
%{_bindir}/fiologparser.py
%{_bindir}/fiologparser_hist.py
%{_bindir}/genfio
%dir %{_datadir}/fio
%{_datadir}/fio/graph2D.gpm
%{_datadir}/fio/graph3D.gpm
%{_datadir}/fio/math.gpm
%{_mandir}/man1/*



%changelog
* Mon Apr 16 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.0.7-1
+ Revision: 791317
- update to 2.0.7

* Thu Apr 05 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.0.6-1
+ Revision: 789416
- update to 2.0.6

* Tue Feb 21 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.3-1
+ Revision: 778758
- version update 2.0.3

* Mon Oct 17 2011 Andrey Bondrov <abondrov@mandriva.org> 1.60-1
+ Revision: 705040
- New version 1.60 (stable-1.x)

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.37-2mdv2011.0
+ Revision: 610425
- rebuild

* Tue Feb 23 2010 Frederik Himpe <fhimpe@mandriva.org> 1.37-1mdv2010.1
+ Revision: 510322
- update to new version 1.37

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.34-1mdv2010.0
+ Revision: 443188
- update to new version 1.34

* Wed Aug 26 2009 Frederik Himpe <fhimpe@mandriva.org> 1.32-1mdv2010.0
+ Revision: 421528
- Update to new version 1.32

* Fri Jul 10 2009 Erwan Velu <erwan@mandriva.org> 1.31-1mdv2010.0
+ Revision: 394220
- 1.31

* Wed Nov 19 2008 Erwan Velu <erwan@mandriva.org> 1.23-1mdv2009.1
+ Revision: 304416
- 1.23

* Mon Nov 17 2008 Erwan Velu <erwan@mandriva.org> 1.22-1mdv2009.1
+ Revision: 303953
- 1.22

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.21-2mdv2009.0
+ Revision: 266801
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Erwan Velu <erwan@mandriva.org> 1.21-1mdv2009.0
+ Revision: 217057
- 1.21

* Tue Feb 19 2008 Erwan Velu <erwan@mandriva.org> 1.18.1-1mdv2008.1
+ Revision: 173000
- 1.18.1

* Wed Feb 06 2008 Erwan Velu <erwan@mandriva.org> 1.18-1mdv2008.1
+ Revision: 162988
- 1.18

* Fri Feb 01 2008 Erwan Velu <erwan@mandriva.org> 1.17.3-1mdv2008.1
+ Revision: 161046
- 1.17.3
- 1.17.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Erwan Velu <erwan@mandriva.org> 1.17-1mdv2008.0
+ Revision: 66821
- 1.17

* Fri Jul 20 2007 Erwan Velu <erwan@mandriva.org> 1.16.8-3mdv2008.0
+ Revision: 53818
- Adding source file removed by mdvsys update
- Adding source
- Adding source file
- Rebuild
- Oups, I forgot some examples

* Thu Jul 19 2007 Erwan Velu <erwan@mandriva.org> 1.16.8-1mdv2008.0
+ Revision: 53628
- Fixing wrong %%doc
- Releases goes fast theses days ;)
- Adding missing documentation

* Thu Jul 19 2007 Erwan Velu <erwan@mandriva.org> 1.16.6-1mdv2008.0
+ Revision: 53480
- 1.16.6

* Fri May 04 2007 Erwan Velu <erwan@mandriva.org> 1.16-1mdv2008.0
+ Revision: 22508
- Import fio

