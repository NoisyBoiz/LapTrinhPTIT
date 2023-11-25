#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n) {
    if(n == 0) return 1;
    if(n == 1) return x;
    double rs = myPow(x, n/2);
    rs = rs * rs;
    if(n % 2 == 1) rs = rs * x;
    return rs;
}

int main(){
    int n;
    cin >> n;
    while(n--){
        double x;
        int n;
        cin >> x >> n;
        double rs = myPow(x, abs(n));
        if(n > 0) cout << rs << endl;
        else cout << 1/rs << endl;
    }
}
