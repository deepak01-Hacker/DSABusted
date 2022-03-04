class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
   constexpr int kRows = 100;
  vector<vector<double>> dp(kRows, vector<double>(kRows));
  dp[0][0] = poured;
  for (int i = 1; i < kRows; ++i)
    for (int j = 0; j <= i; ++j) {
      if (j > 0) dp[i][j] += max(0.0, (dp[i - 1][j - 1] - 1) / 2.0);
      if (j < i) dp[i][j] += max(0.0, (dp[i - 1][j    ] - 1) / 2.0);
    }
  return std::min(1.0, dp[query_row][query_glass]);
}
};
