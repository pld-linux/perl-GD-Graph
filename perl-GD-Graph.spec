#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	GD
%define		pnam	Graph
Summary:	GD::Graph - graph plotting module for Perl
Summary(pl.UTF-8):	GD::Graph - moduł do rysowania grafów dla Perla
Name:		perl-GD-Graph
Version:	1.54
Release:	1
Epoch:		1
# same as perl, but contains GPL v2+ font file required by examples, so
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	38c6a188519e6272e9b2b722b315c3d8
Patch0:		%{name}-samples.patch
URL:		http://search.cpan.org/dist/GDGraph/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-TextUtil >= 0.80
%endif
Requires:	perl-GD >= 1.18
Requires:	perl-GD-TextUtil >= 0.80
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD::Graph is a Perl module to create charts, using the GD module.

%description -l pl.UTF-8
Moduł Perla GD::Graph służy do tworzenia wykresów przy pomocy modułu
GD.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch -P0 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

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

cp -p samples/*.{dat,pl,png,txt} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
