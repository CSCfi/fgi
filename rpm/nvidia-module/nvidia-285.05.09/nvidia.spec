Name:		nvidia
Version:	285.05.09	
Release:	1%{?dist}
Summary:	NVIDIA kernel module 

Group:		Applications/Communication
License:	Proprietary
#URL:		
Source0:	nvidia-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64

#BuildRequires:	
Requires:	yum
Requires: 	kernel(x86-64) = kernel-2.6.32-131.21.1.el6

%description
NVIDIA binary modules


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
mkdir -p $RPM_BUILD_ROOT/lib/modules/2.6.32-131.17.1.el6.x86_64/kernel/drivers/video

pwd
ls
cp unpack/libGL.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libGL.so.285.05.09
cp unpack/libglx.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/xorg/modules/extensions/libglx.so.285.05.09
cp unpack/libnvidia-tls.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libnvidia-tls.so.285.05.09
cp unpack/tls/libnvidia-tls.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/tls/libnvidia-tls.so.285.05.09
cp unpack/nvidia_drv.so $RPM_BUILD_ROOT/usr/lib64/xorg/modules/drivers/nvidia_drv.so
cp unpack/libnvidia-wfb.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/xorg/modules/libnvidia-wfb.so.285.05.09
cp unpack/libXvMCNVIDIA.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libXvMCNVIDIA.so.285.05.09
cp unpack/libnvidia-ml.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libnvidia-ml.so.285.05.09
cp unpack/libnvidia-cfg.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libnvidia-cfg.so.285.05.09
cp unpack/libcuda.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libcuda.so.285.05.09
cp unpack/libOpenCL.so.1.0.0 $RPM_BUILD_ROOT/usr/lib64/libOpenCL.so.1.0.0
cp unpack/libnvidia-compiler.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libnvidia-compiler.so.285.05.09
cp unpack/libvdpau.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libvdpau.so.285.05.09
cp unpack/libvdpau_trace.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/vdpau/libvdpau_trace.so.285.05.09
cp unpack/libvdpau_nvidia.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/vdpau/libvdpau_nvidia.so.285.05.09
cp unpack/libnvcuvid.so.285.05.09 $RPM_BUILD_ROOT/usr/lib64/libnvcuvid.so.285.05.09
cp unpack/32/libcuda.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libcuda.so.285.05.09
cp unpack/32/libnvidia-ml.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libnvidia-ml.so.285.05.09
cp unpack/32/libOpenCL.so.1.0.0 $RPM_BUILD_ROOT/usr/lib/libOpenCL.so.1.0.0
cp unpack/32/libnvidia-compiler.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libnvidia-compiler.so.285.05.09
cp unpack/32/libGL.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libGL.so.285.05.09
cp unpack/32/libnvidia-glcore.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libnvidia-glcore.so.285.05.09
cp unpack/32/libnvidia-tls.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libnvidia-tls.so.285.05.09
cp unpack/32/tls/libnvidia-tls.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/tls/libnvidia-tls.so.285.05.09
cp unpack/32/libvdpau.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/libvdpau.so.285.05.09
cp unpack/32/libvdpau_trace.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/vdpau/libvdpau_trace.so.285.05.09
cp unpack/32/libvdpau_nvidia.so.285.05.09 $RPM_BUILD_ROOT/usr/lib/vdpau/libvdpau_nvidia.so.285.05.09
cp unpack/kernel/nvidia.ko    $RPM_BUILD_ROOT/lib/modules/2.6.32-131.17.1.el6.x86_64/kernel/drivers/video/nvidia.ko

cp unpack/nvidia-debugdump $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-smi $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-xconfig $RPM_BUILD_ROOT/usr/bin
cp unpack/nvidia-settings $RPM_BUILD_ROOT/usr/bin

cp nvidia-installer-disable-nouveau.conf $RPM_BUILD_ROOT/etc/modprobe.d

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib64/libGL.so.285.05.09
/usr/lib64/xorg/modules/extensions/libglx.so.285.05.09
/usr/lib64/libnvidia-tls.so.285.05.09
/usr/lib64/tls/libnvidia-tls.so.285.05.09
/usr/lib64/xorg/modules/drivers/nvidia_drv.so
/usr/lib64/xorg/modules/libnvidia-wfb.so.285.05.09
/usr/lib64/libXvMCNVIDIA.so.285.05.09
/usr/lib64/libnvidia-ml.so.285.05.09
/usr/lib64/libnvidia-cfg.so.285.05.09
/usr/lib64/libcuda.so.285.05.09
/usr/lib64/libOpenCL.so.1.0.0
/usr/lib64/libnvidia-compiler.so.285.05.09
/usr/lib64/libvdpau.so.285.05.09
/usr/lib64/vdpau/libvdpau_trace.so.285.05.09
/usr/lib64/vdpau/libvdpau_nvidia.so.285.05.09
/usr/lib64/libnvcuvid.so.285.05.09
/usr/lib/libcuda.so.285.05.09
/usr/lib/libnvidia-ml.so.285.05.09
/usr/lib/libOpenCL.so.1.0.0
/usr/lib/libnvidia-compiler.so.285.05.09
/usr/lib/libGL.so.285.05.09
/usr/lib/libnvidia-glcore.so.285.05.09
/usr/lib/libnvidia-tls.so.285.05.09
/usr/lib/tls/libnvidia-tls.so.285.05.09
/usr/lib/libvdpau.so.285.05.09
/usr/lib/vdpau/libvdpau_trace.so.285.05.09
/usr/lib/vdpau/libvdpau_nvidia.so.285.05.09
/lib/modules/2.6.32-131.17.1.el6.x86_64/kernel/drivers/video/nvidia.ko
/usr/bin/nvidia-debugdump
/usr/bin/nvidia-smi
/usr/bin/nvidia-xconfig
/usr/bin/nvidia-settings
/etc/modprobe.d/nvidia-installer-disable-nouveau.conf 

%changelog
* Mon Nov 28 2011 Ulf Tigerstedt <tigerste@csc.fi> 1
- Initial version (NVIDIA 285.05.09



/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libGL.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/extensions/libglx.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-tls.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/tls/libnvidia-tls.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/drivers/nvidia_drv.so
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/xorg/modules/libnvidia-wfb.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libXvMCNVIDIA.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-ml.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-cfg.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libcuda.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libOpenCL.so.1.0.0
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvidia-compiler.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libvdpau.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/vdpau/libvdpau_trace.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/vdpau/libvdpau_nvidia.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib64/libnvcuvid.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libcuda.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-ml.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libOpenCL.so.1.0.0
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-compiler.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libGL.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-glcore.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libnvidia-tls.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/tls/libnvidia-tls.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/libvdpau.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/vdpau/libvdpau_trace.so.285.05.09
/usr/bin/chcon -t textrel_shlib_t /usr/lib/vdpau/libvdpau_nvidia.so.285.05.09

