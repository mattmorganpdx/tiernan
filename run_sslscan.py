import subprocess


def scan(target):
    scan_result = subprocess.run(
        ["/usr/bin/sslscan", target],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    return scan_result.stdout
