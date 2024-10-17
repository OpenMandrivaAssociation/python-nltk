%define module	nltk

Summary:	Natural Language Toolkit for Python
Name:		python-%{module}
Version:	2.0.4
Release:	3
Epoch:		0
License:	Apache License 2.0
Group:		Development/Python
Url:		https://www.nltk.org/
Source0:	http://download.sourceforge.net/nltk/nltk-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-yaml >= 3.0.9
Suggests:	python-numpy >= 1.5.1
Suggests:	python-matplotlib >= 1.0.1
BuildRequires:	python-yaml >= 3.0.9
BuildRequires:	python-devel
BuildRequires:	python-distribute

%description
NLTK (the Natural Language Toolkit) is a suite of open source Python
modules, data and documentation for research and development in
natural language processing.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
