# 
# Do not Edit! Generated by:
# spec-builder version 0.13
# 

Name:       metacity
Summary:    Metacity window manager
Version:    20090115
Group:      User Interface/Desktops
License:    GPLv2+
URL:        http://www.moblin.org
Release:    1%{?dist}
Source0:  metacity-%{version}.tar.bz2
Requires:   startup-notification
Requires:   GConf2
Requires:   dbus-x11
Requires(post):  /sbin/service
Requires(post):  /sbin/chkconfig
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
BuildRequires:  pkgconfig(clutter-0.8)
BuildRequires:  pkgconfig(clutter-glx-0.8)
BuildRequires:  pkgconfig(clutter-x11-0.8)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(sm)
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gettext
BuildRequires:  gnome-common

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Metacity is a simple window manager that integrates nicely with
GNOME 2.


%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{version}
%description devel
Development files for %{name}



%prep
%setup -q -n %{name}-%{version}

%build
# >> build pre
# << build pre
%autogen --disable-static \
    --with-clutter \
    --disable-xinerama

make %{?_smp_mflags}
# >> build post
# << build post

%install
# >> install pre
cp blah bleh
for i in blah:
    mv blh uitppt 
done
# << install pre
rm -rf %{buildroot}
%make_install

# >> install post
# << install post

%find_lang metacity

%clean
rm -rf %{buildroot}
%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/cheese.schemas \
    > /dev/null || :
fi
%preun
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/cheese.schemas \
    > /dev/null || :
fi
%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/cheese.schemas  > /dev/null || :

%postun
/sbin/ldconfig

%files -f metacity.lang
%defattr(-,root,root,-)
# >> files 
%doc COPYING
/some/bin/file
/some/share/file
%{_libdir}/libcairo*.so.0.1
%{_libdir}/libcairo*.so.0
%{_libdir}/foo/some.a
/etc/init.d/blah
%{_libdir}/libfoo.so.2
%{_libdir}/libfoo.so.2.1.0
%{python_sitearch}/foo/bar
%{_datadir}/icons/hicolor/*.png
%{_bindir}/cheese
%{_datadir}/applications/cheese.desktop
%{_datadir}/cheese
%{_datadir}/icons/hicolor/*/apps/cheese.png
%{_datadir}/icons/hicolor/scalable/apps/cheese.svg
%{_sysconfdir}/gconf/schemas/cheese.schemas
%{_libexecdir}/cheese
%{_datadir}/dbus-1/services/org.gnome.Cheese.service


# << files 

%files devel
%defattr(-,root,root,-)
# >> files devel
/some/devel/file
/some/devel/file.so
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/cairo
# << files devel
