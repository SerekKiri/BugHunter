const Discord = require('discord.js');

// importing files
const config = require('./config.json')
const help = require('./commands/help')
const report = require('./commands/report')

// variables
let channelsBugs = ['478884266852483073', '478886481281417216']

const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bug hunter has started, with ${client.users.size} users, in ${client.channels.size} channels of ${client.guilds.size} guilds`)
    client.user.setPresence({ game: { name: client.users.size + ' bugs hunters', type: 3 } })
  })

client.on('message', async (message) => {
    if (message.content.substring(0, config.prefix.length) === config.prefix) {
        const command = message.content.slice(config.prefix.length)

            if(message.content.startsWith(config.prefix + 'bug')) {
               report(message)
            }
            if(command === 'help') {
                help(message)
            }
        }
    })

client.login(config.token)