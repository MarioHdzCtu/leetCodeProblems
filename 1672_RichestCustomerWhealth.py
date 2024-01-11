"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth."""

def maximumWhealth(accounts: list[list]) -> int:
    """Calculates the richest person given a 2D array with the quantity of money a person has in each bank

    Args:
        accounts (list[list]): The given 2D array

    Returns:
        int: The sum (wealth) of the richest person
    """
    max_wealth = 0
    for account in accounts:
        wealth = 0
        for i in account:
            wealth += i
            if wealth > max_wealth:
                max_wealth = wealth
    return max_wealth

accounts = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(maximumWhealth(accounts=accounts))