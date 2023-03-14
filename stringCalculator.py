class stringCalculator:

    #task  1 & 2
    def string1(self, nums):
        if not nums:
            return 0
        return int(nums)

    #task 3
    def string2(self, nums):
        if nums[1] == ',':
            return int(nums[0])+int(nums[2])

    #task 4
    def string3(self, nums):
        if nums[1] == '\n':
            return int(nums[0])+int(nums[2])

    #task 5
    def string4(self, nums):
        num1 = 0
        sum = 0
        count = 0
        for element in nums:
             if element.isdigit():
                 num1 = num1 * 10 + int(element)
             else:
                 sum = sum + num1
                 num1 = 0;
        sum = sum + num1
        return sum

    #task 6
    def string6(self, nums):
        if not nums[0] == "-":
            raise Exception("It is a negative number")

    #task 7
    def string7(self, num1, num2):
        if int(num1) > 1000:
            if int(num2) > 1000:
                raise Exception("all numbers are greater than 1000")
            else:
                return int(num2)
        else:
            if int(num2) > 1000:
                return int(num1)
            else:
                return int(num1), int(num2)

