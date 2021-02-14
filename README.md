# Google Autocomplete Explorer

A simple script that fetches data from Google autocomplete starting with a single keyword and generating a tree with alphabetical suffixes combinations.

## How it works
With initial keyword, a set of queries is generated attaching each letter of the alphabet to the initial query.
Each generated query is used against Google autocomplete, returning a suggestion dataset.
With each result dataset entry the process is repeated until reaching `MAXDEPTH` depth.

### Sample execution
#### Depth=1
Using `apartment` as initial keyword, first queries are:
```
apartment a
apartment b
apartment c
...
apartment z
```
Each query is sent to Google autocomplete.

The resultset of `apartment a` query is:
```
apartment amsterdam
apartment abbreviation
apartment adda
...
```
#### Depth=2
For each one of these entries, another alphabetical-suffix list is generated:
```
apartment amsterdam a
apartment amsterdam b
apartment amsterdam c
...
apartment amsterdam z
apartment abbreviation a
apartment abbreviation b
apartment abbreviation c
...
apartment abbreviation z
...
```
#### Depth=N
The process is repeated until reaching `MAXDEPTH`


## Requirements
You need docker installed

## How to run
- Clone this repository
- Run the following command

```
docker run -it -v $(pwd)/ac:/runtime/app \
  -e START=hotel \
  -e HL=en \
  -e MAXDEPTH=2 \
  --entrypoint "/usr/bin/scrapy" aciobanu/scrapy crawl ac -L CRITICAL
```
where
- `START` is the initial keyword
- `HL` is the language code for the query (Google might ignore it and give results based on ip-based location)
- `MAXDEPTH` no queries generated after this level (usually 3 is sufficient)
- `-L CRITICAL` represents the loglevel, you can use `DEBUG` if you want details of what's happening. `CRITICAL` suppresses almost everything.


## Output
A json-lines with the following format

```
{
  "origin": "<originating keyword>",
  "letter": "<alphabetical suffix>",
  "depth": <current depth>,
  "suggestion": "<suggestion output>",
  "url": "<origin url>"
}
```

### Sample output
```
{
  "origin": "hotel",
  "letter": "a",
  "depth": 1,
  "suggestion": "hotel astoria",
  "url": "https://www.google.com/complete/search?hl=en&oe=utf-8&output=toolbar&q=hotel%20a"
}
```
