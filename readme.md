AnimeRadar - An auto downloading radar for your favorite anime(s)
---

Ever wondered if there was something for downloading your favorite anime right after its release? Fear not, 
AnimeRadar is a powerful automatic downloader for the anime(s) of your choice.

You can simply just let this program run in your device or server 24/7 with little to no network bandwidth consumption.

All you have to do is simply configure the `subscriptions.txt` with just the names of your favorite anime(s). 
What's more? You can even add regular expressions for matching the names of your anime by adding 'regexp:' as the prefix.

Oh? so you're a super weeb (a weeb that wants all the anime downloaded, no exceptions, anything and everything)? Fear not, you can leave the `subscriptions.txt` 
alone and the radar will trigger itself when a new anime is detected.

Further Configuration
---

AnimeRadar is a configurable package. That means you can add more powerful anime API (I mean, the one included is the source for most) 
to the program by inheriting the datacaller. Just make sure your datacaller can both fetch and download. 

You can increase the detection delays as you wish and with the included datacaller for GogoAnime, you can even turn on proxy if you want to get 
real freaky and anonymous with your downloads.