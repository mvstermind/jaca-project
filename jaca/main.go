package main

import (
	"log"
	"os"
	"os/signal"

	"github.com/gopxl/beep/v2/wav"
	"github.com/gordonklaus/portaudio"
)

const DevEnvMicID int8 = 4

func main() {
	err := portaudio.Initialize()
	if err != nil {
		log.Fatal("couldn't initalize portaudio: ", err)
	}
	defer portaudio.Terminate()

	stream, err := portaudio.OpenDefaultStream(1, 1, 44100, 16)
	if err != nil {
		log.Fatal("error while streaming: ", err)
	}
	defer stream.Close()

	filename := "file.wav"

	f, err := os.Create(filename)
	if err != nil {
		log.Fatal(err)
	}

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, os.Interrupt, os.Kill)
	go func() {
		<-sig
		stream.Stop()
		stream.Close()
	}()

	stream.Start()

}

// use this in new envs to know which mic id to use
func listDeviceNames() {
	// i can't really tell if i prefet to have it printed
	// or is it better as slice string
	devices, err := portaudio.Devices()
	if err != nil {
		log.Println("error getting default device: ", err)
	}
	// deviceNames := make([]string, len(devices))

	println("[id] Device name")
	for i, device := range devices {
		// deviceNames = append(deviceNames, device.Name)
		print("[", i, "]  ")
		println(device.Name)
	}

}
