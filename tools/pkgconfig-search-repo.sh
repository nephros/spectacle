#!/bin/bash

repos="jolla"
if [ ! -z "$1" ]; then
repos="$@"
else
	printf "I: no repo names given on command line, using default: '%s'\n" "$repos" >/dev/stderr
fi
for repo in $repos
do
	printf "I: Packages from repo %s\n" "$repo" >/dev/stderr
	if [ $EUID = 0 ]; then
		printf "I: Refreshing repo %s\n" "$repo" >/dev/stderr
		zypper ref -r $repo >/dev/null
	else
	printf "W: Not being run as root, can not refresh repo.\n" > /dev/stderr
	fi
	for p in $(zypper search -r $repo devel | awk 'FS="|" {print $2}'|grep devel|sort -u)
	do
		info=$(zypper info --provides "$p" | grep pkgconfig | sed "s/[[:space:]]*//g;s/=.*$//;s/\\(.*\\)/$p,\\1/")
		if [ -z "$info" ]; then
			printf "I: no pkgconfig file in: %s\n" "$p" >/dev/stderr
		else
			printf "%s\n" "$info"
		fi
	done
done
