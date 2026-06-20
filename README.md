# URL Shortener 
This is a university project developed for a course assignment. It demonstrates the use of distributed architecture and event streaming.

## Architecture & Data Flow

The application is a fast URL shortener with a built-in "shadow banning" mechanism for malicious words in link. (e.g in this code it name of programming language)

1. **Fast Write:** The user submits a URL. The API saves it in the database (Cassandra) and returns the shortened link.
2. **Validation:** The API checks the link for banned words.
3. **Queueing (Background):** If the link is suspicious, the server doesn't block the user. Instead, it sends an incident event to the **Kafka** broker.
4. **Cleaning:** An external worker (`cleaner-service`) clean database from expired links.
## Tech Stack

* **FastAPI** (`writer-service`, `reader-service`) – HTTP traffic handling.
* **Apache Cassandra** – multi-node NoSQL database for storing links.
* **Apache Kafka (KRaft)** – message broker for routing of security logs.
* **Docker Compose** – full containerization of the entire environment.
