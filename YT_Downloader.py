from pytube import YouTube

#Asking user to enter the link of the video to download
link=input("Enter the YouTube video link you want to download :")
yt=YouTube(link)
#Details related to the video 
print("Author :",yt.author)
print("Title : ",yt.title)
print("Total number of views : ",yt.views)
print("Total length of the video : ",yt.length)
print("Rating of Video :",yt.rating)
print("Published Date :",yt.published_date)

#Getting the possible highest resolution
ys=yt.streams.get_highest_resolution()

#Entering the location
location=input("Enter the location :")
print("Downloading......")
ys.download(location)
print("You have successfully downloaded the video ")
print("Coded by : Sudharshan Chennupalle ")
