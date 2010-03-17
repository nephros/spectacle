--- output.orig.spec	2010-03-17 21:15:07.000000000 +0800
+++ output.spec	2010-03-17 21:15:07.000000000 +0800
@@ -14,6 +14,8 @@ License:    BSD
 URL:        http://www.testpkg.org/
 Source0:    http://www.testpkg.org/testpkg-%{version}.tar.gz
 Source100:  testpkg.yaml
+Requires(post): /sbin/install-info
+Requires(postun):  /sbin/install-info
 
 %description
 Sample package for spectacle testings, which will be used as
@@ -55,12 +57,19 @@ rm -rf %{buildroot}
 
 
 
+%post
+%install_info --info-dir=%_infodir %{_infodir}/*.info.gz
 
+%postun
+if [ $1 = 0 ] ;then
+%install_info_delete --info-dir=%{_infodir} %{_infodir}/*.info.gz
+fi
 
 
 
 %files
 %defattr(-,root,root,-)
+%{_infodir}/*.info.gz
 # >> files
 # << files
 