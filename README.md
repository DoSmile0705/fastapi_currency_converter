# Instructions for Installing and Running the Project

## 1. Clone the Repository

```
git clone https://github.com/DoSmile0705/fastapi_currency_converter.git
```

## 2. Navigate to the Project Directory

```
cd fastapi_currency_converter
```

## 3. Build and Run the Project

```
docker-compose -f docker-compose.yml up --build -d
```

> *Migration was defined in the Dockerfile.

This step ensures that the database is initialized with the necessary tables and data.

Adjust these commands based on your actual project structure and requirements.


# Currency Converter API Usage Examples

## 1. Update Exchange Rates

**Endpoint:** /update_exchange_rates

**HTTP Method:** GET

```
curl -X POST "http://localhost:8000/update_exchange_rates"
```

This will trigger an update of the exchange rates in the database.

## 2. Get Last Update Time

**Endpoint:** /last_update

**HTTP Method:** GET

```
curl -X GET "http://localhost:8000/last_update"
```

This will return the date and time of the last update of rates in the database.

## 3. Convert Currency

**Endpoint:** /convert

**HTTP Method:** POST

```
curl -X POST "http://localhost:8000/convert" -H "accept: application/json" -H "Content-Type: application/json" -d '{"source": "USD", "target": "EUR", "amount": 100.0}'
```

This will convert 100 USD to EUR based on the current exchange rates.

## Notes:

* Ensure that Docker and Docker Compose are installed on your system.
* If there are API keys required for external services, make sure to include them in the requests.
