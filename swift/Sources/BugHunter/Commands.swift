//
//  Commands.swift
//  BugHunter
//
//  Created by Oskar Chybowski on 02/09/2018.
//

import Foundation
import Sword

func findMessage(message: Message) {
    if message.content == "/helpbeta" {
        let helpMessage = configureEmbededMessage(
                title: "Bug Hunter commands:",
                color: 15605837,
                footerText: "BugHunter by Oschły [Swift version]",
                footerIconURL: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCaZDPW_-dzsNbodLC5KiAT3BlciGOybFjsUZPRSKI2u7tuQg2BQ",
                thumbnail: "https://assets.kogan.com/files/Sidebar/HelpCentre.png",
                description: """
                    **Prefix: report**
                    
                    **Aviable commands:**
                    /help (Help command)
                    /invite (If you want to invite me on your server use this command!)
                    report bug <bug description>
                    
                    First you need to set up channel with logs.
                    To do this just type on channel where you want
                    to see logs `add channel` and you ready to go.
                    """)
            message.channel.send(helpMessage)

    } else if message.content == "/reportbeta" {
        message.reply(with: "To nie działa")
    } else if message.content == "/invitebeta" {
        message.reply(with: "i to też nie działa")
    }
}

// FIX: Footer is printing nil
func configureEmbededMessage(title: String, color: Int, footerText: String, footerIconURL: String, thumbnail: String, description: String) -> Embed {
    var embededMessage = Embed()
    
    embededMessage.title = title
    embededMessage.color = color
    embededMessage.footer?.text = footerText
    embededMessage.footer?.iconUrl = footerIconURL
    embededMessage.thumbnail?.url = thumbnail
    embededMessage.description = description
    
    return embededMessage
}
