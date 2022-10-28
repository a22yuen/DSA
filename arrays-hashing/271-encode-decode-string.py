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

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))