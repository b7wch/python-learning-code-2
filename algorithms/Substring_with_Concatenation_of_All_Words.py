#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/11/7
import time
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        s_len = len(s)
        words_len = len(words)
        per_word_len = len(words[0])
        sub_len = words_len * per_word_len
        index = 0
        result = list()
        word_couter = self.dict_count(words)
        while index <= s_len - sub_len:
            sub = s[index:sub_len + index]
            flag = True
            _words_copy = word_couter.copy()
            for i in range(words_len):
                ss = sub[i * per_word_len:per_word_len * (i + 1)]
                if ss not in _words_copy:
                    flag = False
                    break
                _words_copy[ss] -= 1
                if _words_copy[ss] < 0:
                    flag = False
                    break
            if flag:
                result.append(index)
            index += 1
        return result

    @staticmethod
    def dict_count(wl):
        result = collections.defaultdict(int)
        for e in wl:
            result[e] += 1
        return result


class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        size = len(words[0])
        counter = collections.defaultdict(int)
        for word in words:
            counter[word] += 1

        res = []
        length = len(words)

        for idx in range(len(s) - size * length + 1):
            hash_table = collections.defaultdict(int)
            j = 0
            while j < length:
                cur_word = s[idx + j * size:idx + (j + 1) * size]
                if cur_word not in counter:
                    break

                hash_table[cur_word] += 1
                if hash_table[cur_word] > counter[cur_word]:
                    break

                j += 1

            if j == length:
                res.append(idx)

        return res


S = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
t = time.time()
for _ in xrange(10000):
    S.findSubstring(s, words)
print time.time()-t
