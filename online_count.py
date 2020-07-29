# python challenge 3 #
# https://pythonprinciples.com/challenges/Online-status/ #
# solution is O(n) time complexity
# Alex Hill #

def online_count(dict_in):
    online = 0
    dict(dict_in)
    for x,y in dict_in.items():
        if(y == "online"):
            online += 1
    return online

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
