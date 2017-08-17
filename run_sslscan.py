#!/usr/bin/env python
import subprocess

def scan(target):
    scan_result = subprocess.run(
        ["/home/mmorgan/bin/sslscan", target],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    return scan_result.stdout


if __name__ == "__main__":
    print(scan("qaappvault.jamasoftware.net"))
