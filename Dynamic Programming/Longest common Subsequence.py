int ceilArr(int tail[], int l, int r, int x)
{
    while(l < r)
    {
        int m = l + (r-l)/2;
        
        if(tail[m] >= x)
        {
            r = m;
        }
        else
        {
            l = m + 1;
        }
    }
    
    return r;
}

int longestSubsequence(int n, int arr[])
{
    int len = 1;
    
    int tail[n];
    tail[0] = arr[0];
    
    for(int i = 1; i < n; i++)
    {
        if(arr[i] > tail[len-1])
        {
            tail[len] = arr[i];
            len++;
        }
        else
        {
            int c = ceilArr(tail, 0, len-1, arr[i]);
            tail[c] = arr[i];
        }
    }
    return len;
}
