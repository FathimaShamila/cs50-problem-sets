#include<cs50.h>
#include<stdio.h>
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);
int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change Owed:");
    }
    while(cents < 0);
    int quarters = calculate_quarters(cents);
    printf("Quarters:%i\n",quarters);
    int change = cents % 25;
    int dimes = calculate_dimes(change);
    change = change % 10;
    printf("Dimes:%i\n",dimes);
    int nickels = calculate_nickels(change);
    change = change % 5;
    printf("Nickels:%i\n",nickels);
    int pennies = calculate_pennies(change);
    printf("Pennies:%i\n",pennies);
    int total_coins = quarters + dimes + nickels + pennies;
    printf("Coins:%i\n",total_coins);

}
int calculate_quarters(int cents)
{
    int quarters = cents/25;
    return quarters;
}
int calculate_dimes(int cents)
{
    int dimes = cents/10;
    return dimes;
}
int calculate_nickels(int cents)
{
    int nickels = cents/5;
    return nickels;
}
int calculate_pennies(int cents)
{
    int pennies = cents/1;
    return pennies;
}

