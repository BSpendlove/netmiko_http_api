# Netmiko HTTP API
This is a demonstration of a Flask Frontend + API (manual API) to interact between the Netmiko Module and Devices.

Please note, this is a demo project for learning and shouldn't be used in a production enviornment.

The user database stores usernames and passwords in plain text and presents them on the frontend GUI for testing so please do not expose any real passwords within the database. (I use it for lab credentials)

### How to run

1. Clone the repository

```console
$ git clone git@github.com:BSpendlove/netmiko_http_api.git
```

2. Install the requirements

```console
$ cd netmiko_http_api
$ pip install -r requirements.txt
```

3. Create the database

```console
$ python db_create.py
```

4. Run the Flask Application

```console
$ python run.py
```


### Frontend Example
The frontend is typically powered via Flask routes + functions. Devices should reference the User (id) and Vendor (Netmiko device_type). See an example below to create a device with the cisco_ios device_type.

1. Creating the User

![User Frontend](/screenshots/gui_add_user.jpg)

2. Creating the Device

![Device Frontend](/screenshots/gui_add_device.jpg)

3. View Devices

![Device Frontend View](/screenshots/gui_devices.jpg)


### API Example
The API exposes functions used in the Frontend but either shows via a pretty output (in web browser) or returns JSON data if 'application/json' is used.

API Routes:
```
/api
/api/devices
/api/devices/<id>
/api/devices/<id>/get_hostname
/api/devices/<id>/get_interfaces
/api/devices/<id>/send_command
/api/users
/api/users/<id>
```

### Example [GET] (Frontend)
/api/devices

![Device API devices](/screenshots/api_devices.jpg)

/api/devices/1/get_interfaces

![Device API get_interfaces](/screenshots/api_get_interfaces.jgp)

### Example [GET] (API)

/api/devices/1

JSON:
```json
    {
        "friendly_name": "CSW01",
        "id": 1,
        "ip_addr": "192.168.0.252",
        "user": 1,
        "vendor": "cisco_ios"
    }
```

### Example [POST] (API)

/api/devices

POST Body:
```json
    {
        "friendly_name": "api-sw-1",
        "ip_addr": "192.168.1.1",
        "user": 1,
        "vendor": "cisco_ios"
    }
```

/api/devices/1/send_command

POST Body:
```json
    {
        "command_string": "show switch"
    }
```

Response:
```json
{
  "error": false,
  "send_command": {
    "cli_output": "Switch/Stack Mac Address : 0016.c886.5180\n                                           H/W   Current\nSwitch#  Role   Mac Address     Priority Version  State \n----------------------------------------------------------\n*1       Master 0016.c886.5180     1      0       Ready               \n\n\n"
  }
}
```


