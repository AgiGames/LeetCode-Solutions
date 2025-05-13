typedef long long ll;
const ll mod = 1e9 + 7;

class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        ll frequency_map[26] = {0};

        for (char c : s) {
            frequency_map[c - 'a']++;
        }

        while (t--) {
            ll copy[26] = {0};

            for (int i = 0; i < 26; ++i) {
                if (frequency_map[i] == 0) continue;

                if (i == 25) {
                    copy[0] = (copy[0] + frequency_map[i]) % mod; // z -> a
                    copy[1] = (copy[1] + frequency_map[i]) % mod; // z -> b
                } else {
                    copy[i + 1] = (copy[i + 1] + frequency_map[i]) % mod; // shift
                }
            }

            for (int i = 0; i < 26; ++i) {
                frequency_map[i] = copy[i];
            }
        }

        ll total = 0;
        for (int i = 0; i < 26; ++i) {
            total = (total + frequency_map[i]) % mod;
        }

        return static_cast<int>(total);
    }
};
