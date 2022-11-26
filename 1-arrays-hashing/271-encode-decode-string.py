# -----------------------------------------------------------
# 271. Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Code encode and decode such that for a given string, encode(str) = x and decode(encode(str)) = str.

# You are not allowed to solve the problem using any serialize methods (such as eval).
 
# Example 1:
# 	Input: dummy_input = ["Hello","World"]
# 	Output: ["Hello","World"]
#   Explanation:
#   Machine 1:
#   	Codec encoder = new Codec();
#   	String msg = encoder.encode(strs);
#   Machine 1 ---msg---> Machine 2
# 	Machine 2:
# 		Codec decoder = new Codec();
# 		String[] strs = decoder.decode(msg);
# Example 2:
# 	Input: dummy_input = [""]
# 	Output: [""]
# -----------------------------------------------------------

# Separate words by using character not part of the accepted characters
class Codec:
    def encode(self, strs) -> str:
        r = ""
        for x in strs:
            r += x
            r += chr(257)
        return r

    def decode(self, s: str):
        r = []
        currs = ""
        for x in s:
            if(ord(x) != 257):
                currs += x
            else:
                r.append(currs)
                currs = ""
        return r
        
# Chunking by length
class Codec2:
    def encode(self, strs):
        r = ""
        for x in strs:
            l = len(x)
            r += f'{l:03d}'
            r += x
        return r

    def decode(self, s: str):
        i = 0
        r = []
        while i < len(s):
            l = int(s[i:i+3])
            i += 3
            r.append(s[i:i+l])
            i += l
        return r



codec = Codec2()
print(codec.encode(["Hello","World"]))