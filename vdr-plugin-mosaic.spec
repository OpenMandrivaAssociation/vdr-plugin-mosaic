
%define plugin	mosaic
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	6

Summary:	VDR plugin: Browse mosaic channel
Name:		%name
Version:	%version
Release:	%rel
Group:		Video
License:	GPL+
URL:		http://vdrwiki.free.fr/vdr/mosaic/
Source:		http://vdrwiki.free.fr/vdr/mosaic/files/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Mosaic is a plugin for VDR that brings the ability to quickly browse
the mosaic channels of Canalsat on Astra. It shows the EPG
information and plays the audio of the selected channel.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 files/*.conf %{buildroot}%{vdr_plugin_cfgdir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README
%config(noreplace) %{vdr_plugin_cfgdir}/%plugin.conf




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0-3mdv2009.1
+ Revision: 359338
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-2mdv2009.0
+ Revision: 197950
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0-1mdv2009.0
+ Revision: 197692
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- drop patch, fixed upstream

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2008.1
+ Revision: 145132
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2008.1
+ Revision: 103156
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2008.0
+ Revision: 81883
- 0.0.3
- adapt license tag to new policy
- add a patch to fix build (mosaic-wrong-endif.patch)

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2008.0
+ Revision: 50018
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2008.0
+ Revision: 42104
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2008.0
+ Revision: 22755
- rebuild for new vdr


* Fri Mar 02 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
+ Revision: 130898
- 0.0.2

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-7mdv2007.1
+ Revision: 90942
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-6mdv2007.1
+ Revision: 74048
- rebuild for new vdr
- Import vdr-plugin-mosaic

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1-1mdv2007.0
- initial Mandriva release

