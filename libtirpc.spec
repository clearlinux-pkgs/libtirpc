#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtirpc
Version  : 1.0.1
Release  : 6
URL      : http://downloads.sourceforge.net/project/libtirpc/libtirpc/1.0.1/libtirpc-1.0.1.tar.bz2
Source0  : http://downloads.sourceforge.net/project/libtirpc/libtirpc/1.0.1/libtirpc-1.0.1.tar.bz2
Summary  : Transport Independent RPC Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libtirpc-lib
Requires: libtirpc-data
Requires: libtirpc-doc
Patch1: 0001-Use-vendor-config-files-as-fallback-for-a-stateless-.patch

%description
LIBTIRPC 0.1 FROM SUN'S TIRPCSRC 2.3 29 Aug 1994
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of Open Network
Computing (ONC), and is derived directly from the Solaris 2.3 source.

%package data
Summary: data components for the libtirpc package.
Group: Data

%description data
data components for the libtirpc package.


%package dev
Summary: dev components for the libtirpc package.
Group: Development
Requires: libtirpc-lib
Requires: libtirpc-data
Provides: libtirpc-devel

%description dev
dev components for the libtirpc package.


%package doc
Summary: doc components for the libtirpc package.
Group: Documentation

%description doc
doc components for the libtirpc package.


%package lib
Summary: lib components for the libtirpc package.
Group: Libraries
Requires: libtirpc-data

%description lib
lib components for the libtirpc package.


%prep
%setup -q -n libtirpc-1.0.1
%patch1 -p1

%build
%configure --disable-static --disable-gssapi
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc
cp doc/netconfig %{buildroot}/usr/share/defaults/etc/netconfig
## make_install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/netconfig

%files dev
%defattr(-,root,root,-)
/usr/include/tirpc/netconfig.h
/usr/include/tirpc/rpc/auth.h
/usr/include/tirpc/rpc/auth_des.h
/usr/include/tirpc/rpc/auth_unix.h
/usr/include/tirpc/rpc/clnt.h
/usr/include/tirpc/rpc/clnt_soc.h
/usr/include/tirpc/rpc/clnt_stat.h
/usr/include/tirpc/rpc/des.h
/usr/include/tirpc/rpc/des_crypt.h
/usr/include/tirpc/rpc/key_prot.h
/usr/include/tirpc/rpc/nettype.h
/usr/include/tirpc/rpc/pmap_clnt.h
/usr/include/tirpc/rpc/pmap_prot.h
/usr/include/tirpc/rpc/pmap_rmt.h
/usr/include/tirpc/rpc/raw.h
/usr/include/tirpc/rpc/rpc.h
/usr/include/tirpc/rpc/rpc_com.h
/usr/include/tirpc/rpc/rpc_msg.h
/usr/include/tirpc/rpc/rpcb_clnt.h
/usr/include/tirpc/rpc/rpcb_prot.h
/usr/include/tirpc/rpc/rpcb_prot.x
/usr/include/tirpc/rpc/rpcent.h
/usr/include/tirpc/rpc/svc.h
/usr/include/tirpc/rpc/svc_auth.h
/usr/include/tirpc/rpc/svc_dg.h
/usr/include/tirpc/rpc/svc_mt.h
/usr/include/tirpc/rpc/svc_soc.h
/usr/include/tirpc/rpc/types.h
/usr/include/tirpc/rpc/xdr.h
/usr/include/tirpc/rpcsvc/crypt.h
/usr/include/tirpc/rpcsvc/crypt.x
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
