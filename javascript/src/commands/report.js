function bug(message) {

    // variables
    let mes = message.content.slice(11).split('|')
    let img = message.content.split('| ')
    let video
    let text = ''
    if (img[1].startsWith('https://www.youtube.com/watch?v=')) {
      video = img[1].split('https://www.youtube.com/watch?v=')
      text = '**Link:**' + '\n' + img[1]
    } else if (img[1].startsWith('https://youtu.be/')) {
      video = img[1].split('https://youtu.be/')
      text = '**Link:**' + '\n' + img[1]
    } else {
      video = ''
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
        message.reply('You need to describe bug, min 10 letters')
    } else {
    try {
        const embed = {
            title: `Report from ${aut}`,
            description: '**Report text:**\n' + mes[0] + '\n\n' + text,
            timestamp: time,
            color: 15859772,
            footer: {
              icon_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ',
              text: 'BugHunter by R1SK and Kiritito',
            },
           "image": {
              "url": `https://img.youtube.com/vi/${video[1]}/0.jpg`
            },
            thumbnail: {
              url: avatar,
            }
          }
          message.guild.channels.find("name", chan).send({ embed })
          // message.channel.send({ embed })
      } catch (err) {
        console.log(err)
    }
 }
}
  
  module.exports = bug