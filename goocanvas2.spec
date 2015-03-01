Summary:	Cairo/GTK+3 Canvas
Summary(pl.UTF-8):	Płótno Cairo/GTK+3
Name:		goocanvas2
Version:	2.0.2
Release:	2
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goocanvas/2.0/goocanvas-%{version}.tar.xz
# Source0-md5:	26740994cfa5e57dfb70d40c4ec55200
URL:		http://live.gnome.org/GooCanvas
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygobject-devel >= 2.28
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.28.0
Requires:	gtk+3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GooCanvas is a new canvas widget for GTK+ that uses the Cairo 2D
library for drawing. It has a model/view split, and uses interfaces
for canvas items and views, so you can easily turn any application
object into canvas items.

This version is for GTK+ 3.

%description -l pl.UTF-8
GooCanvas to nowy widget "płótna" dla GTK+ wykorzystujący do rysowania
bibliotekę Cairo 2D. Ma podział model/widok i używa interfejsów dla
elementów i widoków, więc można łatwo zamieniać dowolny obiekt
aplikacji w elementy płótna.

Ta wersja jest przeznaczona dla GTK+ 3.

%package devel
Summary:	Header files for goocanvas
Summary(pl.UTF-8):	Pliki nagłówkowe goocanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.0
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0

%description devel
Header files for goocanvas.

%description devel -l pl.UTF-8
Pliki nagłówkowe goocanvas.

%package static
Summary:	GooCanvas static library
Summary(pl.UTF-8):	Statyczna biblioteka GooCanvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GooCanvas static library.

%description static -l pl.UTF-8
Statyczna biblioteka GooCanvas.

%package apidocs
Summary:	goocanvas API documentation
Summary(pl.UTF-8):	Dokumentacja API goocanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
goocanvas API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API goocanvas.

%package examples
Summary:	Example programs using goocanvas library
Summary(pl.UTF-8):	Przykładowe programy używające biblioteki goocanvas
Group:		X11/Development/Libraries

%description examples
Example programs using goocanvas library.

%description examples -l pl.UTF-8
Przykładowe programy używające biblioteki goocanvas.

%package -n python-%{name}
Summary:	Python binding for GooCanvas 2.x library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GooCanvas 2.x
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject >= 2.28

%description -n python-%{name}
Python binding for GooCanvas 2.x library.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona do biblioteki GooCanvas 2.x.

%prep
%setup -q -n goocanvas-%{version}

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# prepare and install examples
%{__make} clean -C demo
cp demo/*.c demo/*.h demo/*.png $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# obsoleted by pkgconfig support
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%find_lang %{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgoocanvas-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoocanvas-2.0.so.9
%{_libdir}/girepository-1.0/GooCanvas-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoocanvas-2.0.so
%{_includedir}/goocanvas-2.0
%{_datadir}/gir-1.0/GooCanvas-2.0.gir
%{_pkgconfigdir}/goocanvas-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoocanvas-2.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/goocanvas2

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitedir}/gi/overrides/GooCanvas.py[co]
