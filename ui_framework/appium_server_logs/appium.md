2021-03-11 16:23:41:101 [Appium] Welcome to Appium v1.20.0
2021-03-11 16:23:41:102 [Appium] Non-default server args:
2021-03-11 16:23:41:103 [Appium]   logFile: appium.md
2021-03-11 16:23:41:143 [Appium] Appium REST http interface listener started on 0.0.0.0:4723
2021-03-11 16:23:56:688 [HTTP] Request idempotency key: 6cdba2b4-417b-40ae-af2e-483be6251f35
2021-03-11 16:23:56:703 [HTTP] --> POST /wd/hub/session
2021-03-11 16:23:56:704 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-11 16:23:56:705 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-11 16:23:56:706 [BaseDriver] Event 'newSessionRequested' logged at 1615479836705 (00:23:56 GMT+0800 (中国标准时间))
2021-03-11 16:23:57:201 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-11 16:23:57:204 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-11 16:23:57:205 [BaseDriver] Creating session with W3C capabilities: {
2021-03-11 16:23:57:205 [BaseDriver]   "alwaysMatch": {
2021-03-11 16:23:57:205 [BaseDriver]     "platformName": "Android",
2021-03-11 16:23:57:205 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-11 16:23:57:206 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-11 16:23:57:206 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-11 16:23:57:206 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-11 16:23:57:206 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-11 16:23:57:207 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-11 16:23:57:207 [BaseDriver]     "appium:noReset": true
2021-03-11 16:23:57:207 [BaseDriver]   },
2021-03-11 16:23:57:207 [BaseDriver]   "firstMatch": [
2021-03-11 16:23:57:208 [BaseDriver]     {}
2021-03-11 16:23:57:208 [BaseDriver]   ]
2021-03-11 16:23:57:208 [BaseDriver] }
2021-03-11 16:23:57:215 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-11 16:23:57:215 [BaseDriver]   skipDeviceInstallation
2021-03-11 16:23:57:216 [BaseDriver] Session created with session id: c9d94353-84db-4346-93bc-3b6391f302f0
2021-03-11 16:23:57:216 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-11 16:23:57:224 [ADB] Found 1 'build-tools' folders under 'E:\Android\android-sdk' (newest first):
2021-03-11 16:23:57:224 [ADB]     E:/Android/android-sdk/build-tools/29.0.3
2021-03-11 16:23:57:225 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-11 16:23:57:225 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-11 16:23:57:520 [AndroidDriver] Retrieving device list
2021-03-11 16:23:57:521 [ADB] Trying to find a connected android device
2021-03-11 16:23:57:521 [ADB] Getting connected devices
2021-03-11 16:23:57:833 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-11 16:23:57:834 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-11 16:23:57:835 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-11 16:23:57:835 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-11 16:23:58:132 [ADB] Setting device id to 127.0.0.1:21503
2021-03-11 16:23:58:132 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-11 16:23:58:464 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-11 16:23:58:465 [ADB] Device API level: 22
2021-03-11 16:23:58:465 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-11 16:23:58:466 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-11 16:23:58:762 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-11 16:23:59:063 [AndroidDriver] Pushing settings apk to device...
2021-03-11 16:23:59:064 [ADB] Getting install status for io.appium.settings
2021-03-11 16:23:59:064 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-11 16:23:59:376 [ADB] 'io.appium.settings' is installed
2021-03-11 16:23:59:377 [ADB] Getting package info for 'io.appium.settings'
2021-03-11 16:23:59:377 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-11 16:23:59:692 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-11 16:23:59:693 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-11 16:23:59:694 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-11 16:23:59:694 [ADB] Using ps-based PID detection
2021-03-11 16:23:59:694 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-11 16:23:59:997 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-11 16:24:00:311 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-11 16:24:00:312 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-11 16:24:00:875 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-11 16:24:01:192 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-11 16:24:01:193 [ADB] Forwarding system: 8200 to device: 6790
2021-03-11 16:24:01:193 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-11 16:24:01:508 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-11 16:24:01:509 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-11 16:24:01:510 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-11 16:24:01:517 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-11 16:24:01:518 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-11 16:24:02:154 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-11 16:24:02:155 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-11 16:24:02:156 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-11 16:24:02:528 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:24:02:529 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:24:02:535 [WD Proxy] socket hang up
2021-03-11 16:24:02:705 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-11 16:24:03:539 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:24:03:540 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:24:03:543 [WD Proxy] socket hang up
2021-03-11 16:24:04:544 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:24:04:545 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:24:04:563 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-11 16:24:04:563 [UiAutomator2] The initialization of the instrumentation process took 2409ms
2021-03-11 16:24:04:564 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-11 16:24:04:564 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-11 16:24:04:575 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3"}}
2021-03-11 16:24:04:576 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-11 16:24:04:588 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/appium/device/info] with no body
2021-03-11 16:24:04:601 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-11 16:24:04:601 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-11 16:24:04:923 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-11 16:24:04:925 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-11 16:24:04:925 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-11 16:24:08:885 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/appium/device/pixel_ratio] with no body
2021-03-11 16:24:08:890 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":1.5}
2021-03-11 16:24:08:891 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-11 16:24:08:891 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/appium/device/system_bars] with no body
2021-03-11 16:24:08:899 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"statusBar":38}}
2021-03-11 16:24:08:900 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-11 16:24:08:900 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/window/current/size] with no body
2021-03-11 16:24:08:912 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"height":1280,"width":720}}
2021-03-11 16:24:08:913 [Appium] New AndroidUiautomator2Driver session created successfully, session c9d94353-84db-4346-93bc-3b6391f302f0 added to master session list
2021-03-11 16:24:08:914 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-11 16:24:08:914 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-11 16:24:08:915 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-11 16:24:08:915 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-11 16:24:08:919 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":null}
2021-03-11 16:24:08:920 [BaseDriver] Event 'newSessionStarted' logged at 1615479848920 (00:24:08 GMT+0800 (中国标准时间))
2021-03-11 16:24:08:921 [W3C (c9d94353)] Cached the protocol value 'W3C' for the new session c9d94353-84db-4346-93bc-3b6391f302f0
2021-03-11 16:24:08:922 [W3C (c9d94353)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-11 16:24:08:927 [HTTP] <-- POST /wd/hub/session 200 12222 ms - 1080
2021-03-11 16:24:08:927 [HTTP] 
2021-03-11 16:24:08:929 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/timeouts
2021-03-11 16:24:08:930 [HTTP] {"implicit":10000}
2021-03-11 16:24:08:932 [W3C (c9d94353)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:08:933 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-11 16:24:08:933 [BaseDriver] Set implicit wait to 10000ms
2021-03-11 16:24:08:934 [W3C (c9d94353)] Responding to client with driver.timeouts() result: null
2021-03-11 16:24:08:935 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/timeouts 200 5 ms - 14
2021-03-11 16:24:08:935 [HTTP] 
2021-03-11 16:24:08:938 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element
2021-03-11 16:24:08:939 [HTTP] {"using":"xpath","value":"//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]"}
2021-03-11 16:24:08:942 [W3C (c9d94353)] Calling AppiumDriver.findElement() with args: ["xpath","//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]","c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:08:943 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:24:08:944 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:24:08:945 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:24:08:945 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]","context":"","multiple":false}
2021-03-11 16:24:10:214 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"ELEMENT":"358ee298-90f6-498d-8544-9a7f4782b455","element-6066-11e4-a52e-4f735466cecf":"358ee298-90f6-498d-8544-9a7f4782b455"}}
2021-03-11 16:24:10:216 [W3C (c9d94353)] Responding to client with driver.findElement() result: {"element-6066-11e4-a52e-4f735466cecf":"358ee298-90f6-498d-8544-9a7f4782b455","ELEMENT":"358ee298-90f6-498d-8544-9a7f4782b455"}
2021-03-11 16:24:10:217 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element 200 1278 ms - 137
2021-03-11 16:24:10:217 [HTTP] 
2021-03-11 16:24:10:218 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element/358ee298-90f6-498d-8544-9a7f4782b455/click
2021-03-11 16:24:10:219 [HTTP] {"id":"358ee298-90f6-498d-8544-9a7f4782b455"}
2021-03-11 16:24:10:221 [W3C (c9d94353)] Calling AppiumDriver.click() with args: ["358ee298-90f6-498d-8544-9a7f4782b455","c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:10:222 [WD Proxy] Matched '/element/358ee298-90f6-498d-8544-9a7f4782b455/click' to command name 'click'
2021-03-11 16:24:10:222 [WD Proxy] Proxying [POST /element/358ee298-90f6-498d-8544-9a7f4782b455/click] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/element/358ee298-90f6-498d-8544-9a7f4782b455/click] with body: {"element":"358ee298-90f6-498d-8544-9a7f4782b455"}
2021-03-11 16:24:10:808 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":null}
2021-03-11 16:24:10:809 [W3C (c9d94353)] Responding to client with driver.click() result: null
2021-03-11 16:24:10:810 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element/358ee298-90f6-498d-8544-9a7f4782b455/click 200 591 ms - 14
2021-03-11 16:24:10:810 [HTTP] 
2021-03-11 16:24:10:812 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element
2021-03-11 16:24:10:812 [HTTP] {"using":"xpath","value":"//*[@resource-id=\"com.xueqiu.android:id/action_search\"]"}
2021-03-11 16:24:10:813 [W3C (c9d94353)] Calling AppiumDriver.findElement() with args: ["xpath","//*[@resource-id=\"com.xueqiu.android:id/action_search\"]","c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:10:813 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:24:10:813 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:24:10:814 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:24:10:814 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/action_search\"]","context":"","multiple":false}
2021-03-11 16:24:13:104 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"ELEMENT":"37e7b986-f5ef-4434-887b-d515ff6ef79d","element-6066-11e4-a52e-4f735466cecf":"37e7b986-f5ef-4434-887b-d515ff6ef79d"}}
2021-03-11 16:24:13:105 [W3C (c9d94353)] Responding to client with driver.findElement() result: {"element-6066-11e4-a52e-4f735466cecf":"37e7b986-f5ef-4434-887b-d515ff6ef79d","ELEMENT":"37e7b986-f5ef-4434-887b-d515ff6ef79d"}
2021-03-11 16:24:13:106 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element 200 2294 ms - 137
2021-03-11 16:24:13:106 [HTTP] 
2021-03-11 16:24:13:108 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element/37e7b986-f5ef-4434-887b-d515ff6ef79d/click
2021-03-11 16:24:13:108 [HTTP] {"id":"37e7b986-f5ef-4434-887b-d515ff6ef79d"}
2021-03-11 16:24:13:109 [W3C (c9d94353)] Calling AppiumDriver.click() with args: ["37e7b986-f5ef-4434-887b-d515ff6ef79d","c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:13:110 [WD Proxy] Matched '/element/37e7b986-f5ef-4434-887b-d515ff6ef79d/click' to command name 'click'
2021-03-11 16:24:13:111 [WD Proxy] Proxying [POST /element/37e7b986-f5ef-4434-887b-d515ff6ef79d/click] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/element/37e7b986-f5ef-4434-887b-d515ff6ef79d/click] with body: {"element":"37e7b986-f5ef-4434-887b-d515ff6ef79d"}
2021-03-11 16:24:13:213 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":null}
2021-03-11 16:24:13:214 [W3C (c9d94353)] Responding to client with driver.click() result: null
2021-03-11 16:24:13:215 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element/37e7b986-f5ef-4434-887b-d515ff6ef79d/click 200 107 ms - 14
2021-03-11 16:24:13:215 [HTTP] 
2021-03-11 16:24:13:217 [HTTP] --> POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element
2021-03-11 16:24:13:217 [HTTP] {"using":"xpath","value":"//*[]@resource-id=\"com.xueqiu.android:id/search_input_text\""}
2021-03-11 16:24:13:217 [W3C (c9d94353)] Calling AppiumDriver.findElement() with args: ["xpath","//*[]@resource-id=\"com.xueqiu.android:id/search_input_text\"","c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:13:218 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:24:13:218 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:24:13:219 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:24:13:219 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3/element] with body: {"strategy":"xpath","selector":"//*[]@resource-id=\"com.xueqiu.android:id/search_input_text\"","context":"","multiple":false}
2021-03-11 16:24:13:351 [WD Proxy] Got response with status 400: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":{"error":"invalid selector","message":"java.lang.IllegalArgumentException: Unable to compile '//*[]@resource-id=\"com.xueqiu.android:id/search_input_text\"'. See Cause.","stacktrace":"io.appium.uiautomator2.common.exceptions.InvalidSelectorException: java.lang.IllegalArgumentException: Unable to compile '//*[]@resource-id=\"com.xueqiu.android:id/search_input_text\"'. See Cause.\n\tat io.appium.uiautomator2.core.AccessibilityNodeInfoDumper.findNodes(AccessibilityNodeInfoDumper.java:193)\n\tat io.appium.uiautomator2.utils.ElementLocationHelpers.getXPathNodeMatch(ElementLocationHelpers.java:113)\n\tat io.appium.uiautomator2.handler.FindElement.findElement(FindElement.java:89)\n\tat io.appium.uiautomator2.handler.FindElement.safeHandle(FindElement.java:68)\n\tat io.appium.uiautomator2.handler.request.SafeRequestHandler.handle(SafeRequestHandler.java:41)\n\tat io.appium.uiautomator2.server.AppiumServlet.handleRequest(AppiumServlet.java:261)\n\tat io.ap...
2021-03-11 16:24:13:352 [W3C] Matched W3C error code 'invalid selector' to InvalidSelectorError
2021-03-11 16:24:13:408 [W3C (c9d94353)] Encountered internal error running command: io.appium.uiautomator2.common.exceptions.InvalidSelectorException: java.lang.IllegalArgumentException: Unable to compile '//*[]@resource-id="com.xueqiu.android:id/search_input_text"'. See Cause.
2021-03-11 16:24:13:410 [W3C (c9d94353)] 	at io.appium.uiautomator2.core.AccessibilityNodeInfoDumper.findNodes(AccessibilityNodeInfoDumper.java:193)
2021-03-11 16:24:13:410 [W3C (c9d94353)] 	at io.appium.uiautomator2.utils.ElementLocationHelpers.getXPathNodeMatch(ElementLocationHelpers.java:113)
2021-03-11 16:24:13:411 [W3C (c9d94353)] 	at io.appium.uiautomator2.handler.FindElement.findElement(FindElement.java:89)
2021-03-11 16:24:13:411 [W3C (c9d94353)] 	at io.appium.uiautomator2.handler.FindElement.safeHandle(FindElement.java:68)
2021-03-11 16:24:13:411 [W3C (c9d94353)] 	at io.appium.uiautomator2.handler.request.SafeRequestHandler.handle(SafeRequestHandler.java:41)
2021-03-11 16:24:13:412 [W3C (c9d94353)] 	at io.appium.uiautomator2.server.AppiumServlet.handleRequest(AppiumServlet.java:261)
2021-03-11 16:24:13:412 [W3C (c9d94353)] 	at io.appium.uiautomator2.server.AppiumServlet.handleHttpRequest(AppiumServlet.java:255)
2021-03-11 16:24:13:414 [W3C (c9d94353)] 	at io.appium.uiautomator2.http.ServerHandler.channelRead(ServerHandler.java:68)
2021-03-11 16:24:13:414 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)
2021-03-11 16:24:13:414 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:352)
2021-03-11 16:24:13:415 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:345)
2021-03-11 16:24:13:415 [W3C (c9d94353)] 	at io.netty.handler.codec.MessageToMessageDecoder.channelRead(MessageToMessageDecoder.java:102)
2021-03-11 16:24:13:415 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)
2021-03-11 16:24:13:415 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:352)
2021-03-11 16:24:13:416 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:345)
2021-03-11 16:24:13:416 [W3C (c9d94353)] 	at io.netty.channel.CombinedChannelDuplexHandler$DelegatingChannelHandlerContext.fireChannelRead(CombinedChannelDuplexHandler.java:435)
2021-03-11 16:24:13:416 [W3C (c9d94353)] 	at io.netty.handler.codec.ByteToMessageDecoder.fireChannelRead(ByteToMessageDecoder.java:293)
2021-03-11 16:24:13:417 [W3C (c9d94353)] 	at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:267)
2021-03-11 16:24:13:418 [W3C (c9d94353)] 	at io.netty.channel.CombinedChannelDuplexHandler.channelRead(CombinedChannelDuplexHandler.java:250)
2021-03-11 16:24:13:418 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)
2021-03-11 16:24:13:419 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:352)
2021-03-11 16:24:13:419 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:345)
2021-03-11 16:24:13:419 [W3C (c9d94353)] 	at io.netty.handler.timeout.IdleStateHandler.channelRead(IdleStateHandler.java:266)
2021-03-11 16:24:13:420 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)
2021-03-11 16:24:13:420 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:352)
2021-03-11 16:24:13:420 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:345)
2021-03-11 16:24:13:421 [W3C (c9d94353)] 	at io.netty.channel.DefaultChannelPipeline$HeadContext.channelRead(DefaultChannelPipeline.java:1294)
2021-03-11 16:24:13:421 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)
2021-03-11 16:24:13:421 [W3C (c9d94353)] 	at io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:352)
2021-03-11 16:24:13:422 [W3C (c9d94353)] 	at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:911)
2021-03-11 16:24:13:422 [W3C (c9d94353)] 	at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:131)
2021-03-11 16:24:13:422 [W3C (c9d94353)] 	at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:611)
2021-03-11 16:24:13:423 [W3C (c9d94353)] 	at io.netty.channel.nio.NioEventLoop.processSelectedKeysPlain(NioEventLoop.java:514)
2021-03-11 16:24:13:423 [W3C (c9d94353)] 	at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:468)
2021-03-11 16:24:13:423 [W3C (c9d94353)] 	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:438)
2021-03-11 16:24:13:423 [W3C (c9d94353)] 	at io.netty.util.concurrent.SingleThreadEventExecutor$2.run(SingleThreadEventExecutor.java:140)
2021-03-11 16:24:13:424 [W3C (c9d94353)] 	at io.netty.util.concurrent.DefaultThreadFactory$DefaultRunnableDecorator.run(DefaultThreadFactory.java:144)
2021-03-11 16:24:13:425 [W3C (c9d94353)] 	at java.lang.Thread.run(Thread.java:818)
2021-03-11 16:24:13:425 [W3C (c9d94353)] Caused by: java.lang.IllegalArgumentException: Unable to compile '//*[]@resource-id="com.xueqiu.android:id/search_input_text"'. See Cause.
2021-03-11 16:24:13:425 [W3C (c9d94353)] 	at org.jdom2.xpath.jaxen.JaxenCompiled.<init>(JaxenCompiled.java:152)
2021-03-11 16:24:13:426 [W3C (c9d94353)] 	at org.jdom2.xpath.jaxen.JaxenXPathFactory.compile(JaxenXPathFactory.java:82)
2021-03-11 16:24:13:426 [W3C (c9d94353)] 	at org.jdom2.xpath.XPathFactory.compile(XPathFactory.java:282)
2021-03-11 16:24:13:427 [W3C (c9d94353)] 	at io.appium.uiautomator2.core.AccessibilityNodeInfoDumper.findNodes(AccessibilityNodeInfoDumper.java:191)
2021-03-11 16:24:13:427 [W3C (c9d94353)] 	... 37 more
2021-03-11 16:24:13:428 [W3C (c9d94353)] Caused by: org.jaxen.XPathSyntaxException: Unexpected ']'
2021-03-11 16:24:13:428 [W3C (c9d94353)] 	at org.jaxen.BaseXPath.<init>(BaseXPath.java:121)
2021-03-11 16:24:13:428 [W3C (c9d94353)] 	at org.jaxen.BaseXPath.<init>(BaseXPath.java:142)
2021-03-11 16:24:13:429 [W3C (c9d94353)] 	at org.jdom2.xpath.jaxen.JaxenCompiled.<init>(JaxenCompiled.java:150)
2021-03-11 16:24:13:429 [W3C (c9d94353)] 	... 40 more
2021-03-11 16:24:13:429 [W3C (c9d94353)] Caused by: class org.jaxen.saxpath.XPathSyntaxException: //*[]@resource-id="com.xueqiu.android:id/search_input_text": 4: Unexpected ']'
2021-03-11 16:24:13:430 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.createSyntaxException(XPathReader.java:1085)
2021-03-11 16:24:13:430 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.pathExpr(XPathReader.java:190)
2021-03-11 16:24:13:430 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.unionExpr(XPathReader.java:1007)
2021-03-11 16:24:13:430 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.unaryExpr(XPathReader.java:995)
2021-03-11 16:24:13:431 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.multiplicativeExpr(XPathReader.java:943)
2021-03-11 16:24:13:431 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.additiveExpr(XPathReader.java:913)
2021-03-11 16:24:13:432 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.relationalExpr(XPathReader.java:860)
2021-03-11 16:24:13:432 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.equalityExpr(XPathReader.java:829)
2021-03-11 16:24:13:432 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.andExpr(XPathReader.java:809)
2021-03-11 16:24:13:433 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.orExpr(XPathReader.java:787)
2021-03-11 16:24:13:433 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.expr(XPathReader.java:780)
2021-03-11 16:24:13:433 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.predicateExpr(XPathReader.java:775)
2021-03-11 16:24:13:433 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.predicate(XPathReader.java:766)
2021-03-11 16:24:13:434 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.predicates(XPathReader.java:751)
2021-03-11 16:24:13:434 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.nameTest(XPathReader.java:717)
2021-03-11 16:24:13:436 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.nodeTest(XPathReader.java:600)
2021-03-11 16:24:13:436 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.step(XPathReader.java:541)
2021-03-11 16:24:13:436 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.steps(XPathReader.java:442)
2021-03-11 16:24:13:437 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.absoluteLocationPath(XPathReader.java:390)
2021-03-11 16:24:13:437 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.locationPath(XPathReader.java:326)
2021-03-11 16:24:13:437 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.pathExpr(XPathReader.java:185)
2021-03-11 16:24:13:437 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.unionExpr(XPathReader.java:1007)
2021-03-11 16:24:13:438 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.unaryExpr(XPathReader.java:995)
2021-03-11 16:24:13:438 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.multiplicativeExpr(XPathReader.java:943)
2021-03-11 16:24:13:438 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.additiveExpr(XPathReader.java:913)
2021-03-11 16:24:13:438 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.relationalExpr(XPathReader.java:860)
2021-03-11 16:24:13:439 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.equalityExpr(XPathReader.java:829)
2021-03-11 16:24:13:439 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.andExpr(XPathReader.java:809)
2021-03-11 16:24:13:439 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.orExpr(XPathReader.java:787)
2021-03-11 16:24:13:440 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.expr(XPathReader.java:780)
2021-03-11 16:24:13:440 [W3C (c9d94353)] 	at org.jaxen.saxpath.base.XPathReader.parse(XPathReader.java:100)
2021-03-11 16:24:13:440 [W3C (c9d94353)] 	at org.jaxen.BaseXPath.<init>(BaseXPath.java:116)
2021-03-11 16:24:13:441 [W3C (c9d94353)] 	... 42 more
2021-03-11 16:24:13:441 [W3C (c9d94353)] 
2021-03-11 16:24:13:444 [HTTP] <-- POST /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0/element 400 225 ms - 7425
2021-03-11 16:24:13:444 [HTTP] 
2021-03-11 16:24:13:653 [HTTP] --> DELETE /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0
2021-03-11 16:24:13:655 [HTTP] {}
2021-03-11 16:24:13:658 [W3C (c9d94353)] Calling AppiumDriver.deleteSession() with args: ["c9d94353-84db-4346-93bc-3b6391f302f0"]
2021-03-11 16:24:13:660 [BaseDriver] Event 'quitSessionRequested' logged at 1615479853659 (00:24:13 GMT+0800 (中国标准时间))
2021-03-11 16:24:13:660 [Appium] Removing session c9d94353-84db-4346-93bc-3b6391f302f0 from our master session list
2021-03-11 16:24:13:662 [UiAutomator2] Deleting UiAutomator2 session
2021-03-11 16:24:13:662 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-11 16:24:13:664 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-11 16:24:13:665 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/77aa7088-0cdd-4d7a-898d-8fd6556221e3] with no body
2021-03-11 16:24:13:673 [WD Proxy] Got response with status 200: {"sessionId":"77aa7088-0cdd-4d7a-898d-8fd6556221e3","value":null}
2021-03-11 16:24:13:674 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-11 16:24:14:007 [Instrumentation] .
2021-03-11 16:24:14:078 [Instrumentation] Time: 11.025
2021-03-11 16:24:14:079 [Instrumentation] 
2021-03-11 16:24:14:079 [Instrumentation] OK (1 test)
2021-03-11 16:24:14:289 [Instrumentation] The process has exited with code 0
2021-03-11 16:24:14:377 [Logcat] Stopping logcat capture
2021-03-11 16:24:14:382 [ADB] Removing forwarded port socket connection: 8200 
2021-03-11 16:24:14:383 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-11 16:24:14:693 [BaseDriver] Event 'quitSessionFinished' logged at 1615479854692 (00:24:14 GMT+0800 (中国标准时间))
2021-03-11 16:24:14:693 [W3C (c9d94353)] Received response: null
2021-03-11 16:24:14:694 [W3C (c9d94353)] But deleting session, so not returning
2021-03-11 16:24:14:694 [W3C (c9d94353)] Responding to client with driver.deleteSession() result: null
2021-03-11 16:24:14:696 [HTTP] <-- DELETE /wd/hub/session/c9d94353-84db-4346-93bc-3b6391f302f0 200 1043 ms - 14
2021-03-11 16:24:14:696 [HTTP] 
2021-03-11 16:25:40:967 [HTTP] Request idempotency key: 4d4a973d-3112-4ef9-8b02-5dc098f1958f
2021-03-11 16:25:40:969 [HTTP] --> POST /wd/hub/session
2021-03-11 16:25:40:969 [HTTP] {"capabilities":{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]},"desiredCapabilities":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true}}
2021-03-11 16:25:40:970 [W3C] Calling AppiumDriver.createSession() with args: [{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"settings[waitForIdleTimeout]":1,"noReset":true},null,{"firstMatch":[{"platformName":"Android","appium:automationName":"UiAutomator2","appium:deviceName":"127.0.0.1:21503","appium:appPackage":"com.xueqiu.android","appium:appActivity":"com.xueqiu.android.main.view.MainActivity","appium:skipServerInstallation":true,"appium:skipDeviceInstallation":true,"appium:settings[waitForIdleTimeout]":1,"appium:noReset":true}]}]
2021-03-11 16:25:40:971 [BaseDriver] Event 'newSessionRequested' logged at 1615479940970 (00:25:40 GMT+0800 (中国标准时间))
2021-03-11 16:25:40:972 [Appium] Appium v1.20.0 creating new AndroidUiautomator2Driver (v1.60.0) session
2021-03-11 16:25:40:973 [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
2021-03-11 16:25:40:974 [BaseDriver] Creating session with W3C capabilities: {
2021-03-11 16:25:40:974 [BaseDriver]   "alwaysMatch": {
2021-03-11 16:25:40:975 [BaseDriver]     "platformName": "Android",
2021-03-11 16:25:40:976 [BaseDriver]     "appium:automationName": "UiAutomator2",
2021-03-11 16:25:40:976 [BaseDriver]     "appium:deviceName": "127.0.0.1:21503",
2021-03-11 16:25:40:976 [BaseDriver]     "appium:appPackage": "com.xueqiu.android",
2021-03-11 16:25:40:977 [BaseDriver]     "appium:appActivity": "com.xueqiu.android.main.view.MainActivity",
2021-03-11 16:25:40:977 [BaseDriver]     "appium:skipServerInstallation": true,
2021-03-11 16:25:40:978 [BaseDriver]     "appium:skipDeviceInstallation": true,
2021-03-11 16:25:40:981 [BaseDriver]     "appium:noReset": true
2021-03-11 16:25:40:981 [BaseDriver]   },
2021-03-11 16:25:40:982 [BaseDriver]   "firstMatch": [
2021-03-11 16:25:40:982 [BaseDriver]     {}
2021-03-11 16:25:40:983 [BaseDriver]   ]
2021-03-11 16:25:40:983 [BaseDriver] }
2021-03-11 16:25:40:988 [BaseDriver] The following capabilities were provided, but are not recognized by Appium:
2021-03-11 16:25:40:988 [BaseDriver]   skipDeviceInstallation
2021-03-11 16:25:40:989 [BaseDriver] Session created with session id: d4599237-38f0-431e-8b07-1110d17b7348
2021-03-11 16:25:40:989 [UiAutomator2] Starting 'com.xueqiu.android' directly on the device
2021-03-11 16:25:40:991 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-11 16:25:40:992 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-11 16:25:41:348 [AndroidDriver] Retrieving device list
2021-03-11 16:25:41:349 [ADB] Trying to find a connected android device
2021-03-11 16:25:41:350 [ADB] Getting connected devices
2021-03-11 16:25:41:685 [ADB] Connected devices: [{"udid":"127.0.0.1:21503","state":"device"}]
2021-03-11 16:25:41:686 [AndroidDriver] Using device: 127.0.0.1:21503
2021-03-11 16:25:41:687 [ADB] Using 'adb.exe' from 'E:\Android\android-sdk\platform-tools\adb.exe'
2021-03-11 16:25:41:687 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 start-server'
2021-03-11 16:25:42:028 [ADB] Setting device id to 127.0.0.1:21503
2021-03-11 16:25:42:030 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell getprop ro.build.version.sdk'
2021-03-11 16:25:42:360 [ADB] Current device property 'ro.build.version.sdk': 22
2021-03-11 16:25:42:361 [ADB] Device API level: 22
2021-03-11 16:25:42:361 [AndroidDriver] No app sent in, not parsing package/activity
2021-03-11 16:25:42:361 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 wait-for-device'
2021-03-11 16:25:42:673 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell echo ping'
2021-03-11 16:25:42:999 [AndroidDriver] Pushing settings apk to device...
2021-03-11 16:25:42:999 [ADB] Getting install status for io.appium.settings
2021-03-11 16:25:43:000 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-11 16:25:43:318 [ADB] 'io.appium.settings' is installed
2021-03-11 16:25:43:319 [ADB] Getting package info for 'io.appium.settings'
2021-03-11 16:25:43:319 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys package io.appium.settings'
2021-03-11 16:25:43:643 [ADB] The version name of the installed 'io.appium.settings' is greater or equal to the application version name ('3.2.1' >= '3.2.1')
2021-03-11 16:25:43:644 [ADB] There is no need to install/upgrade 'C:\Users\Administrator\AppData\Roaming\npm\node_modules\appium\node_modules\io.appium.settings\apks\settings_apk-debug.apk'
2021-03-11 16:25:43:645 [ADB] Getting IDs of all 'io.appium.settings' processes
2021-03-11 16:25:43:645 [ADB] Using ps-based PID detection
2021-03-11 16:25:43:645 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps --help'
2021-03-11 16:25:43:987 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell ps'
2021-03-11 16:25:44:357 [AndroidDriver] io.appium.settings is already running. There is no need to reset its permissions.
2021-03-11 16:25:44:359 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell settings put secure mock_location 1'
2021-03-11 16:25:44:976 [Logcat] Starting logs capture with command: E:\\Android\\android-sdk\\platform-tools\\adb.exe -P 5037 -s 127.0.0.1\:21503 logcat -v threadtime
2021-03-11 16:25:45:340 [UiAutomator2] Forwarding UiAutomator2 Server port 6790 to local port 8200
2021-03-11 16:25:45:341 [ADB] Forwarding system: 8200 to device: 6790
2021-03-11 16:25:45:341 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward tcp:8200 tcp:6790'
2021-03-11 16:25:45:710 [UiAutomator2] 'skipServerInstallation' is set. Skipping UIAutomator2 server installation.
2021-03-11 16:25:45:711 [UiAutomator2] No app capability. Assuming it is already on the device
2021-03-11 16:25:45:711 [UiAutomator2] Performing shallow cleanup of automation leftovers
2021-03-11 16:25:45:714 [UiAutomator2] No obsolete sessions have been detected (socket hang up)
2021-03-11 16:25:45:715 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop io.appium.uiautomator2.server.test'
2021-03-11 16:25:46:352 [UiAutomator2] 'skipServerInstallation' is set. Attempting to use UIAutomator2 server from the device
2021-03-11 16:25:46:353 [UiAutomator2] Waiting up to 30000ms for UiAutomator2 to be online...
2021-03-11 16:25:46:354 [ADB] Creating ADB subprocess with args: ["-P",5037,"-s","127.0.0.1:21503","shell","am","instrument","-w","io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner"]
2021-03-11 16:25:46:765 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:25:46:766 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:25:46:769 [WD Proxy] socket hang up
2021-03-11 16:25:46:957 [Instrumentation] io.appium.uiautomator2.server.test.AppiumUiAutomator2Server:
2021-03-11 16:25:47:772 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:25:47:773 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:25:47:776 [WD Proxy] socket hang up
2021-03-11 16:25:48:777 [WD Proxy] Matched '/status' to command name 'getStatus'
2021-03-11 16:25:48:777 [WD Proxy] Proxying [GET /status] to [GET http://127.0.0.1:8200/wd/hub/status] with no body
2021-03-11 16:25:48:793 [WD Proxy] Got response with status 200: {"sessionId":"None","value":{"message":"UiAutomator2 Server is ready to accept commands","ready":true}}
2021-03-11 16:25:48:794 [UiAutomator2] The initialization of the instrumentation process took 2441ms
2021-03-11 16:25:48:794 [WD Proxy] Matched '/session' to command name 'createSession'
2021-03-11 16:25:48:795 [WD Proxy] Proxying [POST /session] to [POST http://127.0.0.1:8200/wd/hub/session] with body: {"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}}}
2021-03-11 16:25:48:804 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"capabilities":{"firstMatch":[{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503"}],"alwaysMatch":{}},"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47"}}
2021-03-11 16:25:48:804 [WD Proxy] Determined the downstream protocol as 'W3C'
2021-03-11 16:25:48:806 [WD Proxy] Proxying [GET /appium/device/info] to [GET http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/appium/device/info] with no body
2021-03-11 16:25:48:817 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"androidId":"ad3f85e1ed8a9381","apiVersion":"22","bluetooth":{"state":"OFF"},"brand":"HUAWEI","carrierName":"China Mobile GSM","displayDensity":240,"locale":"zh_CN","manufacturer":"HUAWEI","model":"TAS-AN00","networks":[{"capabilities":{"SSID":null,"linkDownBandwidthKbps":1048576,"linkUpstreamBandwidthKbps":1048576,"networkCapabilities":"NET_CAPABILITY_NOT_RESTRICTED,NET_CAPABILITY_NOT_VPN,NET_CAPABILITY_INTERNET,NET_CAPABILITY_TRUSTED","signalStrength":null,"transportTypes":"TRANSPORT_WIFI"},"detailedState":"CONNECTED","extraInfo":"\"ekgjmg5877\"","isAvailable":true,"isConnected":true,"isFailover":false,"isRoaming":false,"state":"CONNECTED","subtype":0,"subtypeName":"","type":1,"typeName":"WIFI"}],"platformVersion":"5.1.1","realDisplaySize":"720x1280","timeZone":"Asia/Shanghai"}}
2021-03-11 16:25:48:818 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell dumpsys window'
2021-03-11 16:25:49:139 [AndroidDriver] Screen already unlocked, doing nothing
2021-03-11 16:25:49:140 [UiAutomator2] Starting 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity and waiting for 'com.xueqiu.android/com.xueqiu.android.main.view.MainActivity'
2021-03-11 16:25:49:140 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am start -W -n com.xueqiu.android/com.xueqiu.android.main.view.MainActivity -S -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -f 0x10200000'
2021-03-11 16:25:53:031 [WD Proxy] Proxying [GET /appium/device/pixel_ratio] to [GET http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/appium/device/pixel_ratio] with no body
2021-03-11 16:25:53:035 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":1.5}
2021-03-11 16:25:53:036 [WD Proxy] Matched '/appium/device/system_bars' to command name 'getSystemBars'
2021-03-11 16:25:53:036 [WD Proxy] Proxying [GET /appium/device/system_bars] to [GET http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/appium/device/system_bars] with no body
2021-03-11 16:25:53:040 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"statusBar":38}}
2021-03-11 16:25:53:041 [WD Proxy] Matched '/window/current/size' to command name 'getWindowSize'
2021-03-11 16:25:53:041 [WD Proxy] Proxying [GET /window/current/size] to [GET http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/window/current/size] with no body
2021-03-11 16:25:53:047 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"height":1280,"width":720}}
2021-03-11 16:25:53:048 [Appium] New AndroidUiautomator2Driver session created successfully, session d4599237-38f0-431e-8b07-1110d17b7348 added to master session list
2021-03-11 16:25:53:048 [Appium] Applying the initial values to Appium settings parsed from W3C caps: {"waitForIdleTimeout":1}
2021-03-11 16:25:53:048 [UiAutomator2] Forwarding the following settings to the UiAutomator2 server: ["waitForIdleTimeout"]
2021-03-11 16:25:53:049 [WD Proxy] Matched '/appium/settings' to command name 'updateSettings'
2021-03-11 16:25:53:050 [WD Proxy] Proxying [POST /appium/settings] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/appium/settings] with body: {"settings":{"waitForIdleTimeout":1}}
2021-03-11 16:25:53:055 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":null}
2021-03-11 16:25:53:055 [BaseDriver] Event 'newSessionStarted' logged at 1615479953055 (00:25:53 GMT+0800 (中国标准时间))
2021-03-11 16:25:53:056 [W3C (d4599237)] Cached the protocol value 'W3C' for the new session d4599237-38f0-431e-8b07-1110d17b7348
2021-03-11 16:25:53:056 [W3C (d4599237)] Responding to client with driver.createSession() result: {"capabilities":{"platform":"LINUX","webStorageEnabled":false,"takesScreenshot":true,"javascriptEnabled":true,"databaseEnabled":false,"networkConnectionEnabled":true,"locationContextEnabled":false,"warnings":{},"desired":{"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true},"platformName":"Android","automationName":"UiAutomator2","deviceName":"127.0.0.1:21503","appPackage":"com.xueqiu.android","appActivity":"com.xueqiu.android.main.view.MainActivity","skipServerInstallation":true,"skipDeviceInstallation":true,"noReset":true,"deviceUDID":"127.0.0.1:21503","deviceApiLevel":22,"platformVersion":"5.1.1","deviceScreenSize":"720x1280","deviceScreenDensity":240,"deviceModel":"TAS-AN00","deviceManufacturer":"HUAWEI","pixelRatio":1.5,"statBarHeight":38,"viewportRect":{"left":0,"top":38,"width":720,"height":1242}}}
2021-03-11 16:25:53:057 [HTTP] <-- POST /wd/hub/session 200 12088 ms - 1080
2021-03-11 16:25:53:059 [HTTP] 
2021-03-11 16:25:53:061 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/timeouts
2021-03-11 16:25:53:061 [HTTP] {"implicit":10000}
2021-03-11 16:25:53:062 [W3C (d4599237)] Calling AppiumDriver.timeouts() with args: [null,null,null,null,10000,"d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:53:062 [BaseDriver] W3C timeout argument: {"implicit":10000}}
2021-03-11 16:25:53:063 [BaseDriver] Set implicit wait to 10000ms
2021-03-11 16:25:53:063 [W3C (d4599237)] Responding to client with driver.timeouts() result: null
2021-03-11 16:25:53:064 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/timeouts 200 3 ms - 14
2021-03-11 16:25:53:064 [HTTP] 
2021-03-11 16:25:53:066 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element
2021-03-11 16:25:53:066 [HTTP] {"using":"xpath","value":"//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]"}
2021-03-11 16:25:53:067 [W3C (d4599237)] Calling AppiumDriver.findElement() with args: ["xpath","//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:53:067 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:25:53:067 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:25:53:068 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:25:53:069 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/tab_name\" and @text=\"行情\"]","context":"","multiple":false}
2021-03-11 16:25:54:335 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"ELEMENT":"32bb4a77-c984-4a18-ac90-8724b03397eb","element-6066-11e4-a52e-4f735466cecf":"32bb4a77-c984-4a18-ac90-8724b03397eb"}}
2021-03-11 16:25:54:338 [W3C (d4599237)] Responding to client with driver.findElement() result: {"element-6066-11e4-a52e-4f735466cecf":"32bb4a77-c984-4a18-ac90-8724b03397eb","ELEMENT":"32bb4a77-c984-4a18-ac90-8724b03397eb"}
2021-03-11 16:25:54:339 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element 200 1273 ms - 137
2021-03-11 16:25:54:340 [HTTP] 
2021-03-11 16:25:54:341 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/32bb4a77-c984-4a18-ac90-8724b03397eb/click
2021-03-11 16:25:54:341 [HTTP] {"id":"32bb4a77-c984-4a18-ac90-8724b03397eb"}
2021-03-11 16:25:54:342 [W3C (d4599237)] Calling AppiumDriver.click() with args: ["32bb4a77-c984-4a18-ac90-8724b03397eb","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:54:343 [WD Proxy] Matched '/element/32bb4a77-c984-4a18-ac90-8724b03397eb/click' to command name 'click'
2021-03-11 16:25:54:344 [WD Proxy] Proxying [POST /element/32bb4a77-c984-4a18-ac90-8724b03397eb/click] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element/32bb4a77-c984-4a18-ac90-8724b03397eb/click] with body: {"element":"32bb4a77-c984-4a18-ac90-8724b03397eb"}
2021-03-11 16:25:54:929 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":null}
2021-03-11 16:25:54:930 [W3C (d4599237)] Responding to client with driver.click() result: null
2021-03-11 16:25:54:931 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/32bb4a77-c984-4a18-ac90-8724b03397eb/click 200 590 ms - 14
2021-03-11 16:25:54:931 [HTTP] 
2021-03-11 16:25:54:932 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element
2021-03-11 16:25:54:933 [HTTP] {"using":"xpath","value":"//*[@resource-id=\"com.xueqiu.android:id/action_search\"]"}
2021-03-11 16:25:54:933 [W3C (d4599237)] Calling AppiumDriver.findElement() with args: ["xpath","//*[@resource-id=\"com.xueqiu.android:id/action_search\"]","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:54:934 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:25:54:934 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:25:54:935 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:25:54:935 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/action_search\"]","context":"","multiple":false}
2021-03-11 16:25:54:974 [WD Proxy] Got response with status 404: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"error":"no such element","message":"An element could not be located on the page using the given search parameters","stacktrace":"io.appium.uiautomator2.common.exceptions.ElementNotFoundException: An element could not be located on the page using the given search parameters\n\tat io.appium.uiautomator2.handler.FindElement.findElement(FindElement.java:91)\n\tat io.appium.uiautomator2.handler.FindElement.safeHandle(FindElement.java:68)\n\tat io.appium.uiautomator2.handler.request.SafeRequestHandler.handle(SafeRequestHandler.java:41)\n\tat io.appium.uiautomator2.server.AppiumServlet.handleRequest(AppiumServlet.java:261)\n\tat io.appium.uiautomator2.server.AppiumServlet.handleHttpRequest(AppiumServlet.java:255)\n\tat io.appium.uiautomator2.http.ServerHandler.channelRead(ServerHandler.java:68)\n\tat io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)\n\tat io.netty.channel.AbstractChannelHandlerCont...
2021-03-11 16:25:54:975 [W3C] Matched W3C error code 'no such element' to NoSuchElementError
2021-03-11 16:25:54:976 [BaseDriver] Waited for 42 ms so far
2021-03-11 16:25:55:480 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:25:55:481 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/action_search\"]","context":"","multiple":false}
2021-03-11 16:25:56:587 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"ELEMENT":"e530f3d3-d782-4b5f-9639-5cae430a04b0","element-6066-11e4-a52e-4f735466cecf":"e530f3d3-d782-4b5f-9639-5cae430a04b0"}}
2021-03-11 16:25:56:587 [W3C (d4599237)] Responding to client with driver.findElement() result: {"element-6066-11e4-a52e-4f735466cecf":"e530f3d3-d782-4b5f-9639-5cae430a04b0","ELEMENT":"e530f3d3-d782-4b5f-9639-5cae430a04b0"}
2021-03-11 16:25:56:588 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element 200 1656 ms - 137
2021-03-11 16:25:56:589 [HTTP] 
2021-03-11 16:25:56:590 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/e530f3d3-d782-4b5f-9639-5cae430a04b0/click
2021-03-11 16:25:56:590 [HTTP] {"id":"e530f3d3-d782-4b5f-9639-5cae430a04b0"}
2021-03-11 16:25:56:592 [W3C (d4599237)] Calling AppiumDriver.click() with args: ["e530f3d3-d782-4b5f-9639-5cae430a04b0","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:56:592 [WD Proxy] Matched '/element/e530f3d3-d782-4b5f-9639-5cae430a04b0/click' to command name 'click'
2021-03-11 16:25:56:593 [WD Proxy] Proxying [POST /element/e530f3d3-d782-4b5f-9639-5cae430a04b0/click] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element/e530f3d3-d782-4b5f-9639-5cae430a04b0/click] with body: {"element":"e530f3d3-d782-4b5f-9639-5cae430a04b0"}
2021-03-11 16:25:56:865 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":null}
2021-03-11 16:25:56:866 [W3C (d4599237)] Responding to client with driver.click() result: null
2021-03-11 16:25:56:867 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/e530f3d3-d782-4b5f-9639-5cae430a04b0/click 200 277 ms - 14
2021-03-11 16:25:56:867 [HTTP] 
2021-03-11 16:25:56:868 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element
2021-03-11 16:25:56:869 [HTTP] {"using":"xpath","value":"//*[@resource-id=\"com.xueqiu.android:id/search_input_text\"]"}
2021-03-11 16:25:56:869 [W3C (d4599237)] Calling AppiumDriver.findElement() with args: ["xpath","//*[@resource-id=\"com.xueqiu.android:id/search_input_text\"]","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:56:870 [BaseDriver] Valid locator strategies for this request: xpath, id, class name, accessibility id, css selector, -android uiautomator
2021-03-11 16:25:56:870 [BaseDriver] Waiting up to 10000 ms for condition
2021-03-11 16:25:56:870 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:25:56:871 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/search_input_text\"]","context":"","multiple":false}
2021-03-11 16:25:57:217 [WD Proxy] Got response with status 404: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"error":"no such element","message":"An element could not be located on the page using the given search parameters","stacktrace":"io.appium.uiautomator2.common.exceptions.ElementNotFoundException: An element could not be located on the page using the given search parameters\n\tat io.appium.uiautomator2.handler.FindElement.findElement(FindElement.java:91)\n\tat io.appium.uiautomator2.handler.FindElement.safeHandle(FindElement.java:68)\n\tat io.appium.uiautomator2.handler.request.SafeRequestHandler.handle(SafeRequestHandler.java:41)\n\tat io.appium.uiautomator2.server.AppiumServlet.handleRequest(AppiumServlet.java:261)\n\tat io.appium.uiautomator2.server.AppiumServlet.handleHttpRequest(AppiumServlet.java:255)\n\tat io.appium.uiautomator2.http.ServerHandler.channelRead(ServerHandler.java:68)\n\tat io.netty.channel.AbstractChannelHandlerContext.invokeChannelRead(AbstractChannelHandlerContext.java:366)\n\tat io.netty.channel.AbstractChannelHandlerCont...
2021-03-11 16:25:57:218 [W3C] Matched W3C error code 'no such element' to NoSuchElementError
2021-03-11 16:25:57:219 [BaseDriver] Waited for 349 ms so far
2021-03-11 16:25:57:721 [WD Proxy] Matched '/element' to command name 'findElement'
2021-03-11 16:25:57:721 [WD Proxy] Proxying [POST /element] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element] with body: {"strategy":"xpath","selector":"//*[@resource-id=\"com.xueqiu.android:id/search_input_text\"]","context":"","multiple":false}
2021-03-11 16:25:58:006 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":{"ELEMENT":"f50d73cf-1dd0-4459-b79e-6619641fb501","element-6066-11e4-a52e-4f735466cecf":"f50d73cf-1dd0-4459-b79e-6619641fb501"}}
2021-03-11 16:25:58:007 [W3C (d4599237)] Responding to client with driver.findElement() result: {"element-6066-11e4-a52e-4f735466cecf":"f50d73cf-1dd0-4459-b79e-6619641fb501","ELEMENT":"f50d73cf-1dd0-4459-b79e-6619641fb501"}
2021-03-11 16:25:58:008 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element 200 1140 ms - 137
2021-03-11 16:25:58:008 [HTTP] 
2021-03-11 16:25:58:010 [HTTP] --> POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/f50d73cf-1dd0-4459-b79e-6619641fb501/value
2021-03-11 16:25:58:010 [HTTP] {"text":"alibaba","value":["a","l","i","b","a","b","a"],"id":"f50d73cf-1dd0-4459-b79e-6619641fb501"}
2021-03-11 16:25:58:011 [W3C (d4599237)] Calling AppiumDriver.setValue() with args: [["a","l","i","b","a","b","a"],"f50d73cf-1dd0-4459-b79e-6619641fb501","d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:25:58:012 [WD Proxy] Matched '/element/f50d73cf-1dd0-4459-b79e-6619641fb501/value' to command name 'setValue'
2021-03-11 16:25:58:012 [Protocol Converter] Added 'value' property ["a","l","i","b","a","b","a"] to 'setValue' request body
2021-03-11 16:25:58:012 [WD Proxy] Proxying [POST /element/f50d73cf-1dd0-4459-b79e-6619641fb501/value] to [POST http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47/element/f50d73cf-1dd0-4459-b79e-6619641fb501/value] with body: {"elementId":"f50d73cf-1dd0-4459-b79e-6619641fb501","text":"alibaba","replace":false,"value":["a","l","i","b","a","b","a"]}
2021-03-11 16:25:58:546 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":null}
2021-03-11 16:25:58:547 [W3C (d4599237)] Responding to client with driver.setValue() result: null
2021-03-11 16:25:58:548 [HTTP] <-- POST /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348/element/f50d73cf-1dd0-4459-b79e-6619641fb501/value 200 538 ms - 14
2021-03-11 16:25:58:548 [HTTP] 
2021-03-11 16:26:03:551 [HTTP] --> DELETE /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348
2021-03-11 16:26:03:552 [HTTP] {}
2021-03-11 16:26:03:552 [W3C (d4599237)] Calling AppiumDriver.deleteSession() with args: ["d4599237-38f0-431e-8b07-1110d17b7348"]
2021-03-11 16:26:03:552 [BaseDriver] Event 'quitSessionRequested' logged at 1615479963552 (00:26:03 GMT+0800 (中国标准时间))
2021-03-11 16:26:03:553 [Appium] Removing session d4599237-38f0-431e-8b07-1110d17b7348 from our master session list
2021-03-11 16:26:03:553 [UiAutomator2] Deleting UiAutomator2 session
2021-03-11 16:26:03:553 [UiAutomator2] Deleting UiAutomator2 server session
2021-03-11 16:26:03:553 [WD Proxy] Matched '/' to command name 'deleteSession'
2021-03-11 16:26:03:554 [WD Proxy] Proxying [DELETE /] to [DELETE http://127.0.0.1:8200/wd/hub/session/fc2330e0-543c-4ba4-a314-95d68fda3b47] with no body
2021-03-11 16:26:03:558 [WD Proxy] Got response with status 200: {"sessionId":"fc2330e0-543c-4ba4-a314-95d68fda3b47","value":null}
2021-03-11 16:26:03:559 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 shell am force-stop com.xueqiu.android'
2021-03-11 16:26:03:993 [Instrumentation] .
2021-03-11 16:26:04:194 [Logcat] Stopping logcat capture
2021-03-11 16:26:04:198 [ADB] Removing forwarded port socket connection: 8200 
2021-03-11 16:26:04:199 [ADB] Running 'E:\Android\android-sdk\platform-tools\adb.exe -P 5037 -s 127.0.0.1:21503 forward --remove tcp:8200'
2021-03-11 16:26:04:490 [Instrumentation] Time: 17.038
2021-03-11 16:26:04:490 [Instrumentation] 
2021-03-11 16:26:04:490 [Instrumentation] OK (1 test)
2021-03-11 16:26:04:509 [BaseDriver] Event 'quitSessionFinished' logged at 1615479964508 (00:26:04 GMT+0800 (中国标准时间))
2021-03-11 16:26:04:509 [W3C (d4599237)] Received response: null
2021-03-11 16:26:04:509 [W3C (d4599237)] But deleting session, so not returning
2021-03-11 16:26:04:510 [W3C (d4599237)] Responding to client with driver.deleteSession() result: null
2021-03-11 16:26:04:511 [HTTP] <-- DELETE /wd/hub/session/d4599237-38f0-431e-8b07-1110d17b7348 200 960 ms - 14
2021-03-11 16:26:04:511 [HTTP] 
2021-03-11 16:26:04:536 [Instrumentation] The process has exited with code 0
