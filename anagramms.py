# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
source_string = ["eat", "tea", "tan", "ate", "nat", "bat"]
anogramms = []
result = []
k=0
for word in source_string:
    anogramms =[]
    for word2 in source_string:
        if set(word2) == set(word):
            anogramms.insert(k,word2)
    if anogramms not in result:
        result.insert(k,anogramms)
    k+1
print(result)


