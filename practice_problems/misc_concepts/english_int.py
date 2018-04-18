

def english_int(integer):
    number = EnglishInt(integer)
    return number.to_english()

KEY_ONES = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine'
}

KEY_TENS = {
    10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty',
    70: 'Seventy', 80: 'Eighty', 90: 'Ninty'
}


KEY_TEENS = {
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen'
}

KEY_POWERS = {
    100: "Hundred", 1000: "Thousand", 1000000: "Million"
}

KEY_UNDER_100 = {
    1: KEY_ONES,
    10: KEY_TENS
}


# 1211

class EnglishInt():

    def __init__(self, integer):
        self.integer = integer
        self.place = 1
        self.result = ''

    def to_english(self):
        self.handle_less_than_100()
        self.handle_greater_than_99()

        return self.result.rstrip()

    def handle_greater_than_99(self):
        while self.integer:
            place = 3
            divisor = 10**place

            while self.integer % divisor == 0:
                place += 1
                divisor = 10**place

            remainder = self.integer % divisor
            power = 10 ** (place - 1)

            base = self.get_english_base(power)
            sig_digit = self.get_english_less_than_100(remainder // power)


            self.result = sig_digit + ' ' + base \
                          + ' ' + self.result

    def get_english_base(self, base):
        return KEY_POWERS[base]

    def handle_less_than_100(self):
        number = self.integer % 100
        if  self.is_teen(number):
            english_number = self.get_english_teen(number)
        else:
            english_number = self.get_english_less_than_100(number)

        self.integer -= self.integer % 100
        self.result = english_number + ' ' + self.result

    def get_english_less_than_100(self, integer):
        temp_result = ''
        power = 0
        while integer > 0:
            key = KEY_UNDER_100[10**power]
            divisor = 10**power * 10
            remainder = integer % divisor

            if remainder:
                temp_result = key[remainder] + ' ' + temp_result
                integer -= remainder

            power += 1

        return temp_result.rstrip()


    def get_english_teen(self, teen):
        key = KEY_UNDER_100['teen']
        return key[teen]

    def is_teen(self, number):
        return 10 < number % 100 < 20
