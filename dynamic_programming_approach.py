def optimal_stock(stocks: dict, capital: int):
  """returns a tuple of the optimal stocks to purchase based on capital constraints , balance
    Using dynamic programming
    p.s doesn't work well with floating point numbers and has large space complexity
  """
  
  import numpy as np
  stocks_name = list(stocks)
  stocks_price = list(map(lambda x: int(x), stock.values))
  
  link = {}

  n = len(stocks) + 1
  m = capital + 1

  grid = np.zeros((n,m))
  
  for i in range(n):
    for j in range(m):
        
        if i == 0 or j == 0:
            grid[i][j] = 0
        elif costs[i - 1] <= j:
            grid[i,j] = max(stocks_price[i - 1] + grid[i - 1][j - stocks_price[i - 1]], grid[i - 1][j])
            link[(i,j)] = [stocks_name[i - 1]] + link.get((i-1, j - stocks_price[i-1]), [])
        else:
            grid[i][j] = grid[i - 1][j]
            link[(i, j)] = link.get((i - 1, j), [])
  
  last_roll = len(stocks_name)
  spent = max(grid[last_roll])
  balance = capital - spent
  max_column = np.argmax(grid[last_roll])
  optimal_stocks = link[(last_roll,max_column)]
  
  return (optimal_stocks, balance)
  
  


