"""Convenience script to seed demo jobs into PostgreSQL."""
from worker.ingest import seed

if __name__ == "__main__":
    import asyncio
    asyncio.run(seed())