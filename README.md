# Docker-Privilege-Escalation

## Disclaimer
> [!CAUTION]
> This is a Proof of Concept (PoC) developed for cybersecurity research and educational purposes only. The author does not promote any illegal use of this software and is not responsible for any misuse or damages caused by it.
>
> This script exploits a LOTL (Living-Off-The-Land) vulnerability in systems in which docker commands can be executed by non-privileged users.

## Usage

This project uses 3 built-in Python modules, so no external dependencies are required.

```bash"
git clone https://github.com/Volodishlav/Docker-Privilege-Escalation
cd Docker-Privilege-Escalation
python3 main.py
```

## Explanation

In environments where non-privileged users are allowed to execute Docker commands, this can be abused to gain full control over the system.

By creating a container with elevated access to host resources (mounting "/" on a container folder), an attacker is able to expose the host filesystem inside the container. Since processes running inside the container can execute with root privileges, the attacker could then interact with host files as a privileged user. Sensitive files, configuration files, user data, authentication mechanisms, or startup scripts could be viewed, modified, or replaced, leading to complete compromise of the machine.

This concept was successfully exploited (manually) on EducaAndOS 20.04
