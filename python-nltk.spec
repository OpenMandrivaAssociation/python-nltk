%define module	nltk
%define rel	rc1

Summary:	Natural Language Toolkit for Python
Name:		python-%{module}
Version:	2.0.4
Release:	1
Epoch:		0
License:	Apache License 2.0
Group:		Development/Python
Url:		http://www.nltk.org/
Source0:	http://download.sourceforge.net/nltk/nltk-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-yaml >= 3.0.9
Suggests:	python-numpy >= 1.5.1
Suggests:	python-matplotlib >= 1.0.1
BuildRequires:	python-yaml >= 3.0.9
BuildRequires:	python-devel

%description
NLTK â€” the Natural Language Toolkit â€” is a suite of open source Python
modules, data and documentation for research and development in
natural language processing.

%prep
%setup -q -n %{module}-%{version}%{rel}

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%py_puresitedir/*egg-info


%changelog
* Sun Aug 07 2011 Lev Givon <lev@mandriva.org> 0:2.0.1-0.rc1.1mdv2012.0
+ Revision: 693619
- Need python-devel to build on 2010.1.

* Mon Jul 25 2011 Lev Givon <lev@mandriva.org> 0:2.0.1-0.rc1
+ Revision: 691632
- Update to 2.0.1rc1.

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0:1.4.4-9mdv2011.0
+ Revision: 594962
- rebuild for py 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:1.4.4-9mdv2010.0
+ Revision: 442322
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0:1.4.4-8mdv2009.1
+ Revision: 323810
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:1.4.4-7mdv2009.0
+ Revision: 242422
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild

* Sun Sep 09 2007 David Walluck <walluck@mandriva.org> 0:1.4.4-4mdv2008.0
+ Revision: 83166
- rebuild


* Mon Sep 04 2006 David Walluck <walluck@mandriva.org> 0:1.4.4-3mdv2007.0
- rebuild to fix release
- clean %%{buildroot} in %%install

* Thu Dec 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.4-2mdk
- Add BuildRequires: python-devel

* Sun Nov 06 2005 David Walluck <walluck@mandriva.org> 0:1.4.4-1mdk
- release


