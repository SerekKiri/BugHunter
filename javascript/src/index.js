const Discord = require('discord.js');
const config = require('./config.json')

const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bug hunter has started, with ${client.users.size} users, in ${client.channels.size} channels of ${client.guilds.size} guilds`)
    client.user.setPresence({ game: { name: client.users.size + ' bugs hunters', type: 3 } })
  })

client.on('message', async (message) => {
    if (message.content.substring(0, config.prefix.length) === config.prefix) {
        const command = message.content.slice(config.prefix.length);

        switch (command) {
            case 'report':
              report(message);
              break;
            case 'help':
              help(message);
              break;
          }
    }
})

client.login(config.token)