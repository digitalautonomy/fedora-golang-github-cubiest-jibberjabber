To fix: To build you need to manually clone and generate the tar.gz expected by the spec file.
Spec files uploaded to Fedora's repo auto download the source code. I would fix this later.

```
wget https://github.com/cubiest/jibberjabber/archive/v2.0.zip
unzip v2.0.zip
rm v2.0.zip
tar zcf jibberjabber-2.0.tar.gz jibberjabber-2.0/
rm -rf jibberjabber-2.0/
```

To build this package you would need to install the `golang-x-text-devel` package.

Building the package:
```
fedpkg --release f31 local
```
