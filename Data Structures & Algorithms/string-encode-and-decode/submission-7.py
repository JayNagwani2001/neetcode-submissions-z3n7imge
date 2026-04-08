class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        isempty = len(strs) == 0
        if isempty:
            return "`"
        for ele in strs:
            encoded_str.append(ele)
            encoded_str.append("-")
        encoded_str = ''.join(encoded_str[:-1])
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "`":
            return []

        decoded_list = []
        curr = ""
        print(s)
        if s == '':
            return [""]
        decoded_list = s.split('-')
        return decoded_list