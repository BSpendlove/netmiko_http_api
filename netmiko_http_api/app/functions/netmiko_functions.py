from netmiko import ConnectHandler

class NetmikoAPI():
    def __init__(self, **kwargs):
        self.device_type = None

        for value, key in kwargs.items():
            if value == "device_type":
                self.device_type = key

        self.ssh_session = ConnectHandler(**kwargs)

    def throw_exception(self, msg):
        return {"error": msg}

    def send_command(self, **kwargs):
        output = self.ssh_session.send_command(**kwargs)
        return {"send_command": "{}".format(output)}

    def get_hostname(self):
        prompt = self.ssh_session.base_prompt
        return {"get_hostname": "{}".format(prompt)}

    def get_interfaces(self, command=None, **kwargs):
        CMD_MAPPER = {
            "cisco_ios": "show interfaces",
            "huawei": "display interfaces",
            "linux": "ifconfig -a"
        }

        output = None

        if command:
            output = self.ssh_session.send_command(command, **kwargs)
        
        else:
            for vendor, cmd in CMD_MAPPER.items():
                if self.device_type == vendor:
                    output = self.ssh_session.send_command(cmd)

        return output