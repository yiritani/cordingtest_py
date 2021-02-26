class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for _ in range(numRows)]
        insert_index = {i for i in range(numRows)}
        index = 0
        list_s = [i for i in s]
        is_list_empty, is_bottom = False, False

        while is_list_empty is False:
            for i in range(len(result)):
                if len(list_s) == 0:
                    is_list_empty = True
                    break

                if index % numRows == 0 and index > 0:
                    for rest in insert_index - {1}:
                        result[rest].append('')
                    else:
                        result[1].append(list_s.pop(0))
                        index = 0
                        continue
                else:
                    result[index].append(list_s.pop(0))
                index += 1

        print(result)
        result_dock = ''
        for i in result:
            result_dock += ''.join(i)

        return result_dock



m = "PAYPALISHIRING"
s = Solution()
print(s.convert(m, 3))
