%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Registry
Summary:	XML::Registry perl module
Summary(pl):	Modu³ perla XML::Registry
Name:		perl-XML-Registry
Version:	0.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Registry - module for loading and saving an XML registry.

%description -l pl
XML::Registry - modu³ do ³adowania i zapisywania rejestru XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/XML/Registry.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
