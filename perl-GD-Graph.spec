#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GD
%define	pnam	Graph
Summary:	GD::Graph perl module
Summary(pl):	Modu� perla GD::Graph
Name:		perl-GD-Graph
Version:	1.43
Release:	1
# same as perl, but contains GPL v2+ font file required by examples, so
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	cf546f2de827a56458afe288ab0807f2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
%if %{with tests}
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-TextUtil >= 0.80
%endif
BuildArch:	noarch
Requires:	perl-GD >= 1.18
Requires:	perl-GD-TextUtil >= 0.80
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph perl module - a package to generate charts, using GD.pm.

%description -l pl
Modu� perla GD::Graph - s�u��cy do generowania wykres�w z u�yciem GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}
%{?with_tests:%{__make} samples}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install samples/*.{dat,pl,png,txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples
install *.ttf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/GD/Graph.pm
%{perl_vendorlib}/GD/Graph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
