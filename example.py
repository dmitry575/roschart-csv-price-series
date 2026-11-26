"""Print one published price series; preserve missing observations and source units."""
import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--item', required=True, help='A unique substring of the Russian source label')
    parser.add_argument('--csv', default=str(Path(__file__).with_name('russia_consumer_prices_1998_2025.csv')))
    args = parser.parse_args()
    with open(args.csv, encoding='utf-8-sig', newline='') as source:
        rows = list(csv.DictReader(source))
    names = sorted({r['item_ru'] for r in rows if args.item.casefold() in r['item_ru'].casefold()})
    if len(names) != 1:
        parser.error('Choose one source series; matches: ' + '; '.join(names))
    print(names[0])
    print('Prices are per source-defined unit; see provenance.json and original workbook footnotes.')
    previous = None
    for row in sorted((r for r in rows if r['item_ru'] == names[0]), key=lambda r: int(r['year'])):
        year = int(row['year'])
        if row['observed'] != '1' or row['price_rubles_per_source_unit'] == '':
            print(year, 'MISSING', sep='\t')
            previous = None
            continue
        value = float(row['price_rubles_per_source_unit'])
        rate = 'not available'
        if previous and previous[0] + 1 == year and previous[1] != 0:
            rate = f'{(value / previous[1] - 1) * 100:.2f}%'
        print(year, value, rate, sep='\t')
        previous = year, value


if __name__ == '__main__':
    main()
