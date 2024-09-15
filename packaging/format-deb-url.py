#!/usr/bin/env python3
import yaml
import platform


qtc_deb_url_fmt = "https://download.qt.io/{release_type}_releases/qtcreator/{qtcv_maj}/{qtcv_full}/cpack_experimental/qtcreator-opensource-linux-{arch}-{qtcv_full}.deb"

if __name__ == '__main__':
    with open("versions.yaml", 'r') as file:
        versions = yaml.safe_load(file)
        qtc_version = versions['qtc_version']
        qtc_dev_tag = versions.get('qtc_dev_tag', str())

    release = not qtc_dev_tag

    if not release and not (qtc_dev_tag.find("beta") == -1 or qtc_dev_tag.find("rc") == -1):
        raise RuntimeWarning(f"Invalid development tag '{qtc_dev_tag}'. Valid tags contain 'beta' or 'rc'.")

    ver_split = qtc_version.split('.')
    qtc_ver_major = ver_split[0]
    qtc_ver_minor = ver_split[1] if len(ver_split)>1 else 0
    qtc_ver_patch = ver_split[2] if len(ver_split)>2 else 0
    qtc_ver_maj = f"{qtc_ver_major}.{qtc_ver_minor}"
    qtc_ver_full = f"{qtc_ver_maj}.{qtc_ver_patch}"

    if not release:
        qtc_ver_full += f"-{qtc_dev_tag}"

    arch = platform.machine()

    deb_url = qtc_deb_url_fmt.format(release_type = "official" if release else "development",
                                     qtcv_maj = qtc_ver_maj,
                                     qtcv_full = qtc_ver_full,
                                     arch = arch,)

    print(deb_url)
