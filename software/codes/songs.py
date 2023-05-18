import random
from playsound import playsound
songs=["21.mp3","2.mp3","3.mp3","4.mp3","5.mp3","6.mp3","7.mp3","8.mp3","9.mp3","10.mp3","11.mp3","12.mp3","13.mp3","14.mp3","15.mp3","16.mp3","17.mp3","18.mp3","19.mp3","20.mp3"]
# getting numbers from 0 to 20
inputNumbers =range(0,20)
while True:
  # generating 20 random numbers from the given range which are non-repeating using random.sample() function
  random_no=random.sample(inputNumbers, 20)
  for i in random_no:
    song_to_play = songs[i]
    print(song_to_play)
    playsound(song_to_play)
