import sys
import unittest
import subprocess

class TestForwarding(unittest.TestCase):

    @staticmethod
    def run_shell(args, timeout=30):
        process = subprocess.Popen(['electrum/tests/test_forwarding/test_forwarding.sh'] + args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            sys.stdout.write(line.decode(sys.stdout.encoding))
        process.wait(timeout=timeout)
        process.stdout.close()
        assert process.returncode == 0

    @classmethod
    def setUpClass(cls):
        cls.run_shell(['start'])

    @classmethod
    def tearDownClass(cls):
        cls.run_shell(['stop'])

    def test_forwarding(self):
        self.run_shell(['open'])
        self.run_shell(['status'])
        self.run_shell(['pay'])
        self.run_shell(['status'])
        self.run_shell(['close'])
