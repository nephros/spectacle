--- ../base/testpkg.yaml	2023-12-02 15:24:50.591185072 +0100
+++ testpkg.yaml	2025-04-17 13:50:48.315142950 +0200
@@ -13,7 +13,9 @@ Description: |
     specified, plus with one sub package "devel".
 
 Configure: none
-Builder: none
+Builder: meson
+
+Check: true
 
 SubPackages:
     - Name: devel
