/* ------------------------------------------------------------
 * Sub    : [BOJ] 문제 제목
 * Date   : 2026-10-06
 * Link   : https://www.acmicpc.net/problem/
 * Level  : Bronze 4
 * Tag    : C++, Math
 * ------------------------------------------------------------
 * Approach
 *
 * ------------------------------------------------------------
 */

#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

int main() {
    if (FILE* fp = fopen("./input_test.txt", "r")) {
        fclose(fp);
        freopen("./input_test.txt", "r", stdin);
    }
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    /* 📥 Input */
    ll n;
    cin >> n;

    /* ⚙️ Logic */
    vector<ll> small, large;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            small.push_back(i);
            if (i != n / i) large.push_back(n / i);  // 제곱수일 때 중복 방지
        }
    }

    /* 🚀 Output */
    for (ll x : small) cout << x << ' ';
    for (auto it = large.rbegin(); it != large.rend(); ++it) cout << *it << ' ';
    cout << '\n';

    return 0;
}
