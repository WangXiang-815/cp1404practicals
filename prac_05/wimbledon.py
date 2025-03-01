"""
estimated time: 15mins
actual time:
"""

FILENAME = 'wimbledon.csv'
INDEX_COUNTRIES = 1
INDEX_CHAMPIONS = 2

def main():
    """read csv data and print wimbledon champions and countries details"""
    records = load_record(FILENAME)
    champion_to_count, countries = process_record(records) #TODO:write process record func
    display_records(champion_to_count, countries)#TODO:write display func

def load_record(FILENAME):
    """load data and create a list of lists to store"""
    records = []
    with open(FILENAME,'r', encoding="utf-8-sig") as file:
        file.readline() #remove header
        for line in file:
            parts = line.strip().split()
            records.append(parts) #split and store to record list

    return records

def process_record(records):
    """create a dict to store champions and set of countries from list of lists(records)"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRIES])
        try:
            champion_to_count[record[INDEX_CHAMPIONS]] += 1

        except KeyError:
            champion_to_count[record[INDEX_CHAMPIONS]] = 1

    return champion_to_count, countries

