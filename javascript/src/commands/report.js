function bug(message, client) {
    let mes = message.content.slice(11)
    const time = new Date(message.createdTimestamp)
    const aut = message.author.username + ' #' +  message.author.discriminator
    const avatar = message.author.avatarURL
    if (mes === null && mes.length < 10) {
        message.reply('You need to describe bug, min 10 letters')
    } else {
    try {
        const embed = {
            title: `Report from ${aut}`,
            description: '**Report text:**\n' + mes,
            timestamp: time,
            color: 15605837,
            footer: {
              icon_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ',
              text: 'BugHunter by R1SK and Kiritito',
            },
            thumbnail: {
              url: avatar,
            }
          }
          message.channel.send({ embed })
      } catch (err) {
        console.log(err)
    }
 }
}
  
  module.exports = bug