#!/bin/bash

extract_ozip() {
    java -jar ozipdecrypt.jar "$1" "$2"
}

create_ext4_image() {
    mke2fs -t ext4 -d "$1" -r / -L EXT4_IMAGE "$2"
}

main() {
    read -p "Enter the path to the Oppo OZIP file: " ozip_path
    if [ ! -f "$ozip_path" ]; then
        echo "Error: OZIP file not found."
        exit 1
    fi

    extract_dir="ozip_extracted"
    mkdir -p "$extract_dir"

    extract_ozip "$ozip_path" "$extract_dir"

    read -p "Enter the path for the output Ext4 image: " output_image
    create_ext4_image "$extract_dir" "$output_image"

    rm -rf "$extract_dir"
}

main "$@"
