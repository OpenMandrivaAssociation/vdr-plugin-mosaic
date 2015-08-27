%define plugin	mosaic

Summary:	VDR plugin: Browse mosaic channel
Name:		vdr-plugin-%plugin
Version:	0.1.0
Release:	7
Group:		Video
License:	GPL+
URL:		http://vdrwiki.free.fr/vdr/mosaic/
Source:		http://vdrwiki.free.fr/vdr/mosaic/files/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Mosaic is a plugin for VDR that brings the ability to quickly browse
the mosaic channels of Canalsat on Astra. It shows the EPG
information and plays the audio of the selected channel.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
install -m644 files/*.conf %{buildroot}%{vdr_plugin_cfgdir}

%files -f %plugin.vdr
%doc README
%config(noreplace) %{vdr_plugin_cfgdir}/%plugin.conf




