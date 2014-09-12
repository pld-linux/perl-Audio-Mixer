#
# Conditional build:
%bcond_with	tests	# perform "make test" (opens /dev/mixer)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Mixer
Summary:	Audio::Mixer - Perl extension for sound mixer control
Summary(pl.UTF-8):	Audio::Mixer - rozszerzenie Perla do sterowania mikserem dźwięku
Name:		perl-Audio-Mixer
Version:	0.7
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5aaa808a4852ed68f952705172ece2a8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is just a very simple Perl interface which allows to set various
sound mixer parameters. The most important probably 'vol' (volume).
The list of all mixer parameters can be obtained using
get_mixer_params() function.

%description -l pl.UTF-8
To jest bardzo prosty perlowy interfejs, pozwalający na ustawianie
różnych parametrów miksera dźwięku. Prawdopodobnie najważniejszym jest
'vol' (głośność). Listę wszystkich parametrów miksera można odczytać
funkcją get_mixer_params().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{perl_vendorarch}/Audio/volume.pl
%{perl_vendorarch}/Audio/Mixer.pm
%dir %{perl_vendorarch}/auto/Audio/Mixer
%{perl_vendorarch}/auto/Audio/Mixer/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Mixer/*.so
%{_mandir}/man3/*
