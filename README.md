# Simple-Music-Scraper
Dependencies: 

Pytube - Used to download all videos 

ffpmeg - Used to convert .m4a files into .mp4 files look at convert.py if thats needed 

requests - Used for scraping the spotify web player 

Beautiful Soup - Used to parse the html 

youtubesearchpython - Used to search youtube for the closest 1 to 1 match to download 


This main purpose of this project is to download my spotify playlists so I could store them on my phone. It can also be used to bulk scrape spotify playlists to make data sets if anyone is interested in repurposing it. 


To run this all you need to do is make a filename.txt in the toDownload folder and run Download.py. In filename.txt go to the spotify playlist you want to download click cntrl a to highlight all songs and cntrl c. The clipboard will give back enter formatted data of spotify web player links. Paste into the filename.txt. After run there will be .m4a files stored in a sub folder named filename inside the FinishedDownloaded folder. If you want to convert these into .mp4 files can run the Convert.py but need to change the target and output folder names to the corresponding. 
