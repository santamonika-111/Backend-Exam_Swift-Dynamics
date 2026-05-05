"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        
        if number == 0:
            return "ศูนย์"
        
        units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        positions = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        def convert(n):
            result = ""
            pos = 0
            
            while n > 0:
                digit = n % 10
                
                if pos == 0:  
                    if digit == 1 and n > 10:
                        result = "เอ็ด" + result
                    elif digit > 0:
                        result = units[digit] + result
                
                elif pos == 1:  
                    if digit == 2:
                        result = "ยี่" + positions[pos] + result
                    elif digit == 1:
                        result = positions[pos] + result
                    elif digit > 0:
                        result = units[digit] + positions[pos] + result
                
                else:  
                    if digit > 0:
                        result = units[digit] + positions[pos] + result
                
                n //= 10
                pos += 1
            
            return result

        if number >= 1_000_000:
            million_part = number // 1_000_000
            rest = number % 1_000_000
            
            result = convert(million_part) + "ล้าน"
            if rest > 0:
                result += convert(rest)
            return result
        
        return convert(number)