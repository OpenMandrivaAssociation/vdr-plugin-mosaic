
%define plugin	mosaic
%define name	vdr-plugin-%plugin
%define version	0.1.0
%define rel	1

Summary:	VDR plugin: Browse mosaic channel
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://vdrwiki.free.fr/vdr/mosaic/
Source:		http://vdrwiki.free.fr/vdr/mosaic/files/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
install -m644 files/*.conf %{buildroot}%{_vdr_plugin_cfgdir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin.conf


