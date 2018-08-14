function bug(message) {

    // variables
    let mes = message.content.slice(11).split('|')
    let img = message.content.split('| ')
    let text = ''
    if (!(img[1] === undefined)) {
      text = img[1]
    } else {
      text = 'There is no link'
    }
    const time = new Date(message.createdTimestamp)
    const aut = message.author.username + '#' +  message.author.discriminator
    const avatar = message.author.avatarURL
     if (message.guild.id === '367325058353594378') {
      chan = 'bugs-js'
     } else if (message.guild.id === '382070408226275328'){
       chan = '👾-devtycoon™-bugs'
     } else {
       chan = '👾-devtycoon™-bugs'
     }

    if (mes[0].length < 10) {
        message.reply('You need to describe your problem with minimum 10 letters')
    } else {
    try {
        const embed = {
            title: `Report from ${aut}`,
            description: '**Report text:**\n' + mes[0] + '\n\n' + '**Link:**' + '\n' + text,
            timestamp: time,
            color: 15859772,
            footer: {
              icon_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ',
              text: 'BugHunter by R1SK and Kiritito',
            },
            thumbnail: {
              url: avatar,
            }
          }
          message.guild.channels .find(v => v.name === chan).send({ embed })
          // message.channel.send({ embed })
      } catch (err) {
        console.log(err)
    }
 }
}
  
  module.exports = bug