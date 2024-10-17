Name:           gap-sonata
Version:        2.6
Release:        2.0%{?dist}
Summary:        GAP package for systems of nearrings


License:        GPLv2
URL:            https://www.algebra.uni-linz.ac.at/Sonata/
Source0:        http://www.algebra.uni-linz.ac.at/Sonata/sonata-%{version}/sonata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gap-devel

Provides:       gap-pkg-sonata = %{version}-%{release}
Requires:       gap-core

%description
SONATA stands for "systems of nearrings and their applications".  It
provides methods for the construction and the analysis of finite
nearrings.  A left nearring is an algebra (N;+,*), where (N,+) is a (not
necessarily abelian) group, (N,*) is a semigroup, and x*(y+z) = x*y + x*z
holds for all x,y,z in N.

As a typical example of a nearring, we may consider the set of all
mappings from a group G into G, where the addition is the pointwise
addition of mappings in G, and the multiplication is composition of
functions.  If functions are written on the right of their arguments,
then the left distributive law holds, while the right distributive law
is not satisfied for non-trivial G.

The SONATA package provides methods for the construction and analysis of
finite nearrings.
1. Methods for constructing all endomorphisms and all fixed-point-free
   automorphisms of a given group.
2. Methods for constructing the following nearrings of functions on a
   group G:
   - the nearring of polynomial functions of G (in the sense of
     Lausch-Nöbauer);
   - the nearring of compatible functions of G;
   - distributively generated nearrings such as I(G), A(G), E(G);
   - centralizer nearrings. 
3. A library of all small nearrings (up to order 15) and all small
   nearrings with identity (up to order 31).
4. Functions to obtain solvable fixed-point-free automorphism groups on
   abelian groups, nearfields, planar nearrings, as well as designs from
   those.
5. Various functions to study the structure (size, ideals, N-groups, ...)
   of nearrings, to determine properties of nearring elements, and to
   decide whether two nearrings are isomorphic.
6. If the package XGAP is installed, the lattices of one- and two-sided
   ideals of a nearring can be studied interactively using a graphical
   representation. 

%prep
%setup -q -n sonata

# Fix file encodings
for f in PackageInfo.g README.sonata; do
  iconv -f iso8859-1 -t utf-8 -o ${f}.utf8 $f
  touch -r $f ${f}.utf8
  mv -f ${f}.utf8 $f
done

# Delete KDE Desktop files
find . -name .directory | xargs rm -f

# Delete documentation log files
find . -name \*.log | xargs rm -f

%build
# Compress large data files
gzip --best nr/*.nr nri/*.nr

%install
mkdir -p $RPM_BUILD_ROOT%{_gap_dir}/pkg
cd ..
cp -a sonata $RPM_BUILD_ROOT%{_gap_dir}/pkg
rm -f $RPM_BUILD_ROOT%{_gap_dir}/pkg/sonata/README.sonata
rm -f $RPM_BUILD_ROOT%{_gap_dir}/pkg/sonata/doc/{make_doc,convert.pl}

%post
    %{_bindir}/update-gap-workspace

%postun
    %{_bindir}/update-gap-workspace

%files
%doc README.sonata
%{_gap_dir}/pkg/sonata/

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb  6 2013 Jerry James <loganjerry@gmail.com> - 2.6-1
- New upstream release
- License changed from GPLv2 to GPLv2+

* Mon Sep 17 2012 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Initial RPM
