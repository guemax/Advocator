#!/usr/bin/env bash
help() {
  printf "This script has been written for automating the build of an .ankiaddon file.\n\n"
  echo "Usage: ./build.sh -v 1.30.2"
  printf "Options:\n\n"
  echo "-h        Show help information"
  echo "-v        Build .ankiaddon file for version <version> (int)"
}

while getopts ":hv:" option; do
  case $option in
    v) version=$OPTARG;;
    h)
      help
      exit;;
    \?)
      printf "Error: Invalid option used. See help information for available options:\n\n"
      help
      exit;;
  esac
done

echo "Building .ankiaddon file for Advocator $version:"
echo

addon_file="advocator${version}.ankiaddon"
zip -r "$addon_file" . -i \*.py config.json config.md README.md LICENSE -x venv/\*

echo
echo "File $addon_file has been written successfully."