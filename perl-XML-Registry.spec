%include	/usr/lib/rpm/macros.perl
Summary:	XML-Registry perl module
Summary(pl):	Modu³ perla XML-Registry
Name:		perl-XML-Registry
Version:	0.02
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Registry-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-Registry - module for loading and saving an XML registry.

%description -l pl
XML-Registry - modu³ do ³adowania i zapisywania rejestru XML.

%prep
%setup -q -n XML-Registry-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/XML/Registry.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
