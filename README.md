# remote-monintor
[![.github/workflows/main.yml](https://github.com/SiriusKoan/remote-monitor/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/SiriusKoan/remote-monitor/actions/workflows/main.yml)

A simple network services monitoring system written in python.

## Credits
<a href="https://www.flaticon.com/free-icons/monitor" title="monitor icons">Monitor icons created by juicy_fish - Flaticon</a>

## Setup
1. Clone this project
```
$ git clone https://github.com/SiriusKoan/remote-monintor.git
```

2. Make sure Docker is installed

3. Update `backend/app/monitor/hosts.py` with your IP addresses and functions.

4. Run it
```
$ docker-compose up -d
```

5. Check whether it works on 80 port.

## Customization
You can also create your monitoring functions.

All the functions are callable class, so you must write your monitoring function in `__call__` method.

Please add them in `backend/app/monitor/funcs.py`, and make sure
1. They are callable
2. `__call__` accept one argument `host`
3. The class has proper `__init__`

## CLI
The application also provides CLI tool.

Before using it, you have to install necessary dependencies.
```
$ pip install -r cli/requirements.txt
```

And then you can run it.
```
$ python3 cli/main.py
```

It will update the results of the monitoring functions every second.

But because the results of text functions may be too long, the interface will NOT show text functions.

## Screenshot
### Web UI
![image](https://user-images.githubusercontent.com/26023540/180340423-064cec57-7bea-45c6-87fd-b79628390969.png)

### CLI
![image](https://user-images.githubusercontent.com/26023540/180774516-dd81fbe3-aa40-4fc2-bb32-fe19dda5dc0e.png)
