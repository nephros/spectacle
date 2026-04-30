--- output.orig.spec	2025-04-17 15:09:06.562376149 +0200
+++ output.spec	2025-04-17 15:09:08.025366277 +0200
@@ -16,6 +16,7 @@ License:    BSD
 URL:        http://www.testpkg.org/
 Source0:    http://www.testpkg.org/testpkg-%{version}.tar.gz
 Source100:  testpkg.yaml
+Patch0:     patch-one.diff
 
 %description
 Sample package for spectacle testings, which will be used as
@@ -32,7 +33,7 @@ Requires:   %{name} = %{version}-%{relea
 This package contains development files for %{name}.
 
 %prep
-%setup -q -n %{name}-%{version}
+%autosetup -p0 -n %{name}-%{version}
 
 # >> setup
 # << setup
