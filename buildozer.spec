[app]
title = My Kivy App
package.name = myapp
package.domain = org.mykivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk = 25b
perms = INTERNET

[android:entrypoint]
main = main:MyApp
