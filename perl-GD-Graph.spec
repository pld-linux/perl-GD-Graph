%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	Graph
Summary:	GD::Graph perl module
Summary(pl):	Modu³ perla GD::Graph
Name:		perl-GD-Graph
Version:	1.35
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-TextUtil
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph perl module - a package to generate charts, using GD.pm.

%description -l pl
Modu³ perla GD::Graph - s³u¿±cy do generowania wykresów z u¿yciem GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README 20thcent_Read_Me.txt *.ttf
%{perl_sitelib}/GD/Graph.pm
%{perl_sitelib}/GD/Graph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
