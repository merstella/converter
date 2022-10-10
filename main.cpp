#include <bits/stdc++.h>
using namespace std;
vector<string> getans(string s) {
    vector<string> tmp(4);
    int a = s.find("A."), b = s.find("B."), c = s.find("C."), d = s.find("D.");
    tmp[0] = s.substr(a + 2, b - a - 2);
    tmp[1] = s.substr(b + 2, c - b - 2);
    tmp[2] = s.substr(c + 2, d - c - 2);
    tmp[3] = s.substr(d + 2);
    return tmp;
}
int main() {
    ifstream inf{ "source.txt" };
    ofstream outf{ "output.txt" };
    outf << "question = [\"";
    int cnt = 0;
    vector<vector<string>> answer;
    while (inf) {
        string quest, ans, key;
        getline(inf, quest); getline(inf, ans); 
        if (ans.find('.') == -1) break;
        if (cnt > 0) outf << ", \"";
        answer.push_back(getans(ans));
        cnt++;
        outf << quest.substr(quest.find('.') + 2) << "\"";
    }
    outf << "];\n";
    inf.close();
    inf.open("ans.txt");
    cnt = 0;
    while (inf) {
        string key;
        getline(inf, key);
        if (key[key.size() - 1] == 'B') swap(answer[cnt][0], answer[cnt][1]);
        if (key[key.size() - 1] == 'C') swap(answer[cnt][0], answer[cnt][2]);
        if (key[key.size() - 1] == 'D') swap(answer[cnt][0], answer[cnt][3]);
        cnt++;
    }
    for (int i = 0; i < answer.size(); ++i) {
        for (int j = 0; j < 4; ++j) {
            int l, r;
            string s = answer[i][j];
            for (l = 0; l < (s).size(); ++l) if ((s)[l] != ' ') break;
            for (r = (s).size() - 1; r >= 0; --r) if ((s)[r] != ' ') break;
            outf << "answer[" << i << "][" << j << "] = \"" << s.substr(l, r - l + 1) << "\";\n";
        }
    }
    return 0;
}
// Attention!!
// Cau truc file source.txt bat buoc phai nhu sau:
// Cau hoi 1
// Cau tra loi 1
// Cau hoi 2
// Cau tra loi 2
// ...

// Cau truc file ans.txt bat buoc phai nhu sau:
// Question 1 A
// Question 2 B
// Question 3 C
// ...
// Luu y: Khong thua dau cach o dang sau 'A', 'B', 'C', ...

// 4 dap an A, B, C, D phai nam tren cung mot dong
