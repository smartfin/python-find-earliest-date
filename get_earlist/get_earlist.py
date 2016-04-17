from itertools import permutations
from datetime import date

class InvalidDateException(Exception):
    pass

class GetEarlist:
    MAX_YEAR = 2999
    MIN_YEAR = 2000

    def find(self, numbers):
        all_dates = []
        for first_number, second_number, third_number in permutations(numbers):
            try:
                composed_date = date(first_number, second_number, third_number)
                if composed_date.year < self.MIN_YEAR:
                    year = composed_date.year + self.MIN_YEAR
                    if year > self.MAX_YEAR:
                        # illegal year!
                        continue
                    composed_date = date(year, composed_date.month, composed_date.day)

                all_dates.append(composed_date)
            except ValueError:
                continue

        try:
            min_data = min(all_dates)
            return min_data.strftime('%Y-%-m-%-d')
        except ValueError:
            raise InvalidDateException

    def process_string(self, string):
        numbers = map(int, string.split('/'))
        return self.find(numbers)
