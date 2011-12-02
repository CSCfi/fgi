Name:		nvidia-cuda
Version:	285.05.09	
Release:	1%{?dist}
Summary:	NVIDIA kernel module 

%define CUDAVersion 285.05.09
%define Kernelversion 2.6.32-131.21.1.el6


Group:		Applications/Communication
License:	Proprietary
#URL:		
Source0:	nvidia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64

#BuildRequires:	
Requires:	yum
#Requires: 	kernel(x86-64) = kernel-2.6.32-131.21.1.el6
Requires: 	kernel(x86-64) = %{Kernelversion}

%package kmod-nvidia-%{Kernelversion}
Requires: 	kernel(x86-64) = %{Kernelversion}
Requires:	nvidia-cuda
Summary: 	Kernel module for CUDA

%description
NVIDIA binary modules


%description kmod-nvidia-%{Kernelversion}
NVIDIA binary module for %{Kernelversion}


%define debug_package %{nil}

%prep
%setup -q


%build
./configure 
chmod 0755 unpack/*.so.* unpack/32/*.so.*

%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/lib64/xorg/modules/extensions
mkdir -p $RPM_BUILD_ROOT/usr/lib64/xorg/modules/drivers
mkdir -p $RPM_BUILD_ROOT/usr/lib64/tls
mkdir -p $RPM_BUILD_ROOT/usr/lib64/vdpau/
mkdir -p $RPM_BUILD_ROOT/usr/lib/vdpau/
mkdir -p $RPM_BUILD_ROOT/usr/lib/tls
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/modprobe.d
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{Kernelversion}.x86_64/kernel/drivers/video


cp unpack/libGL.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libGL.so.%{CUDAVersion}
cp unpack/libglx.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/xorg/modules/extensions/libglx.so.%{CUDAVersion}
cp unpack/libnvidia-tls.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvidia-tls.so.%{CUDAVersion}
cp unpack/tls/libnvidia-tls.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/tls/libnvidia-tls.so.%{CUDAVersion}
cp unpack/nvidia_drv.so $RPM_BUILD_ROOT/usr/lib64/xorg/modules/drivers/nvidia_drv.so
cp unpack/libnvidia-wfb.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/xorg/modules/libnvidia-wfb.so.%{CUDAVersion}
cp unpack/libXvMCNVIDIA.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libXvMCNVIDIA.so.%{CUDAVersion}
cp unpack/libnvidia-ml.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvidia-ml.so.%{CUDAVersion}
cp unpack/libnvidia-glcore.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvidia-glcore.so.%{CUDAVersion}
cp unpack/libnvidia-cfg.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvidia-cfg.so.%{CUDAVersion}
cp unpack/libcuda.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libcuda.so.%{CUDAVersion}
cp unpack/libOpenCL.so.1.0.0 $RPM_BUILD_ROOT/usr/lib64/libOpenCL.so.1.0.0
cp unpack/libnvidia-compiler.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvidia-compiler.so.%{CUDAVersion}
cp unpack/libvdpau.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libvdpau.so.%{CUDAVersion}
cp unpack/libvdpau_trace.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/vdpau/libvdpau_trace.so.%{CUDAVersion}
cp unpack/libvdpau_nvidia.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/vdpau/libvdpau_nvidia.so.%{CUDAVersion}
cp unpack/libnvcuvid.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib64/libnvcuvid.so.%{CUDAVersion}
cp unpack/32/libcuda.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libcuda.so.%{CUDAVersion}
cp unpack/32/libnvidia-ml.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libnvidia-ml.so.%{CUDAVersion}
cp unpack/32/libOpenCL.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libOpenCL.so.1.0.0
cp unpack/32/libnvidia-compiler.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libnvidia-compiler.so.%{CUDAVersion}
cp unpack/32/libGL.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libGL.so.%{CUDAVersion}
cp unpack/32/libnvidia-glcore.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libnvidia-glcore.so.%{CUDAVersion}
cp unpack/32/libnvidia-tls.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libnvidia-tls.so.%{CUDAVersion}
cp unpack/32/tls/libnvidia-tls.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/tls/libnvidia-tls.so.%{CUDAVersion}
cp unpack/32/libvdpau.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/libvdpau.so.%{CUDAVersion}
cp unpack/32/libvdpau_trace.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/vdpau/libvdpau_trace.so.%{CUDAVersion}
cp unpack/32/libvdpau_nvidia.so.%{CUDAVersion} $RPM_BUILD_ROOT/usr/lib/vdpau/libvdpau_nvidia.so.%{CUDAVersion}
cp unpack/kernel/nvidia.ko    $RPM_BUILD_ROOT/lib/modules/%{Kernelversion}.x86_64/kernel/drivers/video/nvidia.ko

cp unpack/nvidia-debugdump $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-smi $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-xconfig $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-settings $RPM_BUILD_ROOT/usr/bin

cp nvidia-installer-disable-nouveau.conf $RPM_BUILD_ROOT/etc/modprobe.d
cp nvidia-kmod $RPM_BUILD_ROOT/etc/init.d

%clean
rm -rf $RPM_BUILD_ROOT


%post 
/sbin/chkconfig --add nvidia-kmod
/sbin/chkconfig nvidia-kmod on
/sbin/service nvidia-kmod start
/sbin/ldconfig

%preun 
/sbin/chkconfig --del nvidia-kmod

%postun
/sbin/ldconfig

%post kmod-nvidia-%{Kernelversion}
/sbin/depmod -a

%postun kmod-nvidia-%{Kernelversion}
/sbin/depmod -a

%files  kmod-nvidia-%{Kernelversion}
%defattr(-,root,root,-)
/lib/modules/%{Kernelversion}.x86_64/kernel/drivers/video/nvidia.ko


%files
%defattr(-,root,root,-)
/usr/lib64/libGL.so.%{CUDAVersion}
/usr/lib64/xorg/modules/extensions/libglx.so.%{CUDAVersion}
/usr/lib64/libnvidia-tls.so.%{CUDAVersion}
/usr/lib64/tls/libnvidia-tls.so.%{CUDAVersion}
/usr/lib64/xorg/modules/drivers/nvidia_drv.so
/usr/lib64/xorg/modules/libnvidia-wfb.so.%{CUDAVersion}
/usr/lib64/libXvMCNVIDIA.so.%{CUDAVersion}
/usr/lib64/libnvidia-ml.so.%{CUDAVersion}
/usr/lib64/libnvidia-glcore.so.%{CUDAVersion}
/usr/lib64/libnvidia-cfg.so.%{CUDAVersion}
/usr/lib64/libcuda.so.%{CUDAVersion}
/usr/lib64/libOpenCL.so.1.0.0
/usr/lib64/libnvidia-compiler.so.%{CUDAVersion}
/usr/lib64/libvdpau.so.%{CUDAVersion}
/usr/lib64/vdpau/libvdpau_trace.so.%{CUDAVersion}
/usr/lib64/vdpau/libvdpau_nvidia.so.%{CUDAVersion}
/usr/lib64/libnvcuvid.so.%{CUDAVersion}
/usr/lib/libcuda.so.%{CUDAVersion}
/usr/lib/libnvidia-ml.so.%{CUDAVersion}
/usr/lib/libOpenCL.so.1.0.0
/usr/lib/libnvidia-compiler.so.%{CUDAVersion}
/usr/lib/libGL.so.%{CUDAVersion}
/usr/lib/libnvidia-glcore.so.%{CUDAVersion}
/usr/lib/libnvidia-tls.so.%{CUDAVersion}
/usr/lib/tls/libnvidia-tls.so.%{CUDAVersion}
/usr/lib/libvdpau.so.%{CUDAVersion}
/usr/lib/vdpau/libvdpau_trace.so.%{CUDAVersion}
/usr/lib/vdpau/libvdpau_nvidia.so.%{CUDAVersion}
/usr/bin/nvidia-debugdump
/usr/bin/nvidia-smi
/usr/bin/nvidia-xconfig
/usr/bin/nvidia-settings
/etc/modprobe.d/nvidia-installer-disable-nouveau.conf 
/etc/init.d/nvidia-kmod

%changelog
* Mon Nov 28 2011 Ulf Tigerstedt <tigerste@csc.fi> 1
- Initial version (NVIDIA 285.05.09



/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libGL.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/extensions/libglx.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-tls.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/tls/libnvidia-tls.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/drivers/nvidia_drv.so
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/libnvidia-wfb.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libXvMCNVIDIA.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-ml.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-cfg.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libcuda.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libOpenCL.so.1.0.0
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-compiler.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libvdpau.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/vdpau/libvdpau_trace.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/vdpau/libvdpau_nvidia.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvcuvid.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libcuda.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-ml.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libOpenCL.so.1.0.0
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-compiler.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libGL.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-glcore.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-tls.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/tls/libnvidia-tls.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libvdpau.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/vdpau/libvdpau_trace.so.%{CUDAVersion}
/usr/bin/chcon -t textrel_shlib_t /usr/lib/vdpau/libvdpau_nvidia.so.%{CUDAVersion}

