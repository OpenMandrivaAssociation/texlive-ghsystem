Name:		texlive-ghsystem
Version:	53822
Release:	2
Summary:	Globally harmonised system of chemical (etc) naming
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ghsystem
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghsystem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghsystem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to typeset all the hazard and
precautionary statements and pictograms in a straightforward
way. The statements are taken from EU regulation 1272/2008.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ghsystem
%doc %{_texmfdistdir}/doc/latex/ghsystem

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
