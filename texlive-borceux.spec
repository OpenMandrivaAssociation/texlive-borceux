Name:		texlive-borceux
Version:	21047
Release:	1
Summary:	Diagram macros by Francois Borceux
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/borceux
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/borceux.r21047.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/borceux.doc.r21047.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros support the construction of diagrams, such as those
that appear in category theory texts. The user gives the list
of vertices and arrows to be included, just as when composing a
matrix, and the program takes care of computing the dimensions
of the arrows and realizing the pagesetting. All the user has
to do about the arrows is to specify their type (monomorphism,
pair of adjoint arrows, etc.) and their direction (north,
south-east, etc.); 12 types and 32 directions are available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/borceux/Diagram
%{_texmfdistdir}/tex/generic/borceux/MaxiDiagram
%{_texmfdistdir}/tex/generic/borceux/MicroDiagram
%{_texmfdistdir}/tex/generic/borceux/MiniDiagram
%{_texmfdistdir}/tex/generic/borceux/MultipleArrows
%doc %{_texmfdistdir}/doc/generic/borceux/Diagram_Mode_d_Emploi
%doc %{_texmfdistdir}/doc/generic/borceux/Diagram_Read_Me
%doc %{_texmfdistdir}/doc/generic/borceux/README
%doc %{_texmfdistdir}/doc/generic/borceux/compatibility/OldDiagram
%doc %{_texmfdistdir}/doc/generic/borceux/compatibility/OldMaxiDiagram
%doc %{_texmfdistdir}/doc/generic/borceux/compatibility/OldMicroDiagram
%doc %{_texmfdistdir}/doc/generic/borceux/compatibility/OldMiniDiagram
%doc %{_texmfdistdir}/doc/generic/borceux/compatibility/OldMultipleArrows

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
