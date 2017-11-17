#!/bin/bash
name=`grep ^Name *.spec | sed -e "s/^Name:\ //"`
version=`grep ^Version *.spec | sed -e "s/^Version:\ //"`

if [ -e "$name-$version" ] ; then
 echo rm -rf "$name-$version"
fi
mkdir "$name-$version"
cp -r usr/ var/ etc/ $name.spec "$name-$version"
tar --exclude-vcs -cvzf "$name-$version.tar.gz" "$name-$version"
rm -rf "$name-$version"
