# Docker-Privilege-Escalation

## Disclaimer
> [!CAUTION]
> This is a Proof of Concept (PoC) developed for cybersecurity research and educational purposes only. The author does not promote any illegal use of this software and is not responsible for any misuse or damages caused by it.
>
> This script exploits a Living-Off-the-Land (LOTL) vulnerability in systems in which docker commands can be executed by non-privileged users.

## Usage

This project uses 3 built-in Python modules, so no external dependencies are required.

```bash"
git clone https://github.com/Volodishlav/Docker-Privilege-Escalation
cd Docker-Privilege-Escalation
python3 main.py
```
## Real scenario

This concept was successfully exploited (manually) on the following operating systems:

- EducaAndOS 20.04
