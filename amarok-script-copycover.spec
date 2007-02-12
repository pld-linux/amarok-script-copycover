%define		scriptname	copycover
Summary:	CopyCover amaroK Script
Summary(pl.UTF-8):	Skrypt CopyCover dla amaroKa
Name:		amarok-script-copycover
Version:	1.6
Release:	0.1
Epoch:		0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/khotnewstuff/amarokscripts/downloads/22517-%{scriptname}.amarokscript.tar.bz2
# Source0-md5:	58ef540f1ffee891ff4119c51b6cf7c6
URL:		http://www.kde-apps.org/content/show.php?content=22517
BuildRequires:	sed >= 4.0
Requires:	amarok >= 1.2.3
Requires:	python >= 2.3
Requires:	python-PyQt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
Copy the cover of current playing track to the song's dir. Does not
overwrite existing images in this folder. The filenames can be
configured with the "Configure" dialog. By default, it's the album's
name, with spaces replaced by underscores.

%description -l pl.UTF-8
Skrypt kopiujący okładkę aktualnie odtwarzanej ścieżki do katalogu z
utworem. Nie nadpisuje istniejących obrazków w folderze. Nazwy plików
mogą być konfigurowane w oknie dialogowym "Configure". Domyślnie jest
to nazwa albumu ze spacjami zamienionymi na podkreślenia.

%prep
%setup -q -n %{scriptname}
sed -i -e '1s,#!/usr/bin/env python,#!%{_bindir}/python,' *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp -a . $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_scriptdir}/%{scriptname}
%{_scriptdir}/%{scriptname}/README
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.py
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.sh
