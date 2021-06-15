for file in *.jpg
do
    exiftool -all= "$file" -overwrite_original
done
