--- output.orig.spec	2025-04-17 13:50:10.563850210 +0200
+++ output.spec	2025-04-17 13:50:49.564121721 +0200
@@ -16,6 +16,7 @@ License:    BSD
 URL:        http://www.testpkg.org/
 Source0:    http://www.testpkg.org/testpkg-%{version}.tar.gz
 Source100:  testpkg.yaml
+BuildRequires:  meson
 
 %description
 Sample package for spectacle testings, which will be used as
@@ -42,6 +43,7 @@ This package contains development files 
 # << build pre
 
 
+%meson_build
 
 # >> build post
 # << build post
@@ -50,10 +52,16 @@ This package contains development files 
 rm -rf %{buildroot}
 # >> install pre
 # << install pre
+%meson_install
 
 # >> install post
 # << install post
 
+%check
+# >> check
+%meson_test
+# << check
+
 %files
 %defattr(-,root,root,-)
 # >> files
