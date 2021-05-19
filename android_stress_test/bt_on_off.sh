#!/system/bin/sh
am start -n com.android.settings/com.android.settings.Settings
#后台抓取 log 至 logcat.log
# shellcheck disable=SC2034
i=0
cont=20
input tap 700 250