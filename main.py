import sys
from src.optimizer import AegeanTourOptimizer

class AegeanTourApp:

    def normalize_transport(self, t: str) -> str:
        """
        Normalize transport string to one of:
        'airborne and by-sea'
        """
        t = t.strip().lower()

        # fix common airborne typos
        if t.startswith("airborne"):
            return "airborne"

        # normalize sea typos
        if t in {"by-sea", "bysea", "sea"}:
            return "by-sea"

        return "by-sea"

    def parse_input(self, text: str):
        lines = text.strip().splitlines()
        H = int(lines[0])
        C = int(lines[1])

        customers = []
        for i in range(2, 2 + C):
            prefs = []
            for pair in lines[i].split(", "):
                hop, transport = pair.split()
                transport = self.normalize_transport(transport)
                prefs.append((int(hop), transport))
            customers.append(prefs)

        return H, customers


    def format_output(self, itinerary):
        if not itinerary:
            return "NO ITINERARY"
        return ", ".join(f"{hop} {transport}" for hop, transport in itinerary)


    def main(self):
        if len(sys.argv) > 1:
            with open(sys.argv[1]) as f:
                input_text = f.read()
        else:
            input_text = sys.stdin.read().strip()

        H, customers = self.parse_input(input_text)
        optimizer = AegeanTourOptimizer(H, customers)
        result = optimizer.solve()

        if result is None:
            print("NO ITINERARY")
        else:
            print(self.format_output(result))

if __name__ == "__main__":
    app = AegeanTourApp()
    app.main()