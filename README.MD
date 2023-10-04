# Repo for CyberPATRIOT Tools
![logo](CYBERPATRIOT_mid.jpg)

# Power Shell tricks #


## Check authorized users ##
Copy paste all the authorized usernames into C:\CyberPatriot\authorized.txt, including administrators. 

You can run command that will check and remove users that are on the system:
```PowerShell
 (Get-LocalUser).Name | ForEach-Object -Process {  if ( $_ -notin  (Get-Content -Path C:\CyberPatriot\authorized.txt)) {  Remove-LocalUser -Name $_ -Confirm } }

```

Explanation for the command:<br/>
```(Get-LocalUser).Name``` lists all the current users on the system:
```
Administrator
ashat
DefaultAccount
Guest
WDAGUtilityAccount
```
```(Get-Content -Path C:\CyberPatriot\authorized.txt)``` lists all the names copy pasted from Cyberpatriot instructions

```PowerShell
(Get-LocalUser).Name | ForEach-Object -Process {   $_  }
``` 
iterates over each local user on the system and executes code in ```-Process``` block in ```{ }``` with ```$_``` variable for username of the local user

Now we check if the local users are in our authorized list file, with operator ```-notin```:
```PowerShell
 (Get-LocalUser).Name | ForEach-Object -Process {  $_ -notin  (Get-Content -Path C:\CyberPatriot\authorized.txt)  }

```
Putting it all together with ```if``` users not in our authorized file list, we run PowerShell remove users command: ```Remove-LocalUser -Name $_ -Confirm```

First we want to display which users we will remove:
```PowerShell
 (Get-LocalUser).Name | ForEach-Object -Process {  if ( $_ -notin  (Get-Content -Path C:\CyberPatriot\authorized.txt)) {   $_  } }
 ```

Then we execute actual ```Remove-LocalUser```

```PowerShell
 (Get-LocalUser).Name | ForEach-Object -Process {  if ( $_ -notin  (Get-Content -Path C:\CyberPatriot\authorized.txt)) {  Remove-LocalUser -Name $_ -Confirm } }
```

[Python scan tool](PYTHON_TOOL.MD)




