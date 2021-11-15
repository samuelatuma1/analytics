def optimize_investments(investments: list, available: int or float) -> dict:
    """
        uses a greedy approach to determine the best investments to make based on a list of available investments and available capital.
        Returns a dictionary containing the best investments(bests_investment) and the remaining_balance(available_balance)
    """
    
    best_investments: list = []
    
    best_investment =  best_investment_choice(investments, available)
    while best_investment is not None:
        best = investments.pop(investments.index(best_investment))
        best_investments.append(best)
        available -= best['cost']
        best_investment =  best_investment_choice(investments, available)
        
    return {"best_investments": best_investments, "available_balance": available}


def best_investment_choice(investments: list, available: int or float) -> dict:
    """
        Given a list of investments and the total available funding, returns the single investment that yields the most profit(revenue - cost)
    """
    best_investment = None
    best_worth = 0
    for investment in investments:
        if investment["revenue"] - investment["cost"] > best_worth and investment["cost"] <= available:
            best_investment = investment
            best_worth = investment["revenue"] - investment["cost"]
    
    return best_investment