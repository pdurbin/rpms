# $Id$
# Authority: dries
# Upstream: Greg Ward <gward$python,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Tabular

Summary: Table-driven argument parsing
Name: perl-Getopt-Tabular
Version: 0.3
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Tabular/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Tabular-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Getopt::Tabular is a Perl 5 module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Getopt/Tabular.p*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
