
for f in $(find ./ -name '*1001.png' -or -name '*1001.exr') ; 
do 
    cp "$f" "./archives/${f}" ; 
done


for f in ./*.png ./*.exr ./**/*.png ./**/*.exr ; 
do 
    cp "$f" "/archives/${f}" ; 
done

for f in *1001.png ; 
do 
    directory="${backup%%_*}/"
    cp "$f" "$directory" ; 
done

for f in $(find "$Beauty" -name *1001.png)
do
  echo "$f"
done
