#pip install scrapetube

import scrapetube

videos = scrapetube.get_channel("UCh4JH8axA_jUjB8YoRnm0cg")
videos = list(videos)
#videos = videos[::-1]
  
with open('moviedome.asx', 'a') as file:
    for video in videos:
        file.write("<entry>\n")
        
        #<ref href = "https://www.youtube.com/watch?v=Agmjy0nLC74" />
        
        file.write("<ref href = \"https://www.youtube.com/watch?v="+str(video['videoId'])+"\"\n")
        
        #file.write("https://www.youtube.com/watch?v="+str(video['videoId'])+"\n")
        
        file.write("</entry>\n")
