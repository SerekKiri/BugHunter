const Discord = require('discord.js');
const { createStore, applyMiddleware } = require('redux');
const TurndownService = require('turndown')
const turndownService = new TurndownService()

// importing files
const config = require('./config.json')
const help = require('./commands/help')
const report = require('./commands/report')
const server = require('./commands/server')

const initialState = require('./initial-state')
const middleware = require('./middleware')
const reducer = require('./reducer')

const client = new Discord.Client();
const store = createStore(reducer, initialState.jsonData, applyMiddleware(middleware.updateData))

client.on('ready', () => {
    console.log(`Bug hunter has started, with ${client.users.size} users, in ${client.channels.size} channels of ${client.guilds.size} guilds`)
    client.user.setPresence({ game: { name: '/help', type: 1 } })
})

client.on('message', async (message) => {

    if (message.content.startsWith(config.prefix + 'bug')) {
        report(message)
    }

    if (message.content.startsWith('/help')) {
        help(message)
    }

    if (message.content.startsWith('/invite')) {
        client.generateInvite(['SEND_MESSAGES', 'MANAGE_GUILD'])
        .then(link => {
          const embed = {
            title: 'Generated link',
            description: turndownService.turndown(`<a href="${link}">Click here to invite me!</a>`),
            color: 1554076,
            footer: {
                text: 'BugHunter by R1SK, Kiritito and Piter',
              },
          }
          message.channel.send({ embed })
        })
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
    client
}
