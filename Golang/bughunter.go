package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/bwmarrin/discordgo"
)

type Config struct {
	BotToken string `json:"BotToken"`
	Prefix   string `json:"Prefix"`
}

var botID string

func loadConfig() Config {

	jsonData, err := ioutil.ReadFile("./config/config.json")

	if err != nil {
		log.Panicf(err.Error())
	}

	config := Config{}
	if err := json.Unmarshal(jsonData, &config); err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	return config
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

	if m.Author.ID == botID {
		return
	}

	if m.Content == "ping" {
		_, _ = s.ChannelMessageSend(m.ChannelID, "pong")
	}

	if m.Content == ""

}
