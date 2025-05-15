--- output.orig.spec	2025-04-17 13:37:20.244159122 +0200
+++ output.spec	2025-04-17 13:37:38.240352380 +0200
@@ -16,6 +16,7 @@ License:    BSD
 URL:        http://www.testpkg.org/
 Source0:    http://www.testpkg.org/testpkg-%{version}.tar.gz
 Source100:  testpkg.yaml
+BuildRequires:  meson
 
 %description
 Sample package for spectacle testings, which will be used as
@@ -41,7 +42,8 @@ This package contains development files 
 # >> build pre
 # << build pre
 
-
+%meson 
+%meson_build
 
 # >> build post
 # << build post
@@ -50,6 +52,7 @@ This package contains development files 
 rm -rf %{buildroot}
 # >> install pre
 # << install pre
+%meson_install
 
 # >> install post
 # << install post
