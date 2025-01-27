class Solution:
    def compress(self, chars: List[str]) -> int:
        # count=1
        # new1=[]
        # index=0
        # new=chars[index]
        # for i in range(1,len(chars)):
        #     # for j in range(i+1,len(chars)):
        #     # print(new)
        #     if i==len(chars)-1:
        #         new1.append(new)
        #         new1.append(count+1)
        #     if chars[i]==new:
        #         count+=1
        #     elif chars[i]!=new:
        #         new1.append(new)
        #         new1.append(count)
        #         count=1
        #         new=chars[i]
        # chars.clear()
        # for i in new1:
        #     chars.append(i)
                
        # print(new1)
        count=1
        compress=[]
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                compress.append(str(chars[i-1]))
                if count!=1:
                    compress.append(str(count))
                count=1
        compress.append(chars[-1])
        if count!=1:

            compress.append(str(count))

        chars.clear()

        result="".join(compress)
        for char in result:
            chars.append(char)
        print(result)


        