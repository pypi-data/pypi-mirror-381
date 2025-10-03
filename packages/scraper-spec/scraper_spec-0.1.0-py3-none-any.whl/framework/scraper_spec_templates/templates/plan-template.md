# Scraper Implementation Plan

## Critical Path

Acquire → Identify → Collect → Extract

*Abstract phases that apply to any data acquisition method (web, API, feed, file)*

## Selectors

Defined in /specs/<site>.yaml

## Baselines

Stored in /baselines/<site>.expected.json + snapshot.html + screenshots

## Logs

Stored in /logs/<site>\_<timestamp>.log.json

## Testing

Use /test to compare against baselines

## Release

Use /release to freeze spec and baseline as stable
