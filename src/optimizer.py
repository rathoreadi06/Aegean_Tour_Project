#!/usr/bin/env python3
from typing import List, Tuple, Optional
from collections import defaultdict


class AegeanTourOptimizer:
    def __init__(self, num_hops: int, customers: List[List[Tuple[int, str]]]):
        self.H = num_hops
        self.customers = customers

    def solve(self) -> Optional[List[Tuple[int, str]]]:
        """
        Returns the optimal itinerary with minimum airborne hops
        or None if no valid itinerary exists.
        """
        # step 1: separate preferences
        airborne_prefs = []
        sea_prefs = []

        for customer in self.customers:
            air = set()
            sea = set()
            for hop, transport in customer:
                if transport == "airborne":
                    air.add(hop)
                else:
                    sea.add(hop)
            airborne_prefs.append(air)
            sea_prefs.append(sea)
        # print(f"airborne_prefs:{airborne_prefs}")
        # print(f"sea_prefs:{sea_prefs}")
        # step 2: Select minimum airborne hops
        airborne_selected = set()
        unsatisfied_customers = set(range(len(self.customers)))

        while True:
            customers_needing_air = set()

            # find customers who cannot be satisfied by sea
            for i in unsatisfied_customers:
                if not sea_prefs[i]:
                    customers_needing_air.add(i)

            # if no one strictly needs airborne, stop
            if not customers_needing_air:
                break

            # count how many customers each airborne hop satisfy
            hop_frequency = defaultdict(int)
            for i in customers_needing_air:
                for hop in airborne_prefs[i]:
                    if 0 <= hop < self.H:
                        hop_frequency[hop] += 1

            if not hop_frequency:
                return None  # impossible
            #print(f"hop_frequency:{hop_frequency}")
            # choose the hop satisfying the most customers
            best_hop = max(hop_frequency, key=hop_frequency.get)
            #print(f"best hop:{best_hop}")
            airborne_selected.add(best_hop)

            # mark satisfied customers
            satisfied_now = set()
            for i in customers_needing_air:
                if best_hop in airborne_prefs[i]:
                    satisfied_now.add(i)

            unsatisfied_customers -= satisfied_now
            #print(f"unsatisfied_customers:{unsatisfied_customers}")

        # step 3: Build itinerary
        itinerary = []
        for hop in range(self.H):
            if hop in airborne_selected:
                itinerary.append((hop, "airborne"))
            else:
                itinerary.append((hop, "by-sea"))

        # step 4: Final validation
        for customer_index, preferences in enumerate(self.customers):
            customer_satisfied = False

            for hop, transport in preferences:
                if 0 <= hop < self.H:
                    if itinerary[hop][1] == transport:
                        customer_satisfied = True
                        break

            if not customer_satisfied:
                return None

        return itinerary