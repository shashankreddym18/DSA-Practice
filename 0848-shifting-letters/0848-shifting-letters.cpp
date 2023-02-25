class Solution {
public:
  string shiftingLetters(string S, vector<int>& shifts) {
    int c = 0;
    for (int i = shifts.size() - 1; i >= 0; --i) {
      c += (shifts[i] % 26);
      S[i] = (S[i] - 'a' + c) % 26 + 'a';
    }          
    return S;
  }
};