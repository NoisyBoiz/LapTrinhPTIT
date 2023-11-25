#include <bits/stdc++.h>
using namespace std;

struct matrix{
    long long a[2][2];
    matrix operator* (matrix &b){
        matrix rs;
        rs.a[0][0] = a[0][0] * b.a[0][0] + a[0][1] * b.a[1][0];
        rs.a[0][1] = a[0][0] * b.a[0][1] + a[0][1] * b.a[1][1];
        rs.a[1][0] = a[1][0] * b.a[0][0] + a[1][1] * b.a[1][0];
        rs.a[1][1] = a[1][0] * b.a[0][1] + a[1][1] * b.a[1][1];
        return rs;
    }
};

matrix poww(matrix a, long long n){
    if(n == 1) return a;
    matrix rs = poww(a, n/2);
    rs = rs * rs;
    if(n % 2 == 1) rs = rs * a;
    return rs;
}

int main(){
    int n;
    cin >> n;
    while(n--){
        int n;
        cin >> n;
        if(n==0) {
            cout << 0 << endl;
            continue;
        }
        matrix a;
        a.a[0][0] = 1;
        a.a[0][1] = 1;
        a.a[1][0] = 1;
        a.a[1][1] = 0;
        matrix rs = poww(a, n);
        cout << rs.a[0][1] << endl;
    }
}