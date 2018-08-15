function bug(message) {
  // variables
  const fs = require('fs')
  const serv = fs.readFileSync('./servers.json')
  const guildID = message.guild.id
  const obj = JSON.parse(serv)
  let mes = message.content.slice(11).split('|')
  let img = message.content.split('| ')
  let text = ''
  if (!(img[1] === undefined)) {
    text = img[1]
  } else {
    text = 'No links added'
  }
  const time = new Date(message.createdTimestamp)
  const aut = message.author.username + '#' +  message.author.discriminator
  const avatar = message.author.avatarURL
 if (obj.servers[guildID]) {
  if (mes[0].length < 10) {
      message.reply('You need to describe bug, min 10 letters')
  } else {
  try {
      const embed = {
          title: `Report from ${aut}`,
          description: '**Report text:**\n' + mes[0] + '\n\n' + '**Link:**' + '\n' + text,
          timestamp: time,
          color: 15859772,
          footer: {
            text: 'BugHunter by R1SK, Kiritito and Piter',
          },
          thumbnail: {
            url: avatar,
          }
        }
        message.guild.channels.get(obj.servers[guildID]).send({ embed })
    } catch (err) {
      console.log(err)
   }
  }
 } else {
  message.reply('You need to setup channel with logs. Just write ``add channel``.')
 }
}

module.exports = bug