#include <bits/stdc++.h>
using namespace std;

int main()
{
      int tests;
      cin >> tests;
      while (tests--)
      {
            int n;
            cin >> n;

            vector<int> a(n);
            for (int i = 0; i < n; i++)
            {
                  cin >> a[i];
            }

            vector<int> cnt(31);
            for (int bit = 30; bit >= 0; bit--)
            {
                  for (int i = 0; i < n; i++)
                  {
                        if ((1 << bit) & a[i])
                              cnt[bit]++;
                  }
            }

			cout<<" Vector elements are \n";
			for (auto i=cnt.begin(); i!=cnt.end(); i++){
				cout<<*i<<" ";
			}
			cout<<endl;

            int ans = 0;
            for (int bit = 30; bit >= 0; bit--)
            {
                  if (cnt[bit] > 1)
                  {
                        ans += (1 << bit);
                  }
            }

            cout << ans << endl;
      }
      return 0;
}