for entry in `ls $search_dir`; do
    if [ ! -s $entry ] || ! grep -q '[^[:space:]]' "$entry"
    then
        echo $entry
    fi
done