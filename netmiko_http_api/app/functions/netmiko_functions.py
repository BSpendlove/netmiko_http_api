from netmiko import ConnectHandler
from app.utils.textfsm_extractor import textfsm_extractor

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

    def get_interfaces(self, command=None, use_textfsm=True, **kwargs):
        CMD_MAPPER = {
            "cisco_ios": {"command": "show interfaces", "template": "cisco_ios_show_interfaces"},
            "huawei": {"command": "display interfaces", "template": "huawei_display_interfaces"},
            "linux": {"command": "ifconfig -a", "template": None}
        }

        output = None

        if command:
            output = self.ssh_session.send_command(command, **kwargs)
        else:
            for vendor, value in CMD_MAPPER.items():
                if self.device_type == vendor:
                    output = self.ssh_session.send_command(value["command"])

                    if use_textfsm:
                        output = textfsm_extractor(value["template"], output)

        return output
