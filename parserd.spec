%define name	parserd
%define version	2.2.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A server of parsers
License:	Artistic or GPL
Group:		Sciences/Computer science
Url:		https://gforge.inria.fr/projects/lingwb/
Source:		https://gforge.inria.fr/frs/download.php/5679/%{name}-%{version}.tar.gz
Requires(pre):		rpm-helper
Requires(post):		rpm-helper
Requires(preun):	rpm-helper
Requires(postun):	rpm-helper
Obsoletes:	parser_server
Provides:	parser_server
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%{_sbindir}/%{name}_service
%{_libdir}/pkgconfig/parserd.pc
%{_datadir}/%{name}
%{_mandir}/man1/register_parsers.1*

%files modperl
%defattr(-,root,root)
%{_var}/www/perl/parser.pl

%files cgi
%defattr(-,root,root)
%{_var}/www/cgi-bin/*



%changelog
* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-1mdv2010.0
+ Revision: 393719
- new version

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.1.4-4mdv2009.0
+ Revision: 255042
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.1.4-2mdv2008.1
+ Revision: 136639
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import parserd


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-2mdv2007.0
- Rebuild

* Fri Mar 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-1mdk
- new version
- %%mkrel

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.3-1mdk 
- new version
- spec cleanup
- requires
- init script is not configuration

* Fri Feb 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.1.1-2mdk
- spec file cleanups, remove the ADVX-build stuff

* Thu Dec 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.1-1mdk 
- new version
- name change
- drop patch, fixed upstream
- cgi and modperl viewver subpackages
- create dedicated user
- better summary and description

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0.2-3mdk 
- fix buildrequires

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0.2-2mdk 
- install init script

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0.2-1mdk 
- first mdk release
