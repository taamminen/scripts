for file in *.mp3
do
    ffmpeg -i "$file" \
    -c:v mjpeg \
    -metadata:s:v title="Album cover" \
    -metadata:s:v comment="Cover (Front)" \
    -id3v2_version 3 -write_id3v1 1 \
    -ac 2 -ab 128k -ar 44100 \
    "./converted/$file"
done
