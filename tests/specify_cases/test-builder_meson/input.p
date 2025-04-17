--- ../base/testpkg.yaml	2023-12-02 15:24:50.591185072 +0100
+++ testpkg.yaml	2025-04-17 13:37:37.035272959 +0200
@@ -12,8 +12,8 @@ Description: |
     the base of all testings. In this YAML file, only basic keywords
     specified, plus with one sub package "devel".
 
-Configure: none
-Builder: none
+Configure: meson
+Builder: meson
 
 SubPackages:
     - Name: devel
