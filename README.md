# Consumer-price time series from Russia: reproducible CSV example

This small data project demonstrates how to read annual statistical prices without turning missing observations into zero or silently combining incompatible units.

The attached CSV contains **86 source series and 2,408 series-year cells for 1998–2025**. Of these, 2,298 are observed and 110 are missing. Source: Rosstat, transformed to long format using [the Roschart dataset](https://roschart.ru/dataset/sred-potreb-cen-1991-2025-srednie-potrebitelskie-ceny-na-otd). Snapshot retrieved on 26 November 2026. This is a historical data extract, not a live feed or a forecast.

## Files and fields

- `russia_consumer_prices_1998_2025.csv`: UTF-8 with BOM; one row per original series and year.
- `provenance.json`: original dataset ID, public source links, available methodological footnotes, extraction date and source content hash.
- `example.py`: a standard-library example that prints one series and computes changes only between consecutive observed years. No API credential is needed for the attached snapshot.

`series_index` is the row index in the source extract, not a permanent product classification. `item_ru` preserves the Russian source label, including unit annotations and footnote markers. `year` is the year label from the source. `price_rubles_per_source_unit` is the unrounded published value. A blank field with `observed=0` is missing; an observed numeric zero stays zero.

## Run

```sh
python3 example.py --item 'Рис шлифованный'
python3 example.py --item 'Яйца куриные'
```

The script does not interpolate missing years. It refuses to divide by zero and reports no annual rate across a gap. Product matching is by source label; inspect the printed label before using a result.

## Interpretation limits

These are prices per **the unit defined by each source series**, not a table where every item costs one kilogram. Some services have an explicit transaction or time basis; eggs are quoted per ten items; labels can include methodological changes. Keep the source footnotes with the CSV and consult the linked original workbook before comparing a row across its full history.

The API-provided notes are preserved in `provenance.json`; this does not replace the full original workbook. We have not certified every series as methodologically continuous. There is no weighting or aggregation across products and no calculation of a consumer-price index in this repository.

Years before 1998 are excluded to keep the extract after the ruble denomination. This is not a normalization of every possible definition or source revision. There are no invented observations and no conversion of missing values to zeros.

For a refresh, consult the [Roschart API documentation](https://roschart.ru/docs), first identify the current dataset and read its metadata. Use your own key where required, respect the current request limits and keep keys out of URLs, notebooks and commits. This example does not rely on a promised free or paid allowance.

Original publisher: Federal State Statistics Service (Rosstat). Conversion and example: Roschart. The source data are third-party statistical material; the MIT license below applies to the example code only. This is a processed extract, not an official Rosstat publication.
