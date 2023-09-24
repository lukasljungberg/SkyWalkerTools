import subprocess
from common import *


class CMDHandler:
    def handle_cmd(self, cmd: str) -> str | None:
        if self.cmd_type(cmd) == "append":
            if self.cmd_action(cmd).lower() == "host":
                val = self.cmd_value(cmd)
                if is_ipv4(val):
                    self.append_host(val)
                    return val
        if self.cmd_type(cmd) == "delete":
            if self.cmd_action(cmd).lower() == "host":
                val = self.cmd_value(cmd)
                self.delete_host(val)
                return val

        output = subprocess.check_output(cmd.split(' '))
        return output

    def cmd_type(self, cmd) -> str:
        return str(cmd.split(" ")[0]).lower()

    def cmd_action(self, cmd) -> str:
        try:
            return str(cmd.split(" ")[1]).lower()
        except:
            return False

    def cmd_value(self, cmd):
        try:
            return str(cmd.split(" ")[-1]).lower()
        except:
            return False

    def append_host(self, addr: str) -> bool:
        if is_ipv4(addr):
            with open("./proxy_list.hosts", "a") as f:
                f.write(addr + "\n")
            return True
        else:
            return False

    def add_hosts(self, wid):
        with open("./proxy_list.hosts", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            for line in lines:
                if line:
                    wid.remote_host.addItem(line)
                    wid.next_host.addItem(line)

    def delete_host(self, host):
        lines = None
        with open("./proxy_list.hosts", "r") as f:
            lines = f.read()
            lines = lines.split('\n')
            lines.remove(host)
        with open("./proxy_list.hosts", "w") as f:
            f.write(''.join([line + "\n" for line in lines if line]))
