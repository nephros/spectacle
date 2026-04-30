--- ../base/testpkg.yaml	2023-12-02 15:24:50.591185072 +0100
+++ testpkg.yaml	2025-04-17 14:51:40.165952978 +0200
@@ -7,6 +7,11 @@ License: BSD
 URL: http://www.testpkg.org/
 Sources:
     - http://www.testpkg.org/testpkg-%{version}.tar.gz
+Patches:
+    - patch-one.diff
+AutoSetup: true
+SetupOptions: -p0 -n %{name}-%{version}
+
 Description: |
     Sample package for spectacle testings, which will be used as
     the base of all testings. In this YAML file, only basic keywords
