Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genre

userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

# Output: {
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }
from collections import defaultdict,Counter

output=defaultdict(list)
rev_sg={}
temp=defaultdict(list)
for k,v in songGenres.items():
    for s in v:
        rev_sg[s]=k

for k,v in userSongs.items():
    for s in v:
        temp[k].append(rev_sg[s])

for k,v in temp.items():
    freq=Counter(v)
    counter=freq[max(freq)]
    for s in v:
        if v.count(s)==counter:
            if s not in output[k]:
                output[k].append(s)

print(output)
