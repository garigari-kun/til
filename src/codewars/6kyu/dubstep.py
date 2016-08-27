"""

6kyu
Dubstep

For example, a song with words "I AM X" can transform into a dubstep remix as
"WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track,
but since he isn't into modern music, he decided to find out
what was the initial song that Polycarpus remixed.
Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND


"""
def song_decoder(song):
    sep_song = song.split('WUB')
    result = ''
    for char in sep_song:
        if char:
            result = result + char + ' '
    return result.strip()



song_decoder("AWUBBWUBC")
song_decoder("AWUBWUBWUBBWUBWUBWUBC")
song_decoder("WUBAWUBBWUBCWUB")
