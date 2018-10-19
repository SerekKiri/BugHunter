package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strings"

	"github.com/bwmarrin/discordgo"
)

type Config struct {
	BotToken string `json:"BotToken"`
	Prefix   string `json:"Prefix"`
}

type Servers struct {
	Servers map[string]string `json:"servers"`
}

var botID string

func loadConfig() Config {

	jsonData, err := ioutil.ReadFile("./config/config.json")

	if err != nil {
		log.Panicf(err.Error())
	}

	config := Config{}
	if err := json.Unmarshal(jsonData, &config); err != nil {
		log.Panicf(err.Error())
		os.Exit(2)
	}

	return config
}

func loadServers() Servers {
	jsonData, err := ioutil.ReadFile("./servers/servers.json")

	if err != nil {
		log.Panicf(err.Error())
	}

	servers := Servers{}

	if err := json.Unmarshal(jsonData, &servers); err != nil {
		log.Panicf(err.Error())
		os.Exit(2)
	}

	return servers
}

func main() {
	config := loadConfig()

	dg, err := discordgo.New("Bot " + config.BotToken)

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	u, err := dg.User("@me")

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	botID = u.ID

	dg.AddHandler(messageHandler)

	err = dg.Open()

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	fmt.Println("Bug Hunter started looking for bugs...")

	<-make(chan struct{})
	return
}

func messageHandler(s *discordgo.Session, m *discordgo.MessageCreate) {

	config := loadConfig()
	servers := loadServers()

	if m.Author.ID == botID {
		return
	}

	if m.Content == "ping" {
		_, _ = s.ChannelMessageSend(m.ChannelID, "pong")
	}

	if strings.HasPrefix(m.Content, config.Prefix+"bug") {
		_, _ = s.ChannelMessageSend(m.ChannelID, "ddd")
	}

	if m.Content == "add channel" {
		// You need o paste your server id becouse right now discordgo doesn't support it
		// Will change it in future
		guildID := "Your_guild_ID"
		c := servers.Servers[guildID]
		// actually you need to set up channel by adding it to servers.json :(
		_, _ = s.ChannelMessageSend(c, "Channel successfully added")
	}
}
