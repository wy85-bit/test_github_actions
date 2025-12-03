import json
from datetime import datetime
import os

def main():
    data = {
        "generated_at": datetime.now().isoformat(),
        "message": "Hello from GitHub Actions",
    }

    # Map aanmaken
    os.makedirs("data", exist_ok=True)

    # Schrijf JSON weg
    with open("data/generated.json", "w") as f:
        json.dump(data, f, indent=4)

    print("JSON opgeslagen in data/generated.json")

if __name__ == "__main__":
    main()
