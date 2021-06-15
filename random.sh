for f in *.jpg
do
    mv -n "$f" "${f/*/$RANDOM.jpg}"
done
