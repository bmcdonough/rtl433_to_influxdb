#! /usr/bin/python3

import sys
import select
import time
import json


read_list = [sys.stdin]
timeout = 0.1 # seconds
last_work_time = time.time()

db_name = "rtl433_temp"
influx_host = "http://admin@:password@192.168.100.1:8086/write?db=%s&precision=s" % (db_name)
print("###DEBUG influx_host: ", influx_host)


def write_influx(key_values):
    for key, value in key_values.items():
        curly= ("curl -i -XPOST 'http://admin:password@localhost:8086/write?db=database_name&precision=ms' --data-binary 'balances,account=%s value=%s,other=%s %s'" % (matchObj102[0][0],matchObj102[1][1],matchObj102[2][1],wilmcd_gdate))
    from subprocess import call
    status = call(curly, shell=True)
    return (status)

def convert_temp(temp, unit):
    unit = unit.lower()
    if unit == "c":
        temp = 9.0 / 5.0 * temp + 32
        return (temp)
    if unit == "f":
        temp = (temp - 32) / 9.0 * 5.0
        return (temp)

def is_json(myjson):
  print("###DEBUG is_json()")
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def treat_input(linein):
  global last_work_time
  print("Workin' it!", linein, end="")
  print(is_json(linein))
  if is_json:
      json_object = json.loads(linein)
      for key, value in json_object.items():
          print(key, value)
          if key == "temperature_C":
              temp_change = convert_temp(value, "C")
              temp_change = round(temp_change, 1)
              print("temperature_F", temp_change)
  time.sleep(1) # working takes time
  print('Done')
  last_work_time = time.time()

def idle_work():
  global last_work_time
  now = time.time()
  # do some other stuff every 2 seconds of idleness
  if now - last_work_time > 2:
    print('Idle for too long; doing some other stuff.')
    last_work_time = now

def reading_loop():
    global read_list
    while read_list:
#       select.select(rlist, wlist, xlist[, timeout])
        ready = select.select(read_list, [], [], timeout)[0]
        if not ready:
            idle_work()
        else:
            for file in ready:
                line = file.readline()
                if not line: # EOF, remove file from input list
                    read_list.remove(file)
                elif line.rstrip(): # optional: skipping empty lines
                    treat_input(line)


def main():
    print("###DEBUG main()")
    reading_loop()
    return None


if __name__ == '__main__':
  main()

