#  Bug Hunter

### Golang version by [SerekKir](https://github.com/SerekKiri)

Discord bot which will help bot that will help you sort out bugs.


To run this bot you need:
- [Golang](https://golang.org/doc/install)
- Discord Bot Token ([How to create your own bot guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token))

 How to run bot:

1. Rename ``example.config.json`` to ``config.json``

2. Change ``BotToken`` from ``Your bot token here`` on your own bot token
3. Install all depedencies

    ```
    go get -v
    ```
    - with [`dep`](https://github.com/golang/dep)
    ```
    dep ensure
    ```

4. Now let's run the bot!
    ```
    go run bughunter.go
    ```
    - Building application
    ```
    go build bughunter.go
    ```

### Join our discord server

[Invite link](https://discord.gg/Wn3zEyh)

### Organization

[github.com/fosscord](https://github.com/fosscord)

### Website

[fosscord.github.io](https://fosscord.github.io/)

### Invite bot on your server

[discordapp.com/oauth2/authorize](https://discordapp.com/oauth2/authorize?client_id=478867142633062410&scope=bot&permissions=0)

⚠️ Remember about giving bot role with proper permissions! ⚠️

Please report all bugs and your ideas in [issues](https://github.com/SerekKiri/BugHunter/issues). Thanks for your help!