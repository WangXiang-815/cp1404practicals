"""
estimated time: 15mins
actual time:
"""

FILENAME = 'wimbledon.csv'


def main():
    """read csv data and print wimbledon champions and countries details"""
    records = load_record(FILENAME)
    champion_to_count, countries = process_record(records) #TODO:write process record func
    display_records(champion_to_count, countries)#TODO:write display func

def load_record(FILENAME):
    """load data and create a list of lists to store"""
    record = []
    with open(FILENAME,'r', encoding="utf-8-sig") as file:
        file.readline() #remove header
        for line in file:
            parts = line.strip().split()
            record.append(parts) #split and store to record list

    return record

