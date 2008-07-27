#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph
Summary:	GD::Graph - graph plotting module for Perl
Summary(pl.UTF-8):	GD::Graph - moduł do rysowania grafów dla Perla
Name:		perl-GD-Graph
Version:	1.4308
Release:	5
# same as perl, but contains GPL v2+ font file required by examples, so
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	fcdd34d5e09ae917b5d264887734b3b1
Patch0:		%{name}-samples.patch
URL:		http://search.cpan.org/dist/GDGraph/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
GD::Graph is a Perl module to create charts, using the GD module.

%description -l pl.UTF-8
Moduł Perla GD::Graph służy do tworzenia wykresów przy pomocy modułu
GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}
%{?with_tests:%{__make} samples}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/*.{dat,pl,png,txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/GD/Graph/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/GD/Graph.pm
%{perl_vendorlib}/GD/Graph
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
