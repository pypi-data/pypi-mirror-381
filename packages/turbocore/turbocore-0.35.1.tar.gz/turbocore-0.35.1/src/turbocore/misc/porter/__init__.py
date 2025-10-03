import subprocess
import threading
import configparser
import multiprocessing

import os
import sys
import signal

class ConnectedPort:

    def __init__(self, name, cfg, default_cfg):
        self._name = name
        self._cfg = cfg
        self._default_cfg = default_cfg
        self._thread = None
        self._p = None
        self._lock = threading.Lock()



    def info(self):
        stat = "no"
        with self._lock:
            stat = "yes" if self._p is not None and self._p.poll() is None else "no"
        return "<%s connected=%s>" % (self._name, stat)


    def connect(self):
        if self._thread is None or not self._thread.is_alive():
            self._thread = threading.Thread(target=self.execute_connect, daemon=True)
            self._thread.start()

    def kill_connection(self, timeout=2.0):
        with self._lock:
            p = self._p
        if not p:
            print("kein subprocess vorhanden")
            return
        try:
            print("sending SIGTERM to pgid", p.pid)
            os.killpg(p.pid, signal.SIGTERM)
        except Exception as e:
            print("error sending SIGTERM:", e)

        try:
            p.wait(timeout=timeout)
            print("process exited after SIGTERM")
        except subprocess.TimeoutExpired:
            print("nicht reagiert, sende SIGKILL")

        with self._lock:
            # p.poll() könnte None->exit, setze self._p auf None
            if self._p is not None:
                try:
                    self._p.wait(timeout=0.1)
                except Exception:
                    pass
                self._p = None

        if self._thread is not None:
            self._thread.join(timeout=0.1)

    def execute_connect(self):
        try:
            idfile = self._cfg["id"]
            user = self._cfg["user"]
            mine = int(self._cfg["mine"])
            her = int(self._cfg["her"])
            host = self._cfg["host"]

            cmd = [
                "ssh", "-q", "-n", "-T", "-N",
                "-F", "/dev/null",
                "-o", "StrictHostKeyChecking=no",
                "-o", "UserKnownHostsFile=/dev/null",
                "-i", idfile,
                "-l", user,
                "-L", f"127.0.0.1:{mine}:127.0.0.1:{her}",
                host
            ]

            # Startet den SSH-Subprozess in einer neuen Session/Prozessgruppe
            p = subprocess.Popen(cmd, start_new_session=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            with self._lock:
                self._p = p

            # Optional: wir könnten stdout/stderr lesen oder logged ausgeben
            # warte bis ssh beendet
            stdout, stderr = p.communicate()  # blockiert bis Ende
            # Debugausgabe
            if stdout:
                print("SSH stdout:", stdout)
            if stderr:
                print("SSH stderr:", stderr)

            print("SSH EXIT:", p.returncode)

        except Exception as e:
            print("error execute_connect:", e)
        finally:
            with self._lock:
                self._p = None




def main():
    ini = configparser.ConfigParser()
    try:
        ini.read_file(open(os.path.expanduser("~/porter.ini")))
    except:
        print("""
cat >~/porter.ini <<EOF              
[displayname]
id=~/.ssh/id_key
her=25
mine=25000
host=1.2.3.4
user=root
EOF
""")
        sys.exit(0)

    print("porter")
    connections = {}
    threads = {}
    kv_default = {}

    for section in ini.sections():
        kv = dict(ini[section].items())

        if "id" in kv:
            kv["id"] = os.path.expanduser(kv["id"])
        
        if section == "default":
            kv_default = kv
            continue

        connections[section] = kv

    for n in connections.keys():
        threads[n] = ConnectedPort(name=n, cfg=connections[n], default_cfg=kv_default)




    while True:
        i=1
        for n in sorted(threads.keys()):
            t = threads[n]
            print("%d: %s" % (i, t.info()))
            i+=1
        
        x = input("# ")
        if x == "q":
            for n in list(sorted(threads.keys())):
                threads[n].kill_connection()
            sys.exit(0)

        if x.startswith("c "):
            idx = int(x.split(" ")[1])
            n = list(sorted(threads.keys()))[idx-1]
            threads[n].connect()
            print("connecting %s" % n)

        if x.startswith("d "):
            idx = int(x.split(" ")[1])
            n = list(sorted(threads.keys()))[idx-1]
            threads[n].kill_connection()
            print("killed %s" % n)
