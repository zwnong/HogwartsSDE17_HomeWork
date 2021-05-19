adb push ./bt_on_off.sh /data
adb shell
cd data
chmod 777test.sh
nohup ./test.sh &