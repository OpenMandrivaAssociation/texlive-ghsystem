%global tl_name ghsystem
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.8c
Release:	%{tl_revision}.1
Summary:	Globally harmonised system of chemical (etc) naming
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ghsystem
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ghsystem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ghsystem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to typeset all the hazard and
precautionary statements and pictograms in a straightforward way. The
statements are taken from EU regulation 1272/2008.

