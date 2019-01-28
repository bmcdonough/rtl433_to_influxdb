# rtl_433 to InfluxDB

A python based script to parse JSON output from rtl_433 and pass it to influx.
* [rtl_433](https://github.com/merbanan/rtl_433)

```
pi@pi-a020d3-1375f082:~/github/rtl433_to_influxdb $ sudo rtl_433 -R 73 -F json
rtl_433 version unknown
Trying conf file at "rtl_433.conf"...
Trying conf file at "/root/.rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...
Registered 1 out of 120 device decoding protocols [ 73 ]
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
[R82XX] PLL not locked!
Sample rate set to 250000 S/s.
Tuner gain set to Auto.
Tuned to 433.920MHz.
{"time" : "2019-01-28 08:36:19", "model" : "LaCrosse TX141TH-Bv2 sensor", "id" : 247, "temperature_C" : -5.900, "humidity" : 58, "battery" : "OK", "test" : "No"}
{"time" : "2019-01-28 08:36:42", "model" : "LaCrosse TX141TH-Bv2 sensor", "id" : 44, "temperature_C" : 18.300, "humidity" : 44, "battery" : "OK", "test" : "No"}
{"time" : "2019-01-28 08:36:52", "model" : "LaCrosse TX141TH-Bv2 sensor", "id" : 82, "temperature_C" : 10.700, "humidity" : 32, "battery" : "OK", "test" : "No"}
```
