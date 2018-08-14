const Discord = require('discord.js')
// const config = require('./config')
//const token = "NDc4NjY3NzkwOTQxODE0Nzg3.DlOCkA.CpqyVESgduKQV-Ow1fx9DA3y8wQ"
// commands import

// variables

const client = new Discord.Client({ disableEveryone: true })

client.on('ready', () => {
  console.log(`\nInitialized on ${new Date().toUTCString()}.`)
  client.user.setPresence({ game: 'DevTycoon bugs' , type: 3 })
})

// client.login(token)
client.login(process.env.BOT_TOKEN);
