# $Id$
# Authority: matthias

Summary: Set of portable libraries especially useful for games
Name: plib
Version: 1.8.3
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://plib.sourceforge.net/
Source: http://plib.sourceforge.net/dist/plib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: Mesa, libpng
BuildRequires: gcc-c++
BuildRequires: Mesa-devel, glut-devel, libpng-devel

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NOTICE NEWS README
%{_libdir}/libplib*
%{_includedir}/plib


%changelog
* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-1
- Update to 1.8.3.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.6.0-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.6.0.

* Wed Jun 20 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

