//
//  main.swift
//  BugHunter
//
//  Created by Oskar Chybowski on 02/09/2018.
//  Copyright © 2018 Fosscord. All rights reserved.
//

import Sword

let client = Sword(token:"NDc5MjQyMTc5ODY1MzQ2MDQ5.Dm21vg.aBA1zFyws0v5Pni6hOYu4HkUEF0")
client.editStatus(to: "online", playing: "with Sword!")

client.on(.messageCreate) { data in
    let message = data as! Message
    
    findMessage(message: message)
}

client.connect()
