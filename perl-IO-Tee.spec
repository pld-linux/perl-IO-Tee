%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Tee
Summary:	IO::Tee perl module
Summary(pl):	Modu³ perla IO::Tee
Name:		perl-IO-Tee
Version:	0.64
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Tee - Multiplex output to multiple output handles.

%description -l pl
Modu³ perla IO::Tee - powielaj±cy wyj¶cie na wiele uchwytów plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/IO/Tee.pm
%{_mandir}/man3/*
