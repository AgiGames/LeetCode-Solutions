class Solution {
public:
    string longestPalindrome(string &s) {
        int substringLength = 0;
        int maxLength = 0;
        std::string longest_palindrome;

        std::string substring;
        for (int i = 0; i < s.size(); i++){
            for (int j = i+1; j < s.size(); j++){
                if (CheckIfPalindrome(s, i, j))
                    substring = s.substr(i, j-i+1);
                    substringLength = substring.size();
                    if (substringLength > maxLength){
                        maxLength = substringLength;
                        longest_palindrome = substring;
                    }
            }
        }

        if (longest_palindrome.size() == 0)
            longest_palindrome.push_back(s[0]);
        
        return longest_palindrome;
    }

private:
    bool CheckIfPalindrome(std::string &s, int i, int j){
        while(i<j){
            if(s[i] != s[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }    
};
