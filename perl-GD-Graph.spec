%include	/usr/lib/rpm/macros.perl
Summary:	GD-Graph perl module
Summary(pl):	Modu³ perla GD-Graph
Name:		perl-GD-Graph
Version:	1.32
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GDGraph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-GD
BuildRequires:	perl-GD-TextUtil
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-Graph perl module

%description -l pl
Modu³ perla GD-Graph

%prep
%setup -q -n GDGraph-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install samples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GD/Graph
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,20thcent_Read_Me.txt}.gz *.ttf

%{perl_sitelib}/GD/Graph.pm
%{perl_sitelib}/GD/Graph/*

%{perl_sitearch}/auto/GD/Graph

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
