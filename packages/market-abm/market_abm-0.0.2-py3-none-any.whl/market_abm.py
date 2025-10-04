import numpy as np
import random
from scipy.stats import norm
from collections import defaultdict
import json
import matplotlib.pyplot as plt




# ------------------------------
# 3. Income Distribution
# ------------------------------

def gen_income(gini, mean_income ,size):
    sigma = np.sqrt(2) * norm.ppf((gini + 1) / 2)
    mu = np.log(mean_income) - (sigma ** 2) / 2
    return np.random.lognormal(mean=mu, sigma=sigma, size=size)

# ------------------------------
# 4. Buyer Class
# ------------------------------
class Buyer:
    def __init__(self, id, budget, product_ids, product_catalog, product_decay_params, product_recovery_params):
        self.id = id
        self.budget = budget

        self.base_utility = {
            pid: product_catalog[pid]['base_utility'] + random.randint(-2, 2)
            for pid in product_ids
        }

        self.current_utility = self.base_utility.copy()
        self.utility_decay = {
            pid: max(0, np.random.normal(
                loc=product_decay_params[pid]['decay_rate'],
                scale=product_decay_params[pid]['randomness']
            )) for pid in product_ids
        }
        self.utility_recovery = {
            pid: product_recovery_params.get(pid, 0.05)
            for pid in product_ids
        }

        self.purchase_history = defaultdict(int)
        self.rounds_since_last_purchase = defaultdict(int)
        self.non_purchases = defaultdict(int)

    def current_marginal_utility(self, product_id):
        return max(0, min(self.base_utility[product_id], self.current_utility[product_id]))

    def try_to_buy(self, sellers, product_ids):
        options = []
        for seller in sellers:
            for pid in product_ids:
                if seller.has_inventory(pid):
                    price = seller.get_price(pid)
                    mu = self.current_marginal_utility(pid)
                    # append only products that is within budget
                    if price <= self.budget and price <= mu:
                        options.append((seller, pid, price, mu))

        if not options:
            # Didn't buy anything this round
            for pid in product_ids:
                self.rounds_since_last_purchase[pid] += 1
                self.non_purchases[pid] += 1
                self.current_utility[pid] += self.utility_recovery[pid]
                self.current_utility[pid] = min(self.current_utility[pid], self.base_utility[pid])
            return False

        # Buy product with highest (utility - price)
        seller, pid, price, _ = max(options, key=lambda x: x[3] - x[2])
        seller.sell_product(pid)
        self.budget -= price
        self.purchase_history[pid] += 1
        self.rounds_since_last_purchase[pid] = 0

        # Apply decay
        decay = self.utility_decay[pid]
        self.current_utility[pid] *= np.exp(-decay)

        

        # Recover other products
        for other_pid in product_ids:
            if other_pid != pid:
                self.rounds_since_last_purchase[other_pid] += 1
                self.non_purchases[other_pid] += 1
                self.current_utility[other_pid] += self.utility_recovery[other_pid]
                self.current_utility[other_pid] = min(self.current_utility[other_pid], self.base_utility[other_pid])
        return True

# ------------------------------
# 5. Seller Class
# ------------------------------
class Seller:
    def __init__(self, id, products, supply_costs, prices, max_inventory_capacity , init_cash_reserve):
        self.id = id
        self.products = products
        self.supply_costs = supply_costs
        self.prices = prices

        self.items_sold = defaultdict(int)
        self.revenue = defaultdict(float)
        self.total_profit = defaultdict(float)

        self.cash_reserve = init_cash_reserve
        self.bankruptcy_counter = 0
        self.active = True
        self.max_inventory_capacity = max_inventory_capacity

    def has_inventory(self, pid):
        return self.products.get(pid, 0) > 0

    def get_price(self, pid):
        return self.prices.get(pid, float('inf'))

    def sell_product(self, pid):
        self.products[pid] -= 1
        price = self.prices[pid]
        self.revenue[pid] += price
        self.items_sold[pid] += 1

    def restock(self):
        current_inventory = sum(self.products.values())
        for pid in self.products:
            cost = self.supply_costs[pid]
            sales_last_round = self.items_sold[pid]
            target_restock = max(int(sales_last_round * 0.4), 3)

            max_affordable = int(self.cash_reserve // cost)
            available_space = self.max_inventory_capacity - current_inventory
            restock_qty = min(target_restock, max_affordable, available_space)

            if restock_qty > 0:
                self.products[pid] += restock_qty
                self.cash_reserve -= restock_qty * cost
                current_inventory += restock_qty

    def adjust_prices(self, min_price_markup , learning_rate):
        for pid in self.products:
            total_offered = self.products[pid] + self.items_sold[pid]
            if total_offered == 0:
                continue
            demand_ratio = self.items_sold[pid] / total_offered
            price = self.prices[pid]
            min_price = self.supply_costs[pid] * min_price_markup

            if demand_ratio > 0.75:
                price *= (1 + learning_rate)
            elif demand_ratio < 0.25 and price > min_price:
                price = max(min_price, price * (1 - learning_rate))

            self.prices[pid] = round(price, 2)
            self.items_sold[pid] = 0

    def calculate_profit(self,operating_cost_per_item,fixed_operating_cost_base,bankruptcy_threshold):
        total_revenue = sum(self.revenue.values()) 
        variable_cost = sum(self.items_sold[pid] * operating_cost_per_item for pid in self.items_sold)
        self.cash_reserve += total_revenue - fixed_operating_cost_base - variable_cost

        for pid in self.revenue:
            self.total_profit[pid] += self.revenue[pid]
            self.revenue[pid] = 0

        if self.cash_reserve < 0:
            self.bankruptcy_counter += 1
        else:
            self.bankruptcy_counter = 0

        if self.bankruptcy_counter >= bankruptcy_threshold:
            self.active = False
            print(f"Seller {self.id} has gone bankrupt.")

