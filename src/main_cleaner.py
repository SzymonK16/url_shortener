import time
import logging
from datetime import datetime, timezone, timedelta
from src.database.db_core import db_provider
from src.config.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - CLEANER_SERVICE - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


def run_cleaner():
    logger.info("Uruchamianie serwisu czyszczącego")
    db_provider.connect()
    db = db_provider.session

    while True:
        logger.info(f"Przeszukuje baze pod kątem nieuzywanych linków")
        now = datetime.now(timezone.utc)



        max_unused_date = now - timedelta(days=settings.TTL_UNUSED_CLEAR_DAYS)

        try:
            rows = db.execute("SELECT short_url, created_at, last_used_at FROM urls")
            deleted_count = 0

            for row in rows:
                created_at = row.created_at.replace(tzinfo=timezone.utc)
                last_used_at = row.last_used_at.replace(tzinfo=timezone.utc)


                is_unused = last_used_at < max_unused_date

                if is_unused:
                    logger.info(
                        f"Usuwam wpis [{row.short_url}].Utworzono: {created_at.date()}, Ostatnie użycie: {last_used_at.date()}")

                    db.execute("DELETE FROM urls WHERE short_url = %s", (row.short_url,))
                    deleted_count += 1

            logger.info(f"Usunięto {deleted_count} wpisów.")

        except Exception as e:
            logger.error(f"Wystąpił błąd podczas czyszczenia bazy: {e}")


        logger.info(f"Oczekiwanie {settings.CLEAR_SCRIPT_INTERVAL} sekund do następnego skanowania")
        time.sleep(settings.CLEAR_SCRIPT_INTERVAL)


if __name__ == "__main__":
    run_cleaner()