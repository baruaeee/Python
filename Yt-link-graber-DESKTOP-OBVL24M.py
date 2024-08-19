#pip install scrapetube

import scrapetube

channel_ID = input("Enter Channel ID: ")
file_name = input("File name with .asx: ")

videos = scrapetube.get_channel(channel_ID)
videos = list(videos)
#videos = videos[::-1]
  
with open(file_name, 'a') as file:
    for video in videos:
        file.write("<entry>\n")
        
        #<ref href = "https://www.youtube.com/watch?v=Agmjy0nLC74" />
        
        file.write("<ref href = \"https://www.youtube.com/watch?v="+str(video['videoId'])+"\"\n")
        
        #file.write("https://www.youtube.com/watch?v="+str(video['videoId'])+"\n")
        
        file.write("</entry>\n")
