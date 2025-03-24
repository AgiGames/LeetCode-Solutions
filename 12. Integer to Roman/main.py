class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        cache = {}
        cache[1] = "I"
        cache[2] = "II"
        cache[3] = "III"
        cache[4] = "IV"
        cache[5] = "V"
        cache[6] = "VI"
        cache[7] = "VII"
        cache[8] = "VIII"
        cache[9] = "IX"

        s = ""

        digits = int(floor(math.log10(num))) + 1
        # print("Number of digits in the number: ", digits)

        i = digits
        while(i > 0):
            jth_place_number = num - num % (10 ** (digits - 1))
            # print("Number at the jth place: ", jth_place_number)

            while(jth_place_number >= 10 ** (digits - 1)):
               #  print(jth_place_number, 10 ** (digits - 1))
                if jth_place_number >= 1000:
                    s += "M"
                    jth_place_number -= 1000
                elif jth_place_number < 1000 and jth_place_number >= 500:
                    if jth_place_number == 900:
                        s += "CM"
                        jth_place_number = 0
                        break
                    s += "D"
                    jth_place_number -= 500
                elif jth_place_number < 500 and jth_place_number >= 100:
                    if jth_place_number == 400:
                        s += "CD"
                        jth_place_number = 0
                        break
                    s += "C"
                    jth_place_number -= 100
                elif jth_place_number < 100 and jth_place_number >= 50:
                    if jth_place_number == 90:
                        s += "XC"
                        jth_place_number = 0
                        break
                    s += "L"
                    jth_place_number -= 50
                elif jth_place_number < 50 and jth_place_number >= 10:
                    if jth_place_number == 40:
                        s += "XL"
                        jth_place_number = 0
                        break
                    s += "X"
                    jth_place_number -= 10
                elif jth_place_number < 10:
                    s += cache[jth_place_number]
                    jth_place_number = 0
                # print(s)
                # print(jth_place_number, 10 ** (digits - 1))

            num = num % (10 ** (digits - 1))
            i -= 1
            digits -= 1
        
        return s
