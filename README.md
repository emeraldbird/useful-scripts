# useful-scripts
A set of different scripts


## 1. Check the expiration date of certificates on your hosts
Usage:
1. Add some hostnames to HOSTS list in the script instead of the defaut ones
2. Run the script
`python3 check-certs.py`

You'll get something like this:
```
[UP TO DATE]
   google.com 2030-01-01 00:00:00
   yandex.ru 2022-08-16 00:00:00
   duckduckgo.com 2022-11-26 23:59:59

[ALMOST EXPIRED]

[EXPIRED]

[ERRORS]
```
----

## 2. Get sha512 password hash with random salt
Usage:\
`python3 generate-sha512-hash.py`
output:
```
Password:
```
Type string 'Hello world!'
and get:
```
$6$RBdmKjFZnIyD39zt$zh7uy/tXT1PDOhxFHX0QqrdzpYuB3I1uReU8I3KfOhrJNe/gEBQNAmOWDZ.kG54yNxaIIbYkY6PiUIGu0Qclf/
```
----

## 3. Get a playlist or a single video from the youtube
Requirements: `pip3 install pytube`

Usage:\
`python3 get-from-youtube.py [-h] [--playlist PLAYLIST_URL] [--video VIDEO_URL] --dir <DIR_PATH>`
