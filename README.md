# Felix' Time Tracker

If you are looking for something that already works: [Kimai](https://kimai.felixhummel.de/core/kimai.php)

## Intention

- keep it minimal
- mobile first

## Motivation

I have simple needs:

- start and stop a clock
- CRUD entries
- export to CSV
- neither PHP nor MySQL
- don't do too much

# Development

```
cp .env.sample .env
vi .env
docker-compose up
```

Generate example entries:
```
cat ftt/migrations/_generators/random_entry.sql | dc run postgres psql -h postgres ftt ftt
```

# Trivia
- http://acme.com/catalog/acme.html
