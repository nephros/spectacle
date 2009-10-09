#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
import __builtin__
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.2.2'
__CHEETAH_versionTuple__ = (2, 2, 2, 'final', 0)
__CHEETAH_genTime__ = 1255063346.8163259
__CHEETAH_genTimestamp__ = 'Fri Oct  9 00:42:26 2009'
__CHEETAH_src__ = 'spec.tmpl'
__CHEETAH_srcLastModified__ = 'Fri Oct  9 00:42:25 2009'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class spec(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(spec, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''# 
# Do not Edit! Generated by:
# spec-builder version 0.13
# 

Name:       ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Name",True) # u'${metadata.Name}' on line 6, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Name}')) # from line 6, col 13.
        write(u'''
Summary:    ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Summary",True) # u'${metadata.Summary}' on line 7, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Summary}')) # from line 7, col 13.
        write(u'''
Version:    ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Version",True) # u'${metadata.Version}' on line 8, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Version}')) # from line 8, col 13.
        write(u'''
Group:      ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Group",True) # u'${metadata.Group}' on line 9, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Group}')) # from line 9, col 13.
        write(u'''
License:    ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.License",True) # u'${metadata.License}' on line 10, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.License}')) # from line 10, col 13.
        write(u'''
URL:        ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.URL",True) # u'${metadata.URL}' on line 11, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.URL}')) # from line 11, col 13.
        write(u'''
Release:    ''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Release",True) # u'${metadata.Release}' on line 12, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Release}')) # from line 12, col 13.
        write(u'''%{?dist}
''')
        #  Sources
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("Sources"): # generated from line 14, col 1
            idx = 0
            for source in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Sources",True): # generated from line 16, col 1
                write(u'''Source''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) # u'${idx}' on line 17, col 7
                if _v is not None: write(_filter(_v, rawExpr=u'${idx}')) # from line 17, col 7.
                write(u''':  ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"source",True) # u'$source' on line 17, col 16
                if _v is not None: write(_filter(_v, rawExpr=u'$source')) # from line 17, col 16.
                write(u'''
''')
                idx = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) + 1
        #  Patches
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("Patches"): # generated from line 22, col 1
            idx = 0
            for patch in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Patches",True): # generated from line 24, col 1
                write(u'''Patch''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) # u'${idx}' on line 25, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${idx}')) # from line 25, col 6.
                write(u''':    ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"patch",True) # u'$patch' on line 25, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$patch')) # from line 25, col 17.
                write(u'''
''')
                idx = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) + 1
        #  Requires
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("Requires"): # generated from line 30, col 1
            for req in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Requires",True): # generated from line 31, col 1
                write(u'''Requires:   ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"req",True) # u'$req' on line 32, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'$req')) # from line 32, col 13.
                write(u'''
''')
        #  Requires(post) etc.
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Info",True): # generated from line 36, col 1
            write(u'''Requires(post):  /sbin/install-info
Requires(postun):  /sbin/install-info
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Service",True): # generated from line 40, col 1
            write(u'''Requires(post):  /sbin/service
Requires(post):  /sbin/chkconfig
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
''')
        #  BuildRequires
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("PkgConfigBR"): # generated from line 47, col 1
            for br in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.PkgConfigBR",True): # generated from line 48, col 1
                write(u'''BuildRequires:  pkgconfig(''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"br",True) # u'$br' on line 49, col 27
                if _v is not None: write(_filter(_v, rawExpr=u'$br')) # from line 49, col 27.
                write(u''')
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("PkgBR"): # generated from line 52, col 1
            for br in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.PkgBR",True): # generated from line 53, col 1
                write(u'''BuildRequires:  ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"br",True) # u'$br' on line 54, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$br')) # from line 54, col 17.
                write(u'''
''')
        write(u'''
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
''')
        _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Description",True) # u'${metadata.Description}' on line 61, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'${metadata.Description}')) # from line 61, col 1.
        write(u'''

''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("AutoSubPackages"): # generated from line 63, col 1
            for sp in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.AutoSubPackages",True): # generated from line 64, col 1
                write(u'''%package ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 65, col 10
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 65, col 10.
                write(u'''
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{version}
%description ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 69, col 14
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 69, col 14.
                write(u'''
Development files for %{name}

''')
        write(u'''
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("SubPackages"): # generated from line 75, col 1
            for sp in VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata.SubPackages",True),"keys",False)(): # generated from line 76, col 1
                write(u'''%package ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 77, col 10
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 77, col 10.
                write(u'''
Summary: ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"SubPackages",True)[VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)],"Summary",True) # u'$metadata.SubPackages[$sp].Summary' on line 78, col 10
                if _v is not None: write(_filter(_v, rawExpr=u'$metadata.SubPackages[$sp].Summary')) # from line 78, col 10.
                write(u'''
Group: ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"SubPackages",True)[VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)],"Group",True) # u'$metadata.SubPackages[$sp].Group' on line 79, col 8
                if _v is not None: write(_filter(_v, rawExpr=u'$metadata.SubPackages[$sp].Group')) # from line 79, col 8.
                write(u'''
''')
                if VFN(VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"SubPackages",True)[VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)],"has_key",False)("Requires"): # generated from line 80, col 1
                    for req in VFN(VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"SubPackages",True)[VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)],"Requires",True): # generated from line 81, col 1
                        write(u'''Requires: ''')
                        _v = VFSL([locals()]+SL+[globals(), __builtin__],"req",True) # u'$req' on line 82, col 11
                        if _v is not None: write(_filter(_v, rawExpr=u'$req')) # from line 82, col 11.
                        write(u'''
''')
                if VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) == "devel": # generated from line 85, col 1
                    write(u'''Requires: %{name} = %{version}-%{version}
''')
        write(u'''
%prep
%setup -q -n %{name}-%{version}
''')
        #  Patches
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("Patches"): # generated from line 94, col 1
            idx = 0
            for patch in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Patches",True): # generated from line 96, col 1
                write(u'''%patch''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) # u'${idx}' on line 97, col 7
                if _v is not None: write(_filter(_v, rawExpr=u'${idx}')) # from line 97, col 7.
                write(u''' -p1
''')
                idx = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) + 1
        write(u'''
%build
# >> build pre
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("build") and VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.build",True),"has_key",False)("pre"): # generated from line 104, col 1
            for l in VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.build.pre",True): # generated from line 105, col 1
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 106, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 106, col 1.
                write(u'''
''')
        write(u'''# << build pre
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)('Configure') and VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Configure",True) == 'autogen': # generated from line 110, col 1
            write(u'''%autogen --disable-static''')
        elif VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)('Configure') and VFSL([locals()]+SL+[globals(), __builtin__],"metadata.Configure",True) == 'reconfigure': # generated from line 112, col 1
            write(u'''%reconfigure --disable-static''')
        else: # generated from line 114, col 1
            write(u'''%configure --disable-static''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("ConfigOptions"): # generated from line 117, col 1
            write(u''' \\\n''')
            length = len(VFSL([locals()]+SL+[globals(), __builtin__],"metadata.ConfigOptions",True))
            idx = 1
            for opt in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.ConfigOptions",True): # generated from line 121, col 1
                write(u'''    --''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"opt",True) # u'$opt' on line 122, col 7
                if _v is not None: write(_filter(_v, rawExpr=u'$opt')) # from line 122, col 7.
                if VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) == VFSL([locals()]+SL+[globals(), __builtin__],"length",True): # generated from line 123, col 1
                    write(u'''
''')
                else: # generated from line 125, col 1
                    write(u''' \\\n''')
                idx = VFSL([locals()]+SL+[globals(), __builtin__],"idx",True) + 1
        else: # generated from line 130, col 1
            write(u'''
''')
        write(u'''
make %{?_smp_mflags}
# >> build post
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("build") and  VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.build",True),"has_key",False)("post"): # generated from line 136, col 1
            for l in VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.build.post",True): # generated from line 137, col 1
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 138, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 138, col 1.
                write(u'''
''')
        write(u'''# << build post

%install
# >> install pre
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("install") and  VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.install",True),"has_key",False)("pre"): # generated from line 145, col 1
            for l in VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.install.pre",True): # generated from line 146, col 1
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 147, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 147, col 1.
                write(u'''
''')
        write(u'''# << install pre
rm -rf %{buildroot}
%make_install

# >> install post
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("install") and VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.install",True),"has_key",False)("post"): # generated from line 155, col 1
            for l in VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.install.post",True): # generated from line 156, col 1
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 157, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 157, col 1.
                write(u'''
''')
        write(u'''# << install post

''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("LocaleName"): # generated from line 162, col 1
            write(u'''%find_lang ''')
            _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.LocaleName",True) # u'${metadata.LocaleName}' on line 163, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'${metadata.LocaleName}')) # from line 163, col 12.
            write(u'''
''')
        write(u'''
%clean
rm -rf %{buildroot}
''')
        #  Pre
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 169, col 1
            write(u'''%pre
if [ "$1" -gt 1 ]; then
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 173, col 1
            for schema in VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schemas",True): # generated from line 174, col 1
                write(u'''  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \\\n    ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"schema",True) # u'$schema' on line 177, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$schema')) # from line 177, col 5.
                write(u''' \\\n    > /dev/null || :
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 181, col 1
            write(u'''fi
''')
        #  PreUn
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 185, col 1
            write(u'''%preun
if [ "$1" -gt 1 ]; then
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 189, col 1
            for schema in VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schemas",True): # generated from line 190, col 1
                write(u'''  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \\\n    ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"schema",True) # u'$schema' on line 193, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$schema')) # from line 193, col 5.
                write(u''' \\\n    > /dev/null || :
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 197, col 1
            write(u'''fi
''')
        #  Post
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Info",True) or VFSL([locals()]+SL+[globals(), __builtin__],"extra.Lib",True) or VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)('PostScripts'): # generated from line 201, col 1
            write(u'''%post
''')
        #  -ldconfog
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Lib",True): # generated from line 205, col 1
            write(u'''/sbin/ldconfig
''')
        #  -Schema
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schema",True): # generated from line 209, col 1
            for schema in VFSL([locals()]+SL+[globals(), __builtin__],"extra.Schemas",True): # generated from line 210, col 1
                write(u'''export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \\\n    ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"schema",True) # u'$schema' on line 213, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'$schema')) # from line 213, col 5.
                write(u'''  > /dev/null || :
''')
        #  -Extra Post Script
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)('PostScripts'): # generated from line 217, col 1
            _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.PostScripts",True) # u'$metadata.PostScripts' on line 218, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'$metadata.PostScripts')) # from line 218, col 1.
            write(u'''
''')
        #  -Info
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Info",True): # generated from line 221, col 1
            for inf in VFSL([locals()]+SL+[globals(), __builtin__],"extra.Infos",True): # generated from line 222, col 1
                write(u'''%install_info ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"inf",True) # u'$inf' on line 223, col 15
                if _v is not None: write(_filter(_v, rawExpr=u'$inf')) # from line 223, col 15.
                write(u''' /usr/share/info/dir
''')
        write(u'''
''')
        #  PostUn
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Info",True) or VFSL([locals()]+SL+[globals(), __builtin__],"extra.Lib",True): # generated from line 228, col 1
            write(u'''%postun
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Lib",True): # generated from line 231, col 1
            write(u'''/sbin/ldconfig
''')
        if VFSL([locals()]+SL+[globals(), __builtin__],"extra.Info",True): # generated from line 234, col 1
            for inf in VFSL([locals()]+SL+[globals(), __builtin__],"extra.Infos",True): # generated from line 235, col 1
                write(u'''%install_info_delete ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"inf",True) # u'$inf' on line 236, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'$inf')) # from line 236, col 22.
                write(u''' /usr/share/info/dir
''')
        write(u'''
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("LocaleName"): # generated from line 240, col 1
            write(u'''%files -f ''')
            _v = VFSL([locals()]+SL+[globals(), __builtin__],"metadata.LocaleName",True) # u'${metadata.LocaleName}' on line 241, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'${metadata.LocaleName}')) # from line 241, col 11.
            write(u'''.lang
''')
        else : # generated from line 242, col 1
            write(u'''%files 
''')
        write(u'''%defattr(-,root,root,-)
# >> files 
''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("files") and VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.files",True),"has_key",False)("main"): # generated from line 247, col 1
            for l in VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.files.main",True): # generated from line 248, col 1
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 249, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 249, col 1.
                write(u'''
''')
        write(u'''# << files 

''')
        if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"metadata",True),"has_key",False)("AutoSubPackages"): # generated from line 254, col 1
            for sp in VFSL([locals()]+SL+[globals(), __builtin__],"metadata.AutoSubPackages",True): # generated from line 255, col 1
                write(u'''%files ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 256, col 8
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 256, col 8.
                write(u'''
%defattr(-,root,root,-)
# >> files ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 258, col 12
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 258, col 12.
                write(u'''
''')
                if VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"has_key",False)("files") and VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content.files",True),"has_key",False)(VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)): # generated from line 259, col 1
                    for l in VFN(VFSL([locals()]+SL+[globals(), __builtin__],"extra.content",True),"files",True)[VFSL([locals()]+SL+[globals(), __builtin__],"sp",True)]: # generated from line 260, col 1
                        _v = VFSL([locals()]+SL+[globals(), __builtin__],"l",True) # u'$l' on line 261, col 1
                        if _v is not None: write(_filter(_v, rawExpr=u'$l')) # from line 261, col 1.
                        write(u'''
''')
                write(u'''# << files ''')
                _v = VFSL([locals()]+SL+[globals(), __builtin__],"sp",True) # u'$sp' on line 264, col 12
                if _v is not None: write(_filter(_v, rawExpr=u'$sp')) # from line 264, col 12.
                write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_spec= 'respond'

## END CLASS DEFINITION

if not hasattr(spec, '_initCheetahAttributes'):
    templateAPIClass = getattr(spec, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(spec)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=spec()).run()


