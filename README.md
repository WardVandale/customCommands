# Custom Commands

## easyln
An easy way to make symbolic links for custom commands. This command will get the `current working directory` and add the specified file to the `/usr/local/bin` folder.
This creates an symbolic link.

### Install
```bash easyln easyln```
This command just installed the symbolic link to `/usr/local/bin`. It is now possible to just run `easyln <commandFile>`

## op_login
This command fetches the specified `AWS_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY` from 1Password and stores them in custom variables

### Install
```easyln op_login```

### Usage
Upon executing `op_login`, you will need to verify your identiry (e.g. with Touch ID). The code will export `AWS_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY` variables

## tssh
`tssh`, a.k.a. `Temporary SSH` is a command that won't save the RSA key to the `~/.ssh/known_hosts` file. This is used when a specific server frequently gets an new IP.
e.g. the new IP is automatically linked to a DNS Entry, upon connecting with SSH, you get an error. This command prevents the extra steps needed to remove the host from the known_hosts file

### Install
```easyln tssh```

### Usage
The same as a normal `ssh` command
```tssh <user>@<host>```
or 
```tssh <host>```
You can also enter extra arguments as you would do with the normal ssh command
