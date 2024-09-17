int climbStairs(int n)
{
    if (n < 1)
        return 1;
    else if (n < 4)
        return n;
    else if (n > 45)
        return -1;
    
    int first = 2;
    int second = 3;
    while (3 < n--)
    {
        int temp = first + second;
        first = second;
        second = temp;
    }

    return second;
}