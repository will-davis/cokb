pkgname=cokb
pkgver=1.1.0
pkgrel=1
pkgdesc="Onscreen Keyboard for CachyOS and Wayland using kernel level python-uinput and GTK4 Layer Shell"
arch=('any')
depends=('python' 'python-gobject' 'gtk4' 'gtk4-layer-shell' 'python-uinput')
install=${pkgname}.install
source=("main.py"
        "99-cokb-uinput.rules"
        "uinput-cokb.conf"
        "cokb.desktop")
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
    # Executable
    install -Dm755 "${srcdir}/main.py" "${pkgdir}/usr/bin/${pkgname}"
    
    # Kernel Module Load configuration
    install -Dm644 "${srcdir}/uinput-cokb.conf" "${pkgdir}/usr/lib/modules-load.d/${pkgname}.conf"
    
    # Udev rule for seat-based uaccess
    install -Dm644 "${srcdir}/99-cokb-uinput.rules" "${pkgdir}/usr/lib/udev/rules.d/99-cokb-uinput.rules"
    
    # Desktop Entry
    install -Dm644 "${srcdir}/cokb.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}