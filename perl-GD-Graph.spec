%include	/usr/lib/rpm/macros.perl
Summary:	GD-Graph perl module
Summary(pl):	Modu³ perla GD-Graph
Name:		perl-GD-Graph
Version:	1.33
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GDGraph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	perl-GD-TextUtil
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD-Graph perl module.

%description -l pl
Modu³ perla GD-Graph.

%prep
%setup -q -n GDGraph-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf CHANGES README *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,20thcent_Read_Me.txt}.gz *.ttf
%{perl_sitelib}/GD/Graph.pm
%{perl_sitelib}/GD/Graph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
