const Discord = require('discord.js');
const { createStore, applyMiddleware } = require('redux');

// importing files
const config = require('./config.json')
const help = require('./commands/help')
const report = require('./commands/report')
const server = require('./commands/server')

const initialState = require('./initial-state')
const middleware = require('./middleware')
const reducer = require('./reducer')

// variables
let channelsBugs = ['478884266852483073', '478886481281417216']

const client = new Discord.Client();
const store = createStore(reducer, initialState.jsonData, applyMiddleware(middleware.updateData))

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
        if (message.member.hasPermission('MANAGE_CHANNELS')) {
            store.dispatch(server.actions.addServer(message))
            message.reply('Channel set up successfully!')
        } else {
            message.reply('You need specific permision to use this command("manage channels").')
        }
    }
})

client.login(config.token)

module.exports = {
    store,
}
