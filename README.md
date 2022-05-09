# useful-scripts
A collection of scripts that were once written and even used

### Examples
#### 1. Check your hosts for certificates expiration
Usage:
1. Add your hostnames to HOSTS list in the script
2. Run
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

#### 2. Get sha512 password hash with random salt
Usage:\
`./generate-sha512-hash.py`
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

#### 3. Get a playlist or a single video from the youtube
Requirements: `pip3 install pytube`

Usage:\
`./get-from-youtube [-h] [--playlist PLAYLIST] [--video VIDEO] [--dir DIR]`
