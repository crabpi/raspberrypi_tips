### change source

```
sudo nano /etc/apt/sources.list
```

```
deb http://mirrors.aliyun.com/raspbian/raspbian/ wheezy main non-free contrib
deb-src http://mirrors.aliyun.com/raspbian/raspbian/ wheezy main non-free contrib
```

### install

```
sudo apt-get install motion
```

### config

1.start_motion_daemon yes

```
sudo nano /etc/default/motion
```

```
start_motion_daemon = yes
```

2.webcam_localhost off

```
sudo nano /etc/motion/motion.conf
```

```
webcam_localhost off
```

### start

```
sudo service motion start
```

### web

```
sudo motion
```

### visit

```
http://ip:8081
```

### save to mp4

```
curl -o v.mp4 http://ip:8081
```

### restart.sh

```
ID=`ps -aux | grep curl | awk '{print $2}'`
for id in $ID
do
 kill -9 $id
 echo "killed $id"
done
current=`date "+%Y-%m-%d %H:%M:%S"`
timeStamp=`date -d "$current" +%s`
currentTimeStamp=$((timeStamp*1000+`date "+%N"`/1000000))
screen curl -o static/$currentTimeStamp.mp4 http://localhost:8081

```
