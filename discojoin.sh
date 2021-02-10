for file in *; do
    cd "$file" &&
    printf "file '%s'\n" ./*.mp3 > mylist.txt &&
    ffmpeg -f concat -safe 0 -i mylist.txt -i cover.jpg -map 0:0 -map 1:0 -metadata:s:v title="cover" -metadata:s:v comment="Cover (Front)" -id3v2_version 3 -write_id3v1 1 -c copy "../$file.mp3" &&
    cd ../;
done
