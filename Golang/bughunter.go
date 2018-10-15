package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"

	"github.com/bwmarrin/discordgo"
)

type Configuration struct {
	BotToken string `json:"BotToken"`
	Prefix   string `json:"Prefix"`
}

var botID string

func (c Configuration) toString() string {
	bytes, err := json.Marshal(c)
	if err != nil {
		fmt.Println(err.Error())
	}
	return string(bytes)
}

func getConfig() []Configuration {
	config := make([]Configuration, 1)
	raw, err := ioutil.ReadFile("./config/config.json")

	if err != nil {
		fmt.Println(err.Error())
	}

	json.Unmarshal(raw, &config)
	return config
}

func main() {
	config := getConfig()
	fmt.Println(config)

	for _, conf := range config {
		fmt.Println(conf.toString())
	}

	dg, err := discordgo.New("Bot ")

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
}
