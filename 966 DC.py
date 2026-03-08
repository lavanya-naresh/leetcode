class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = set("aeiou")

        def mask(word):
            return "".join("*" if ch in vowels else ch for ch in word)

        exact = set(wordlist)
        lower_map = {}
        mask_map = {}

        for word in wordlist:
            lower_keyword = word.lower()
            if lower_keyword not in lower_map:
                lower_map[lower_keyword] = word
            masked_word = mask(lower_keyword)
            if masked_word not in mask_map:
                mask_map[masked_word] = word

        result = []
        for query in queries:
            if query in exact:
                result.append(query)
                continue
            lower_query = query.lower()
            if lower_query in lower_map:
                result.append(lower_map[lower_query])
                continue
            masked_query = mask(lower_query)
            if masked_query in mask_map:
                result.append(mask_map[masked_query])
                continue
            result.append("")
        return result
