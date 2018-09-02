function help(message) {
    try {
      const embed = {
        title: 'Bug Hunter commands:',
        description: `**Prefix: report**
        
        **Aviable commands:**
        /help (Help command)
        /invite (If you want to invite me on your server use this command!)
        report bug <bug description>
        
        First you need to set up channel with logs.
        To do this just type on channel where you want
        to see logs \`add channel\` and you ready to go.`,
        color: 15605837,
        footer: {
          icon_url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ',
          text: 'BugHunter by R1SK and Kiritito',
        },
        thumbnail: {
          url: 'https://assets.kogan.com/files/Sidebar/HelpCentre.png',
        }
      }
      message.channel.send({ embed })
    } catch (err) {
      console.log(console.error(err))
    }
  }
  
  module.exports = help