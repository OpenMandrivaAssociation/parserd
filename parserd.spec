%define name	parserd
%define version	2.1.4
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A server of parsers
License:	Artistic or GPL
Group:		Sciences/Computer science
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{name}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#parser_server
Requires(pre):		rpm-helper
Requires(post):		rpm-helper
Requires(preun):	rpm-helper
Requires(postun):	rpm-helper
Obsoletes:	parser_server
Provides:	parser_server
BuildArch:	noarch

%description
This is a parsers server, allowing to run parsers on remote computers easily.
A set of web wievers, CGI and mod_perl based, are also availables.

%package modperl
Summary:	A mod_perl-based viewer for %{name}
Group:		Sciences/Computer science
Requires:	%{name} = %{version}
Requires:	apache-mod_perl

%description modperl
This is a mod_perl-based viewer for %{name}.

%package cgi
Summary:	A mod_perl-based viewer for %{name}
Group:		Sciences/Computer science
Requires:	%{name} = %{version}
Requires:	apache

%description cgi
This is a CGI-based viewer for %{name}.

%prep
%setup -q
# better mdk configuration
perl -pi -e 's/# user = nobody/user = %{name}/' %{name}.conf
perl -pi -e 's/# group = nogroup/group = %{name}/' %{name}.conf

%build
%configure \
	--with-initdir=%{_initrddir} \
	--with-modperldir=%{_var}/www/perl \
	--with-cgidir=%{_var}/www/cgi-bin
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre
%_pre_useradd %{name} %{_datadir}/%{name} /bin/false

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun
%_postun_userdel %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/*
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/register_parsers.1*

%files modperl
%defattr(-,root,root)
%{_var}/www/perl/parser.pl

%files cgi
%defattr(-,root,root)
%{_var}/www/cgi-bin/*

