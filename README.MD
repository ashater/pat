# Repo for CyberPATRIOT Tools
![logo](CYBERPATRIOT_mid.jpg)

### Single Python tool for scan the system

### Multi-platform deploy TBD

### Using ```pyinstaller``` to create distribution:

How to get streamlit to work:
https://discuss.streamlit.io/t/using-pyinstaller-or-similar-to-create-an-executable/902/18


Command to create win ditribution:

```
pyinstaller --onefile --additional-hooks-dir=c:\work\pat\hooks st_run.spec --clean
copy actual python file into the same dir as the executable
```

Hardcoded Win path in ```st_run.spec```







