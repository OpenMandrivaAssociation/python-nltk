%define origname	nltk

Summary:		Natural Language Toolkit for Python
Name:			python-%{origname}
Version:		1.4.4
Release:		%mkrel 3
Epoch:			0
Group:			Development/Python
Url:			http://nltk.sourceforge.net/
Source0:		http://download.sourceforge.net/nltk/nltk-%{version}.tar.bz2
License:		CPL
BuildRoot:		%{_tmppath}/%{name}-buildroot
BuildArch:		noarch
BuildRequires:          python-devel

%description
The Natural Langauge Toolkit is a Python package that simplifies the 
construction of programs that process natural language and defines 
standard interfaces between the different components of an NLP system. 

%prep
%setup -q -n %{origname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}

%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

