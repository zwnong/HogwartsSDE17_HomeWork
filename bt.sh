#!/system/bin/sh

 

am start -n com.android.settings/com.android.settings.Settings
sleep 3
input tap 300 200
i=0
count=20
while(($i<$count))
do
	input tap 1190 130
	sleep 5
	i=$(($i+1))
done

