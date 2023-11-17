# Kafka to PostgreSQL Data Ingestion

This project demonstrates data ingestion from Kafka to PostgreSQL using Python and Docker.

## Prerequisites

- [Docker](https://www.docker.com/)
- Environment variables for configuration:
- `DB_USERNAME`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`: PostgreSQL settings
- `KAFKA_URL`, `KAFKA_TOPIC`: Kafka settings

## Usage

1. Build Docker image:

   ```bash
   docker build -t kafka-postgresql-ingest .
    ```

2. Run Docker container:

   ```bash
   docker run --env-file .env kafka-postgresql-ingest
    ```

## Dockerfile

The Dockerfile sets up the environment and runs the Kafka to PostgreSQL ingestion script.

## License

This project is licensed under the MIT License.

