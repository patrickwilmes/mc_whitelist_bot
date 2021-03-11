# MC Whitelist Bot

This is a simple PoC of a discord bot that takes care of adding
people to a minecraft server whitelist.

# How to run
The bot is written in python3

**Your discord api token must be located in a file called token.txt located in the same directory as main.py**

```bash
pip3 install -r requirements.txt
python3 main.py
```

## How to use

If a user should be added to the whitelist call:
```
/mc_add <MINECRAFT_USERNMAE>
```
For deleting a user from the whitelist call:
```
/mc_del <MINECRAFT_USERNMAE>
```

## About the configuration
```ini
[DATABASE]
name = whitelist.db # name of the database

[DISCORD]
token_file = token.txt # token file to use

[SERVER]
whitelist_target_dir = # the target directory used to save the whitelist.txt. 
# This must be specified without the filename. 
# Leave it empty to store the file in the current working directory
```
