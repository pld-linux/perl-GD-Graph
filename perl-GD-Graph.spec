#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	Graph
Summary:	GD::Graph perl module
Summary(pl):	Modu³ perla GD::Graph
Name:		perl-GD-Graph
Version:	1.39
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildRequires:	ImageMagick
%if %{!?_without_tests:1}0
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-TextUtil
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph perl module - a package to generate charts, using GD.pm.

%description -l pl
Modu³ perla GD::Graph - s³u¿±cy do generowania wykresów z u¿yciem GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}
%{!?_without_tests:%{__make} samples}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/*.{dat,pl,png,txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README *.ttf
%{perl_vendorlib}/GD/Graph.pm
%{perl_vendorlib}/GD/Graph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
