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

2.stream_localhost off

```
sudo nano /etc/motion/motion.conf
```

```
stream_localhost off
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
