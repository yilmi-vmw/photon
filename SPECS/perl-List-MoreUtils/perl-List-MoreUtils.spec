# Got the intial spec from Fedora and modified it
Summary:	Provide the stuff missing in List::Util
Name:		perl-List-MoreUtils
Version:	0.418
Release:	1%{?dist}
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/List-MoreUtils/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/List-MoreUtils-%{version}.tar.gz
%define sha1 List-MoreUtils=6fe3d27e6a87f4516f22ca59b4c65d28093548a9
Vendor:		VMware, Inc.
Distribution:	Photon
BuildArch:      noarch
BuildRequires:	perl
Requires:	perl
BuildRequires:	perl-Exporter-Tiny
Requires:	perl-Exporter-Tiny

%description
List::MoreUtils provides some trivial but commonly needed functionality
on lists that is not going to go into List::Util.

%prep
%setup -q -n List-MoreUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name 'perllocal.pod' -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%{perl_vendorlib}/List/
%{_mandir}/man3/List::MoreUtils.3*
%{_mandir}/man3/List::MoreUtils::PP.3*
%{_mandir}/man3/List::MoreUtils::Contributing.3.gz

%changelog
*   Wed Apr 05 2017 Robert Qi <qij@vmware.com> 0.418-1
-   Update version to 0.418
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.413-2
-	GA - Bump release of all rpms
*   Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 0.413-1
-   Updated to version 0.413
*	Fri Apr 3 2015 Divya Thaluru <dthaluru@vmware.com> 0.410-1
-	Initial version.
