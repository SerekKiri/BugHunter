const Discord = require('discord.js');

// importing files
const config = require('./config.json')
const help = require('./commands/help')
const report = require('./commands/report')
const server = require('./commands/server')

// variables
let channelsBugs = ['478884266852483073', '478886481281417216']

const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bug hunter has started, with ${client.users.size} users, in ${client.channels.size} channels of ${client.guilds.size} guilds`)
    client.user.setPresence({ game: { name: client.users.size + ' bugs hunters', type: 3 } })
  })

client.on('message', async (message) => {
    
            if (message.content.startsWith(config.prefix + 'bug')) {
               report(message)
            }

            if (message.content.startsWith(config.prefix + 'help')) {
                help(message)
            }

            if (message.content.startsWith('add channel')) {
                console.log(message)
                server(message)
            }
    })

client.login(config.token)