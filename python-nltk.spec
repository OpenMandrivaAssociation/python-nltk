%define module	nltk
%define name	python-%{module}
%define version	2.0.1
%define rel	rc1
%define release %mkrel 0.%{rel}

Summary:	Natural Language Toolkit for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		0
License:	Apache License 2.0
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}%{rel}-root
Url:		http://www.nltk.org/
Source0:	http://nltk.googlecode.com/files/%{module}-%{version}%{rel}.tar.gz
BuildArch:	noarch
Requires:	python-yaml >= 3.0.9
Suggests:	python-numpy >= 1.5.1
Suggests:	python-matplotlib >= 1.0.1
BuildRequires:	python-yaml >= 3.0.9

%description
NLTK — the Natural Language Toolkit — is a suite of open source Python
modules, data and documentation for research and development in
natural language processing.

%prep
%setup -q -n %{module}-%{version}%{rel}

%install
%{__rm} -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%{__rm} -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%py_puresitedir/*
