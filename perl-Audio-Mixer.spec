#
# Conditional build:
# _with_tests - perform "make test" (opens /dev/mixer)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Mixer
Summary:	Audio::Mixer Perl module
Summary(pl):	Modu³ Perla Audio::Mixer
Name:		perl-Audio-Mixer
Version:	0.6
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is just a very simple Perl interface which allows to set various
sound mixer parameters. The most important probably 'vol' (volume).
The list of all mixer parameters can be obtained using
get_mixer_params() function.

%description -l pl
To jest bardzo prosty perlowy interfejs, pozwalaj±cy na ustawianie
ró¿nych parametrów miksera d¼wiêku. Prawdopodobnie najwa¿niejszym jest
'vol' (g³o¶no¶æ). Listê wszystkich parametrów miksera mo¿na odczytaæ
funkcj± get_mixer_params().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{perl_sitearch}/Audio/volume.pl
%{perl_sitearch}/Audio/Mixer.pm
%dir %{perl_sitearch}/auto/Audio/Mixer
%{perl_sitearch}/auto/Audio/Mixer/autosplit.ix
%{perl_sitearch}/auto/Audio/Mixer/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/Mixer/*.so
%{_mandir}/man3/*
