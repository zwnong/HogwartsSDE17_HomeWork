2021-03-18 08:21:38:823 [Appium] Welcome to Appium v1.20.0
2021-03-18 08:21:38:824 [Appium] Non-default server args:
2021-03-18 08:21:38:824 [Appium]   logFile: appium.md
2021-03-18 08:21:38:875 [Appium] Appium REST http interface listener started on 0.0.0.0:4723
2021-03-18 08:21:43:367 [HTTP] Request idempotency key: 1b8bc1b5-22f2-49a0-8401-e71f8b16f33e
2021-03-18 08:21:43:416 [HTTP] --> POST /wd/hub/session
2021-03-18 08:21:43:417 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:21:43:419 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:21:43:458 [BaseDriver] Event 'newSessionRequested' logged at 1616055703419 (16:21:43 GMT+0800 (中国标准时间))
2021-03-18 08:21:44:197 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:21:44:199 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:21:44:200 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:21:44:200 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:21:44:200 [BaseDriver]     "platformName": "Android",
2021-03-18 08:21:44:201 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:21:44:201 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:21:44:201 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:21:44:201 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:21:44:202 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:21:44:202 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:21:44:202 [BaseDriver]     "appium:noReset": true
2021-03-18 08:21:44:202 [BaseDriver]   },
2021-03-18 08:21:44:203 [BaseDriver]   "firstMatch": [
2021-03-18 08:21:44:203 [BaseDriver]     {}
2021-03-18 08:21:44:203 [BaseDriver]   ]
2021-03-18 08:21:44:203 [BaseDriver] }
2021-03-18 08:21:44:229 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:21:44:230 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:21:44:231 [BaseDriver] Session created with session id: 2bc662fb-41b0-471a-a37a-98d0d4133be8
2021-03-18 08:21:44:232 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:21:44:238 [ADB] Found 1 'build-tools' folders under 'E:\Android\android-sdk' (newest first):
2021-03-18 08:21:44:240 [ADB]     E:/Android/android-sdk/build-tools/29.0.3
2021-03-18 08:21:44:241 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:21:44:242 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:21:45:198 [AndroidDriver] Retrieving device list
2021-03-18 08:21:45:199 [ADB] Trying to find a connected android device
2021-03-18 08:21:45:200 [ADB] Getting connected devices
2021-03-18 08:21:45:530 [ADB] No connected devices have been detected
2021-03-18 08:21:45:531 [ADB] Could not find online devices
2021-03-18 08:21:45:531 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:45:531 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:46:069 [ADB] Getting connected devices
2021-03-18 08:21:46:399 [ADB] No connected devices have been detected
2021-03-18 08:21:46:399 [ADB] Could not find online devices
2021-03-18 08:21:46:399 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:46:400 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:46:928 [ADB] Getting connected devices
2021-03-18 08:21:47:261 [ADB] No connected devices have been detected
2021-03-18 08:21:47:261 [ADB] Could not find online devices
2021-03-18 08:21:47:261 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:47:262 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:47:795 [ADB] Getting connected devices
2021-03-18 08:21:48:122 [ADB] No connected devices have been detected
2021-03-18 08:21:48:123 [ADB] Could not find online devices
2021-03-18 08:21:48:123 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:48:123 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:48:658 [ADB] Getting connected devices
2021-03-18 08:21:48:986 [ADB] No connected devices have been detected
2021-03-18 08:21:48:987 [ADB] Could not find online devices
2021-03-18 08:21:48:987 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:48:988 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:49:518 [ADB] Getting connected devices
2021-03-18 08:21:49:859 [ADB] No connected devices have been detected
2021-03-18 08:21:49:859 [ADB] Could not find online devices
2021-03-18 08:21:49:859 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:49:860 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:50:412 [ADB] Getting connected devices
2021-03-18 08:21:50:751 [ADB] No connected devices have been detected
2021-03-18 08:21:50:752 [ADB] Could not find online devices
2021-03-18 08:21:50:752 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:50:752 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:51:294 [ADB] Getting connected devices
2021-03-18 08:21:51:695 [ADB] No connected devices have been detected
2021-03-18 08:21:51:695 [ADB] Could not find online devices
2021-03-18 08:21:51:695 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:51:696 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:52:228 [ADB] Getting connected devices
2021-03-18 08:21:52:554 [ADB] No connected devices have been detected
2021-03-18 08:21:52:555 [ADB] Could not find online devices
2021-03-18 08:21:52:555 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:52:555 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:53:091 [ADB] Getting connected devices
2021-03-18 08:21:53:419 [ADB] No connected devices have been detected
2021-03-18 08:21:53:419 [ADB] Could not find online devices
2021-03-18 08:21:53:420 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:53:420 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:53:947 [ADB] Getting connected devices
2021-03-18 08:21:54:272 [ADB] No connected devices have been detected
2021-03-18 08:21:54:272 [ADB] Could not find online devices
2021-03-18 08:21:54:273 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:54:273 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:54:811 [ADB] Getting connected devices
2021-03-18 08:21:55:152 [ADB] No connected devices have been detected
2021-03-18 08:21:55:153 [ADB] Could not find online devices
2021-03-18 08:21:55:153 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:55:153 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:55:684 [ADB] Getting connected devices
2021-03-18 08:21:56:012 [ADB] No connected devices have been detected
2021-03-18 08:21:56:013 [ADB] Could not find online devices
2021-03-18 08:21:56:013 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:56:013 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:56:540 [ADB] Getting connected devices
2021-03-18 08:21:56:882 [ADB] No connected devices have been detected
2021-03-18 08:21:56:883 [ADB] Could not find online devices
2021-03-18 08:21:56:883 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:56:884 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:57:407 [ADB] Getting connected devices
2021-03-18 08:21:57:742 [ADB] No connected devices have been detected
2021-03-18 08:21:57:743 [ADB] Could not find online devices
2021-03-18 08:21:57:743 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:57:744 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:58:272 [ADB] Getting connected devices
2021-03-18 08:21:58:611 [ADB] No connected devices have been detected
2021-03-18 08:21:58:614 [ADB] Could not find online devices
2021-03-18 08:21:58:614 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:58:615 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:21:59:167 [ADB] Getting connected devices
2021-03-18 08:21:59:510 [ADB] No connected devices have been detected
2021-03-18 08:21:59:512 [ADB] Could not find online devices
2021-03-18 08:21:59:512 [ADB] Reconnecting adb (target offline)
2021-03-18 08:21:59:513 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:22:00:054 [ADB] Getting connected devices
2021-03-18 08:22:00:403 [ADB] No connected devices have been detected
2021-03-18 08:22:00:405 [ADB] Could not find online devices
2021-03-18 08:22:00:405 [ADB] Reconnecting adb (target offline)
2021-03-18 08:22:00:405 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:22:00:949 [ADB] Getting connected devices
2021-03-18 08:22:01:278 [ADB] No connected devices have been detected
2021-03-18 08:22:01:279 [ADB] Could not find online devices
2021-03-18 08:22:01:280 [ADB] Reconnecting adb (target offline)
2021-03-18 08:22:01:280 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 reconnect offline'
2021-03-18 08:22:01:865 [ADB] Getting connected devices
2021-03-18 08:22:02:489 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:22:02:491 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:22:02:492 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:22:02:493 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:22:02:871 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:22:02:872 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:22:03:203 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:22:03:204 [ADB] Device API level: 22
2021-03-18 08:22:03:204 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:22:03:205 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:22:03:543 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:22:03:896 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:22:03:897 [ADB] Getting install status for io.appium.settings
2021-03-18 08:22:03:897 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:22:04:348 [ADB] 'io.appium.settings' is installed
2021-03-18 08:22:04:350 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:22:04:350 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:22:04:762 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:22:04:763 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:22:04:763 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:22:04:764 [ADB] Using ps-based PID detection
2021-03-18 08:22:04:764 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:22:05:102 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:22:05:437 [AndroidDriver] Granting permissions SET_ANIMATION_SCALE,CHANGE_CONFIGURATION,ACCESS_FINE_LOCATION to 'io.appium.settings'
2021-03-18 08:22:05:438 [ADB] Granting permissions ["android.permission.SET_ANIMATION_SCALE","android.permission.CHANGE_CONFIGURATION","android.permission.ACCESS_FINE_LOCATION"] to 'io.appium.settings'
2021-03-18 08:22:05:439 [ADB] Got the following command chunks to execute: [["pm","grant","io.appium.settings","android.permission.SET_ANIMATION_SCALE",";","pm","grant","io.appium.settings","android.permission.CHANGE_CONFIGURATION",";","pm","grant","io.appium.settings","android.permission.ACCESS_FINE_LOCATION",";"]]
2021-03-18 08:22:05:439 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell pm grant io.appium.settings android.permission.SET_ANIMATION_SCALE ; pm grant io.appium.settings android.permission.CHANGE_CONFIGURATION ; pm grant io.appium.settings android.permission.ACCESS_FINE_LOCATION ;'
2021-03-18 08:22:06:727 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:22:06:728 [ADB] Using ps-based PID detection
2021-03-18 08:22:06:729 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:22:07:065 [ADB] Starting Appium Settings app
2021-03-18 08:22:07:066 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -n io.appium.settings/.Settings -a android.intent.action.MAIN -c android.intent.category.LAUNCHER'
2021-03-18 08:22:07:840 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:22:07:841 [ADB] Using ps-based PID detection
2021-03-18 08:22:07:842 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:22:08:193 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:22:08:843 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:22:09:263 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:22:09:265 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:22:09:265 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:22:09:625 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:22:09:626 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:22:09:627 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:22:09:694 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:22:09:696 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:22:10:324 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:22:10:326 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:22:10:327 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:22:10:696 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:22:10:697 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:22:10:704 [WD Proxy] socket hang up
2021-03-18 08:22:11:204 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:22:11:714 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:22:11:715 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:22:11:724 [WD Proxy] socket hang up
2021-03-18 08:22:12:725 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:22:12:726 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:22:12:794 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:22:12:795 [UiAutomator2] The initialization of the instrumentation process took 2468ms
2021-03-18 08:22:12:795 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:22:12:796 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:22:12:831 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8"}}
2021-03-18 08:22:12:832 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:22:12:844 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/appium/device/info] with no body
2021-03-18 08:22:12:857 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:22:12:857 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:22:13:192 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:22:13:193 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:22:13:193 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:22:17:548 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/appium/device/pixel_ratio] with no body
2021-03-18 08:22:17:555 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":1.5}
2021-03-18 08:22:17:556 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:22:17:557 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/appium/device/system_bars] with no body
2021-03-18 08:22:17:564 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":{"statusBar":38}}
2021-03-18 08:22:17:565 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:22:17:566 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/window/current/size] with no body
2021-03-18 08:22:17:575 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":{"height":1280,"width":720}}
2021-03-18 08:22:17:576 [Appium] New AndroidUiautomator2Driver session created successfully, session 2bc662fb-41b0-471a-a37a-98d0d4133be8 added to master session list
2021-03-18 08:22:17:576 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:22:17:577 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:22:17:578 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:22:17:579 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:22:17:586 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":null}
2021-03-18 08:22:17:588 [BaseDriver] Event 'newSessionStarted' logged at 1616055737587 (16:22:17 GMT+0800 (中国标准时间))
2021-03-18 08:22:17:588 [W3C (2bc662fb)] Cached the protocol value 'W3C' for the new session 2bc662fb-41b0-471a-a37a-98d0d4133be8
2021-03-18 08:22:17:589 [W3C (2bc662fb)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:22:17:613 [HTTP] <-- POST /wd/hub/session 200 34200 ms - 1080
2021-03-18 08:22:17:614 [HTTP] 
2021-03-18 08:22:17:622 [HTTP] --> POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/timeouts
2021-03-18 08:22:17:622 [HTTP] {"implicit":10000}
2021-03-18 08:22:17:625 [W3C (2bc662fb)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:17:625 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:22:17:626 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:22:17:626 [W3C (2bc662fb)] Responding to client with driver.timeouts() result: null
2021-03-18 08:22:17:628 [HTTP] <-- POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/timeouts 200 5 ms - 14
2021-03-18 08:22:17:628 [HTTP] 
2021-03-18 08:22:17:653 [HTTP] --> POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/element
2021-03-18 08:22:17:655 [HTTP] {"using":"function.get_yaml_data('main_page')['locator']","value":"function.get_yaml_data('main_page')['element']"}
2021-03-18 08:22:17:661 [W3C (2bc662fb)] Calling AppiumDriver.findElement() with args: ["function.get_yaml_data('main_page')['locator']","function.get_yaml_data('main_page')['element']","2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:17:662 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-18 08:22:17:768 [W3C (2bc662fb)] Encountered internal error running command: InvalidSelectorError: Locator Strategy 'function.get_yaml_data('main_page')['locator']' is not supported for this session
2021-03-18 08:22:17:770 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.validateLocatorStrategy (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:392:13)
2021-03-18 08:22:17:771 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.findElOrElsWithProcessing (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\commands\find.js:31:8)
2021-03-18 08:22:17:771 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.findElement (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\commands\find.js:53:21)
2021-03-18 08:22:17:772 [W3C (2bc662fb)]     at commandExecutor (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:334:9)
2021-03-18 08:22:17:773 [W3C (2bc662fb)]     at C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:129:12
2021-03-18 08:22:17:775 [W3C (2bc662fb)]     at AsyncLock._promiseTry (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:253:31)
2021-03-18 08:22:17:776 [W3C (2bc662fb)]     at exec (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:128:9)
2021-03-18 08:22:17:776 [W3C (2bc662fb)]     at AsyncLock.acquire (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:144:3)
2021-03-18 08:22:17:777 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.executeCommand (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:347:39)
2021-03-18 08:22:17:778 [W3C (2bc662fb)]     at AppiumDriver.executeCommand (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\lib\appium.js:547:36)
2021-03-18 08:22:17:781 [W3C (2bc662fb)]     at processTicksAndRejections (internal/process/task_queues.js:93:5)
2021-03-18 08:22:17:781 [W3C (2bc662fb)]     at asyncHandler (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\protocol\protocol.js:297:21)
2021-03-18 08:22:17:783 [HTTP] <-- POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/element 400 129 ms - 2160
2021-03-18 08:22:17:784 [HTTP] 
2021-03-18 08:22:17:787 [HTTP] --> POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/elements
2021-03-18 08:22:17:788 [HTTP] {"using":"xpath","value":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]"}
2021-03-18 08:22:17:792 [W3C (2bc662fb)] Calling AppiumDriver.findElements() with args: ["xpath","//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:17:792 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-18 08:22:17:794 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-18 08:22:17:795 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:17:796 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:19:586 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:19:588 [BaseDriver] Waited for 1791 ms so far
2021-03-18 08:22:20:088 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:20:089 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:20:154 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:20:155 [BaseDriver] Waited for 2359 ms so far
2021-03-18 08:22:20:657 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:20:658 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:20:794 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:20:795 [BaseDriver] Waited for 2999 ms so far
2021-03-18 08:22:21:296 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:21:297 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:21:493 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:21:494 [BaseDriver] Waited for 3698 ms so far
2021-03-18 08:22:21:996 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:21:997 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:22:048 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:22:049 [BaseDriver] Waited for 4253 ms so far
2021-03-18 08:22:22:552 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:22:553 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:22:605 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:22:606 [BaseDriver] Waited for 4810 ms so far
2021-03-18 08:22:23:108 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:23:109 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:23:176 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:23:177 [BaseDriver] Waited for 5381 ms so far
2021-03-18 08:22:23:679 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:23:680 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:23:733 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:23:734 [BaseDriver] Waited for 5938 ms so far
2021-03-18 08:22:24:235 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:24:237 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:24:288 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:24:289 [BaseDriver] Waited for 6493 ms so far
2021-03-18 08:22:24:790 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:24:791 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:24:958 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:24:959 [BaseDriver] Waited for 7163 ms so far
2021-03-18 08:22:25:462 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:25:463 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:25:533 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:25:534 [BaseDriver] Waited for 7738 ms so far
2021-03-18 08:22:26:035 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:26:036 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:26:509 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:26:510 [BaseDriver] Waited for 8714 ms so far
2021-03-18 08:22:27:011 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:27:012 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:27:075 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:27:076 [BaseDriver] Waited for 9280 ms so far
2021-03-18 08:22:27:577 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:27:579 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:27:630 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:27:631 [BaseDriver] Waited for 9835 ms so far
2021-03-18 08:22:28:134 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:28:135 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_agree\" and @text=\"同意\"]","context":"","multiple":true}
2021-03-18 08:22:28:187 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:28:188 [W3C (2bc662fb)] Responding to client with driver.findElements() result: []
2021-03-18 08:22:28:189 [HTTP] <-- POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/elements 200 10401 ms - 12
2021-03-18 08:22:28:189 [HTTP] 
2021-03-18 08:22:28:197 [HTTP] --> POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/elements
2021-03-18 08:22:28:198 [HTTP] {"using":"xpath","value":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]"}
2021-03-18 08:22:28:199 [W3C (2bc662fb)] Calling AppiumDriver.findElements() with args: ["xpath","//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:28:199 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-18 08:22:28:199 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-18 08:22:28:200 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:28:200 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:28:252 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:28:253 [BaseDriver] Waited for 53 ms so far
2021-03-18 08:22:28:755 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:28:756 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:28:811 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:28:813 [BaseDriver] Waited for 613 ms so far
2021-03-18 08:22:29:314 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:29:316 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:29:380 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:29:381 [BaseDriver] Waited for 1181 ms so far
2021-03-18 08:22:29:882 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:29:884 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:29:937 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:29:938 [BaseDriver] Waited for 1738 ms so far
2021-03-18 08:22:30:439 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:30:440 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:30:496 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:30:497 [BaseDriver] Waited for 2297 ms so far
2021-03-18 08:22:30:998 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:30:999 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:31:078 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:31:079 [BaseDriver] Waited for 2879 ms so far
2021-03-18 08:22:31:580 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:31:581 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:31:681 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:31:682 [BaseDriver] Waited for 3482 ms so far
2021-03-18 08:22:32:182 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:32:184 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:32:241 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:32:242 [BaseDriver] Waited for 4043 ms so far
2021-03-18 08:22:32:744 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:32:745 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:32:800 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:32:801 [BaseDriver] Waited for 4601 ms so far
2021-03-18 08:22:33:304 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:33:306 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:33:356 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:33:357 [BaseDriver] Waited for 5157 ms so far
2021-03-18 08:22:33:857 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:33:859 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:33:910 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:33:911 [BaseDriver] Waited for 5711 ms so far
2021-03-18 08:22:34:412 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:34:413 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:34:463 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:34:464 [BaseDriver] Waited for 6264 ms so far
2021-03-18 08:22:34:966 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:34:967 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:35:018 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:35:019 [BaseDriver] Waited for 6819 ms so far
2021-03-18 08:22:35:520 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:35:521 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:35:572 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:35:574 [BaseDriver] Waited for 7373 ms so far
2021-03-18 08:22:36:076 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:36:077 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:36:128 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:36:129 [BaseDriver] Waited for 7929 ms so far
2021-03-18 08:22:36:630 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:36:631 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:36:880 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:36:882 [BaseDriver] Waited for 8681 ms so far
2021-03-18 08:22:37:383 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:37:384 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:37:568 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:37:569 [BaseDriver] Waited for 9369 ms so far
2021-03-18 08:22:38:070 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:38:071 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:38:193 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:38:194 [BaseDriver] Waited for 9994 ms so far
2021-03-18 08:22:38:695 [WD Proxy] Matched '/elements' to command name 'findElements'
2021-03-18 08:22:38:696 [WD Proxy] Proxying [POST /elements] to [POST http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8/elements] with body: {"strategy":"xpath","selector":"//android.widget.TextView[@resource-id=\"com.xueqiu.android:id/tv_left\" and @text=\"取消\"]","context":"","multiple":true}
2021-03-18 08:22:38:751 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":[]}
2021-03-18 08:22:38:752 [W3C (2bc662fb)] Responding to client with driver.findElements() result: []
2021-03-18 08:22:38:753 [HTTP] <-- POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/elements 200 10556 ms - 12
2021-03-18 08:22:38:754 [HTTP] 
2021-03-18 08:22:38:757 [HTTP] --> POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/element
2021-03-18 08:22:38:757 [HTTP] {"using":"function.get_yaml_data('main_page')['locator']","value":"function.get_yaml_data('main_page')['element']"}
2021-03-18 08:22:38:758 [W3C (2bc662fb)] Calling AppiumDriver.findElement() with args: ["function.get_yaml_data('main_page')['locator']","function.get_yaml_data('main_page')['element']","2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:38:758 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-18 08:22:38:760 [W3C (2bc662fb)] Encountered internal error running command: InvalidSelectorError: Locator Strategy 'function.get_yaml_data('main_page')['locator']' is not supported for this session
2021-03-18 08:22:38:760 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.validateLocatorStrategy (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:392:13)
2021-03-18 08:22:38:762 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.findElOrElsWithProcessing (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\commands\find.js:31:8)
2021-03-18 08:22:38:763 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.findElement (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\commands\find.js:53:21)
2021-03-18 08:22:38:763 [W3C (2bc662fb)]     at commandExecutor (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:334:9)
2021-03-18 08:22:38:763 [W3C (2bc662fb)]     at C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:129:12
2021-03-18 08:22:38:764 [W3C (2bc662fb)]     at AsyncLock._promiseTry (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:253:31)
2021-03-18 08:22:38:764 [W3C (2bc662fb)]     at exec (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:128:9)
2021-03-18 08:22:38:765 [W3C (2bc662fb)]     at AsyncLock.acquire (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\async-lock\lib\index.js:144:3)
2021-03-18 08:22:38:765 [W3C (2bc662fb)]     at AndroidUiautomator2Driver.executeCommand (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\basedriver\driver.js:347:39)
2021-03-18 08:22:38:766 [W3C (2bc662fb)]     at AppiumDriver.executeCommand (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\lib\appium.js:547:36)
2021-03-18 08:22:38:766 [W3C (2bc662fb)]     at processTicksAndRejections (internal/process/task_queues.js:93:5)
2021-03-18 08:22:38:767 [W3C (2bc662fb)]     at asyncHandler (C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\appium-base-driver\lib\protocol\protocol.js:297:21)
2021-03-18 08:22:38:768 [HTTP] <-- POST /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8/element 400 10 ms - 2160
2021-03-18 08:22:38:768 [HTTP] 
2021-03-18 08:22:39:011 [HTTP] --> DELETE /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8
2021-03-18 08:22:39:012 [HTTP] {}
2021-03-18 08:22:39:013 [W3C (2bc662fb)] Calling AppiumDriver.deleteSession() with args: ["2bc662fb-41b0-471a-a37a-98d0d4133be8"]
2021-03-18 08:22:39:013 [BaseDriver] Event 'quitSessionRequested' logged at 1616055759013 (16:22:39 GMT+0800 (中国标准时间))
2021-03-18 08:22:39:013 [Appium] Removing session 2bc662fb-41b0-471a-a37a-98d0d4133be8 from our master session list
2021-03-18 08:22:39:014 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:22:39:015 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:22:39:015 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:22:39:015 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/9f7d3640-e8ba-4a01-9527-80cbcf58bbb8] with no body
2021-03-18 08:22:39:022 [WD Proxy] Got response with status 200: {"sessionId":"9f7d3640-e8ba-4a01-9527-80cbcf58bbb8","value":null}
2021-03-18 08:22:39:022 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:22:39:320 [Instrumentation] .
2021-03-18 08:22:39:501 [Instrumentation] Time: 28.099
2021-03-18 08:22:39:503 [Instrumentation] 
2021-03-18 08:22:39:503 [Instrumentation] OK (1 test)
2021-03-18 08:22:39:710 [Instrumentation] The process has exited with code 0
2021-03-18 08:22:39:711 [Logcat] Stopping logcat capture
2021-03-18 08:22:39:716 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:22:39:716 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:22:40:052 [BaseDriver] Event 'quitSessionFinished' logged at 1616055760052 (16:22:40 GMT+0800 (中国标准时间))
2021-03-18 08:22:40:053 [W3C (2bc662fb)] Received response: null
2021-03-18 08:22:40:053 [W3C (2bc662fb)] But deleting session, so not returning
2021-03-18 08:22:40:054 [W3C (2bc662fb)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:22:40:055 [HTTP] <-- DELETE /wd/hub/session/2bc662fb-41b0-471a-a37a-98d0d4133be8 200 1044 ms - 14
2021-03-18 08:22:40:055 [HTTP] 
2021-03-18 08:27:25:884 [HTTP] Request idempotency key: 42e7070c-eac0-47c8-8c82-23a223485bec
2021-03-18 08:27:25:886 [HTTP] --> POST /wd/hub/session
2021-03-18 08:27:25:887 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:27:25:888 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:27:25:888 [BaseDriver] Event 'newSessionRequested' logged at 1616056045888 (16:27:25 GMT+0800 (中国标准时间))
2021-03-18 08:27:25:889 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:27:25:890 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:27:25:890 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:27:25:891 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:27:25:891 [BaseDriver]     "platformName": "Android",
2021-03-18 08:27:25:892 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:27:25:892 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:27:25:893 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:27:25:893 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:27:25:894 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:27:25:894 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:27:25:896 [BaseDriver]     "appium:noReset": true
2021-03-18 08:27:25:898 [BaseDriver]   },
2021-03-18 08:27:25:898 [BaseDriver]   "firstMatch": [
2021-03-18 08:27:25:899 [BaseDriver]     {}
2021-03-18 08:27:25:899 [BaseDriver]   ]
2021-03-18 08:27:25:899 [BaseDriver] }
2021-03-18 08:27:25:906 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:27:25:907 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:27:25:907 [BaseDriver] Session created with session id: ef1169d2-2308-4415-a827-c4404df28fea
2021-03-18 08:27:25:908 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:27:25:909 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:27:25:910 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:27:26:249 [AndroidDriver] Retrieving device list
2021-03-18 08:27:26:250 [ADB] Trying to find a connected android device
2021-03-18 08:27:26:251 [ADB] Getting connected devices
2021-03-18 08:27:26:573 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:27:26:574 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:27:26:576 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:27:26:576 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:27:26:898 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:27:26:899 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:27:27:235 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:27:27:236 [ADB] Device API level: 22
2021-03-18 08:27:27:236 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:27:27:237 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:27:27:563 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:27:27:896 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:27:27:897 [ADB] Getting install status for io.appium.settings
2021-03-18 08:27:27:897 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:27:28:232 [ADB] 'io.appium.settings' is installed
2021-03-18 08:27:28:234 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:27:28:235 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:27:28:600 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:27:28:601 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:27:28:602 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:27:28:602 [ADB] Using ps-based PID detection
2021-03-18 08:27:28:602 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:27:28:943 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:27:29:289 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:27:29:290 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:27:29:887 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:27:30:242 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:27:30:244 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:27:30:244 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:27:30:584 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:27:30:585 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:27:30:586 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:27:30:590 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:27:30:592 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:27:31:190 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:27:31:191 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:27:31:192 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:27:31:550 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:27:31:551 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:27:31:555 [WD Proxy] socket hang up
2021-03-18 08:27:31:903 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:27:32:556 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:27:32:557 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:27:32:560 [WD Proxy] socket hang up
2021-03-18 08:27:33:562 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:27:33:563 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:27:33:630 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:27:33:631 [UiAutomator2] The initialization of the instrumentation process took 2440ms
2021-03-18 08:27:33:631 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:27:33:632 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:27:33:652 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457"}}
2021-03-18 08:27:33:654 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:27:33:667 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457/appium/device/info] with no body
2021-03-18 08:27:33:678 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:27:33:679 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:27:34:016 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:27:34:017 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:27:34:018 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:27:37:924 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457/appium/device/pixel_ratio] with no body
2021-03-18 08:27:37:929 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":1.5}
2021-03-18 08:27:37:931 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:27:37:931 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457/appium/device/system_bars] with no body
2021-03-18 08:27:37:939 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":{"statusBar":38}}
2021-03-18 08:27:37:939 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:27:37:940 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457/window/current/size] with no body
2021-03-18 08:27:37:946 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":{"height":1280,"width":720}}
2021-03-18 08:27:37:947 [Appium] New AndroidUiautomator2Driver session created successfully, session ef1169d2-2308-4415-a827-c4404df28fea added to master session list
2021-03-18 08:27:37:947 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:27:37:948 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:27:37:949 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:27:37:950 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:27:37:958 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":null}
2021-03-18 08:27:37:958 [BaseDriver] Event 'newSessionStarted' logged at 1616056057958 (16:27:37 GMT+0800 (中国标准时间))
2021-03-18 08:27:37:959 [W3C (ef1169d2)] Cached the protocol value 'W3C' for the new session ef1169d2-2308-4415-a827-c4404df28fea
2021-03-18 08:27:37:960 [W3C (ef1169d2)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:27:37:962 [HTTP] <-- POST /wd/hub/session 200 12076 ms - 1080
2021-03-18 08:27:37:962 [HTTP] 
2021-03-18 08:27:37:965 [HTTP] --> POST /wd/hub/session/ef1169d2-2308-4415-a827-c4404df28fea/timeouts
2021-03-18 08:27:37:965 [HTTP] {"implicit":10000}
2021-03-18 08:27:37:966 [W3C (ef1169d2)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"ef1169d2-2308-4415-a827-c4404df28fea"]
2021-03-18 08:27:37:967 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:27:37:967 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:27:37:968 [W3C (ef1169d2)] Responding to client with driver.timeouts() result: null
2021-03-18 08:27:37:969 [HTTP] <-- POST /wd/hub/session/ef1169d2-2308-4415-a827-c4404df28fea/timeouts 200 5 ms - 14
2021-03-18 08:27:37:969 [HTTP] 
2021-03-18 08:27:38:138 [HTTP] --> DELETE /wd/hub/session/ef1169d2-2308-4415-a827-c4404df28fea
2021-03-18 08:27:38:139 [HTTP] {}
2021-03-18 08:27:38:140 [W3C (ef1169d2)] Calling AppiumDriver.deleteSession() with args: ["ef1169d2-2308-4415-a827-c4404df28fea"]
2021-03-18 08:27:38:140 [BaseDriver] Event 'quitSessionRequested' logged at 1616056058140 (16:27:38 GMT+0800 (中国标准时间))
2021-03-18 08:27:38:141 [Appium] Removing session ef1169d2-2308-4415-a827-c4404df28fea from our master session list
2021-03-18 08:27:38:142 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:27:38:142 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:27:38:143 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:27:38:143 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/30269bed-eeea-40d9-99a5-6b5f1703f457] with no body
2021-03-18 08:27:38:151 [WD Proxy] Got response with status 200: {"sessionId":"30269bed-eeea-40d9-99a5-6b5f1703f457","value":null}
2021-03-18 08:27:38:152 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:27:38:934 [Instrumentation] .
2021-03-18 08:27:39:021 [Logcat] Stopping logcat capture
2021-03-18 08:27:39:026 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:27:39:027 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:27:39:314 [Instrumentation] Time: 7.036
2021-03-18 08:27:39:315 [Instrumentation] 
2021-03-18 08:27:39:316 [Instrumentation] OK (1 test)
2021-03-18 08:27:39:339 [Instrumentation] The process has exited with code 0
2021-03-18 08:27:39:368 [BaseDriver] Event 'quitSessionFinished' logged at 1616056059368 (16:27:39 GMT+0800 (中国标准时间))
2021-03-18 08:27:39:369 [W3C (ef1169d2)] Received response: null
2021-03-18 08:27:39:370 [W3C (ef1169d2)] But deleting session, so not returning
2021-03-18 08:27:39:370 [W3C (ef1169d2)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:27:39:371 [HTTP] <-- DELETE /wd/hub/session/ef1169d2-2308-4415-a827-c4404df28fea 200 1233 ms - 14
2021-03-18 08:27:39:371 [HTTP] 
2021-03-18 08:28:13:668 [HTTP] Request idempotency key: c5952b38-b3fe-49c7-9fcd-e480177b921c
2021-03-18 08:28:13:669 [HTTP] --> POST /wd/hub/session
2021-03-18 08:28:13:670 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:28:13:671 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:28:13:672 [BaseDriver] Event 'newSessionRequested' logged at 1616056093671 (16:28:13 GMT+0800 (中国标准时间))
2021-03-18 08:28:13:673 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:28:13:674 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:28:13:675 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:28:13:675 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:28:13:676 [BaseDriver]     "platformName": "Android",
2021-03-18 08:28:13:676 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:28:13:676 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:28:13:677 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:28:13:677 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:28:13:679 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:28:13:680 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:28:13:680 [BaseDriver]     "appium:noReset": true
2021-03-18 08:28:13:681 [BaseDriver]   },
2021-03-18 08:28:13:682 [BaseDriver]   "firstMatch": [
2021-03-18 08:28:13:682 [BaseDriver]     {}
2021-03-18 08:28:13:683 [BaseDriver]   ]
2021-03-18 08:28:13:683 [BaseDriver] }
2021-03-18 08:28:13:689 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:28:13:690 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:28:13:691 [BaseDriver] Session created with session id: 73d31bec-d0d5-4919-8c77-187c3c41d4b6
2021-03-18 08:28:13:691 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:28:13:692 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:28:13:693 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:28:14:027 [AndroidDriver] Retrieving device list
2021-03-18 08:28:14:028 [ADB] Trying to find a connected android device
2021-03-18 08:28:14:028 [ADB] Getting connected devices
2021-03-18 08:28:14:359 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:28:14:360 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:28:14:361 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:28:14:362 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:28:14:689 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:28:14:690 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:28:15:027 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:28:15:028 [ADB] Device API level: 22
2021-03-18 08:28:15:028 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:28:15:029 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:28:15:365 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:28:15:698 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:28:15:699 [ADB] Getting install status for io.appium.settings
2021-03-18 08:28:15:700 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:28:16:033 [ADB] 'io.appium.settings' is installed
2021-03-18 08:28:16:034 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:28:16:035 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:28:16:376 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:28:16:377 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:28:16:377 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:28:16:378 [ADB] Using ps-based PID detection
2021-03-18 08:28:16:378 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:28:16:727 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:28:17:065 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:28:17:066 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:28:17:666 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:28:17:995 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:28:17:997 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:28:17:997 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:28:18:354 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:28:18:355 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:28:18:355 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:28:18:359 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:28:18:360 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:28:18:956 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:28:18:957 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:28:18:958 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:28:19:310 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:28:19:311 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:28:19:315 [WD Proxy] socket hang up
2021-03-18 08:28:19:653 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:28:20:316 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:28:20:318 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:28:20:321 [WD Proxy] socket hang up
2021-03-18 08:28:21:324 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:28:21:325 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:28:21:392 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:28:21:393 [UiAutomator2] The initialization of the instrumentation process took 2436ms
2021-03-18 08:28:21:393 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:28:21:394 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:28:21:414 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e"}}
2021-03-18 08:28:21:415 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:28:21:416 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e/appium/device/info] with no body
2021-03-18 08:28:21:427 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:28:21:427 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:28:21:778 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:28:21:779 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:28:21:780 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:28:25:823 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e/appium/device/pixel_ratio] with no body
2021-03-18 08:28:25:832 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":1.5}
2021-03-18 08:28:25:833 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:28:25:835 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e/appium/device/system_bars] with no body
2021-03-18 08:28:25:840 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":{"statusBar":38}}
2021-03-18 08:28:25:841 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:28:25:842 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e/window/current/size] with no body
2021-03-18 08:28:25:848 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":{"height":1280,"width":720}}
2021-03-18 08:28:25:848 [Appium] New AndroidUiautomator2Driver session created successfully, session 73d31bec-d0d5-4919-8c77-187c3c41d4b6 added to master session list
2021-03-18 08:28:25:849 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:28:25:849 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:28:25:851 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:28:25:851 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:28:25:857 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":null}
2021-03-18 08:28:25:857 [BaseDriver] Event 'newSessionStarted' logged at 1616056105857 (16:28:25 GMT+0800 (中国标准时间))
2021-03-18 08:28:25:858 [W3C (73d31bec)] Cached the protocol value 'W3C' for the new session 73d31bec-d0d5-4919-8c77-187c3c41d4b6
2021-03-18 08:28:25:859 [W3C (73d31bec)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:28:25:860 [HTTP] <-- POST /wd/hub/session 200 12190 ms - 1080
2021-03-18 08:28:25:860 [HTTP] 
2021-03-18 08:28:25:862 [HTTP] --> POST /wd/hub/session/73d31bec-d0d5-4919-8c77-187c3c41d4b6/timeouts
2021-03-18 08:28:25:864 [HTTP] {"implicit":10000}
2021-03-18 08:28:25:865 [W3C (73d31bec)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"73d31bec-d0d5-4919-8c77-187c3c41d4b6"]
2021-03-18 08:28:25:865 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:28:25:866 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:28:25:868 [W3C (73d31bec)] Responding to client with driver.timeouts() result: null
2021-03-18 08:28:25:869 [HTTP] <-- POST /wd/hub/session/73d31bec-d0d5-4919-8c77-187c3c41d4b6/timeouts 200 7 ms - 14
2021-03-18 08:28:25:870 [HTTP] 
2021-03-18 08:28:26:028 [HTTP] --> DELETE /wd/hub/session/73d31bec-d0d5-4919-8c77-187c3c41d4b6
2021-03-18 08:28:26:030 [HTTP] {}
2021-03-18 08:28:26:031 [W3C (73d31bec)] Calling AppiumDriver.deleteSession() with args: ["73d31bec-d0d5-4919-8c77-187c3c41d4b6"]
2021-03-18 08:28:26:031 [BaseDriver] Event 'quitSessionRequested' logged at 1616056106031 (16:28:26 GMT+0800 (中国标准时间))
2021-03-18 08:28:26:032 [Appium] Removing session 73d31bec-d0d5-4919-8c77-187c3c41d4b6 from our master session list
2021-03-18 08:28:26:033 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:28:26:033 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:28:26:035 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:28:26:035 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/e75fd37c-da05-4d87-acb5-a7d632155c4e] with no body
2021-03-18 08:28:26:043 [WD Proxy] Got response with status 200: {"sessionId":"e75fd37c-da05-4d87-acb5-a7d632155c4e","value":null}
2021-03-18 08:28:26:044 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:28:26:687 [Instrumentation] .
2021-03-18 08:28:26:874 [Instrumentation] Time: 7.037
2021-03-18 08:28:26:875 [Instrumentation] 
2021-03-18 08:28:26:876 [Instrumentation] OK (1 test)
2021-03-18 08:28:26:938 [Logcat] Stopping logcat capture
2021-03-18 08:28:26:942 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:28:26:943 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:28:27:222 [Instrumentation] The process has exited with code 0
2021-03-18 08:28:27:275 [BaseDriver] Event 'quitSessionFinished' logged at 1616056107274 (16:28:27 GMT+0800 (中国标准时间))
2021-03-18 08:28:27:276 [W3C (73d31bec)] Received response: null
2021-03-18 08:28:27:277 [W3C (73d31bec)] But deleting session, so not returning
2021-03-18 08:28:27:277 [W3C (73d31bec)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:28:27:278 [HTTP] <-- DELETE /wd/hub/session/73d31bec-d0d5-4919-8c77-187c3c41d4b6 200 1250 ms - 14
2021-03-18 08:28:27:278 [HTTP] 
2021-03-18 08:29:27:823 [HTTP] Request idempotency key: 7f19e5a0-3600-47a7-b6c1-7a4c1b4521d4
2021-03-18 08:29:27:825 [HTTP] --> POST /wd/hub/session
2021-03-18 08:29:27:826 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:29:27:826 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:29:27:827 [BaseDriver] Event 'newSessionRequested' logged at 1616056167826 (16:29:27 GMT+0800 (中国标准时间))
2021-03-18 08:29:27:828 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:29:27:830 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:29:27:830 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:29:27:831 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:29:27:832 [BaseDriver]     "platformName": "Android",
2021-03-18 08:29:27:833 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:29:27:833 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:29:27:835 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:29:27:836 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:29:27:836 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:29:27:837 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:29:27:837 [BaseDriver]     "appium:noReset": true
2021-03-18 08:29:27:837 [BaseDriver]   },
2021-03-18 08:29:27:838 [BaseDriver]   "firstMatch": [
2021-03-18 08:29:27:839 [BaseDriver]     {}
2021-03-18 08:29:27:839 [BaseDriver]   ]
2021-03-18 08:29:27:840 [BaseDriver] }
2021-03-18 08:29:27:845 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:29:27:846 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:29:27:847 [BaseDriver] Session created with session id: 283a3040-2674-4dec-9b6c-462a6862e933
2021-03-18 08:29:27:847 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:29:27:850 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:29:27:850 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:29:28:198 [AndroidDriver] Retrieving device list
2021-03-18 08:29:28:199 [ADB] Trying to find a connected android device
2021-03-18 08:29:28:199 [ADB] Getting connected devices
2021-03-18 08:29:28:535 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:29:28:537 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:29:28:537 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:29:28:538 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:29:28:864 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:29:28:866 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:29:29:206 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:29:29:207 [ADB] Device API level: 22
2021-03-18 08:29:29:208 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:29:29:208 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:29:29:543 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:29:29:879 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:29:29:881 [ADB] Getting install status for io.appium.settings
2021-03-18 08:29:29:882 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:29:30:223 [ADB] 'io.appium.settings' is installed
2021-03-18 08:29:30:224 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:29:30:225 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:29:30:565 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:29:30:566 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:29:30:567 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:29:30:568 [ADB] Using ps-based PID detection
2021-03-18 08:29:30:569 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:29:30:906 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:29:31:243 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:29:31:244 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:29:31:851 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:29:32:184 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:29:32:186 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:29:32:186 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:29:32:529 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:29:32:530 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:29:32:531 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:29:32:534 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:29:32:534 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:29:33:137 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:29:33:138 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:29:33:138 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:29:33:479 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:29:33:480 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:29:33:484 [WD Proxy] socket hang up
2021-03-18 08:29:33:827 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:29:34:485 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:29:34:486 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:29:34:489 [WD Proxy] socket hang up
2021-03-18 08:29:35:489 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:29:35:491 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:29:35:561 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:29:35:562 [UiAutomator2] The initialization of the instrumentation process took 2425ms
2021-03-18 08:29:35:563 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:29:35:564 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:29:35:583 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335"}}
2021-03-18 08:29:35:585 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:29:35:586 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335/appium/device/info] with no body
2021-03-18 08:29:35:597 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:29:35:598 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:29:35:934 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:29:35:936 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:29:35:936 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:29:40:143 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335/appium/device/pixel_ratio] with no body
2021-03-18 08:29:40:149 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":1.5}
2021-03-18 08:29:40:150 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:29:40:150 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335/appium/device/system_bars] with no body
2021-03-18 08:29:40:155 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":{"statusBar":38}}
2021-03-18 08:29:40:156 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:29:40:156 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335/window/current/size] with no body
2021-03-18 08:29:40:161 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":{"height":1280,"width":720}}
2021-03-18 08:29:40:163 [Appium] New AndroidUiautomator2Driver session created successfully, session 283a3040-2674-4dec-9b6c-462a6862e933 added to master session list
2021-03-18 08:29:40:164 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:29:40:164 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:29:40:166 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:29:40:166 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:29:40:174 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":null}
2021-03-18 08:29:40:175 [BaseDriver] Event 'newSessionStarted' logged at 1616056180175 (16:29:40 GMT+0800 (中国标准时间))
2021-03-18 08:29:40:176 [W3C (283a3040)] Cached the protocol value 'W3C' for the new session 283a3040-2674-4dec-9b6c-462a6862e933
2021-03-18 08:29:40:176 [W3C (283a3040)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:29:40:178 [HTTP] <-- POST /wd/hub/session 200 12353 ms - 1080
2021-03-18 08:29:40:178 [HTTP] 
2021-03-18 08:29:40:180 [HTTP] --> POST /wd/hub/session/283a3040-2674-4dec-9b6c-462a6862e933/timeouts
2021-03-18 08:29:40:180 [HTTP] {"implicit":10000}
2021-03-18 08:29:40:183 [W3C (283a3040)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"283a3040-2674-4dec-9b6c-462a6862e933"]
2021-03-18 08:29:40:183 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:29:40:184 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:29:40:184 [W3C (283a3040)] Responding to client with driver.timeouts() result: null
2021-03-18 08:29:40:185 [HTTP] <-- POST /wd/hub/session/283a3040-2674-4dec-9b6c-462a6862e933/timeouts 200 5 ms - 14
2021-03-18 08:29:40:186 [HTTP] 
2021-03-18 08:29:40:342 [HTTP] --> DELETE /wd/hub/session/283a3040-2674-4dec-9b6c-462a6862e933
2021-03-18 08:29:40:343 [HTTP] {}
2021-03-18 08:29:40:344 [W3C (283a3040)] Calling AppiumDriver.deleteSession() with args: ["283a3040-2674-4dec-9b6c-462a6862e933"]
2021-03-18 08:29:40:344 [BaseDriver] Event 'quitSessionRequested' logged at 1616056180344 (16:29:40 GMT+0800 (中国标准时间))
2021-03-18 08:29:40:345 [Appium] Removing session 283a3040-2674-4dec-9b6c-462a6862e933 from our master session list
2021-03-18 08:29:40:345 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:29:40:346 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:29:40:346 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:29:40:347 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/f18a74c4-d187-496d-a0ca-06e6a1200335] with no body
2021-03-18 08:29:40:354 [WD Proxy] Got response with status 200: {"sessionId":"f18a74c4-d187-496d-a0ca-06e6a1200335","value":null}
2021-03-18 08:29:40:355 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:29:40:924 [Instrumentation] .
2021-03-18 08:29:41:110 [Instrumentation] Time: 7.099
2021-03-18 08:29:41:112 [Instrumentation] 
2021-03-18 08:29:41:113 [Instrumentation] OK (1 test)
2021-03-18 08:29:41:227 [Logcat] Stopping logcat capture
2021-03-18 08:29:41:231 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:29:41:232 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:29:41:515 [Instrumentation] The process has exited with code 0
2021-03-18 08:29:41:567 [BaseDriver] Event 'quitSessionFinished' logged at 1616056181567 (16:29:41 GMT+0800 (中国标准时间))
2021-03-18 08:29:41:569 [W3C (283a3040)] Received response: null
2021-03-18 08:29:41:569 [W3C (283a3040)] But deleting session, so not returning
2021-03-18 08:29:41:570 [W3C (283a3040)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:29:41:570 [HTTP] <-- DELETE /wd/hub/session/283a3040-2674-4dec-9b6c-462a6862e933 200 1229 ms - 14
2021-03-18 08:29:41:571 [HTTP] 
2021-03-18 08:30:11:207 [HTTP] Request idempotency key: c0b581e9-fc1d-439e-8010-098d17ce3c83
2021-03-18 08:30:11:208 [HTTP] --> POST /wd/hub/session
2021-03-18 08:30:11:209 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:30:11:210 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:30:11:211 [BaseDriver] Event 'newSessionRequested' logged at 1616056211210 (16:30:11 GMT+0800 (中国标准时间))
2021-03-18 08:30:11:212 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:30:11:213 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:30:11:213 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:30:11:213 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:30:11:214 [BaseDriver]     "platformName": "Android",
2021-03-18 08:30:11:215 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:30:11:215 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:30:11:216 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:30:11:218 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:30:11:219 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:30:11:219 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:30:11:220 [BaseDriver]     "appium:noReset": true
2021-03-18 08:30:11:220 [BaseDriver]   },
2021-03-18 08:30:11:220 [BaseDriver]   "firstMatch": [
2021-03-18 08:30:11:221 [BaseDriver]     {}
2021-03-18 08:30:11:221 [BaseDriver]   ]
2021-03-18 08:30:11:222 [BaseDriver] }
2021-03-18 08:30:11:226 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:30:11:226 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:30:11:228 [BaseDriver] Session created with session id: b4f02348-4cbd-4d82-8afe-8bb18d51e098
2021-03-18 08:30:11:228 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:30:11:230 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:30:11:230 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:30:11:576 [AndroidDriver] Retrieving device list
2021-03-18 08:30:11:577 [ADB] Trying to find a connected android device
2021-03-18 08:30:11:577 [ADB] Getting connected devices
2021-03-18 08:30:11:913 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:30:11:914 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:30:11:915 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:30:11:915 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:30:12:278 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:30:12:279 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:30:12:626 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:30:12:628 [ADB] Device API level: 22
2021-03-18 08:30:12:628 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:30:12:629 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:30:12:963 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:30:13:299 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:30:13:300 [ADB] Getting install status for io.appium.settings
2021-03-18 08:30:13:301 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:30:13:637 [ADB] 'io.appium.settings' is installed
2021-03-18 08:30:13:638 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:30:13:638 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:30:13:975 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:30:13:977 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:30:13:977 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:30:13:977 [ADB] Using ps-based PID detection
2021-03-18 08:30:13:978 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:30:14:315 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:30:14:682 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:30:14:684 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:30:15:298 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:30:15:643 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:30:15:645 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:30:15:645 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:30:16:028 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:30:16:029 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:30:16:030 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:30:16:033 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:30:16:034 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:30:16:641 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:30:16:643 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:30:16:643 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:30:16:994 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:30:16:996 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:30:17:000 [WD Proxy] socket hang up
2021-03-18 08:30:17:343 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:30:18:001 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:30:18:002 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:30:18:006 [WD Proxy] socket hang up
2021-03-18 08:30:19:007 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:30:19:008 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:30:19:076 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:30:19:077 [UiAutomator2] The initialization of the instrumentation process took 2434ms
2021-03-18 08:30:19:078 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:30:19:078 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:30:19:100 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3"}}
2021-03-18 08:30:19:104 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:30:19:117 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3/appium/device/info] with no body
2021-03-18 08:30:19:127 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:30:19:129 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:30:19:471 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:30:19:472 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:30:19:473 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:30:23:521 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3/appium/device/pixel_ratio] with no body
2021-03-18 08:30:23:526 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":1.5}
2021-03-18 08:30:23:527 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:30:23:528 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3/appium/device/system_bars] with no body
2021-03-18 08:30:23:534 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":{"statusBar":38}}
2021-03-18 08:30:23:537 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:30:23:538 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3/window/current/size] with no body
2021-03-18 08:30:23:546 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":{"height":1280,"width":720}}
2021-03-18 08:30:23:547 [Appium] New AndroidUiautomator2Driver session created successfully, session b4f02348-4cbd-4d82-8afe-8bb18d51e098 added to master session list
2021-03-18 08:30:23:548 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:30:23:548 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:30:23:550 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:30:23:552 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:30:23:558 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":null}
2021-03-18 08:30:23:558 [BaseDriver] Event 'newSessionStarted' logged at 1616056223558 (16:30:23 GMT+0800 (中国标准时间))
2021-03-18 08:30:23:560 [W3C (b4f02348)] Cached the protocol value 'W3C' for the new session b4f02348-4cbd-4d82-8afe-8bb18d51e098
2021-03-18 08:30:23:561 [W3C (b4f02348)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:30:23:563 [HTTP] <-- POST /wd/hub/session 200 12354 ms - 1080
2021-03-18 08:30:23:564 [HTTP] 
2021-03-18 08:30:23:566 [HTTP] --> POST /wd/hub/session/b4f02348-4cbd-4d82-8afe-8bb18d51e098/timeouts
2021-03-18 08:30:23:567 [HTTP] {"implicit":10000}
2021-03-18 08:30:23:568 [W3C (b4f02348)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"b4f02348-4cbd-4d82-8afe-8bb18d51e098"]
2021-03-18 08:30:23:570 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:30:23:571 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:30:23:572 [W3C (b4f02348)] Responding to client with driver.timeouts() result: null
2021-03-18 08:30:23:573 [HTTP] <-- POST /wd/hub/session/b4f02348-4cbd-4d82-8afe-8bb18d51e098/timeouts 200 6 ms - 14
2021-03-18 08:30:23:573 [HTTP] 
2021-03-18 08:30:23:731 [HTTP] --> DELETE /wd/hub/session/b4f02348-4cbd-4d82-8afe-8bb18d51e098
2021-03-18 08:30:23:733 [HTTP] {}
2021-03-18 08:30:23:733 [W3C (b4f02348)] Calling AppiumDriver.deleteSession() with args: ["b4f02348-4cbd-4d82-8afe-8bb18d51e098"]
2021-03-18 08:30:23:734 [BaseDriver] Event 'quitSessionRequested' logged at 1616056223733 (16:30:23 GMT+0800 (中国标准时间))
2021-03-18 08:30:23:734 [Appium] Removing session b4f02348-4cbd-4d82-8afe-8bb18d51e098 from our master session list
2021-03-18 08:30:23:735 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:30:23:737 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:30:23:737 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:30:23:738 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/6f922a20-691e-4cdc-895f-cff56b4157e3] with no body
2021-03-18 08:30:23:745 [WD Proxy] Got response with status 200: {"sessionId":"6f922a20-691e-4cdc-895f-cff56b4157e3","value":null}
2021-03-18 08:30:23:746 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:30:24:398 [Instrumentation] .
2021-03-18 08:30:24:582 [Logcat] Stopping logcat capture
2021-03-18 08:30:24:586 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:30:24:586 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:30:24:862 [Instrumentation] Time: 7.06
2021-03-18 08:30:24:863 [Instrumentation] 
2021-03-18 08:30:24:863 [Instrumentation] OK (1 test)
2021-03-18 08:30:24:887 [Instrumentation] The process has exited with code 0
2021-03-18 08:30:24:916 [BaseDriver] Event 'quitSessionFinished' logged at 1616056224916 (16:30:24 GMT+0800 (中国标准时间))
2021-03-18 08:30:24:917 [W3C (b4f02348)] Received response: null
2021-03-18 08:30:24:918 [W3C (b4f02348)] But deleting session, so not returning
2021-03-18 08:30:24:918 [W3C (b4f02348)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:30:24:920 [HTTP] <-- DELETE /wd/hub/session/b4f02348-4cbd-4d82-8afe-8bb18d51e098 200 1188 ms - 14
2021-03-18 08:30:24:920 [HTTP] 
2021-03-18 08:32:26:270 [HTTP] Request idempotency key: 233c59b5-1b58-49ba-a662-3b7341bfc797
2021-03-18 08:32:26:272 [HTTP] --> POST /wd/hub/session
2021-03-18 08:32:26:272 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:32:26:273 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:32:26:273 [BaseDriver] Event 'newSessionRequested' logged at 1616056346273 (16:32:26 GMT+0800 (中国标准时间))
2021-03-18 08:32:26:274 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:32:26:275 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:32:26:275 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:32:26:276 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:32:26:276 [BaseDriver]     "platformName": "Android",
2021-03-18 08:32:26:276 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:32:26:277 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:32:26:277 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:32:26:278 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:32:26:278 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:32:26:279 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:32:26:279 [BaseDriver]     "appium:noReset": true
2021-03-18 08:32:26:281 [BaseDriver]   },
2021-03-18 08:32:26:281 [BaseDriver]   "firstMatch": [
2021-03-18 08:32:26:282 [BaseDriver]     {}
2021-03-18 08:32:26:282 [BaseDriver]   ]
2021-03-18 08:32:26:283 [BaseDriver] }
2021-03-18 08:32:26:286 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:32:26:286 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:32:26:287 [BaseDriver] Session created with session id: 309bd827-10cd-431f-9e98-6c4adc0f614e
2021-03-18 08:32:26:287 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:32:26:288 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:32:26:289 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:32:26:618 [AndroidDriver] Retrieving device list
2021-03-18 08:32:26:619 [ADB] Trying to find a connected android device
2021-03-18 08:32:26:620 [ADB] Getting connected devices
2021-03-18 08:32:26:952 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:32:26:953 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:32:26:955 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:32:26:955 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:32:27:311 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:32:27:312 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:32:27:646 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:32:27:648 [ADB] Device API level: 22
2021-03-18 08:32:27:648 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:32:27:649 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:32:27:981 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:32:28:310 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:32:28:312 [ADB] Getting install status for io.appium.settings
2021-03-18 08:32:28:312 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:32:28:691 [ADB] 'io.appium.settings' is installed
2021-03-18 08:32:28:693 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:32:28:693 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:32:29:030 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:32:29:031 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:32:29:031 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:32:29:032 [ADB] Using ps-based PID detection
2021-03-18 08:32:29:032 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:32:29:377 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:32:29:716 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:32:29:717 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:32:30:318 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:32:30:661 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:32:30:662 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:32:30:662 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:32:31:010 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:32:31:011 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:32:31:011 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:32:31:015 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:32:31:016 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:32:31:616 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:32:31:617 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:32:31:617 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:32:31:965 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:32:31:966 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:32:31:970 [WD Proxy] socket hang up
2021-03-18 08:32:32:318 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:32:32:971 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:32:32:972 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:32:32:975 [WD Proxy] socket hang up
2021-03-18 08:32:33:976 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:32:33:977 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:32:34:045 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:32:34:046 [UiAutomator2] The initialization of the instrumentation process took 2429ms
2021-03-18 08:32:34:046 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:32:34:047 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:32:34:067 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e"}}
2021-03-18 08:32:34:069 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:32:34:070 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e/appium/device/info] with no body
2021-03-18 08:32:34:081 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:32:34:081 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:32:34:418 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:32:34:419 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:32:34:420 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:32:38:386 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e/appium/device/pixel_ratio] with no body
2021-03-18 08:32:38:391 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":1.5}
2021-03-18 08:32:38:392 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:32:38:392 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e/appium/device/system_bars] with no body
2021-03-18 08:32:38:398 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":{"statusBar":38}}
2021-03-18 08:32:38:398 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:32:38:399 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e/window/current/size] with no body
2021-03-18 08:32:38:408 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":{"height":1280,"width":720}}
2021-03-18 08:32:38:409 [Appium] New AndroidUiautomator2Driver session created successfully, session 309bd827-10cd-431f-9e98-6c4adc0f614e added to master session list
2021-03-18 08:32:38:409 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:32:38:410 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:32:38:411 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:32:38:412 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:32:38:418 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":null}
2021-03-18 08:32:38:418 [BaseDriver] Event 'newSessionStarted' logged at 1616056358418 (16:32:38 GMT+0800 (中国标准时间))
2021-03-18 08:32:38:418 [W3C (309bd827)] Cached the protocol value 'W3C' for the new session 309bd827-10cd-431f-9e98-6c4adc0f614e
2021-03-18 08:32:38:419 [W3C (309bd827)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:32:38:420 [HTTP] <-- POST /wd/hub/session 200 12149 ms - 1080
2021-03-18 08:32:38:421 [HTTP] 
2021-03-18 08:32:38:423 [HTTP] --> POST /wd/hub/session/309bd827-10cd-431f-9e98-6c4adc0f614e/timeouts
2021-03-18 08:32:38:423 [HTTP] {"implicit":10000}
2021-03-18 08:32:38:425 [W3C (309bd827)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"309bd827-10cd-431f-9e98-6c4adc0f614e"]
2021-03-18 08:32:38:425 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:32:38:426 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:32:38:426 [W3C (309bd827)] Responding to client with driver.timeouts() result: null
2021-03-18 08:32:38:427 [HTTP] <-- POST /wd/hub/session/309bd827-10cd-431f-9e98-6c4adc0f614e/timeouts 200 4 ms - 14
2021-03-18 08:32:38:427 [HTTP] 
2021-03-18 08:32:38:582 [HTTP] --> DELETE /wd/hub/session/309bd827-10cd-431f-9e98-6c4adc0f614e
2021-03-18 08:32:38:584 [HTTP] {}
2021-03-18 08:32:38:585 [W3C (309bd827)] Calling AppiumDriver.deleteSession() with args: ["309bd827-10cd-431f-9e98-6c4adc0f614e"]
2021-03-18 08:32:38:586 [BaseDriver] Event 'quitSessionRequested' logged at 1616056358585 (16:32:38 GMT+0800 (中国标准时间))
2021-03-18 08:32:38:587 [Appium] Removing session 309bd827-10cd-431f-9e98-6c4adc0f614e from our master session list
2021-03-18 08:32:38:588 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:32:38:588 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:32:38:588 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:32:38:589 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/7cf351db-6393-4cf7-aa48-9c65b0b9790e] with no body
2021-03-18 08:32:38:596 [WD Proxy] Got response with status 200: {"sessionId":"7cf351db-6393-4cf7-aa48-9c65b0b9790e","value":null}
2021-03-18 08:32:38:597 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:32:39:362 [Instrumentation] .
2021-03-18 08:32:39:466 [Logcat] Stopping logcat capture
2021-03-18 08:32:39:470 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:32:39:471 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:32:39:748 [Instrumentation] Time: 7.046
2021-03-18 08:32:39:749 [Instrumentation] 
2021-03-18 08:32:39:749 [Instrumentation] OK (1 test)
2021-03-18 08:32:39:750 [Instrumentation] The process has exited with code 0
2021-03-18 08:32:39:801 [BaseDriver] Event 'quitSessionFinished' logged at 1616056359801 (16:32:39 GMT+0800 (中国标准时间))
2021-03-18 08:32:39:802 [W3C (309bd827)] Received response: null
2021-03-18 08:32:39:803 [W3C (309bd827)] But deleting session, so not returning
2021-03-18 08:32:39:803 [W3C (309bd827)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:32:39:804 [HTTP] <-- DELETE /wd/hub/session/309bd827-10cd-431f-9e98-6c4adc0f614e 200 1222 ms - 14
2021-03-18 08:32:39:805 [HTTP] 
2021-03-18 08:34:54:857 [HTTP] Request idempotency key: 52d8f423-b4d2-4fdc-8bb7-9dab4d2b9a85
2021-03-18 08:34:54:858 [HTTP] --> POST /wd/hub/session
2021-03-18 08:34:54:859 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:34:54:860 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:34:54:860 [BaseDriver] Event 'newSessionRequested' logged at 1616056494860 (16:34:54 GMT+0800 (中国标准时间))
2021-03-18 08:34:54:861 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:34:54:862 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:34:54:862 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:34:54:862 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:34:54:863 [BaseDriver]     "platformName": "Android",
2021-03-18 08:34:54:863 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:34:54:864 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:34:54:864 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:34:54:864 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:34:54:865 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:34:54:865 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:34:54:866 [BaseDriver]     "appium:noReset": true
2021-03-18 08:34:54:866 [BaseDriver]   },
2021-03-18 08:34:54:866 [BaseDriver]   "firstMatch": [
2021-03-18 08:34:54:867 [BaseDriver]     {}
2021-03-18 08:34:54:869 [BaseDriver]   ]
2021-03-18 08:34:54:869 [BaseDriver] }
2021-03-18 08:34:54:872 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:34:54:873 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:34:54:873 [BaseDriver] Session created with session id: 4700a9c0-3246-425d-a177-e249130a0599
2021-03-18 08:34:54:874 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:34:54:875 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:34:54:875 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:34:55:226 [AndroidDriver] Retrieving device list
2021-03-18 08:34:55:227 [ADB] Trying to find a connected android device
2021-03-18 08:34:55:228 [ADB] Getting connected devices
2021-03-18 08:34:55:558 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:34:55:559 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:34:55:560 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:34:55:561 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:34:55:902 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:34:55:903 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:34:56:236 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:34:56:238 [ADB] Device API level: 22
2021-03-18 08:34:56:238 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:34:56:239 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:34:56:566 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:34:56:899 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:34:56:900 [ADB] Getting install status for io.appium.settings
2021-03-18 08:34:56:900 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:34:57:239 [ADB] 'io.appium.settings' is installed
2021-03-18 08:34:57:241 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:34:57:241 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:34:57:616 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:34:57:617 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:34:57:618 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:34:57:618 [ADB] Using ps-based PID detection
2021-03-18 08:34:57:619 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:34:57:958 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:34:58:298 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:34:58:300 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:34:58:894 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:34:59:228 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:34:59:229 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:34:59:230 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:34:59:573 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:34:59:574 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:34:59:575 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:34:59:579 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:34:59:580 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:35:00:221 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:35:00:223 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:35:00:224 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:35:00:570 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:35:00:571 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:35:00:575 [WD Proxy] socket hang up
2021-03-18 08:35:00:923 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:35:01:575 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:35:01:576 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:35:01:579 [WD Proxy] socket hang up
2021-03-18 08:35:02:580 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:35:02:581 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:35:02:649 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:35:02:650 [UiAutomator2] The initialization of the instrumentation process took 2428ms
2021-03-18 08:35:02:651 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:35:02:651 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:35:02:672 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26"}}
2021-03-18 08:35:02:674 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:35:02:675 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26/appium/device/info] with no body
2021-03-18 08:35:02:687 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:35:02:687 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:35:03:022 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:35:03:023 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:35:03:023 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:35:06:923 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26/appium/device/pixel_ratio] with no body
2021-03-18 08:35:06:931 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":1.5}
2021-03-18 08:35:06:933 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:35:06:934 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26/appium/device/system_bars] with no body
2021-03-18 08:35:06:939 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":{"statusBar":38}}
2021-03-18 08:35:06:940 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:35:06:940 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26/window/current/size] with no body
2021-03-18 08:35:06:947 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":{"height":1280,"width":720}}
2021-03-18 08:35:06:947 [Appium] New AndroidUiautomator2Driver session created successfully, session 4700a9c0-3246-425d-a177-e249130a0599 added to master session list
2021-03-18 08:35:06:948 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:35:06:949 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:35:06:950 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:35:06:950 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:35:06:957 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":null}
2021-03-18 08:35:06:958 [BaseDriver] Event 'newSessionStarted' logged at 1616056506958 (16:35:06 GMT+0800 (中国标准时间))
2021-03-18 08:35:06:958 [W3C (4700a9c0)] Cached the protocol value 'W3C' for the new session 4700a9c0-3246-425d-a177-e249130a0599
2021-03-18 08:35:06:959 [W3C (4700a9c0)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:35:06:961 [HTTP] <-- POST /wd/hub/session 200 12102 ms - 1080
2021-03-18 08:35:06:961 [HTTP] 
2021-03-18 08:35:06:964 [HTTP] --> POST /wd/hub/session/4700a9c0-3246-425d-a177-e249130a0599/timeouts
2021-03-18 08:35:06:964 [HTTP] {"implicit":10000}
2021-03-18 08:35:06:965 [W3C (4700a9c0)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"4700a9c0-3246-425d-a177-e249130a0599"]
2021-03-18 08:35:06:966 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:35:06:966 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:35:06:968 [W3C (4700a9c0)] Responding to client with driver.timeouts() result: null
2021-03-18 08:35:06:969 [HTTP] <-- POST /wd/hub/session/4700a9c0-3246-425d-a177-e249130a0599/timeouts 200 6 ms - 14
2021-03-18 08:35:06:970 [HTTP] 
2021-03-18 08:35:07:127 [HTTP] --> DELETE /wd/hub/session/4700a9c0-3246-425d-a177-e249130a0599
2021-03-18 08:35:07:128 [HTTP] {}
2021-03-18 08:35:07:129 [W3C (4700a9c0)] Calling AppiumDriver.deleteSession() with args: ["4700a9c0-3246-425d-a177-e249130a0599"]
2021-03-18 08:35:07:130 [BaseDriver] Event 'quitSessionRequested' logged at 1616056507129 (16:35:07 GMT+0800 (中国标准时间))
2021-03-18 08:35:07:131 [Appium] Removing session 4700a9c0-3246-425d-a177-e249130a0599 from our master session list
2021-03-18 08:35:07:131 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:35:07:132 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:35:07:132 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:35:07:133 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/3183d89e-183a-4a1d-905d-a04021423f26] with no body
2021-03-18 08:35:07:140 [WD Proxy] Got response with status 200: {"sessionId":"3183d89e-183a-4a1d-905d-a04021423f26","value":null}
2021-03-18 08:35:07:141 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:35:07:965 [Instrumentation] .
2021-03-18 08:35:08:001 [Logcat] Stopping logcat capture
2021-03-18 08:35:08:006 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:35:08:006 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:35:08:282 [Instrumentation] Time: 7.046
2021-03-18 08:35:08:283 [Instrumentation] 
2021-03-18 08:35:08:284 [Instrumentation] OK (1 test)
2021-03-18 08:35:08:335 [BaseDriver] Event 'quitSessionFinished' logged at 1616056508334 (16:35:08 GMT+0800 (中国标准时间))
2021-03-18 08:35:08:336 [W3C (4700a9c0)] Received response: null
2021-03-18 08:35:08:337 [W3C (4700a9c0)] But deleting session, so not returning
2021-03-18 08:35:08:337 [W3C (4700a9c0)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:35:08:338 [HTTP] <-- DELETE /wd/hub/session/4700a9c0-3246-425d-a177-e249130a0599 200 1211 ms - 14
2021-03-18 08:35:08:338 [HTTP] 
2021-03-18 08:35:08:432 [Instrumentation] The process has exited with code 0
2021-03-18 08:47:07:095 [HTTP] Request idempotency key: 7b9176b4-fe59-4205-b2f8-6597c781237f
2021-03-18 08:47:07:097 [HTTP] --> POST /wd/hub/session
2021-03-18 08:47:07:098 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:47:07:099 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:47:07:100 [BaseDriver] Event 'newSessionRequested' logged at 1616057227099 (16:47:07 GMT+0800 (中国标准时间))
2021-03-18 08:47:07:101 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:47:07:102 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:47:07:103 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:47:07:104 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:47:07:105 [BaseDriver]     "platformName": "Android",
2021-03-18 08:47:07:107 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:47:07:108 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:47:07:108 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:47:07:109 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:47:07:109 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:47:07:109 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:47:07:110 [BaseDriver]     "appium:noReset": true
2021-03-18 08:47:07:110 [BaseDriver]   },
2021-03-18 08:47:07:111 [BaseDriver]   "firstMatch": [
2021-03-18 08:47:07:112 [BaseDriver]     {}
2021-03-18 08:47:07:113 [BaseDriver]   ]
2021-03-18 08:47:07:113 [BaseDriver] }
2021-03-18 08:47:07:115 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:47:07:118 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:47:07:119 [BaseDriver] Session created with session id: 9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe
2021-03-18 08:47:07:120 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:47:07:122 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:47:07:122 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:47:07:530 [AndroidDriver] Retrieving device list
2021-03-18 08:47:07:531 [ADB] Trying to find a connected android device
2021-03-18 08:47:07:531 [ADB] Getting connected devices
2021-03-18 08:47:07:860 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:47:07:861 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:47:07:862 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:47:07:862 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:47:08:184 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:47:08:186 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:47:08:520 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:47:08:521 [ADB] Device API level: 22
2021-03-18 08:47:08:521 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:47:08:522 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:47:08:853 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:47:09:210 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:47:09:211 [ADB] Getting install status for io.appium.settings
2021-03-18 08:47:09:211 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:47:09:546 [ADB] 'io.appium.settings' is installed
2021-03-18 08:47:09:547 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:47:09:548 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:47:09:888 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:47:09:889 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:47:09:889 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:47:09:890 [ADB] Using ps-based PID detection
2021-03-18 08:47:09:890 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:47:10:226 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:47:10:602 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:47:10:603 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:47:11:202 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:47:11:529 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:47:11:531 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:47:11:531 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:47:11:878 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:47:11:880 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:47:11:881 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:47:11:885 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:47:11:885 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:47:12:483 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:47:12:484 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:47:12:484 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:47:12:898 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:47:12:899 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:47:12:903 [WD Proxy] socket hang up
2021-03-18 08:47:13:250 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:47:13:904 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:47:13:905 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:47:13:909 [WD Proxy] socket hang up
2021-03-18 08:47:14:909 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:47:14:911 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:47:14:978 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:47:14:979 [UiAutomator2] The initialization of the instrumentation process took 2495ms
2021-03-18 08:47:14:979 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:47:14:980 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:47:15:000 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7"}}
2021-03-18 08:47:15:001 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:47:15:014 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7/appium/device/info] with no body
2021-03-18 08:47:15:024 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:47:15:032 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:47:15:369 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:47:15:370 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:47:15:370 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:47:19:424 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7/appium/device/pixel_ratio] with no body
2021-03-18 08:47:19:430 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":1.5}
2021-03-18 08:47:19:431 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:47:19:432 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7/appium/device/system_bars] with no body
2021-03-18 08:47:19:440 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":{"statusBar":38}}
2021-03-18 08:47:19:441 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:47:19:442 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7/window/current/size] with no body
2021-03-18 08:47:19:447 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":{"height":1280,"width":720}}
2021-03-18 08:47:19:448 [Appium] New AndroidUiautomator2Driver session created successfully, session 9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe added to master session list
2021-03-18 08:47:19:450 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:47:19:450 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:47:19:451 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:47:19:452 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:47:19:458 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":null}
2021-03-18 08:47:19:458 [BaseDriver] Event 'newSessionStarted' logged at 1616057239458 (16:47:19 GMT+0800 (中国标准时间))
2021-03-18 08:47:19:459 [W3C (9b5c50b3)] Cached the protocol value 'W3C' for the new session 9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe
2021-03-18 08:47:19:460 [W3C (9b5c50b3)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:47:19:461 [HTTP] <-- POST /wd/hub/session 200 12365 ms - 1080
2021-03-18 08:47:19:462 [HTTP] 
2021-03-18 08:47:19:464 [HTTP] --> POST /wd/hub/session/9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe/timeouts
2021-03-18 08:47:19:465 [HTTP] {"implicit":10000}
2021-03-18 08:47:19:466 [W3C (9b5c50b3)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe"]
2021-03-18 08:47:19:467 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:47:19:467 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:47:19:468 [W3C (9b5c50b3)] Responding to client with driver.timeouts() result: null
2021-03-18 08:47:19:469 [HTTP] <-- POST /wd/hub/session/9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe/timeouts 200 5 ms - 14
2021-03-18 08:47:19:469 [HTTP] 
2021-03-18 08:47:19:618 [HTTP] --> DELETE /wd/hub/session/9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe
2021-03-18 08:47:19:620 [HTTP] {}
2021-03-18 08:47:19:620 [W3C (9b5c50b3)] Calling AppiumDriver.deleteSession() with args: ["9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe"]
2021-03-18 08:47:19:621 [BaseDriver] Event 'quitSessionRequested' logged at 1616057239620 (16:47:19 GMT+0800 (中国标准时间))
2021-03-18 08:47:19:622 [Appium] Removing session 9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe from our master session list
2021-03-18 08:47:19:622 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:47:19:623 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:47:19:624 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:47:19:625 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/15e9836b-19d0-4c18-899a-2b634ee50ec7] with no body
2021-03-18 08:47:19:632 [WD Proxy] Got response with status 200: {"sessionId":"15e9836b-19d0-4c18-899a-2b634ee50ec7","value":null}
2021-03-18 08:47:19:633 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:47:20:304 [Instrumentation] .
2021-03-18 08:47:20:550 [Instrumentation] Time: 7.056
2021-03-18 08:47:20:552 [Instrumentation] 
2021-03-18 08:47:20:553 [Instrumentation] OK (1 test)
2021-03-18 08:47:20:561 [Logcat] Stopping logcat capture
2021-03-18 08:47:20:566 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:47:20:566 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:47:20:848 [Instrumentation] The process has exited with code 0
2021-03-18 08:47:20:902 [BaseDriver] Event 'quitSessionFinished' logged at 1616057240902 (16:47:20 GMT+0800 (中国标准时间))
2021-03-18 08:47:20:904 [W3C (9b5c50b3)] Received response: null
2021-03-18 08:47:20:904 [W3C (9b5c50b3)] But deleting session, so not returning
2021-03-18 08:47:20:905 [W3C (9b5c50b3)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:47:20:906 [HTTP] <-- DELETE /wd/hub/session/9b5c50b3-61bb-4ecc-a15e-b5d15d897ebe 200 1288 ms - 14
2021-03-18 08:47:20:906 [HTTP] 
2021-03-18 08:47:55:404 [HTTP] Request idempotency key: 59a2ac82-6ae8-4cef-ae4c-d1e3ea2d7119
2021-03-18 08:47:55:406 [HTTP] --> POST /wd/hub/session
2021-03-18 08:47:55:407 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:47:55:408 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:47:55:409 [BaseDriver] Event 'newSessionRequested' logged at 1616057275408 (16:47:55 GMT+0800 (中国标准时间))
2021-03-18 08:47:55:410 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:47:55:411 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:47:55:412 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:47:55:412 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:47:55:412 [BaseDriver]     "platformName": "Android",
2021-03-18 08:47:55:413 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:47:55:413 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:47:55:416 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:47:55:417 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:47:55:417 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:47:55:418 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:47:55:419 [BaseDriver]     "appium:noReset": true
2021-03-18 08:47:55:419 [BaseDriver]   },
2021-03-18 08:47:55:420 [BaseDriver]   "firstMatch": [
2021-03-18 08:47:55:420 [BaseDriver]     {}
2021-03-18 08:47:55:420 [BaseDriver]   ]
2021-03-18 08:47:55:421 [BaseDriver] }
2021-03-18 08:47:55:425 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:47:55:426 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:47:55:427 [BaseDriver] Session created with session id: d291a4d2-b1ec-44b3-8747-6c16f9ac8779
2021-03-18 08:47:55:427 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:47:55:429 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:47:55:429 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:47:55:763 [AndroidDriver] Retrieving device list
2021-03-18 08:47:55:765 [ADB] Trying to find a connected android device
2021-03-18 08:47:55:765 [ADB] Getting connected devices
2021-03-18 08:47:56:102 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:47:56:103 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:47:56:104 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:47:56:104 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:47:56:436 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:47:56:437 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:47:56:785 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:47:56:786 [ADB] Device API level: 22
2021-03-18 08:47:56:786 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:47:56:787 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:47:57:117 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:47:57:448 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:47:57:449 [ADB] Getting install status for io.appium.settings
2021-03-18 08:47:57:450 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:47:57:781 [ADB] 'io.appium.settings' is installed
2021-03-18 08:47:57:782 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:47:57:782 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:47:58:121 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:47:58:122 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:47:58:123 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:47:58:123 [ADB] Using ps-based PID detection
2021-03-18 08:47:58:124 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:47:58:455 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:47:58:793 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:47:58:794 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:47:59:386 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:47:59:742 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:47:59:744 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:47:59:745 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:48:00:083 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:48:00:084 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:48:00:084 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:48:00:089 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:48:00:089 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:48:00:679 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:48:00:680 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:48:00:680 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:48:01:061 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:48:01:062 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:48:01:067 [WD Proxy] socket hang up
2021-03-18 08:48:01:414 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:48:02:068 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:48:02:069 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:48:02:073 [WD Proxy] socket hang up
2021-03-18 08:48:03:073 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:48:03:074 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:48:03:142 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:48:03:144 [UiAutomator2] The initialization of the instrumentation process took 2463ms
2021-03-18 08:48:03:144 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:48:03:145 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:48:03:165 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"36be818b-c813-43c8-a138-f28961512a31"}}
2021-03-18 08:48:03:167 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:48:03:179 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31/appium/device/info] with no body
2021-03-18 08:48:03:189 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:48:03:189 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:48:03:525 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:48:03:527 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:48:03:527 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:48:07:507 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31/appium/device/pixel_ratio] with no body
2021-03-18 08:48:07:514 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":1.5}
2021-03-18 08:48:07:515 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:48:07:516 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31/appium/device/system_bars] with no body
2021-03-18 08:48:07:521 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":{"statusBar":38}}
2021-03-18 08:48:07:522 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:48:07:522 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31/window/current/size] with no body
2021-03-18 08:48:07:529 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":{"height":1280,"width":720}}
2021-03-18 08:48:07:530 [Appium] New AndroidUiautomator2Driver session created successfully, session d291a4d2-b1ec-44b3-8747-6c16f9ac8779 added to master session list
2021-03-18 08:48:07:533 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:48:07:534 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:48:07:535 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:48:07:536 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:48:07:542 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":null}
2021-03-18 08:48:07:542 [BaseDriver] Event 'newSessionStarted' logged at 1616057287542 (16:48:07 GMT+0800 (中国标准时间))
2021-03-18 08:48:07:543 [W3C (d291a4d2)] Cached the protocol value 'W3C' for the new session d291a4d2-b1ec-44b3-8747-6c16f9ac8779
2021-03-18 08:48:07:544 [W3C (d291a4d2)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:48:07:546 [HTTP] <-- POST /wd/hub/session 200 12139 ms - 1080
2021-03-18 08:48:07:546 [HTTP] 
2021-03-18 08:48:07:548 [HTTP] --> POST /wd/hub/session/d291a4d2-b1ec-44b3-8747-6c16f9ac8779/timeouts
2021-03-18 08:48:07:549 [HTTP] {"implicit":10000}
2021-03-18 08:48:07:549 [W3C (d291a4d2)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"d291a4d2-b1ec-44b3-8747-6c16f9ac8779"]
2021-03-18 08:48:07:550 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:48:07:550 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:48:07:552 [W3C (d291a4d2)] Responding to client with driver.timeouts() result: null
2021-03-18 08:48:07:553 [HTTP] <-- POST /wd/hub/session/d291a4d2-b1ec-44b3-8747-6c16f9ac8779/timeouts 200 4 ms - 14
2021-03-18 08:48:07:553 [HTTP] 
2021-03-18 08:48:07:712 [HTTP] --> DELETE /wd/hub/session/d291a4d2-b1ec-44b3-8747-6c16f9ac8779
2021-03-18 08:48:07:714 [HTTP] {}
2021-03-18 08:48:07:715 [W3C (d291a4d2)] Calling AppiumDriver.deleteSession() with args: ["d291a4d2-b1ec-44b3-8747-6c16f9ac8779"]
2021-03-18 08:48:07:717 [BaseDriver] Event 'quitSessionRequested' logged at 1616057287716 (16:48:07 GMT+0800 (中国标准时间))
2021-03-18 08:48:07:717 [Appium] Removing session d291a4d2-b1ec-44b3-8747-6c16f9ac8779 from our master session list
2021-03-18 08:48:07:718 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:48:07:719 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:48:07:720 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:48:07:721 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/36be818b-c813-43c8-a138-f28961512a31] with no body
2021-03-18 08:48:07:731 [WD Proxy] Got response with status 200: {"sessionId":"36be818b-c813-43c8-a138-f28961512a31","value":null}
2021-03-18 08:48:07:732 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:48:08:448 [Instrumentation] .
2021-03-18 08:48:08:618 [Logcat] Stopping logcat capture
2021-03-18 08:48:08:622 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:48:08:623 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:48:08:897 [Instrumentation] Time: 7.038
2021-03-18 08:48:08:898 [Instrumentation] 
2021-03-18 08:48:08:898 [Instrumentation] OK (1 test)
2021-03-18 08:48:08:899 [Instrumentation] The process has exited with code 0
2021-03-18 08:48:08:950 [BaseDriver] Event 'quitSessionFinished' logged at 1616057288949 (16:48:08 GMT+0800 (中国标准时间))
2021-03-18 08:48:08:951 [W3C (d291a4d2)] Received response: null
2021-03-18 08:48:08:951 [W3C (d291a4d2)] But deleting session, so not returning
2021-03-18 08:48:08:952 [W3C (d291a4d2)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:48:08:953 [HTTP] <-- DELETE /wd/hub/session/d291a4d2-b1ec-44b3-8747-6c16f9ac8779 200 1241 ms - 14
2021-03-18 08:48:08:953 [HTTP] 
2021-03-18 08:53:08:998 [HTTP] Request idempotency key: eb5dd214-c946-4173-9413-b5a8e7d7bf2a
2021-03-18 08:53:09:001 [HTTP] --> POST /wd/hub/session
2021-03-18 08:53:09:005 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:53:09:007 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:53:09:008 [BaseDriver] Event 'newSessionRequested' logged at 1616057589007 (16:53:09 GMT+0800 (中国标准时间))
2021-03-18 08:53:09:010 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:53:09:011 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:53:09:011 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:53:09:012 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:53:09:012 [BaseDriver]     "platformName": "Android",
2021-03-18 08:53:09:013 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:53:09:013 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:53:09:014 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:53:09:014 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:53:09:015 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:53:09:017 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:53:09:019 [BaseDriver]     "appium:noReset": true
2021-03-18 08:53:09:023 [BaseDriver]   },
2021-03-18 08:53:09:024 [BaseDriver]   "firstMatch": [
2021-03-18 08:53:09:025 [BaseDriver]     {}
2021-03-18 08:53:09:026 [BaseDriver]   ]
2021-03-18 08:53:09:026 [BaseDriver] }
2021-03-18 08:53:09:031 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:53:09:031 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:53:09:032 [BaseDriver] Session created with session id: 53a6830c-fd8e-412e-821c-f666cb280410
2021-03-18 08:53:09:032 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:53:09:034 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:53:09:034 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:53:09:373 [AndroidDriver] Retrieving device list
2021-03-18 08:53:09:375 [ADB] Trying to find a connected android device
2021-03-18 08:53:09:375 [ADB] Getting connected devices
2021-03-18 08:53:09:699 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:53:09:700 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:53:09:701 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:53:09:701 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:53:10:022 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:53:10:023 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:53:10:374 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:53:10:375 [ADB] Device API level: 22
2021-03-18 08:53:10:375 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:53:10:376 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:53:10:706 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:53:11:033 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:53:11:034 [ADB] Getting install status for io.appium.settings
2021-03-18 08:53:11:036 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:53:11:366 [ADB] 'io.appium.settings' is installed
2021-03-18 08:53:11:368 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:53:11:369 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:53:11:734 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:53:11:736 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:53:11:736 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:53:11:737 [ADB] Using ps-based PID detection
2021-03-18 08:53:11:737 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:53:12:083 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:53:12:417 [AndroidDriver] Granting permissions SET_ANIMATION_SCALE,CHANGE_CONFIGURATION,ACCESS_FINE_LOCATION to 'io.appium.settings'
2021-03-18 08:53:12:419 [ADB] Granting permissions ["android.permission.SET_ANIMATION_SCALE","android.permission.CHANGE_CONFIGURATION","android.permission.ACCESS_FINE_LOCATION"] to 'io.appium.settings'
2021-03-18 08:53:12:419 [ADB] Got the following command chunks to execute: [["pm","grant","io.appium.settings","android.permission.SET_ANIMATION_SCALE",";","pm","grant","io.appium.settings","android.permission.CHANGE_CONFIGURATION",";","pm","grant","io.appium.settings","android.permission.ACCESS_FINE_LOCATION",";"]]
2021-03-18 08:53:12:420 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell pm grant io.appium.settings android.permission.SET_ANIMATION_SCALE ; pm grant io.appium.settings android.permission.CHANGE_CONFIGURATION ; pm grant io.appium.settings android.permission.ACCESS_FINE_LOCATION ;'
2021-03-18 08:53:12:980 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:53:12:982 [ADB] Using ps-based PID detection
2021-03-18 08:53:12:982 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:53:13:317 [ADB] Starting Appium Settings app
2021-03-18 08:53:13:318 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -n io.appium.settings/.Settings -a android.intent.action.MAIN -c android.intent.category.LAUNCHER'
2021-03-18 08:53:14:001 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:53:14:003 [ADB] Using ps-based PID detection
2021-03-18 08:53:14:004 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:53:14:340 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:53:14:935 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:53:15:273 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:53:15:274 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:53:15:275 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:53:15:621 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:53:15:622 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:53:15:623 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:53:15:626 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:53:15:627 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:53:16:281 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:53:16:282 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:53:16:283 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:53:16:622 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:53:16:624 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:53:16:628 [WD Proxy] socket hang up
2021-03-18 08:53:16:975 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:53:17:630 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:53:17:631 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:53:17:635 [WD Proxy] socket hang up
2021-03-18 08:53:18:636 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:53:18:637 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:53:18:704 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:53:18:705 [UiAutomator2] The initialization of the instrumentation process took 2423ms
2021-03-18 08:53:18:706 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:53:18:706 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:53:18:726 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e"}}
2021-03-18 08:53:18:728 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:53:18:729 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e/appium/device/info] with no body
2021-03-18 08:53:18:740 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:53:18:741 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:53:19:078 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:53:19:080 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:53:19:080 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:53:23:157 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e/appium/device/pixel_ratio] with no body
2021-03-18 08:53:23:164 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":1.5}
2021-03-18 08:53:23:165 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:53:23:166 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e/appium/device/system_bars] with no body
2021-03-18 08:53:23:172 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":{"statusBar":38}}
2021-03-18 08:53:23:174 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:53:23:179 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e/window/current/size] with no body
2021-03-18 08:53:23:186 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":{"height":1280,"width":720}}
2021-03-18 08:53:23:189 [Appium] New AndroidUiautomator2Driver session created successfully, session 53a6830c-fd8e-412e-821c-f666cb280410 added to master session list
2021-03-18 08:53:23:195 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:53:23:197 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:53:23:198 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:53:23:199 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:53:23:207 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":null}
2021-03-18 08:53:23:208 [BaseDriver] Event 'newSessionStarted' logged at 1616057603207 (16:53:23 GMT+0800 (中国标准时间))
2021-03-18 08:53:23:208 [W3C (53a6830c)] Cached the protocol value 'W3C' for the new session 53a6830c-fd8e-412e-821c-f666cb280410
2021-03-18 08:53:23:209 [W3C (53a6830c)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:53:23:210 [HTTP] <-- POST /wd/hub/session 200 14210 ms - 1080
2021-03-18 08:53:23:210 [HTTP] 
2021-03-18 08:53:23:212 [HTTP] --> POST /wd/hub/session/53a6830c-fd8e-412e-821c-f666cb280410/timeouts
2021-03-18 08:53:23:213 [HTTP] {"implicit":10000}
2021-03-18 08:53:23:213 [W3C (53a6830c)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"53a6830c-fd8e-412e-821c-f666cb280410"]
2021-03-18 08:53:23:214 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:53:23:214 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:53:23:215 [W3C (53a6830c)] Responding to client with driver.timeouts() result: null
2021-03-18 08:53:23:216 [HTTP] <-- POST /wd/hub/session/53a6830c-fd8e-412e-821c-f666cb280410/timeouts 200 4 ms - 14
2021-03-18 08:53:23:216 [HTTP] 
2021-03-18 08:53:23:372 [HTTP] --> DELETE /wd/hub/session/53a6830c-fd8e-412e-821c-f666cb280410
2021-03-18 08:53:23:374 [HTTP] {}
2021-03-18 08:53:23:375 [W3C (53a6830c)] Calling AppiumDriver.deleteSession() with args: ["53a6830c-fd8e-412e-821c-f666cb280410"]
2021-03-18 08:53:23:376 [BaseDriver] Event 'quitSessionRequested' logged at 1616057603375 (16:53:23 GMT+0800 (中国标准时间))
2021-03-18 08:53:23:377 [Appium] Removing session 53a6830c-fd8e-412e-821c-f666cb280410 from our master session list
2021-03-18 08:53:23:378 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:53:23:379 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:53:23:380 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:53:23:381 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/ac4c0704-37ab-460a-8ff2-009b734dfc5e] with no body
2021-03-18 08:53:23:389 [WD Proxy] Got response with status 200: {"sessionId":"ac4c0704-37ab-460a-8ff2-009b734dfc5e","value":null}
2021-03-18 08:53:23:390 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:53:24:014 [Instrumentation] .
2021-03-18 08:53:24:260 [Logcat] Stopping logcat capture
2021-03-18 08:53:24:264 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:53:24:265 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:53:24:545 [Instrumentation] Time: 7.04
2021-03-18 08:53:24:546 [Instrumentation] 
2021-03-18 08:53:24:547 [Instrumentation] OK (1 test)
2021-03-18 08:53:24:547 [Instrumentation] The process has exited with code 0
2021-03-18 08:53:24:598 [BaseDriver] Event 'quitSessionFinished' logged at 1616057604598 (16:53:24 GMT+0800 (中国标准时间))
2021-03-18 08:53:24:599 [W3C (53a6830c)] Received response: null
2021-03-18 08:53:24:600 [W3C (53a6830c)] But deleting session, so not returning
2021-03-18 08:53:24:600 [W3C (53a6830c)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:53:24:601 [HTTP] <-- DELETE /wd/hub/session/53a6830c-fd8e-412e-821c-f666cb280410 200 1228 ms - 14
2021-03-18 08:53:24:601 [HTTP] 
2021-03-18 08:54:08:153 [HTTP] Request idempotency key: 3ea5f584-d89d-433c-8d39-e7c8768bde6e
2021-03-18 08:54:08:154 [HTTP] --> POST /wd/hub/session
2021-03-18 08:54:08:155 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:54:08:156 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:54:08:156 [BaseDriver] Event 'newSessionRequested' logged at 1616057648156 (16:54:08 GMT+0800 (中国标准时间))
2021-03-18 08:54:08:158 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:54:08:160 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:54:08:161 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:54:08:161 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:54:08:162 [BaseDriver]     "platformName": "Android",
2021-03-18 08:54:08:162 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:54:08:164 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:54:08:165 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:54:08:165 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:54:08:166 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:54:08:166 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:54:08:167 [BaseDriver]     "appium:noReset": true
2021-03-18 08:54:08:167 [BaseDriver]   },
2021-03-18 08:54:08:168 [BaseDriver]   "firstMatch": [
2021-03-18 08:54:08:169 [BaseDriver]     {}
2021-03-18 08:54:08:170 [BaseDriver]   ]
2021-03-18 08:54:08:170 [BaseDriver] }
2021-03-18 08:54:08:174 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:54:08:174 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:54:08:175 [BaseDriver] Session created with session id: 462fc12d-76db-45d5-a360-7f156e0c4c55
2021-03-18 08:54:08:175 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:54:08:176 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:54:08:177 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:54:08:512 [AndroidDriver] Retrieving device list
2021-03-18 08:54:08:513 [ADB] Trying to find a connected android device
2021-03-18 08:54:08:514 [ADB] Getting connected devices
2021-03-18 08:54:08:846 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:54:08:848 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:54:08:849 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:54:08:849 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:54:09:189 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:54:09:190 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:54:09:524 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:54:09:526 [ADB] Device API level: 22
2021-03-18 08:54:09:526 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:54:09:527 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:54:09:856 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:54:10:186 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:54:10:187 [ADB] Getting install status for io.appium.settings
2021-03-18 08:54:10:188 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:54:10:552 [ADB] 'io.appium.settings' is installed
2021-03-18 08:54:10:553 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:54:10:553 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:54:10:889 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:54:10:890 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:54:10:891 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:54:10:891 [ADB] Using ps-based PID detection
2021-03-18 08:54:10:891 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:54:11:225 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:54:11:562 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:54:11:563 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:54:12:152 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:54:12:510 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:54:12:511 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:54:12:512 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:54:12:848 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:54:12:849 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:54:12:849 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:54:12:853 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:54:12:853 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:54:13:454 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:54:13:455 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:54:13:456 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:54:13:796 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:54:13:797 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:54:13:801 [WD Proxy] socket hang up
2021-03-18 08:54:14:148 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:54:14:802 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:54:14:803 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:54:14:807 [WD Proxy] socket hang up
2021-03-18 08:54:15:807 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:54:15:809 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:54:15:877 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:54:15:878 [UiAutomator2] The initialization of the instrumentation process took 2423ms
2021-03-18 08:54:15:879 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:54:15:880 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:54:15:900 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e"}}
2021-03-18 08:54:15:902 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:54:15:915 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e/appium/device/info] with no body
2021-03-18 08:54:15:925 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:54:15:926 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:54:16:261 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:54:16:262 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:54:16:263 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:54:20:383 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e/appium/device/pixel_ratio] with no body
2021-03-18 08:54:20:390 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":1.5}
2021-03-18 08:54:20:391 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:54:20:392 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e/appium/device/system_bars] with no body
2021-03-18 08:54:20:397 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":{"statusBar":38}}
2021-03-18 08:54:20:398 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:54:20:398 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e/window/current/size] with no body
2021-03-18 08:54:20:410 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":{"height":1280,"width":720}}
2021-03-18 08:54:20:410 [Appium] New AndroidUiautomator2Driver session created successfully, session 462fc12d-76db-45d5-a360-7f156e0c4c55 added to master session list
2021-03-18 08:54:20:411 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:54:20:411 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:54:20:413 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:54:20:414 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:54:20:420 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":null}
2021-03-18 08:54:20:420 [BaseDriver] Event 'newSessionStarted' logged at 1616057660420 (16:54:20 GMT+0800 (中国标准时间))
2021-03-18 08:54:20:421 [W3C (462fc12d)] Cached the protocol value 'W3C' for the new session 462fc12d-76db-45d5-a360-7f156e0c4c55
2021-03-18 08:54:20:422 [W3C (462fc12d)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:54:20:424 [HTTP] <-- POST /wd/hub/session 200 12269 ms - 1080
2021-03-18 08:54:20:425 [HTTP] 
2021-03-18 08:54:20:426 [HTTP] --> POST /wd/hub/session/462fc12d-76db-45d5-a360-7f156e0c4c55/timeouts
2021-03-18 08:54:20:427 [HTTP] {"implicit":10000}
2021-03-18 08:54:20:427 [W3C (462fc12d)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"462fc12d-76db-45d5-a360-7f156e0c4c55"]
2021-03-18 08:54:20:428 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:54:20:428 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:54:20:429 [W3C (462fc12d)] Responding to client with driver.timeouts() result: null
2021-03-18 08:54:20:430 [HTTP] <-- POST /wd/hub/session/462fc12d-76db-45d5-a360-7f156e0c4c55/timeouts 200 3 ms - 14
2021-03-18 08:54:20:430 [HTTP] 
2021-03-18 08:54:20:581 [HTTP] --> DELETE /wd/hub/session/462fc12d-76db-45d5-a360-7f156e0c4c55
2021-03-18 08:54:20:583 [HTTP] {}
2021-03-18 08:54:20:584 [W3C (462fc12d)] Calling AppiumDriver.deleteSession() with args: ["462fc12d-76db-45d5-a360-7f156e0c4c55"]
2021-03-18 08:54:20:584 [BaseDriver] Event 'quitSessionRequested' logged at 1616057660584 (16:54:20 GMT+0800 (中国标准时间))
2021-03-18 08:54:20:585 [Appium] Removing session 462fc12d-76db-45d5-a360-7f156e0c4c55 from our master session list
2021-03-18 08:54:20:586 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:54:20:587 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:54:20:588 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:54:20:588 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/bd32b795-fdd8-48d7-a77a-74a5f897235e] with no body
2021-03-18 08:54:20:596 [WD Proxy] Got response with status 200: {"sessionId":"bd32b795-fdd8-48d7-a77a-74a5f897235e","value":null}
2021-03-18 08:54:20:597 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:54:21:184 [Instrumentation] .
2021-03-18 08:54:21:363 [Instrumentation] Time: 7.038
2021-03-18 08:54:21:365 [Instrumentation] 
2021-03-18 08:54:21:365 [Instrumentation] OK (1 test)
2021-03-18 08:54:21:505 [Logcat] Stopping logcat capture
2021-03-18 08:54:21:509 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:54:21:509 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:54:21:790 [Instrumentation] The process has exited with code 0
2021-03-18 08:54:21:842 [BaseDriver] Event 'quitSessionFinished' logged at 1616057661842 (16:54:21 GMT+0800 (中国标准时间))
2021-03-18 08:54:21:843 [W3C (462fc12d)] Received response: null
2021-03-18 08:54:21:844 [W3C (462fc12d)] But deleting session, so not returning
2021-03-18 08:54:21:845 [W3C (462fc12d)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:54:21:846 [HTTP] <-- DELETE /wd/hub/session/462fc12d-76db-45d5-a360-7f156e0c4c55 200 1264 ms - 14
2021-03-18 08:54:21:846 [HTTP] 
2021-03-18 08:56:53:433 [HTTP] Request idempotency key: eacb4c69-8c11-439d-b4d6-e9911840b75f
2021-03-18 08:56:53:435 [HTTP] --> POST /wd/hub/session
2021-03-18 08:56:53:435 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:56:53:436 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:56:53:437 [BaseDriver] Event 'newSessionRequested' logged at 1616057813437 (16:56:53 GMT+0800 (中国标准时间))
2021-03-18 08:56:53:438 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:56:53:439 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:56:53:439 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:56:53:439 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:56:53:440 [BaseDriver]     "platformName": "Android",
2021-03-18 08:56:53:440 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:56:53:441 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:56:53:441 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:56:53:441 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:56:53:442 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:56:53:444 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:56:53:445 [BaseDriver]     "appium:noReset": true
2021-03-18 08:56:53:445 [BaseDriver]   },
2021-03-18 08:56:53:446 [BaseDriver]   "firstMatch": [
2021-03-18 08:56:53:446 [BaseDriver]     {}
2021-03-18 08:56:53:446 [BaseDriver]   ]
2021-03-18 08:56:53:447 [BaseDriver] }
2021-03-18 08:56:53:449 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:56:53:450 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:56:53:450 [BaseDriver] Session created with session id: d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a
2021-03-18 08:56:53:451 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:56:53:452 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:56:53:452 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:56:53:786 [AndroidDriver] Retrieving device list
2021-03-18 08:56:53:787 [ADB] Trying to find a connected android device
2021-03-18 08:56:53:787 [ADB] Getting connected devices
2021-03-18 08:56:54:120 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:56:54:121 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:56:54:122 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:56:54:122 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:56:54:458 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:56:54:460 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:56:54:790 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:56:54:791 [ADB] Device API level: 22
2021-03-18 08:56:54:792 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:56:54:792 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:56:55:121 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:56:55:469 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:56:55:470 [ADB] Getting install status for io.appium.settings
2021-03-18 08:56:55:470 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:56:55:804 [ADB] 'io.appium.settings' is installed
2021-03-18 08:56:55:805 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:56:55:805 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:56:56:151 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:56:56:152 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:56:56:153 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:56:56:153 [ADB] Using ps-based PID detection
2021-03-18 08:56:56:154 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:56:56:490 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:56:56:846 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:56:56:847 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:56:57:464 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:56:57:799 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:56:57:801 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:56:57:802 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:56:58:148 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:56:58:149 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:56:58:150 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:56:58:154 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:56:58:155 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:56:58:752 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:56:58:754 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:56:58:755 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:56:59:102 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:56:59:103 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:56:59:107 [WD Proxy] socket hang up
2021-03-18 08:56:59:462 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:57:00:110 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:57:00:111 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:57:00:115 [WD Proxy] socket hang up
2021-03-18 08:57:01:116 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:57:01:117 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:57:01:184 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:57:01:185 [UiAutomator2] The initialization of the instrumentation process took 2431ms
2021-03-18 08:57:01:185 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:57:01:186 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:57:01:205 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30"}}
2021-03-18 08:57:01:207 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:57:01:208 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30/appium/device/info] with no body
2021-03-18 08:57:01:219 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:57:01:220 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:57:01:577 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:57:01:578 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:57:01:578 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:57:05:356 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30/appium/device/pixel_ratio] with no body
2021-03-18 08:57:05:361 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":1.5}
2021-03-18 08:57:05:362 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:57:05:363 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30/appium/device/system_bars] with no body
2021-03-18 08:57:05:368 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":{"statusBar":38}}
2021-03-18 08:57:05:369 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:57:05:370 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30/window/current/size] with no body
2021-03-18 08:57:05:376 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":{"height":1280,"width":720}}
2021-03-18 08:57:05:377 [Appium] New AndroidUiautomator2Driver session created successfully, session d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a added to master session list
2021-03-18 08:57:05:377 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:57:05:378 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:57:05:380 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:57:05:380 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:57:05:385 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":null}
2021-03-18 08:57:05:386 [BaseDriver] Event 'newSessionStarted' logged at 1616057825385 (16:57:05 GMT+0800 (中国标准时间))
2021-03-18 08:57:05:390 [W3C (d7a3bfd7)] Cached the protocol value 'W3C' for the new session d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a
2021-03-18 08:57:05:391 [W3C (d7a3bfd7)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:57:05:392 [HTTP] <-- POST /wd/hub/session 200 11958 ms - 1080
2021-03-18 08:57:05:392 [HTTP] 
2021-03-18 08:57:05:394 [HTTP] --> POST /wd/hub/session/d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a/timeouts
2021-03-18 08:57:05:394 [HTTP] {"implicit":10000}
2021-03-18 08:57:05:396 [W3C (d7a3bfd7)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a"]
2021-03-18 08:57:05:397 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:57:05:397 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:57:05:397 [W3C (d7a3bfd7)] Responding to client with driver.timeouts() result: null
2021-03-18 08:57:05:398 [HTTP] <-- POST /wd/hub/session/d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a/timeouts 200 4 ms - 14
2021-03-18 08:57:05:399 [HTTP] 
2021-03-18 08:57:05:551 [HTTP] --> DELETE /wd/hub/session/d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a
2021-03-18 08:57:05:552 [HTTP] {}
2021-03-18 08:57:05:553 [W3C (d7a3bfd7)] Calling AppiumDriver.deleteSession() with args: ["d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a"]
2021-03-18 08:57:05:553 [BaseDriver] Event 'quitSessionRequested' logged at 1616057825553 (16:57:05 GMT+0800 (中国标准时间))
2021-03-18 08:57:05:554 [Appium] Removing session d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a from our master session list
2021-03-18 08:57:05:554 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:57:05:555 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:57:05:555 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:57:05:556 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/5c1d13e0-42ae-4af6-a6e2-6deceec59c30] with no body
2021-03-18 08:57:05:569 [WD Proxy] Got response with status 200: {"sessionId":"5c1d13e0-42ae-4af6-a6e2-6deceec59c30","value":null}
2021-03-18 08:57:05:569 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:57:06:414 [Logcat] Stopping logcat capture
2021-03-18 08:57:06:419 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:57:06:419 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:57:06:700 [Instrumentation] .
2021-03-18 08:57:06:701 [Instrumentation] 
2021-03-18 08:57:06:702 [Instrumentation] Time: 7.04
2021-03-18 08:57:06:702 [Instrumentation] 
2021-03-18 08:57:06:703 [Instrumentation] OK (1 test)
2021-03-18 08:57:06:754 [BaseDriver] Event 'quitSessionFinished' logged at 1616057826754 (16:57:06 GMT+0800 (中国标准时间))
2021-03-18 08:57:06:755 [W3C (d7a3bfd7)] Received response: null
2021-03-18 08:57:06:756 [W3C (d7a3bfd7)] But deleting session, so not returning
2021-03-18 08:57:06:756 [W3C (d7a3bfd7)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:57:06:757 [HTTP] <-- DELETE /wd/hub/session/d7a3bfd7-35b1-46e2-ac1f-438ab39ed63a 200 1207 ms - 14
2021-03-18 08:57:06:758 [HTTP] 
2021-03-18 08:57:06:877 [Instrumentation] The process has exited with code 0
2021-03-18 08:59:15:098 [HTTP] Request idempotency key: 31b082fd-391b-48c3-814d-c47c4e34db87
2021-03-18 08:59:15:099 [HTTP] --> POST /wd/hub/session
2021-03-18 08:59:15:100 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-18 08:59:15:100 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-18 08:59:15:101 [BaseDriver] Event 'newSessionRequested' logged at 1616057955100 (16:59:15 GMT+0800 (中国标准时间))
2021-03-18 08:59:15:101 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-18 08:59:15:102 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-18 08:59:15:103 [BaseDriver] Creating session with W3C capabilities: {
2021-03-18 08:59:15:104 [BaseDriver]   "alwaysMatch": {
2021-03-18 08:59:15:104 [BaseDriver]     "platformName": "Android",
2021-03-18 08:59:15:105 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-18 08:59:15:106 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-18 08:59:15:106 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-18 08:59:15:108 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-18 08:59:15:108 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-18 08:59:15:109 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-18 08:59:15:109 [BaseDriver]     "appium:noReset": true
2021-03-18 08:59:15:110 [BaseDriver]   },
2021-03-18 08:59:15:110 [BaseDriver]   "firstMatch": [
2021-03-18 08:59:15:111 [BaseDriver]     {}
2021-03-18 08:59:15:112 [BaseDriver]   ]
2021-03-18 08:59:15:112 [BaseDriver] }
2021-03-18 08:59:15:117 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-18 08:59:15:118 [BaseDriver]   skipDeviceInstallation
2021-03-18 08:59:15:118 [BaseDriver] Session created with session id: c856f737-778b-4676-b1d8-81f91519c668
2021-03-18 08:59:15:118 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-18 08:59:15:120 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:59:15:120 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:59:15:448 [AndroidDriver] Retrieving device list
2021-03-18 08:59:15:449 [ADB] Trying to find a connected android device
2021-03-18 08:59:15:450 [ADB] Getting connected devices
2021-03-18 08:59:15:782 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-18 08:59:15:783 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-18 08:59:15:784 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-18 08:59:15:784 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-18 08:59:16:126 [ADB] Setting device id to 127.0.0.1:21503
2021-03-18 08:59:16:127 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-18 08:59:16:462 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-18 08:59:16:464 [ADB] Device API level: 22
2021-03-18 08:59:16:465 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-18 08:59:16:466 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-18 08:59:16:810 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-18 08:59:17:181 [AndroidDriver] Pushing settings apk to device...
2021-03-18 08:59:17:182 [ADB] Getting install status for io.appium.settings
2021-03-18 08:59:17:183 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:59:17:516 [ADB] 'io.appium.settings' is installed
2021-03-18 08:59:17:517 [ADB] Getting package info for 'io.appium.settings'
2021-03-18 08:59:17:518 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-18 08:59:17:852 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-18 08:59:17:853 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-18 08:59:17:854 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-18 08:59:17:854 [ADB] Using ps-based PID detection
2021-03-18 08:59:17:855 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-18 08:59:18:181 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-18 08:59:18:562 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-18 08:59:18:563 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-18 08:59:19:153 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-18 08:59:19:482 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-18 08:59:19:483 [ADB] Forwarding system: 8200 to device: 6790
2021-03-18 08:59:19:483 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-18 08:59:19:827 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-18 08:59:19:828 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-18 08:59:19:829 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-18 08:59:19:832 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-18 08:59:19:832 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-18 08:59:20:426 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-18 08:59:20:427 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-18 08:59:20:428 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-18 08:59:20:772 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:59:20:773 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:59:20:777 [WD Proxy] socket hang up
2021-03-18 08:59:21:120 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-18 08:59:21:777 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:59:21:779 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:59:21:782 [WD Proxy] socket hang up
2021-03-18 08:59:22:783 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-18 08:59:22:784 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-18 08:59:22:851 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-18 08:59:22:852 [UiAutomator2] The initialization of the instrumentation process took 2425ms
2021-03-18 08:59:22:852 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-18 08:59:22:853 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-18 08:59:22:873 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0"}}
2021-03-18 08:59:22:875 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-18 08:59:22:876 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0/appium/device/info] with no body
2021-03-18 08:59:22:886 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-18 08:59:22:887 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-18 08:59:23:219 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-18 08:59:23:220 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-18 08:59:23:221 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-18 08:59:27:309 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0/appium/device/pixel_ratio] with no body
2021-03-18 08:59:27:314 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":1.5}
2021-03-18 08:59:27:315 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-18 08:59:27:315 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0/appium/device/system_bars] with no body
2021-03-18 08:59:27:321 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":{"statusBar":38}}
2021-03-18 08:59:27:322 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-18 08:59:27:322 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0/window/current/size] with no body
2021-03-18 08:59:27:328 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":{"height":1280,"width":720}}
2021-03-18 08:59:27:328 [Appium] New AndroidUiautomator2Driver session created successfully, session c856f737-778b-4676-b1d8-81f91519c668 added to master session list
2021-03-18 08:59:27:330 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-18 08:59:27:330 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-18 08:59:27:332 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-18 08:59:27:333 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-18 08:59:27:339 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":null}
2021-03-18 08:59:27:340 [BaseDriver] Event 'newSessionStarted' logged at 1616057967339 (16:59:27 GMT+0800 (中国标准时间))
2021-03-18 08:59:27:340 [W3C (c856f737)] Cached the protocol value 'W3C' for the new session c856f737-778b-4676-b1d8-81f91519c668
2021-03-18 08:59:27:341 [W3C (c856f737)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-18 08:59:27:342 [HTTP] <-- POST /wd/hub/session 200 12243 ms - 1080
2021-03-18 08:59:27:342 [HTTP] 
2021-03-18 08:59:27:344 [HTTP] --> POST /wd/hub/session/c856f737-778b-4676-b1d8-81f91519c668/timeouts
2021-03-18 08:59:27:344 [HTTP] {"implicit":10000}
2021-03-18 08:59:27:345 [W3C (c856f737)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"c856f737-778b-4676-b1d8-81f91519c668"]
2021-03-18 08:59:27:345 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-18 08:59:27:346 [BaseDriver] Set implicit wait to 10000ms
2021-03-18 08:59:27:346 [W3C (c856f737)] Responding to client with driver.timeouts() result: null
2021-03-18 08:59:27:347 [HTTP] <-- POST /wd/hub/session/c856f737-778b-4676-b1d8-81f91519c668/timeouts 200 3 ms - 14
2021-03-18 08:59:27:347 [HTTP] 
2021-03-18 08:59:27:505 [HTTP] --> DELETE /wd/hub/session/c856f737-778b-4676-b1d8-81f91519c668
2021-03-18 08:59:27:507 [HTTP] {}
2021-03-18 08:59:27:508 [W3C (c856f737)] Calling AppiumDriver.deleteSession() with args: ["c856f737-778b-4676-b1d8-81f91519c668"]
2021-03-18 08:59:27:510 [BaseDriver] Event 'quitSessionRequested' logged at 1616057967508 (16:59:27 GMT+0800 (中国标准时间))
2021-03-18 08:59:27:510 [Appium] Removing session c856f737-778b-4676-b1d8-81f91519c668 from our master session list
2021-03-18 08:59:27:511 [UiAutomator2] Deleting UiAutomator2 session
2021-03-18 08:59:27:511 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-18 08:59:27:512 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-18 08:59:27:512 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/8e3be39a-364d-425e-98ac-77baf61e58e0] with no body
2021-03-18 08:59:27:520 [WD Proxy] Got response with status 200: {"sessionId":"8e3be39a-364d-425e-98ac-77baf61e58e0","value":null}
2021-03-18 08:59:27:521 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-18 08:59:28:157 [Instrumentation] .
2021-03-18 08:59:28:309 [Instrumentation] Time: 7.04
2021-03-18 08:59:28:310 [Instrumentation] 
2021-03-18 08:59:28:311 [Instrumentation] OK (1 test)
2021-03-18 08:59:28:400 [Logcat] Stopping logcat capture
2021-03-18 08:59:28:403 [ADB] Removing forwarded port socket connection: 8200 
2021-03-18 08:59:28:404 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-18 08:59:28:682 [Instrumentation] The process has exited with code 0
2021-03-18 08:59:28:735 [BaseDriver] Event 'quitSessionFinished' logged at 1616057968735 (16:59:28 GMT+0800 (中国标准时间))
2021-03-18 08:59:28:736 [W3C (c856f737)] Received response: null
2021-03-18 08:59:28:736 [W3C (c856f737)] But deleting session, so not returning
2021-03-18 08:59:28:737 [W3C (c856f737)] Responding to client with driver.deleteSession() result: null
2021-03-18 08:59:28:738 [HTTP] <-- DELETE /wd/hub/session/c856f737-778b-4676-b1d8-81f91519c668 200 1232 ms - 14
2021-03-18 08:59:28:738 [HTTP] 
