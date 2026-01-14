%define		pdir	XML
%define		pnam	Registry
Summary:	XML::Registry perl module
Summary(pl.UTF-8):	Moduł perla XML::Registry
Name:		perl-XML-Registry
Version:	0.02
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	20b3d5614c884a4fac19401779c99c9f
URL:		http://search.cpan.org/dist/XML-Registry/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Registry - module for loading and saving an XML registry.

%description -l pl.UTF-8
XML::Registry - moduł do ładowania i zapisywania rejestru XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Registry.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
