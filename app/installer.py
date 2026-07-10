from app.builders.areas import create_areas_database
from app.seed.seed_areas import seed_areas


def install():

    print("=" * 50)
    print("🚀 Installing Life OS")
    print("=" * 50)

    database = create_areas_database()

    seed_areas(database)

    print()
    print("=" * 50)
    print("✅ Installation abgeschlossen!")
    print("=" * 50)